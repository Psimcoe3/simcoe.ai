use std::io;
use std::path::PathBuf;
use std::sync::{Mutex, OnceLock};

fn active_worktree_state() -> &'static Mutex<Option<PathBuf>> {
    static STATE: OnceLock<Mutex<Option<PathBuf>>> = OnceLock::new();
    STATE.get_or_init(|| Mutex::new(None))
}

fn plan_mode_state() -> &'static Mutex<bool> {
    static STATE: OnceLock<Mutex<bool>> = OnceLock::new();
    STATE.get_or_init(|| Mutex::new(false))
}

pub fn effective_current_dir() -> io::Result<PathBuf> {
    Ok(active_worktree_root().unwrap_or(std::env::current_dir()?))
}

pub fn active_worktree_root() -> Option<PathBuf> {
    active_worktree_state()
        .lock()
        .unwrap_or_else(std::sync::PoisonError::into_inner)
        .clone()
}

pub fn set_active_worktree_root(path: Option<PathBuf>) -> Option<PathBuf> {
    let mut guard = active_worktree_state()
        .lock()
        .unwrap_or_else(std::sync::PoisonError::into_inner);
    std::mem::replace(&mut *guard, path)
}

pub fn clear_active_worktree_root() -> Option<PathBuf> {
    set_active_worktree_root(None)
}

pub fn plan_mode_active() -> bool {
    *plan_mode_state()
        .lock()
        .unwrap_or_else(std::sync::PoisonError::into_inner)
}

pub fn set_plan_mode_active(active: bool) -> bool {
    let mut guard = plan_mode_state()
        .lock()
        .unwrap_or_else(std::sync::PoisonError::into_inner);
    std::mem::replace(&mut *guard, active)
}
