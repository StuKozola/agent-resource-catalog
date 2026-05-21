---
name: subagent-routing
description: Decide whether to handle a task in the main session or delegate to a subagent to protect context. Use when you are about to perform broad exploration, parallel scanning, or any task whose tool output would consume more than ~5k tokens you won't need to reference again.
version: 1.0.0
allowed-tools: "Read, Glob, Grep"
---

# /subagent-routing — Context-Aware Task Routing

Use this skill whenever you are about to start a task and are unsure whether to run it in the main session or delegate to a subagent. The goal is to protect the main context window from bulky, one-shot output.

---

## Decision rule (apply in order)

Ask each question. Stop at the first YES — that answer determines routing.

| # | Question | YES → |
|---|----------|-------|
| 1 | Will you need to reference the raw output of this task in a later step? | **Main session** |
| 2 | Is this a quick lookup (≤3 grep/read calls, output fits in ~2k tokens)? | **Main session** |
| 3 | Does this task require reading many files, scanning large directories, or fetching multiple URLs? | **Subagent** |
| 4 | Is the output a report, summary, or structured artifact the user will read — not something you'll build on? | **Subagent** |
| 5 | Will the task produce parallel fan-out (e.g. 5+ independent searches or file reads)? | **Subagent** |
| 6 | Is the output likely to exceed ~5k tokens that you won't reference again? | **Subagent** |
| Default | Anything else | **Main session** |

---

## Examples

### Route to subagent

- "Search the whole codebase for all usages of X" — broad scan, large output
- "Read all 12 handler files and summarize their IPC channels" — many reads, artifact output
- "Check every test file for a missing mock pattern" — fan-out across many files
- "Run a security audit" — parallel scan + report
- "Explore the architecture of the settings module" — multi-file exploration, output is a summary

### Stay in main session

- "What does this function do?" — one file read, answer needed immediately
- "Find where `useConversation` is defined" — one grep, result used next
- "Show me the IPC handler for `chat:sendMessage`" — targeted lookup
- "Fix this bug in `src/stores/ChatStore.ts`" — edit task, changes must stay in context

---

## Subagent types available in this repo

| Type | When to use |
|------|-------------|
| `Explore` | Codebase exploration, file searches, architecture questions. Quick/medium/very-thorough levels. |
| `general-purpose` | Multi-step research, open-ended investigation, tasks combining search + reasoning. |
| `security-review` | PR-scoped security audit (dual-perspective). |
| `security-review-repo` | Full-codebase security scan (used by `/repo-security-audit`). |
| `claude-code-guide` | Questions about Claude Code CLI, API, or SDK. |
| `Plan` | Designing implementation strategies before coding. |

---

## Context budget guidelines

Current session context is 200k tokens. Autocompact triggers at ~80% (~160k used).

| Remaining context | Posture |
|-------------------|---------|
| >100k free | Comfortable — main session fine for most tasks |
| 50–100k free | Cautious — prefer subagents for exploration tasks |
| <50k free | Aggressive — subagent for anything beyond one-shot edits |

Check `/context` to see current usage before starting a large task.

---

## How to delegate

When routing to a subagent, write a self-contained prompt — the agent has no memory of this conversation:

1. State the goal and why it matters
2. Name the exact files or patterns to look at
3. Describe what you've already ruled out
4. Specify the output format (summary, list, file path, etc.)
5. Set a length cap if you want a short answer ("report in under 200 words")

For parallel fan-out, send all Agent calls in a **single message** so they run concurrently.
