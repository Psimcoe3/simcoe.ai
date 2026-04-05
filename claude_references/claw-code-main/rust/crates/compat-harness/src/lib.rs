use std::fs;
use std::path::{Path, PathBuf};

use commands::{CommandManifestEntry, CommandRegistry, CommandSource};
use runtime::{BootstrapPhase, BootstrapPlan};
use serde::Deserialize;
use tools::{ToolManifestEntry, ToolRegistry, ToolSource};

#[derive(Debug, Clone, PartialEq, Eq)]
pub struct UpstreamPaths {
    repo_root: PathBuf,
}

impl UpstreamPaths {
    #[must_use]
    pub fn from_repo_root(repo_root: impl Into<PathBuf>) -> Self {
        Self {
            repo_root: repo_root.into(),
        }
    }

    #[must_use]
    pub fn from_workspace_dir(workspace_dir: impl AsRef<Path>) -> Self {
        let workspace_dir = workspace_dir
            .as_ref()
            .canonicalize()
            .unwrap_or_else(|_| workspace_dir.as_ref().to_path_buf());
        let primary_repo_root = workspace_dir
            .parent()
            .map_or_else(|| PathBuf::from(".."), Path::to_path_buf);
        let repo_root = resolve_upstream_repo_root(&primary_repo_root);
        Self { repo_root }
    }

    #[must_use]
    pub fn commands_path(&self) -> PathBuf {
        self.repo_root.join("src/commands.ts")
    }

    #[must_use]
    pub fn tools_path(&self) -> PathBuf {
        self.repo_root.join("src/tools.ts")
    }

    #[must_use]
    pub fn cli_path(&self) -> PathBuf {
        self.repo_root.join("src/entrypoints/cli.tsx")
    }

    #[must_use]
    pub fn commands_snapshot_path(&self) -> PathBuf {
        self.repo_root
            .join("src/reference_data/commands_snapshot.json")
    }

    #[must_use]
    pub fn plugins_snapshot_path(&self) -> PathBuf {
        self.repo_root
            .join("src/reference_data/subsystems/plugins.json")
    }
}

#[derive(Debug, Clone, PartialEq, Eq)]
pub struct ExtractedManifest {
    pub commands: CommandRegistry,
    pub tools: ToolRegistry,
    pub bootstrap: BootstrapPlan,
}

#[derive(Debug, Clone, Copy, PartialEq, Eq, PartialOrd, Ord)]
pub enum PluginSurfaceKind {
    Command,
    Module,
}

impl PluginSurfaceKind {
    #[must_use]
    pub fn as_str(self) -> &'static str {
        match self {
            Self::Command => "command",
            Self::Module => "module",
        }
    }
}

#[derive(Debug, Clone, PartialEq, Eq)]
pub struct PluginSurfaceSummary {
    pub name: String,
    pub kind: PluginSurfaceKind,
    pub summary: String,
    pub source_hints: Vec<String>,
    pub archived_file_count: usize,
}

#[derive(Debug, Clone, PartialEq, Eq)]
pub struct PluginCatalog {
    pub archive_name: String,
    pub package_name: String,
    pub module_count: usize,
    pub sample_files: Vec<String>,
    pub surfaces: Vec<PluginSurfaceSummary>,
}

#[derive(Debug, Deserialize)]
struct SnapshotEntry {
    name: String,
    source_hint: String,
    responsibility: String,
}

#[derive(Debug, Deserialize)]
struct PluginSubsystemSnapshot {
    archive_name: String,
    package_name: String,
    module_count: usize,
    sample_files: Vec<String>,
}

fn resolve_upstream_repo_root(primary_repo_root: &Path) -> PathBuf {
    let candidates = upstream_repo_candidates(primary_repo_root);
    candidates
        .into_iter()
        .find(|candidate| candidate.join("src/commands.ts").is_file())
        .unwrap_or_else(|| primary_repo_root.to_path_buf())
}

fn upstream_repo_candidates(primary_repo_root: &Path) -> Vec<PathBuf> {
    let mut candidates = vec![primary_repo_root.to_path_buf()];

    if let Some(explicit) = std::env::var_os("SIMCOE_AI_UPSTREAM") {
        candidates.push(PathBuf::from(explicit));
    }

    for ancestor in primary_repo_root.ancestors().take(4) {
        candidates.push(ancestor.join("claw-code"));
        candidates.push(ancestor.join("clawd-code"));
    }

    candidates.push(primary_repo_root.join("reference-source").join("claw-code"));
    candidates.push(primary_repo_root.join("vendor").join("claw-code"));

    let mut deduped = Vec::new();
    for candidate in candidates {
        if !deduped.iter().any(|seen: &PathBuf| seen == &candidate) {
            deduped.push(candidate);
        }
    }
    deduped
}

pub fn extract_manifest(paths: &UpstreamPaths) -> std::io::Result<ExtractedManifest> {
    let commands_source = fs::read_to_string(paths.commands_path())?;
    let tools_source = fs::read_to_string(paths.tools_path())?;
    let cli_source = fs::read_to_string(paths.cli_path())?;

    Ok(ExtractedManifest {
        commands: extract_commands(&commands_source),
        tools: extract_tools(&tools_source),
        bootstrap: extract_bootstrap_plan(&cli_source),
    })
}

pub fn load_plugin_catalog(paths: &UpstreamPaths) -> std::io::Result<PluginCatalog> {
    let subsystem = read_json::<PluginSubsystemSnapshot>(&paths.plugins_snapshot_path())?;
    let commands = read_json::<Vec<SnapshotEntry>>(&paths.commands_snapshot_path())?;

    let mut grouped =
        std::collections::BTreeMap::<(PluginSurfaceKind, String), PluginSurfaceSummary>::new();

    for entry in commands.into_iter().filter(|entry| {
        entry.source_hint.starts_with("commands/plugin/")
            || entry.source_hint.starts_with("commands/reload-plugins/")
    }) {
        let key = (PluginSurfaceKind::Command, entry.name.clone());
        let surface = grouped.entry(key).or_insert_with(|| PluginSurfaceSummary {
            name: entry.name.clone(),
            kind: PluginSurfaceKind::Command,
            summary: entry.responsibility.clone(),
            source_hints: Vec::new(),
            archived_file_count: 0,
        });
        surface.archived_file_count += 1;
        if !surface
            .source_hints
            .iter()
            .any(|hint| hint == &entry.source_hint)
        {
            surface.source_hints.push(entry.source_hint);
        }
    }

    for sample_file in &subsystem.sample_files {
        let name = plugin_surface_name_from_path(sample_file);
        grouped.insert(
            (PluginSurfaceKind::Module, name.clone()),
            PluginSurfaceSummary {
                name,
                kind: PluginSurfaceKind::Module,
                summary: format!(
                    "Archived plugin subsystem module from {}",
                    subsystem.archive_name
                ),
                source_hints: vec![sample_file.clone()],
                archived_file_count: 1,
            },
        );
    }

    let mut surfaces = grouped.into_values().collect::<Vec<_>>();
    surfaces.sort_by(|left, right| {
        left.kind
            .as_str()
            .cmp(right.kind.as_str())
            .then_with(|| left.name.cmp(&right.name))
    });

    Ok(PluginCatalog {
        archive_name: subsystem.archive_name,
        package_name: subsystem.package_name,
        module_count: subsystem.module_count,
        sample_files: subsystem.sample_files,
        surfaces,
    })
}

pub fn load_plugin_catalog_from_cwd() -> std::io::Result<PluginCatalog> {
    let cwd = std::env::current_dir()?;
    let repo_root = find_snapshot_repo_root(&cwd).ok_or_else(|| {
        std::io::Error::new(
            std::io::ErrorKind::NotFound,
            "could not locate archived plugin snapshots from the current directory",
        )
    })?;
    load_plugin_catalog(&UpstreamPaths::from_repo_root(repo_root))
}

pub fn load_plugin_surface_from_cwd(requested: &str) -> Result<PluginSurfaceSummary, String> {
    let requested = requested.trim();
    if requested.is_empty() {
        return Err(String::from("plugin surface name must not be empty"));
    }

    let catalog = load_plugin_catalog_from_cwd().map_err(|error| error.to_string())?;
    let wanted = canonical_token(requested);
    let matches = catalog
        .surfaces
        .into_iter()
        .filter(|surface| {
            canonical_token(&surface.name) == wanted
                || surface
                    .source_hints
                    .iter()
                    .any(|hint| canonical_token(hint) == wanted)
        })
        .collect::<Vec<_>>();

    match matches.as_slice() {
        [surface] => Ok(surface.clone()),
        [] => Err(format!("unknown plugin surface: {requested}")),
        _ => Err(format!(
            "multiple plugin surfaces matched '{requested}'; use a more specific name"
        )),
    }
}

#[must_use]
pub fn extract_commands(source: &str) -> CommandRegistry {
    let mut entries = Vec::new();
    let mut in_internal_block = false;

    for raw_line in source.lines() {
        let line = raw_line.trim();

        if line.starts_with("export const INTERNAL_ONLY_COMMANDS = [") {
            in_internal_block = true;
            continue;
        }

        if in_internal_block {
            if line.starts_with(']') {
                in_internal_block = false;
                continue;
            }
            if let Some(name) = first_identifier(line) {
                entries.push(CommandManifestEntry {
                    name,
                    source: CommandSource::InternalOnly,
                });
            }
            continue;
        }

        if line.starts_with("import ") {
            for imported in imported_symbols(line) {
                entries.push(CommandManifestEntry {
                    name: imported,
                    source: CommandSource::Builtin,
                });
            }
        }

        if line.contains("feature('") && line.contains("./commands/") {
            if let Some(name) = first_assignment_identifier(line) {
                entries.push(CommandManifestEntry {
                    name,
                    source: CommandSource::FeatureGated,
                });
            }
        }
    }

    dedupe_commands(entries)
}

#[must_use]
pub fn extract_tools(source: &str) -> ToolRegistry {
    let mut entries = Vec::new();

    for raw_line in source.lines() {
        let line = raw_line.trim();
        if line.starts_with("import ") && line.contains("./tools/") {
            for imported in imported_symbols(line) {
                if imported.ends_with("Tool") {
                    entries.push(ToolManifestEntry {
                        name: imported,
                        source: ToolSource::Base,
                    });
                }
            }
        }

        if line.contains("feature('") && line.contains("Tool") {
            if let Some(name) = first_assignment_identifier(line) {
                if name.ends_with("Tool") || name.ends_with("Tools") {
                    entries.push(ToolManifestEntry {
                        name,
                        source: ToolSource::Conditional,
                    });
                }
            }
        }
    }

    dedupe_tools(entries)
}

#[must_use]
pub fn extract_bootstrap_plan(source: &str) -> BootstrapPlan {
    let mut phases = vec![BootstrapPhase::CliEntry];

    if source.contains("--version") {
        phases.push(BootstrapPhase::FastPathVersion);
    }
    if source.contains("startupProfiler") {
        phases.push(BootstrapPhase::StartupProfiler);
    }
    if source.contains("--dump-system-prompt") {
        phases.push(BootstrapPhase::SystemPromptFastPath);
    }
    if source.contains("in-chrome-mcp") {
        phases.push(BootstrapPhase::ChromeMcpFastPath);
    }
    if source.contains("--daemon-worker") {
        phases.push(BootstrapPhase::DaemonWorkerFastPath);
    }
    if source.contains("remote-control") {
        phases.push(BootstrapPhase::BridgeFastPath);
    }
    if source.contains("args[0] === 'daemon'") {
        phases.push(BootstrapPhase::DaemonFastPath);
    }
    if source.contains("args[0] === 'ps'") || source.contains("args.includes('--bg')") {
        phases.push(BootstrapPhase::BackgroundSessionFastPath);
    }
    if source.contains("args[0] === 'new' || args[0] === 'list' || args[0] === 'reply'") {
        phases.push(BootstrapPhase::TemplateFastPath);
    }
    if source.contains("environment-runner") {
        phases.push(BootstrapPhase::EnvironmentRunnerFastPath);
    }
    phases.push(BootstrapPhase::MainRuntime);

    BootstrapPlan::from_phases(phases)
}

fn imported_symbols(line: &str) -> Vec<String> {
    let Some(after_import) = line.strip_prefix("import ") else {
        return Vec::new();
    };

    let before_from = after_import
        .split(" from ")
        .next()
        .unwrap_or_default()
        .trim();
    if before_from.starts_with('{') {
        return before_from
            .trim_matches(|c| c == '{' || c == '}')
            .split(',')
            .filter_map(|part| {
                let trimmed = part.trim();
                if trimmed.is_empty() {
                    return None;
                }
                Some(trimmed.split_whitespace().next()?.to_string())
            })
            .collect();
    }

    let first = before_from.split(',').next().unwrap_or_default().trim();
    if first.is_empty() {
        Vec::new()
    } else {
        vec![first.to_string()]
    }
}

fn first_assignment_identifier(line: &str) -> Option<String> {
    let trimmed = line.trim_start();
    let candidate = trimmed.split('=').next()?.trim();
    first_identifier(candidate)
}

fn first_identifier(line: &str) -> Option<String> {
    let mut out = String::new();
    for ch in line.chars() {
        if ch.is_ascii_alphanumeric() || ch == '_' || ch == '-' {
            out.push(ch);
        } else if !out.is_empty() {
            break;
        }
    }
    (!out.is_empty()).then_some(out)
}

fn dedupe_commands(entries: Vec<CommandManifestEntry>) -> CommandRegistry {
    let mut deduped = Vec::new();
    for entry in entries {
        let exists = deduped.iter().any(|seen: &CommandManifestEntry| {
            seen.name == entry.name && seen.source == entry.source
        });
        if !exists {
            deduped.push(entry);
        }
    }
    CommandRegistry::new(deduped)
}

fn dedupe_tools(entries: Vec<ToolManifestEntry>) -> ToolRegistry {
    let mut deduped = Vec::new();
    for entry in entries {
        let exists = deduped
            .iter()
            .any(|seen: &ToolManifestEntry| seen.name == entry.name && seen.source == entry.source);
        if !exists {
            deduped.push(entry);
        }
    }
    ToolRegistry::new(deduped)
}

fn read_json<T: serde::de::DeserializeOwned>(path: &Path) -> std::io::Result<T> {
    let contents = fs::read_to_string(path)?;
    serde_json::from_str(&contents).map_err(|error| {
        std::io::Error::new(
            std::io::ErrorKind::InvalidData,
            format!("failed to parse {}: {error}", path.display()),
        )
    })
}

fn find_snapshot_repo_root(start: &Path) -> Option<PathBuf> {
    start.ancestors().find_map(|ancestor| {
        let commands = ancestor.join("src/reference_data/commands_snapshot.json");
        let plugins = ancestor.join("src/reference_data/subsystems/plugins.json");
        (commands.is_file() && plugins.is_file()).then(|| ancestor.to_path_buf())
    })
}

fn plugin_surface_name_from_path(path: &str) -> String {
    let path = Path::new(path);
    match path.file_stem().and_then(|stem| stem.to_str()) {
        Some("index") => path
            .parent()
            .and_then(Path::file_name)
            .and_then(|name| name.to_str())
            .unwrap_or("index")
            .to_string(),
        Some(stem) => stem.to_string(),
        None => path.to_string_lossy().to_string(),
    }
}

fn canonical_token(value: &str) -> String {
    value
        .chars()
        .filter(char::is_ascii_alphanumeric)
        .flat_map(char::to_lowercase)
        .collect()
}

#[cfg(test)]
mod tests {
    use super::*;

    fn fixture_paths() -> UpstreamPaths {
        let workspace_dir = Path::new(env!("CARGO_MANIFEST_DIR")).join("../..");
        UpstreamPaths::from_workspace_dir(workspace_dir)
    }

    fn has_upstream_fixture(paths: &UpstreamPaths) -> bool {
        paths.commands_path().is_file()
            && paths.tools_path().is_file()
            && paths.cli_path().is_file()
    }

    #[test]
    fn extracts_non_empty_manifests_from_upstream_repo() {
        let paths = fixture_paths();
        if !has_upstream_fixture(&paths) {
            return;
        }
        let manifest = extract_manifest(&paths).expect("manifest should load");
        assert!(!manifest.commands.entries().is_empty());
        assert!(!manifest.tools.entries().is_empty());
        assert!(!manifest.bootstrap.phases().is_empty());
    }

    #[test]
    fn detects_known_upstream_command_symbols() {
        let paths = fixture_paths();
        if !paths.commands_path().is_file() {
            return;
        }
        let commands =
            extract_commands(&fs::read_to_string(paths.commands_path()).expect("commands.ts"));
        let names: Vec<_> = commands
            .entries()
            .iter()
            .map(|entry| entry.name.as_str())
            .collect();
        assert!(names.contains(&"addDir"));
        assert!(names.contains(&"review"));
        assert!(!names.contains(&"INTERNAL_ONLY_COMMANDS"));
    }

    #[test]
    fn detects_known_upstream_tool_symbols() {
        let paths = fixture_paths();
        if !paths.tools_path().is_file() {
            return;
        }
        let tools = extract_tools(&fs::read_to_string(paths.tools_path()).expect("tools.ts"));
        let names: Vec<_> = tools
            .entries()
            .iter()
            .map(|entry| entry.name.as_str())
            .collect();
        assert!(names.contains(&"AgentTool"));
        assert!(names.contains(&"BashTool"));
    }

    #[test]
    fn loads_plugin_catalog_and_surface_from_snapshots() {
        let root = std::env::temp_dir().join(format!(
            "compat-harness-plugin-{}",
            std::time::SystemTime::now()
                .duration_since(std::time::UNIX_EPOCH)
                .expect("time")
                .as_nanos()
        ));
        let commands_dir = root.join("src/reference_data");
        let subsystems_dir = commands_dir.join("subsystems");
        let rust_dir = root.join("rust");
        fs::create_dir_all(&subsystems_dir).expect("create snapshot dirs");
        fs::create_dir_all(&rust_dir).expect("create rust dir");
        fs::write(
            commands_dir.join("commands_snapshot.json"),
            r#"[
  {"name":"plugin","source_hint":"commands/plugin/index.tsx","responsibility":"plugin index"},
  {"name":"plugin","source_hint":"commands/plugin/plugin.tsx","responsibility":"plugin flow"},
  {"name":"reload-plugins","source_hint":"commands/reload-plugins/index.ts","responsibility":"reload index"},
  {"name":"reload-plugins","source_hint":"commands/reload-plugins/reload-plugins.ts","responsibility":"reload flow"},
  {"name":"other","source_hint":"commands/other/index.ts","responsibility":"other"}
]"#,
        )
        .expect("write command snapshot");
        fs::write(
            subsystems_dir.join("plugins.json"),
            r#"{
  "archive_name": "plugins",
  "package_name": "plugins",
  "module_count": 2,
  "sample_files": ["plugins/builtinPlugins.ts", "plugins/bundled/index.ts"]
}"#,
        )
        .expect("write plugin snapshot");

        let catalog = load_plugin_catalog(&UpstreamPaths::from_repo_root(&root))
            .expect("catalog should load");
        assert_eq!(catalog.archive_name, "plugins");
        assert_eq!(catalog.module_count, 2);
        assert!(catalog
            .surfaces
            .iter()
            .any(|surface| surface.name == "plugin"));
        assert!(catalog
            .surfaces
            .iter()
            .any(|surface| surface.name == "reload-plugins"));
        assert!(catalog
            .surfaces
            .iter()
            .any(|surface| surface.name == "builtinPlugins"));
        assert!(catalog
            .surfaces
            .iter()
            .any(|surface| surface.name == "bundled"));

        let original_cwd = std::env::current_dir().expect("cwd");
        std::env::set_current_dir(&rust_dir).expect("set cwd");

        let plugin = load_plugin_surface_from_cwd("plugin").expect("plugin surface should load");
        assert_eq!(plugin.kind, PluginSurfaceKind::Command);
        assert_eq!(plugin.archived_file_count, 2);
        assert!(plugin
            .source_hints
            .iter()
            .any(|hint| hint == "commands/plugin/index.tsx"));

        let module = load_plugin_surface_from_cwd("bundled").expect("module surface should load");
        assert_eq!(module.kind, PluginSurfaceKind::Module);
        assert_eq!(module.archived_file_count, 1);
        assert_eq!(
            module.source_hints,
            vec![String::from("plugins/bundled/index.ts")]
        );

        std::env::set_current_dir(&original_cwd).expect("restore cwd");
        let _ = fs::remove_dir_all(root);
    }
}
