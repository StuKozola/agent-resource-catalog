---
name: cotm-overview
description: >
  Orientation and routing for Command of the Message (Force Management's value-based sales messaging
  methodology). Use this skill whenever the user asks what Command of the Message is, how it works, how to
  roll it out, where to start, how it differs from other sales methodologies (Challenger, SPIN, Solution
  Selling, Sandler), how it pairs with MEDDICC or MEDDPICC, or whether their team is ready for it. Also
  trigger for "CotM", "value-based selling rollout", "being audible-ready", "Force Management methodology",
  "the three essential questions", "value messaging program", or a request that spans several rollout steps
  at once. For work inside one step (building the Value Framework, discovery questions, training, CRM
  integration, coaching, measurement), route to that step's cotm-* skill.
---

# Command of the Message — Overview and Router

Command of the Message (CotM) is a value-based sales messaging methodology developed by Force Management. It gives every customer-facing person one shared, buyer-centric story about the problems the company solves, how it solves them differently, and where it has done so before. Reps then adapt that story in the moment to what each buyer actually says.

Read `references/methodology-primer.md` for the core concepts, vocabulary and comparisons with other methodologies.

## The core ideas

1. **Start with the buyer's problem, not the product.** Lead with business issues and outcomes. Features appear only as the capabilities that make an outcome possible.
2. **One message, flexibly delivered.** The whole organization works from one Value Framework. Reps are "audible-ready": like a quarterback changing the play at the line, they adjust the message to what they hear from the buyer, without leaving the framework.
3. **Three essential questions.** Every rep should be able to answer, in the buyer's terms: *What problems do we solve? How do we solve them differently or better than the alternatives? Where have we done it before?*
4. **Differentiate on value to earn a premium.** A message tied to a specific buyer problem and outcome is harder to commoditize than a feature comparison, and it supports price.
5. **Message and qualification work together.** CotM shapes *what* reps say; MEDDICC/MEDDPICC shapes *how they qualify and run* the deal. Most rollouts use both.
6. **It is a system, not an event.** Alignment, the framework, field tools, training, process integration, coaching and measurement all have to be in place for the message to stick.

## The rollout, step by step

| Step | What happens | Skill |
|---|---|---|
| 1. Foundations | Understand the methodology, check readiness, set goals | `cotm-overview` (this skill) |
| 2. Executive alignment | Secure sponsorship, agree on goals, plan change management, run the alignment workshop | `cotm-executive-alignment` |
| 3. Value Framework | Build the shared framework: before scenarios, negative consequences, positive business outcomes, required capabilities, metrics, differentiators, proof points | `cotm-value-framework` |
| 4. Field tools | Turn the framework into discovery questions, trap-setting questions, the mantra and talk tracks | `cotm-field-tools` |
| 5. Training and certification | Train every role, practice, certify, build internal trainers | `cotm-training-certification` |
| 6. Sales process integration | Pair with MEDDPICC, embed in CRM, opportunity plans and deal reviews | `cotm-sales-process-integration` |
| 7. Coaching and reinforcement | Manager coaching, call reviews, message refreshes, feedback loops | `cotm-coaching-reinforcement` |
| 8. Impact measurement | Leading and lagging indicators, baselines, reporting | `cotm-impact-measurement` |

The steps overlap. Field tools are drafted while the Value Framework is still being validated, and measurement baselines should be captured before training starts.

## Workflow

### 1. Identify what the user needs

Ask what they are trying to do, what they sell and to whom, and how far along they are. Then choose a path:

- **A single step** ("help me write discovery questions") → route to that step's skill.
- **A full rollout plan** ("we're adopting CotM next quarter") → build a sequenced plan (step 3 below).
- **A readiness check** ("are we ready for this?") → run the readiness check (step 2 below).
- **A concept question** ("what is a positive business outcome?") → answer directly from `references/methodology-primer.md`.

### 2. Run a readiness check

Score each item Ready / Partial / Missing and note the evidence:

- **Sponsorship:** a named executive sponsor (usually the CRO or head of sales) who will attend the workshop and model the behavior.
- **Cross-functional buy-in:** marketing, product, customer success and services leaders agree to work from one framework.
- **Market evidence:** documented buyer personas, market problems, competitive alternatives and customer results to draw on.
- **Sales process:** a defined sales process and a CRM that can hold new fields and stages.
- **Manager capacity:** first-line managers have time to coach weekly.
- **Baselines:** current win rate, deal size, cycle length, ramp time and discount rates are known.
- **Enablement capacity:** someone owns training, certification and refreshes after the initial launch.

Missing sponsorship or manager capacity are the most common reasons a rollout fades; flag them first.

### 3. Build a rollout plan

Sequence the steps against the user's timeline. A typical shape:

1. **Weeks 0–2:** readiness check, sponsor commitment, baselines (`cotm-executive-alignment`, `cotm-impact-measurement`).
2. **Weeks 2–4:** alignment workshop and first-draft Value Framework (`cotm-executive-alignment`, `cotm-value-framework`).
3. **Weeks 4–8:** validate the framework with customers and top reps; draft field tools (`cotm-value-framework`, `cotm-field-tools`).
4. **Weeks 6–10:** train and certify by role; launch at a kickoff if timing allows (`cotm-training-certification`).
5. **Weeks 8–12:** embed in CRM and deal reviews (`cotm-sales-process-integration`).
6. **Ongoing:** coaching cadence, quarterly refreshes, measurement reviews (`cotm-coaching-reinforcement`, `cotm-impact-measurement`).

Adjust for company size: a 10-person team can compress this into a few weeks; a global organization will run it in waves by region or segment.

## Common mistakes to watch for

- **Treating it as a training event.** Without manager coaching and process integration, behavior reverts within a quarter.
- **Sales-only ownership.** If marketing and product keep their own messaging, buyers hear two stories.
- **A framework written from the inside out.** Features dressed up as outcomes, with no buyer validation.
- **Skipping the "before" state.** Reps jump to the solution without establishing the buyer's pain and its cost.
- **Unproven differentiators.** Claims with no proof point, or that a competitor could also make.
- **No baseline.** Without before-and-after numbers, the program can't show its value.

## Related skills

- `pragmatic-positioning`, `pragmatic-buyer-personas`, `pragmatic-market-problems`, `pragmatic-competitive-landscape` — the market evidence the Value Framework is built on.
- `pragmatic-organizational-alignment` — aligning the wider go-to-market organization around one view of the buyer.
- `pragmatic-win-loss-analysis` — a steady source of new proof points and differentiators.

## Using AI with Command of the Message

- Draft first-pass framework sections, discovery questions and role-play scenarios from call recordings, win/loss notes and customer stories.
- Score call transcripts against the framework to show where reps skip the before state or lead with features.
- Generate persona-specific variants of the mantra and talk tracks for review.

Check AI output against real buyer evidence; it will produce plausible outcomes and differentiators no customer has confirmed. Keep customer and deal data in approved tools. People, not the tool, own the message and the deal decisions.

## Reference files

- `references/methodology-primer.md` — Core concepts, vocabulary, the three essential questions, and how CotM compares with and complements other methodologies.

*Command of the Message® is associated with Force Management. This skill is an independent guide based on public descriptions of the methodology and is not affiliated with or endorsed by Force Management.*
