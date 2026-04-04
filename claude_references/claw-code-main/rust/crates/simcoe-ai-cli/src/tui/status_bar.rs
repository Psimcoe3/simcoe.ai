use std::io::{self, IsTerminal, Write};
use std::sync::{Arc, Mutex};
use std::time::{Duration, Instant};

use crossterm::cursor::{MoveTo, RestorePosition, SavePosition};
use crossterm::queue;
use crossterm::style::{Color, Print, ResetColor, SetBackgroundColor, SetForegroundColor};
use crossterm::terminal::{size, Clear, ClearType};
use runtime::{format_usd, pricing_for_model, TokenUsage};

use crate::args::brand_model_name;

#[derive(Debug, Clone)]
pub(crate) struct StatusBarHandle {
    inner: Arc<Mutex<StatusBarState>>,
}

#[derive(Debug, Clone)]
struct StatusBarState {
    model: String,
    permission_mode: String,
    session_id: String,
    git_branch: Option<String>,
    cumulative_usage: TokenUsage,
    current_turn_usage: TokenUsage,
    show_turn_duration: bool,
    turn_started_at: Option<Instant>,
    enabled: bool,
}

impl StatusBarHandle {
    #[must_use]
    pub(crate) fn new(
        model: String,
        permission_mode: String,
        session_id: String,
        git_branch: Option<String>,
        show_turn_duration: bool,
    ) -> Self {
        Self {
            inner: Arc::new(Mutex::new(StatusBarState {
                model,
                permission_mode,
                session_id,
                git_branch,
                cumulative_usage: TokenUsage::default(),
                current_turn_usage: TokenUsage::default(),
                show_turn_duration,
                turn_started_at: None,
                enabled: io::stdout().is_terminal(),
            })),
        }
    }

    pub(crate) fn set_model(&self, model: impl Into<String>) {
        self.with_state(|state| state.model = model.into());
    }

    pub(crate) fn set_permission_mode(&self, permission_mode: impl Into<String>) {
        self.with_state(|state| state.permission_mode = permission_mode.into());
    }

    pub(crate) fn set_session_id(&self, session_id: impl Into<String>) {
        self.with_state(|state| state.session_id = session_id.into());
    }

    pub(crate) fn set_git_branch(&self, git_branch: Option<String>) {
        self.with_state(|state| state.git_branch = git_branch);
    }

    pub(crate) fn set_cumulative_usage(&self, usage: TokenUsage) {
        self.with_state(|state| state.cumulative_usage = usage);
    }

    pub(crate) fn begin_turn(&self, usage: TokenUsage) {
        self.with_state(|state| {
            state.cumulative_usage = usage;
            state.current_turn_usage = TokenUsage::default();
            state.turn_started_at = Some(Instant::now());
        });
    }

    pub(crate) fn update_turn_usage(&self, usage: TokenUsage) {
        self.with_state(|state| state.current_turn_usage = usage);
    }

    pub(crate) fn finish_turn(&self, usage: TokenUsage) {
        self.with_state(|state| {
            state.cumulative_usage = usage;
            state.current_turn_usage = TokenUsage::default();
            state.turn_started_at = None;
        });
    }

    pub(crate) fn render(&self) -> io::Result<()> {
        let snapshot = self.snapshot();
        snapshot.render()
    }

    pub(crate) fn clear(&self) -> io::Result<()> {
        let snapshot = self.snapshot();
        snapshot.clear()
    }

    fn snapshot(&self) -> StatusBarState {
        self.inner
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner)
            .clone()
    }

    fn with_state(&self, update: impl FnOnce(&mut StatusBarState)) {
        let mut state = self
            .inner
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        update(&mut state);
    }
}

impl StatusBarState {
    fn render(&self) -> io::Result<()> {
        if !self.enabled {
            return Ok(());
        }

        let Ok((width, height)) = size() else {
            return Ok(());
        };
        if width == 0 || height == 0 {
            return Ok(());
        }

        let mut stdout = io::stdout();
        let line = self.render_line(width as usize);
        queue!(
            stdout,
            SavePosition,
            MoveTo(0, height.saturating_sub(1)),
            SetBackgroundColor(Color::DarkGrey),
            SetForegroundColor(Color::White),
            Clear(ClearType::CurrentLine),
            Print(line),
            ResetColor,
            RestorePosition
        )?;
        stdout.flush()
    }

    fn clear(&self) -> io::Result<()> {
        if !self.enabled {
            return Ok(());
        }

        let Ok((_, height)) = size() else {
            return Ok(());
        };
        if height == 0 {
            return Ok(());
        }

        let mut stdout = io::stdout();
        queue!(
            stdout,
            SavePosition,
            MoveTo(0, height.saturating_sub(1)),
            Clear(ClearType::CurrentLine),
            RestorePosition
        )?;
        stdout.flush()
    }

    fn render_line(&self, width: usize) -> String {
        let model_segment = short_model(&self.model);
        let permission_segment = short_permission_mode(&self.permission_mode).to_string();
        let session_segment = format!("s:{}", compact_session_id(&self.session_id));
        let token_segment = format!(
            "tok:{}",
            format_token_count(self.combined_usage().total_tokens())
        );
        let branch_segment = self
            .git_branch
            .as_ref()
            .filter(|branch| !branch.is_empty())
            .map(|branch| format!("git:{branch}"));
        let cost_segment = format!("cost:{}", self.cost_label());
        let short_cost_segment = self.cost_label();
        let turn_segment = self.turn_duration_label("turn");
        let short_turn_segment = self.turn_duration_label("t");

        let mut candidates = Vec::new();
        candidates.push(build_segments([
            Some(model_segment.clone()),
            Some(permission_segment.clone()),
            Some(session_segment.clone()),
            Some(token_segment.clone()),
            branch_segment.clone(),
            Some(cost_segment.clone()),
            turn_segment,
        ]));
        candidates.push(build_segments([
            Some(model_segment.clone()),
            Some(permission_segment),
            Some(token_segment.clone()),
            branch_segment.clone(),
            Some(cost_segment),
            self.turn_duration_label("turn"),
        ]));
        candidates.push(build_segments([
            Some(model_segment.clone()),
            Some(token_segment.clone()),
            branch_segment.clone(),
            Some(short_cost_segment),
            short_turn_segment,
        ]));
        candidates.push(build_segments([
            Some(model_segment.clone()),
            Some(token_segment.clone()),
            branch_segment.clone(),
            Some(self.cost_label()),
        ]));
        candidates.push(build_segments([
            Some(model_segment.clone()),
            Some(token_segment.clone()),
            branch_segment.clone(),
        ]));
        candidates.push(build_segments([Some(model_segment), Some(token_segment)]));

        let line = candidates
            .into_iter()
            .map(|segments| segments.join(" | "))
            .find(|candidate| candidate.chars().count() <= width)
            .unwrap_or_else(|| {
                truncate_with_ellipsis(
                    &build_segments([
                        Some(short_model(&self.model)),
                        Some(format!(
                            "tok:{}",
                            format_token_count(self.combined_usage().total_tokens())
                        )),
                        branch_segment,
                    ])
                    .join(" | "),
                    width,
                )
            });

        pad_to_width(&line, width)
    }

    fn combined_usage(&self) -> TokenUsage {
        TokenUsage {
            input_tokens: self
                .cumulative_usage
                .input_tokens
                .saturating_add(self.current_turn_usage.input_tokens),
            output_tokens: self
                .cumulative_usage
                .output_tokens
                .saturating_add(self.current_turn_usage.output_tokens),
            cache_creation_input_tokens: self
                .cumulative_usage
                .cache_creation_input_tokens
                .saturating_add(self.current_turn_usage.cache_creation_input_tokens),
            cache_read_input_tokens: self
                .cumulative_usage
                .cache_read_input_tokens
                .saturating_add(self.current_turn_usage.cache_read_input_tokens),
        }
    }

    fn cost_label(&self) -> String {
        let usage = self.combined_usage();
        let estimate = pricing_for_model(&self.model).map_or_else(
            || usage.estimate_cost_usd(),
            |pricing| usage.estimate_cost_usd_with_pricing(pricing),
        );
        format_usd(estimate.total_cost_usd())
    }

    fn turn_duration_label(&self, label: &str) -> Option<String> {
        if !self.show_turn_duration {
            return None;
        }

        self.turn_started_at
            .map(|started_at| format!("{label}:{}", format_duration(started_at.elapsed())))
    }
}

fn build_segments<const N: usize>(segments: [Option<String>; N]) -> Vec<String> {
    segments.into_iter().flatten().collect()
}

fn short_model(model: &str) -> String {
    match brand_model_name(model) {
        "simcoe-opus" => "sim-opus".to_string(),
        "simcoe-sonnet" => "sim-sonnet".to_string(),
        "simcoe-haiku" => "sim-haiku".to_string(),
        other => other.to_string(),
    }
}

fn short_permission_mode(permission_mode: &str) -> &'static str {
    match permission_mode {
        "read-only" => "ro",
        "workspace-write" => "write",
        "danger-full-access" => "danger",
        _ => "custom",
    }
}

fn compact_session_id(session_id: &str) -> String {
    session_id.chars().take(10).collect()
}

fn format_token_count(tokens: u32) -> String {
    match tokens {
        0..=999 => tokens.to_string(),
        1_000..=999_999 => format!("{:.1}k", f64::from(tokens) / 1_000.0),
        _ => format!("{:.1}m", f64::from(tokens) / 1_000_000.0),
    }
}

fn format_duration(duration: Duration) -> String {
    let seconds = duration.as_secs();
    if seconds < 60 {
        return format!("{seconds}s");
    }
    if seconds < 3_600 {
        return format!("{}m{:02}s", seconds / 60, seconds % 60);
    }
    format!("{}h{:02}m", seconds / 3_600, (seconds % 3_600) / 60)
}

fn truncate_with_ellipsis(value: &str, width: usize) -> String {
    if width == 0 {
        return String::new();
    }
    if width == 1 {
        return String::from(".");
    }
    if width == 2 {
        return String::from("..");
    }

    let visible = width.saturating_sub(3);
    let mut truncated = value.chars().take(visible).collect::<String>();
    truncated.push_str("...");
    truncated
}

fn pad_to_width(value: &str, width: usize) -> String {
    let visible = value.chars().count();
    if visible >= width {
        return value.chars().take(width).collect();
    }

    let mut padded = String::with_capacity(width);
    padded.push_str(value);
    padded.push_str(&" ".repeat(width - visible));
    padded
}

#[cfg(test)]
mod tests {
    use super::{compact_session_id, format_duration, format_token_count, StatusBarState};
    use runtime::TokenUsage;
    use std::time::{Duration, Instant};

    fn sample_state() -> StatusBarState {
        StatusBarState {
            model: String::from("simcoe-opus-4-6"),
            permission_mode: String::from("workspace-write"),
            session_id: String::from("session-1234567890"),
            git_branch: Some(String::from("main")),
            cumulative_usage: TokenUsage {
                input_tokens: 1_200,
                output_tokens: 800,
                cache_creation_input_tokens: 0,
                cache_read_input_tokens: 0,
            },
            current_turn_usage: TokenUsage::default(),
            show_turn_duration: true,
            turn_started_at: None,
            enabled: false,
        }
    }

    #[test]
    fn renders_full_line_when_width_allows() {
        let line = sample_state().render_line(120);

        assert!(line.contains("sim-opus"));
        assert!(line.contains("write"));
        assert!(line.contains("tok:2.0k"));
        assert!(line.contains("git:main"));
        assert!(line.contains("cost:$"));
    }

    #[test]
    fn trims_line_for_narrow_terminals() {
        let line = sample_state().render_line(24);

        assert_eq!(line.chars().count(), 24);
        assert!(line.contains("tok:"));
    }

    #[test]
    fn keeps_branch_and_cost_on_medium_widths() {
        let line = sample_state().render_line(40);

        assert!(line.contains("git:main"));
        assert!(line.contains('$'));
    }

    #[test]
    fn shows_turn_duration_when_active() {
        let mut state = sample_state();
        state.turn_started_at = Instant::now().checked_sub(Duration::from_secs(125));

        let line = state.render_line(120);

        assert!(line.contains("turn:2m05s"));
    }

    #[test]
    fn shortens_session_ids_and_counts() {
        assert_eq!(compact_session_id("session-1234567890"), "session-12");
        assert_eq!(format_token_count(999), "999");
        assert_eq!(format_token_count(1_250), "1.2k");
    }

    #[test]
    fn formats_turn_duration_labels() {
        assert_eq!(format_duration(Duration::from_secs(42)), "42s");
        assert_eq!(format_duration(Duration::from_secs(125)), "2m05s");
    }
}
