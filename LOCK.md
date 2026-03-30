# 🔒 LOCK.md - Task Locking & Coordination

## Purpose

This file prevents concurrent work on the same tasks by multiple agents or sub-agents. When a task is claimed, it's locked until completion or explicit release.

---

## Active Locks

| Task ID | Lock Holder | Started | Est. Duration | Status | Notes |
|---------|-------------|---------|---------------|--------|-------|
| T2 | Main Agent | 2026-03-30 10:30 UTC | ~2h | Active | Component mapping |
| - | - | - | - | - | - |

---

## Locking Protocol

### How to Claim a Task

1. **Check Active Locks** - Review this file for active tasks
2. **Read Current Status** - Check TODO.md for context
3. **Claim the Task** - Add your lock entry above
4. **Start Working** - Begin implementation
5. **Update Progress** - Keep the lock file updated as you work

### How to Release a Lock

**Complete the task:**
```
[Task ID] | Main Agent | 2026-03-30 10:30 UTC | ~2h | ✅ Complete | [Summary of changes]
```

**Release early (before completion):**
```
[Task ID] | Main Agent | 2026-03-30 10:30 UTC | ~2h | 🔄 Released | [Reason + Next owner]
```

---

## Conflict Resolution

| Scenario | Resolution |
|----------|------------|
| **Double-lock** | The later agent must wait or choose a different task | Check TODO.md for context | If urgent, notify the current holder |
| **Lost lock** | Re-acquire the task before starting | Document the loss reason | Notify the team | If urgent, notify the current holder |
| **Task blocked** | Mark as blocked and wait | Document the blocker | Notify the blocking agent | Notify the team |

---

## Sub-Agent Guidelines

### Before Starting

1. ✅ Check if task is already locked
2. ✅ Review TODO.md for context and dependencies
3. ✅ Confirm the task is appropriate for your role
4. ✅ Check if any prerequisites are pending

### While Working

1. 🔄 Update lock status as work progresses
2. 📝 Add notes if you hit blockers
3. 🤝 Notify main agent if you need assistance

### When Done

1. ✅ Update lock to "Complete" with summary
2. ✅ Commit code with relevant task ID
3. ✅ Update TODO.md to reflect completion
4. ✅ Notify main agent

---

## Sub-Agent Roles

| Role | Responsibilities | Lock Limit |
|------|------------------|------------|
| **Coder** | HTML/CSS/JS implementation | 2 tasks |
| **Designer** | Visual design, color schemes | 1 task |
| **Researcher** | Gather content, analyze refs | 1 task |
| **Reviewer** | Quality assurance, testing | 1 task |
| **Coordinator** | Task management, sync | None |

---

## Quick Reference

**Claim a task:**
```markdown
| T2 | Main Agent | 2026-03-30 10:30 UTC | ~2h | 🔄 Active | Component mapping - Reference site analysis
```

**Release a task:**
```markdown
| T2 | Main Agent | 2026-03-30 10:30 UTC | ~2h | ✅ Complete | Mapped 5 key components, created design spec
```

**Block a task:**
```markdown
| T2 | Main Agent | 2026-03-30 10:30 UTC | ~2h | 🔒 Blocked | Waiting on design assets
```

---

## Emergency Override

In case of emergencies (server down, critical bug), use this protocol:

1. Mark task as `🔴 Emergency` in Active Locks
2. Add emergency context in Notes
3. Notify all team members
4. Revert lock after resolution
