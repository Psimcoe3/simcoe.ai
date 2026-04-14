use std::env;
use std::fs;
use std::io;
use std::path::{Path, PathBuf};
use std::time::{SystemTime, UNIX_EPOCH};

use crate::{ContentBlock, MessageRole, Session};

#[derive(Debug, Clone, PartialEq, Eq)]
pub struct SessionHandle {
    pub id: String,
    pub path: PathBuf,
}

#[derive(Debug, Clone, PartialEq, Eq)]
pub struct ManagedSessionSummary {
    pub id: String,
    pub path: PathBuf,
    pub modified_epoch_secs: u64,
    pub message_count: usize,
}

pub fn sessions_dir() -> Result<PathBuf, Box<dyn std::error::Error>> {
    let cwd = env::current_dir()?;
    let path = cwd.join(".simcoe").join("sessions");
    fs::create_dir_all(&path)?;
    Ok(path)
}

fn active_session_marker_path() -> Result<PathBuf, Box<dyn std::error::Error>> {
    Ok(sessions_dir()?.join(".active"))
}

fn absolute_session_path(path: &Path) -> Result<PathBuf, Box<dyn std::error::Error>> {
    if path.is_absolute() {
        Ok(path.to_path_buf())
    } else {
        Ok(env::current_dir()?.join(path))
    }
}

pub fn session_handle_from_path(path: &Path) -> SessionHandle {
    let id = path
        .file_stem()
        .and_then(|value| value.to_str())
        .unwrap_or("unknown")
        .to_string();
    SessionHandle {
        id,
        path: path.to_path_buf(),
    }
}

pub fn create_managed_session_handle() -> Result<SessionHandle, Box<dyn std::error::Error>> {
    let id = generate_session_id();
    let path = sessions_dir()?.join(format!("{id}.json"));
    Ok(SessionHandle { id, path })
}

pub fn load_active_session_handle(
) -> Result<Option<SessionHandle>, Box<dyn std::error::Error>> {
    let marker_path = active_session_marker_path()?;
    let reference = match fs::read_to_string(&marker_path) {
        Ok(reference) => reference,
        Err(error) if error.kind() == io::ErrorKind::NotFound => return Ok(None),
        Err(error) => return Err(error.into()),
    };
    let reference = reference.trim();
    if reference.is_empty() {
        return Ok(None);
    }

    let path = absolute_session_path(Path::new(reference))?;
    if !path.exists() {
        let _ = fs::remove_file(marker_path);
        return Ok(None);
    }

    Ok(Some(session_handle_from_path(&path)))
}

pub fn set_active_session_handle(
    handle: &SessionHandle,
) -> Result<(), Box<dyn std::error::Error>> {
    let marker_path = active_session_marker_path()?;
    let session_path = absolute_session_path(&handle.path)?;
    fs::write(marker_path, session_path.display().to_string())?;
    Ok(())
}

pub fn resolve_session_reference(
    reference: &str,
) -> Result<SessionHandle, Box<dyn std::error::Error>> {
    let direct = PathBuf::from(reference);
    let path = if direct.exists() {
        direct
    } else {
        sessions_dir()?.join(format!("{reference}.json"))
    };
    if !path.exists() {
        return Err(format!("session not found: {reference}").into());
    }
    Ok(session_handle_from_path(&path))
}

pub fn list_managed_sessions(
) -> Result<Vec<ManagedSessionSummary>, Box<dyn std::error::Error>> {
    let mut sessions = Vec::new();
    for entry in fs::read_dir(sessions_dir()?)? {
        let entry = entry?;
        let path = entry.path();
        if path.extension().and_then(|ext| ext.to_str()) != Some("json") {
            continue;
        }
        let metadata = entry.metadata()?;
        let modified_epoch_secs = metadata
            .modified()
            .ok()
            .and_then(|time| time.duration_since(UNIX_EPOCH).ok())
            .map(|duration| duration.as_secs())
            .unwrap_or_default();
        let message_count = Session::load_from_path(&path)
            .map(|session| session.messages.len())
            .unwrap_or_default();
        let id = path
            .file_stem()
            .and_then(|value| value.to_str())
            .unwrap_or("unknown")
            .to_string();
        sessions.push(ManagedSessionSummary {
            id,
            path,
            modified_epoch_secs,
            message_count,
        });
    }
    sessions.sort_by(|left, right| right.modified_epoch_secs.cmp(&left.modified_epoch_secs));
    Ok(sessions)
}

pub fn load_active_managed_session(
) -> Result<(SessionHandle, Session), Box<dyn std::error::Error>> {
    let handle = load_active_session_handle()?
        .ok_or_else(|| String::from("no active managed session to export"))?;
    let session = Session::load_from_path(&handle.path)?;
    Ok((handle, session))
}

pub fn switch_managed_session(
    target: &str,
) -> Result<(SessionHandle, usize), Box<dyn std::error::Error>> {
    let handle = resolve_session_reference(target)?;
    let message_count = Session::load_from_path(&handle.path)?.messages.len();
    set_active_session_handle(&handle)?;
    Ok((handle, message_count))
}

pub fn export_active_session(
    requested_path: Option<&str>,
) -> Result<(SessionHandle, PathBuf, usize), Box<dyn std::error::Error>> {
    let (handle, session) = load_active_managed_session()?;
    let export_path = resolve_export_path(requested_path, &session)?;
    fs::write(&export_path, render_export_text(&session))?;
    Ok((handle, export_path, session.messages.len()))
}

pub fn render_export_text(session: &Session) -> String {
    let mut lines = vec!["# Conversation Export".to_string(), String::new()];
    for (index, message) in session.messages.iter().enumerate() {
        let role = match message.role {
            MessageRole::System => "system",
            MessageRole::User => "user",
            MessageRole::Assistant => "assistant",
            MessageRole::Tool => "tool",
        };
        lines.push(format!("## {}. {role}", index + 1));
        for block in &message.blocks {
            match block {
                ContentBlock::Text { text } => lines.push(text.clone()),
                ContentBlock::ToolUse { id, name, input } => {
                    lines.push(format!("[tool_use id={id} name={name}] {input}"));
                }
                ContentBlock::ToolResult {
                    tool_use_id,
                    tool_name,
                    output,
                    is_error,
                } => {
                    lines.push(format!(
                        "[tool_result id={tool_use_id} name={tool_name} error={is_error}] {output}"
                    ));
                }
            }
        }
        lines.push(String::new());
    }
    lines.join("\n")
}

pub fn resolve_export_path(
    requested_path: Option<&str>,
    session: &Session,
) -> Result<PathBuf, Box<dyn std::error::Error>> {
    let cwd = env::current_dir()?;
    let file_name = requested_path.map_or_else(|| default_export_filename(session), ToOwned::to_owned);
    let final_name = if Path::new(&file_name)
        .extension()
        .is_some_and(|ext| ext.eq_ignore_ascii_case("txt"))
    {
        file_name
    } else {
        format!("{file_name}.txt")
    };
    Ok(cwd.join(final_name))
}

fn generate_session_id() -> String {
    let millis = SystemTime::now()
        .duration_since(UNIX_EPOCH)
        .map(|duration| duration.as_millis())
        .unwrap_or_default();
    format!("session-{millis}")
}

fn default_export_filename(session: &Session) -> String {
    let stem = session
        .messages
        .iter()
        .find_map(|message| match message.role {
            MessageRole::User => message.blocks.iter().find_map(|block| match block {
                ContentBlock::Text { text } => Some(text.as_str()),
                _ => None,
            }),
            _ => None,
        })
        .map_or("conversation", |text| {
            text.lines().next().unwrap_or("conversation")
        })
        .chars()
        .map(|ch| {
            if ch.is_ascii_alphanumeric() {
                ch.to_ascii_lowercase()
            } else {
                '-'
            }
        })
        .collect::<String>()
        .split('-')
        .filter(|part| !part.is_empty())
        .take(8)
        .collect::<Vec<_>>()
        .join("-");
    let fallback = if stem.is_empty() {
        "conversation"
    } else {
        &stem
    };
    format!("{fallback}.txt")
}