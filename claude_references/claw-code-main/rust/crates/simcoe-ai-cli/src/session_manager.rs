pub(crate) use runtime::{
    create_managed_session_handle, list_managed_sessions, load_active_session_handle,
    resolve_session_reference, session_handle_from_path, sessions_dir, set_active_session_handle,
    ManagedSessionSummary, SessionHandle,
};

pub(crate) fn render_session_list(
    active_session_id: Option<&str>,
) -> Result<String, Box<dyn std::error::Error>> {
    let sessions = list_managed_sessions()?;
    let mut lines = vec![
        "Sessions".to_string(),
        format!("  Directory         {}", sessions_dir()?.display()),
    ];
    if sessions.is_empty() {
        lines.push("  No managed sessions saved yet.".to_string());
        return Ok(lines.join("\n"));
    }
    for session in sessions {
        let marker = if active_session_id.is_some_and(|id| session.id == id) {
            "● current"
        } else {
            "○ saved"
        };
        lines.push(format!(
            "  {id:<20} {marker:<10} msgs={msgs:<4} modified={modified} path={path}",
            id = session.id,
            msgs = session.message_count,
            modified = session.modified_epoch_secs,
            path = session.path.display(),
        ));
    }
    Ok(lines.join("\n"))
}
