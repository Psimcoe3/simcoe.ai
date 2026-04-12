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
    pub fn tools_snapshot_path(&self) -> PathBuf {
        self.repo_root
            .join("src/reference_data/tools_snapshot.json")
    }

    #[must_use]
    pub fn plugins_snapshot_path(&self) -> PathBuf {
        self.repo_root
            .join("src/reference_data/subsystems/plugins.json")
    }

    #[must_use]
    pub fn skills_snapshot_path(&self) -> PathBuf {
        self.repo_root
            .join("src/reference_data/subsystems/skills.json")
    }

    #[must_use]
    pub fn cli_snapshot_path(&self) -> PathBuf {
        self.repo_root
            .join("src/reference_data/subsystems/cli.json")
    }

    #[must_use]
    pub fn upstreamproxy_snapshot_path(&self) -> PathBuf {
        self.repo_root
            .join("src/reference_data/subsystems/upstreamproxy.json")
    }

    #[must_use]
    pub fn parity_manifest_path(&self) -> PathBuf {
        self.repo_root
            .join("src/reference_data/parity_manifest.json")
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

#[derive(Debug, Clone, PartialEq, Eq)]
pub struct ArchivedSkillSummary {
    pub name: String,
    pub summary: String,
    pub source_hints: Vec<String>,
    pub archived_file_count: usize,
}

#[derive(Debug, Clone, PartialEq, Eq)]
pub struct SkillCatalog {
    pub archive_name: String,
    pub package_name: String,
    pub module_count: usize,
    pub bundled_skill_samples: Vec<ArchivedSkillSummary>,
    pub support_modules: Vec<String>,
}

#[derive(Debug, Clone, PartialEq, Eq)]
pub struct RemoteCommandSummary {
    pub name: String,
    pub summary: String,
    pub source_hints: Vec<String>,
    pub archived_file_count: usize,
}

#[derive(Debug, Clone, PartialEq, Eq)]
pub struct ArchivedRemoteProxyCatalog {
    pub archive_name: String,
    pub package_name: String,
    pub module_count: usize,
    pub files: Vec<String>,
}

#[derive(Debug, Clone, PartialEq, Eq)]
pub struct RemoteCatalog {
    pub archive_name: String,
    pub package_name: String,
    pub module_count: usize,
    pub transport_files: Vec<String>,
    pub upstream_proxy: Option<ArchivedRemoteProxyCatalog>,
    pub commands: Vec<RemoteCommandSummary>,
}

#[derive(Debug, Clone, PartialEq, Eq)]
pub struct ArchivedToolFamilySummary {
    pub name: String,
    pub summary: String,
    pub source_hints: Vec<String>,
    pub archived_file_count: usize,
}

#[derive(Debug, Clone, PartialEq, Eq)]
pub struct ToolCatalog {
    pub archived_file_count: usize,
    pub families: Vec<ArchivedToolFamilySummary>,
}

#[derive(Debug, Clone, Copy, PartialEq, Eq, Deserialize)]
#[serde(rename_all = "kebab-case")]
pub enum ParityStatus {
    Implemented,
    Partial,
    InspectionOnly,
    DiagnosticOnly,
    Missing,
}

#[derive(Debug, Clone, PartialEq, Eq, Deserialize)]
pub struct ParitySlashCommand {
    pub name: String,
    pub resume_supported: bool,
}

#[derive(Debug, Clone, PartialEq, Eq, Deserialize)]
pub struct ParityCliCommand {
    pub name: String,
}

#[derive(Debug, Clone, PartialEq, Eq, Deserialize)]
pub struct ParitySubsystem {
    pub name: String,
    pub status: ParityStatus,
}

#[derive(Debug, Clone, PartialEq, Eq, Deserialize)]
pub struct ParityManifest {
    pub slash_commands: Vec<ParitySlashCommand>,
    pub named_cli_subcommands: Vec<ParityCliCommand>,
    pub native_tools: Vec<String>,
    pub subsystems: Vec<ParitySubsystem>,
}

#[derive(Debug, Deserialize)]
struct SnapshotEntry {
    name: String,
    source_hint: String,
    responsibility: String,
}

#[derive(Debug, Deserialize)]
struct ArchivedSubsystemSnapshot {
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

pub fn load_parity_manifest(paths: &UpstreamPaths) -> std::io::Result<ParityManifest> {
    read_json(&paths.parity_manifest_path())
}

pub fn load_plugin_catalog(paths: &UpstreamPaths) -> std::io::Result<PluginCatalog> {
    let subsystem = read_json::<ArchivedSubsystemSnapshot>(&paths.plugins_snapshot_path())?;
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
    let repo_root = find_snapshot_repo_root(&cwd, "plugins.json").ok_or_else(|| {
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

pub fn load_skill_catalog(paths: &UpstreamPaths) -> std::io::Result<SkillCatalog> {
    let subsystem = read_json::<ArchivedSubsystemSnapshot>(&paths.skills_snapshot_path())?;
    let mut bundled_skill_samples = subsystem
        .sample_files
        .iter()
        .filter(|sample| is_bundled_skill_sample_file(sample))
        .map(|sample| ArchivedSkillSummary {
            name: skill_surface_name_from_path(sample),
            summary: format!(
                "Archived bundled skill sample from {}",
                subsystem.archive_name
            ),
            source_hints: vec![sample.clone()],
            archived_file_count: 1,
        })
        .collect::<Vec<_>>();
    bundled_skill_samples.sort_by(|left, right| left.name.cmp(&right.name));

    let mut support_modules = subsystem
        .sample_files
        .iter()
        .filter(|sample| !is_bundled_skill_sample_file(sample))
        .cloned()
        .collect::<Vec<_>>();
    support_modules.sort();

    Ok(SkillCatalog {
        archive_name: subsystem.archive_name,
        package_name: subsystem.package_name,
        module_count: subsystem.module_count,
        bundled_skill_samples,
        support_modules,
    })
}

pub fn load_skill_catalog_from_cwd() -> std::io::Result<SkillCatalog> {
    let cwd = std::env::current_dir()?;
    let repo_root = find_snapshot_repo_root(&cwd, "skills.json").ok_or_else(|| {
        std::io::Error::new(
            std::io::ErrorKind::NotFound,
            "could not locate archived skill snapshots from the current directory",
        )
    })?;
    load_skill_catalog(&UpstreamPaths::from_repo_root(repo_root))
}

pub fn load_archived_skill_from_cwd(requested: &str) -> Result<ArchivedSkillSummary, String> {
    let requested = requested.trim();
    if requested.is_empty() {
        return Err(String::from("skill name must not be empty"));
    }

    let catalog = load_skill_catalog_from_cwd().map_err(|error| error.to_string())?;
    let wanted = canonical_token(requested);
    let matches = catalog
        .bundled_skill_samples
        .into_iter()
        .filter(|skill| {
            canonical_token(&skill.name) == wanted
                || skill
                    .source_hints
                    .iter()
                    .any(|hint| canonical_token(hint) == wanted)
        })
        .collect::<Vec<_>>();

    match matches.as_slice() {
        [skill] => Ok(skill.clone()),
        [] => Err(format!("unknown archived bundled skill: {requested}")),
        _ => Err(format!(
            "multiple archived bundled skills matched '{requested}'; use a more specific name"
        )),
    }
}

pub fn load_remote_catalog(paths: &UpstreamPaths) -> std::io::Result<RemoteCatalog> {
    let subsystem = read_json::<ArchivedSubsystemSnapshot>(&paths.cli_snapshot_path())?;
    let commands = read_json::<Vec<SnapshotEntry>>(&paths.commands_snapshot_path())?;
    let upstream_proxy =
        match read_json::<ArchivedSubsystemSnapshot>(&paths.upstreamproxy_snapshot_path()) {
            Ok(snapshot) => Some(ArchivedRemoteProxyCatalog {
                archive_name: snapshot.archive_name,
                package_name: snapshot.package_name,
                module_count: snapshot.module_count,
                files: snapshot.sample_files,
            }),
            Err(error) if error.kind() == std::io::ErrorKind::NotFound => None,
            Err(error) => return Err(error),
        };

    let mut grouped = std::collections::BTreeMap::<String, RemoteCommandSummary>::new();

    for entry in commands.into_iter().filter(|entry| {
        entry.source_hint.starts_with("commands/remote-env/")
            || entry.source_hint.starts_with("commands/remote-setup/")
    }) {
        let family = command_family_from_source_hint(&entry.source_hint)
            .unwrap_or_else(|| entry.name.clone());
        let surface = grouped
            .entry(family.clone())
            .or_insert_with(|| RemoteCommandSummary {
                name: family.clone(),
                summary: entry.responsibility.clone(),
                source_hints: Vec::new(),
                archived_file_count: 0,
            });
        if canonical_token(&entry.name) == canonical_token(&family) || surface.summary.is_empty() {
            surface.summary = entry.responsibility.clone();
        }
        surface.archived_file_count += 1;
        if !surface
            .source_hints
            .iter()
            .any(|hint| hint == &entry.source_hint)
        {
            surface.source_hints.push(entry.source_hint);
        }
    }

    let mut command_surfaces = grouped.into_values().collect::<Vec<_>>();
    command_surfaces.sort_by(|left, right| left.name.cmp(&right.name));

    let transport_files = subsystem
        .sample_files
        .iter()
        .filter(|file| is_remote_transport_sample_file(file))
        .cloned()
        .collect::<Vec<_>>();

    Ok(RemoteCatalog {
        archive_name: subsystem.archive_name,
        package_name: subsystem.package_name,
        module_count: subsystem.module_count,
        transport_files,
        upstream_proxy,
        commands: command_surfaces,
    })
}

pub fn load_remote_catalog_from_cwd() -> std::io::Result<RemoteCatalog> {
    let cwd = std::env::current_dir()?;
    let repo_root = find_snapshot_repo_root(&cwd, "cli.json").ok_or_else(|| {
        std::io::Error::new(
            std::io::ErrorKind::NotFound,
            "could not locate archived cli snapshots from the current directory",
        )
    })?;
    load_remote_catalog(&UpstreamPaths::from_repo_root(repo_root))
}

pub fn load_remote_command_from_cwd(requested: &str) -> Result<RemoteCommandSummary, String> {
    let requested = requested.trim();
    if requested.is_empty() {
        return Err(String::from("remote command name must not be empty"));
    }

    let catalog = load_remote_catalog_from_cwd().map_err(|error| error.to_string())?;
    let wanted = canonical_token(requested);
    let matches = catalog
        .commands
        .into_iter()
        .filter(|command| {
            canonical_token(&command.name) == wanted
                || command
                    .source_hints
                    .iter()
                    .any(|hint| canonical_token(hint) == wanted)
        })
        .collect::<Vec<_>>();

    match matches.as_slice() {
        [command] => Ok(command.clone()),
        [] => Err(format!("unknown remote command: {requested}")),
        _ => Err(format!(
            "multiple remote commands matched '{requested}'; use a more specific name"
        )),
    }
}

pub fn load_tool_catalog(paths: &UpstreamPaths) -> std::io::Result<ToolCatalog> {
    let entries = read_json::<Vec<SnapshotEntry>>(&paths.tools_snapshot_path())?;
    let mut grouped = std::collections::BTreeMap::<String, ArchivedToolFamilySummary>::new();
    let mut archived_file_count = 0;

    for entry in entries
        .into_iter()
        .filter(|entry| entry.source_hint.starts_with("tools/"))
    {
        archived_file_count += 1;
        let family = tool_family_from_source_hint(&entry.source_hint)
            .unwrap_or_else(|| tool_surface_name_from_path(&entry.source_hint));
        let surface = grouped
            .entry(family.clone())
            .or_insert_with(|| ArchivedToolFamilySummary {
                name: family.clone(),
                summary: entry.responsibility.clone(),
                source_hints: Vec::new(),
                archived_file_count: 0,
            });
        if matches_tool_query(&entry.name, &family) || surface.summary.is_empty() {
            surface.summary = entry.responsibility.clone();
        }
        surface.archived_file_count += 1;
        if !surface
            .source_hints
            .iter()
            .any(|hint| hint == &entry.source_hint)
        {
            surface.source_hints.push(entry.source_hint);
        }
    }

    let mut families = grouped.into_values().collect::<Vec<_>>();
    families.sort_by(|left, right| left.name.cmp(&right.name));

    Ok(ToolCatalog {
        archived_file_count,
        families,
    })
}

pub fn load_tool_catalog_from_cwd() -> std::io::Result<ToolCatalog> {
    let cwd = std::env::current_dir()?;
    let repo_root = find_tools_snapshot_repo_root(&cwd).ok_or_else(|| {
        std::io::Error::new(
            std::io::ErrorKind::NotFound,
            "could not locate archived tool snapshots from the current directory",
        )
    })?;
    load_tool_catalog(&UpstreamPaths::from_repo_root(repo_root))
}

pub fn load_tool_family_from_cwd(requested: &str) -> Result<ArchivedToolFamilySummary, String> {
    let requested = requested.trim();
    if requested.is_empty() {
        return Err(String::from("tool family name must not be empty"));
    }

    let catalog = load_tool_catalog_from_cwd().map_err(|error| error.to_string())?;
    let wanted = canonical_tool_query(requested);
    let requested_path = canonical_token(requested);
    let matches = catalog
        .families
        .into_iter()
        .filter(|family| {
            matches_tool_query(&family.name, requested)
                || family
                    .source_hints
                    .iter()
                    .any(|hint| canonical_token(hint) == requested_path)
                || canonical_tool_query(&family.name) == wanted
        })
        .collect::<Vec<_>>();

    match matches.as_slice() {
        [family] => Ok(family.clone()),
        [] => Err(format!("unknown tool family: {requested}")),
        _ => Err(format!(
            "multiple tool families matched '{requested}'; use a more specific name"
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

fn find_snapshot_repo_root(start: &Path, subsystem_snapshot: &str) -> Option<PathBuf> {
    start.ancestors().find_map(|ancestor| {
        let commands = ancestor.join("src/reference_data/commands_snapshot.json");
        let subsystem = ancestor
            .join("src/reference_data/subsystems")
            .join(subsystem_snapshot);
        (commands.is_file() && subsystem.is_file()).then(|| ancestor.to_path_buf())
    })
}

fn find_tools_snapshot_repo_root(start: &Path) -> Option<PathBuf> {
    start.ancestors().find_map(|ancestor| {
        ancestor
            .join("src/reference_data/tools_snapshot.json")
            .is_file()
            .then(|| ancestor.to_path_buf())
    })
}

fn command_family_from_source_hint(source_hint: &str) -> Option<String> {
    let mut parts = source_hint.split('/');
    match (parts.next(), parts.next()) {
        (Some("commands"), Some(family)) if !family.is_empty() => Some(family.to_string()),
        _ => None,
    }
}

fn tool_family_from_source_hint(source_hint: &str) -> Option<String> {
    let trimmed = source_hint.strip_prefix("tools/")?;
    let mut parts = trimmed.split('/');
    let first = parts.next()?;
    if parts.next().is_some() {
        Some(first.to_string())
    } else {
        Some(tool_surface_name_from_path(first))
    }
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

fn tool_surface_name_from_path(path: &str) -> String {
    let path = Path::new(path);
    match path.file_stem().and_then(|stem| stem.to_str()) {
        Some(stem) => stem.to_string(),
        None => path.to_string_lossy().to_string(),
    }
}

fn skill_surface_name_from_path(path: &str) -> String {
    let path = Path::new(path);
    match path.file_stem().and_then(|stem| stem.to_str()) {
        Some(stem) => stem.to_string(),
        None => path.to_string_lossy().to_string(),
    }
}

fn is_remote_transport_sample_file(path: &str) -> bool {
    path == "cli/remoteIO.ts"
        || path == "cli/structuredIO.ts"
        || path.starts_with("cli/transports/")
}

fn is_bundled_skill_sample_file(path: &str) -> bool {
    path.starts_with("skills/bundled/")
        && Path::new(path)
            .file_stem()
            .and_then(|stem| stem.to_str())
            .is_some_and(|stem| stem != "index")
}

fn canonical_token(value: &str) -> String {
    value
        .chars()
        .filter(char::is_ascii_alphanumeric)
        .flat_map(char::to_lowercase)
        .collect()
}

fn canonical_tool_query(value: &str) -> String {
    let canonical = canonical_token(value);
    canonical
        .strip_suffix("tool")
        .unwrap_or(canonical.as_str())
        .to_string()
}

fn matches_tool_query(value: &str, requested: &str) -> bool {
    canonical_tool_query(value) == canonical_tool_query(requested)
}

#[cfg(test)]
mod tests {
    use super::*;
    use std::sync::{Mutex, OnceLock};

    fn env_lock() -> &'static Mutex<()> {
        static LOCK: OnceLock<Mutex<()>> = OnceLock::new();
        LOCK.get_or_init(|| Mutex::new(()))
    }

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
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
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

    #[test]
    fn loads_skill_catalog_and_archived_skill_from_snapshots() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let root = std::env::temp_dir().join(format!(
            "compat-harness-skills-{}",
            std::time::SystemTime::now()
                .duration_since(std::time::UNIX_EPOCH)
                .expect("time")
                .as_nanos()
        ));
        let reference_data = root.join("src/reference_data");
        let subsystems_dir = reference_data.join("subsystems");
        let rust_dir = root.join("rust");
        fs::create_dir_all(&subsystems_dir).expect("create snapshot dirs");
        fs::create_dir_all(&rust_dir).expect("create rust dir");
        fs::write(reference_data.join("commands_snapshot.json"), "[]\n")
            .expect("write command snapshot");
        fs::write(
            subsystems_dir.join("skills.json"),
            r#"{
  "archive_name": "skills",
  "package_name": "skills",
  "module_count": 6,
  "sample_files": [
    "skills/bundled/batch.ts",
    "skills/bundled/verify.ts",
    "skills/bundled/index.ts",
    "skills/bundledSkills.ts",
    "skills/loadSkillsDir.ts",
    "skills/mcpSkillBuilders.ts"
  ]
}"#,
        )
        .expect("write skills snapshot");

        let catalog =
            load_skill_catalog(&UpstreamPaths::from_repo_root(&root)).expect("catalog should load");
        assert_eq!(catalog.archive_name, "skills");
        assert_eq!(catalog.module_count, 6);
        assert_eq!(catalog.bundled_skill_samples.len(), 2);
        assert!(catalog
            .bundled_skill_samples
            .iter()
            .any(|skill| skill.name == "batch"));
        assert!(catalog
            .bundled_skill_samples
            .iter()
            .any(|skill| skill.name == "verify"));
        assert!(catalog
            .support_modules
            .iter()
            .any(|module| module == "skills/loadSkillsDir.ts"));

        let original_cwd = std::env::current_dir().expect("cwd");
        std::env::set_current_dir(&rust_dir).expect("set cwd");

        let verify =
            load_archived_skill_from_cwd("verify").expect("archived bundled skill should load");
        assert_eq!(verify.name, "verify");
        assert_eq!(verify.archived_file_count, 1);
        assert_eq!(
            verify.source_hints,
            vec![String::from("skills/bundled/verify.ts")]
        );

        std::env::set_current_dir(&original_cwd).expect("restore cwd");
        let _ = fs::remove_dir_all(root);
    }

    #[test]
    fn loads_remote_catalog_and_command_from_snapshots() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let root = std::env::temp_dir().join(format!(
            "compat-harness-remote-{}",
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
  {"name":"remote-env","source_hint":"commands/remote-env/index.ts","responsibility":"remote env index"},
  {"name":"remote-env","source_hint":"commands/remote-env/remote-env.tsx","responsibility":"remote env flow"},
  {"name":"api","source_hint":"commands/remote-setup/api.ts","responsibility":"remote setup api"},
  {"name":"remote-setup","source_hint":"commands/remote-setup/index.ts","responsibility":"remote setup index"},
  {"name":"remote-setup","source_hint":"commands/remote-setup/remote-setup.tsx","responsibility":"remote setup flow"},
  {"name":"other","source_hint":"commands/other/index.ts","responsibility":"other"}
]"#,
        )
        .expect("write command snapshot");
        fs::write(
            subsystems_dir.join("cli.json"),
            r#"{
  "archive_name": "cli",
  "package_name": "cli",
  "module_count": 5,
  "sample_files": [
    "cli/print.ts",
    "cli/remoteIO.ts",
    "cli/structuredIO.ts",
    "cli/transports/WebSocketTransport.ts",
    "cli/transports/transportUtils.ts"
  ]
}"#,
        )
        .expect("write cli snapshot");
        fs::write(
            subsystems_dir.join("upstreamproxy.json"),
            r#"{
  "archive_name": "upstreamproxy",
  "package_name": "upstreamproxy",
  "module_count": 2,
  "sample_files": [
    "upstreamproxy/relay.ts",
    "upstreamproxy/upstreamproxy.ts"
  ]
}"#,
        )
        .expect("write upstreamproxy snapshot");

        let catalog = load_remote_catalog(&UpstreamPaths::from_repo_root(&root))
            .expect("catalog should load");
        assert_eq!(catalog.archive_name, "cli");
        assert_eq!(catalog.module_count, 5);
        assert_eq!(catalog.transport_files.len(), 4);
        assert_eq!(
            catalog
                .upstream_proxy
                .as_ref()
                .map(|proxy| proxy.module_count),
            Some(2)
        );
        assert_eq!(
            catalog
                .upstream_proxy
                .as_ref()
                .map(|proxy| proxy.files.clone()),
            Some(vec![
                String::from("upstreamproxy/relay.ts"),
                String::from("upstreamproxy/upstreamproxy.ts"),
            ])
        );
        assert!(catalog
            .commands
            .iter()
            .any(|command| command.name == "remote-env"));
        assert!(catalog
            .commands
            .iter()
            .any(|command| command.name == "remote-setup"));

        let original_cwd = std::env::current_dir().expect("cwd");
        std::env::set_current_dir(&rust_dir).expect("set cwd");

        let setup = load_remote_command_from_cwd("remote-setup").expect("remote setup should load");
        assert_eq!(setup.archived_file_count, 3);
        assert!(setup
            .source_hints
            .iter()
            .any(|hint| hint == "commands/remote-setup/api.ts"));
        assert!(setup.summary.contains("remote setup"));

        std::env::set_current_dir(&original_cwd).expect("restore cwd");
        let _ = fs::remove_dir_all(root);
    }

    #[test]
    fn loads_tool_catalog_and_family_from_snapshots() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let root = std::env::temp_dir().join(format!(
            "compat-harness-tools-{}",
            std::time::SystemTime::now()
                .duration_since(std::time::UNIX_EPOCH)
                .expect("time")
                .as_nanos()
        ));
        let reference_data = root.join("src/reference_data");
        let rust_dir = root.join("rust");
        fs::create_dir_all(&reference_data).expect("create snapshot dir");
        fs::create_dir_all(&rust_dir).expect("create rust dir");
        fs::write(
            reference_data.join("tools_snapshot.json"),
            r#"[
  {"name":"BashTool","source_hint":"tools/BashTool/BashTool.tsx","responsibility":"bash tool"},
  {"name":"bashPermissions","source_hint":"tools/BashTool/bashPermissions.ts","responsibility":"bash permissions"},
  {"name":"ToolSearchTool","source_hint":"tools/ToolSearchTool/ToolSearchTool.ts","responsibility":"tool search"},
  {"name":"queryParser","source_hint":"tools/ToolSearchTool/queryParser.ts","responsibility":"query parser"},
  {"name":"helper","source_hint":"tools/helper.ts","responsibility":"helper"}
]"#,
        )
        .expect("write tool snapshot");

        let catalog =
            load_tool_catalog(&UpstreamPaths::from_repo_root(&root)).expect("catalog should load");
        assert_eq!(catalog.archived_file_count, 5);
        assert!(catalog
            .families
            .iter()
            .any(|family| family.name == "BashTool"));
        assert!(catalog
            .families
            .iter()
            .any(|family| family.name == "ToolSearchTool"));
        assert!(catalog
            .families
            .iter()
            .any(|family| family.name == "helper"));

        let original_cwd = std::env::current_dir().expect("cwd");
        std::env::set_current_dir(&rust_dir).expect("set cwd");

        let bash = load_tool_family_from_cwd("bash").expect("bash family should load");
        assert_eq!(bash.name, "BashTool");
        assert_eq!(bash.archived_file_count, 2);
        assert!(bash
            .source_hints
            .iter()
            .any(|hint| hint == "tools/BashTool/BashTool.tsx"));
        assert!(bash.summary.contains("bash tool"));

        std::env::set_current_dir(&original_cwd).expect("restore cwd");
        let _ = fs::remove_dir_all(root);
    }
}
