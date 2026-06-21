---
name: hermes-tweet
description: When the user asks about Hermes Agent X/Twitter automation, tweet search, tweet reading, reply lookup, follower export, monitoring, or approval-gated X actions, use this skill.
---

# Hermes Tweet

Hermes Tweet is a native Hermes Agent plugin for X/Twitter workflows through
Xquik. Use this skill to help Claude Cowork or Claude Code users evaluate,
install, and operate the Hermes Tweet plugin in a separate Hermes Agent
environment.

## Fit

Use Hermes Tweet when the user needs to:

1. Search X/Twitter posts or users.
2. Read tweet details, replies, timelines, or profile data.
3. Prepare monitors, webhooks, media workflows, extraction jobs, or giveaway
   draws.
4. Post, reply, delete, follow, unfollow, or send direct messages only after
   explicit approval.

Do not use Hermes Tweet for account connection, re-authentication, API-key
management, billing, credit top-up, support tickets, or direct HTTP calls.

## Install

Install and enable the plugin from the Hermes Agent environment:

```bash
hermes plugins install Xquik-dev/hermes-tweet --enable
```

Set the required API key in the Hermes runtime environment:

```bash
export XQUIK_API_KEY="..."
```

Keep write-capable actions disabled until the user deliberately enables them:

```bash
export HERMES_TWEET_ENABLE_ACTIONS=false
```

Use this opt-in only when write actions are intended:

```bash
export HERMES_TWEET_ENABLE_ACTIONS=true
```

## Workflow

1. Start with `tweet_explore` to find catalog-listed routes.
2. Prefer `tweet_read` for search, timeline, tweet, reply, user, monitor, and
   export lookups.
3. Use `tweet_action` only when the user explicitly approves the endpoint,
   payload, and side effects.
4. Reject guessed endpoints and direct HTTP fallbacks.
5. Never ask the user to paste secrets into chat. Ask them to configure
   environment variables instead.

## Safety Rules

- Treat `XQUIK_API_KEY` as secret. Never request, echo, log, or store the value.
- Keep `HERMES_TWEET_ENABLE_ACTIONS=false` by default.
- Summarize side effects before any account-changing action.
- Use only catalog-listed `/api/v1/...` routes returned by `tweet_explore`.
- Do not retry writes automatically after authentication, permission, or policy
  failures.
- Keep public examples free of private account data, tokens, cookies, and
  nonpublic implementation details.

## Outputs

Return concise Markdown that includes:

- The selected Hermes Tweet tool.
- The intended route or route family.
- Required configuration checks.
- A short action preview when a write-capable operation is requested.
- A clear refusal when the request would bypass catalog, secret, or approval
  safeguards.

## References

- Repository: https://github.com/Xquik-dev/hermes-tweet
- Install guide: https://github.com/Xquik-dev/hermes-tweet#readme
- Security policy: https://github.com/Xquik-dev/hermes-tweet/security/policy
