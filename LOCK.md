# 🔒 LOCK.md - Task Locking & Coordination

> **How to use this file:** LOCK.md prevents multiple agents from working on the same task simultaneously. Before starting any task, check the Active Locks table. If the task is free, add your lock entry. When done, move it to Recent Completions. For the task list itself, see [TODO.md](TODO.md). For overall project status, see [PROGRESS.md](PROGRESS.md).

---

## Active Locks

| Task ID | Lock Holder | Started | Status | Notes |
|---------|-------------|---------|--------|-------|
| - | None | - | - | All tasks currently available |

---

## Recent Completions

| Task ID | Holder | Completed | Summary |
|---------|--------|-----------|---------|
| T18–T26 | SureThing Bot | 2026-04-15 | WordPress content migration — Documents & Archives pages, 16 PDFs, nav/footer/sitemap updates (PR #60, #61) |
| T10–T17 | Main Agent | 2026-03-30 | Sprint 5 — Directory membership badges, Google Sheets sync, homepage refactor |
| T1–T9 | Main Agent | 2026-03-30 | Sprints 1–4 — Foundation, design, content, events |

---

## How to Use

### Claiming a Task

1. Check **Active Locks** above — is the task free?
2. Check [TODO.md](TODO.md) for task details and dependencies
3. Add your lock entry:
   ```
   | P1 | Your Name | 2026-04-16 | 🔄 In Progress | Working on Cloudflare deploy |
   ```
4. Start working
5. When done, move the entry to **Recent Completions** and update [TODO.md](TODO.md)

### Releasing a Lock

- **Completed:** Move to Recent Completions with summary
- **Releasing early:** Change status to `🔄 Released` with reason, remove from Active Locks

### Conflict Resolution

| Scenario | Resolution |
|----------|------------|
| **Double-lock** | Later agent must wait or choose a different task |
| **Blocked** | Mark as blocked in Notes, document the blocker |
| **Emergency** | Mark as `🔴 Emergency`, notify team immediately |

---

## Last Updated

**2026-04-16** - All locks cleared after WordPress migration

*See also: [TODO.md](TODO.md) · [PROGRESS.md](PROGRESS.md) · [ROADMAP.md](ROADMAP.md)*
