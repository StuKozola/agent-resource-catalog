---
name: cotm-sales-process-integration
description: >
  Embed Command of the Message in the sales process and CRM: pairing the Value Framework with MEDDICC or
  MEDDPICC qualification, adding value fields (before scenario, negative consequences, positive business
  outcomes, metrics, decision criteria) to opportunities in Salesforce, HubSpot or other CRMs, defining
  stage exit criteria based on value, building opportunity or account plans (sometimes called command
  plans), mutual action plans, value-based deal review and forecast call formats, and SDR-to-AE handoffs.
  Use this skill whenever the user asks how to operationalize CotM, connect CotM and MEDDPICC, design CRM
  fields or stage gates for value selling, build a deal review template, create an opportunity plan, run
  a value-based forecast call, or make the message show up in pipeline management.
---

# Sales Process Integration — Command of the Message, Step 6

Training changes what reps know; process integration changes what they do every week. When value elements are fields in the CRM, stage exit criteria, and questions in every deal review, the message becomes part of how the company runs its business.

**Output:** a CotM–MEDDPICC mapping, CRM field and stage design, an opportunity plan template and a deal review format.

Read `references/meddpicc-mapping.md` for the element-by-element mapping and CRM field suggestions.

## Workflow

### 1. Understand the current process

Ask for the current sales stages and exit criteria, CRM platform, qualification method (if any), forecast categories, and how deal reviews run today. Identify where value information is (or isn't) captured.

### 2. Map CotM to qualification

CotM supplies the content; MEDDPICC (or MEDDICC) supplies the qualification structure. Make the connections explicit:

- **Metrics** ← framework metrics, quantified for this buyer
- **Economic buyer** ← the persona whose PBOs carry the decision
- **Decision criteria** ← shaped by required capabilities and trap-setting questions
- **Identify pain** ← before scenario and negative consequences
- **Champion** ← equipped with the mantra and proof points to sell internally
- **Competition** ← differentiators and proof

Decision process and paper process come from discovery and are not part of the framework itself.

### 3. Design CRM fields

Keep it lean — every field must be used in a review. A typical minimum set on the opportunity:

- Before scenario (text)
- Negative consequences, quantified (text plus a currency or number field)
- Positive business outcomes (text)
- Metrics with baseline and target (text)
- Required capabilities agreed with the buyer (multi-select or text)
- Differentiators that map to decision criteria (multi-select)
- Proof point(s) shared (multi-select or related list)
- MEDDPICC fields: economic buyer, champion, decision criteria, decision process, paper process, competition

Use picklists from the Value Framework where possible so data can be reported on. Work with RevOps on naming, validation rules and page layouts.

### 4. Set value-based stage exit criteria

Tie progress to what the buyer has confirmed, not what the rep has done. For example:

| Stage | Value exit criteria (examples) |
|---|---|
| Discovery | Before scenario and consequences confirmed by the buyer; at least one PBO identified |
| Solution validation | Metrics agreed with baseline; required capabilities reflected in decision criteria; economic buyer engaged |
| Business case | Quantified value accepted by the economic buyer; champion can state the value in their own words |
| Negotiation | Proof points accepted; mutual action plan agreed; paper process mapped |

Adapt to the user's actual stages.

### 5. Build the opportunity plan

Use `templates/opportunity-plan.md` for strategic deals. It records the buyer's value story, qualification status, gaps, and actions. Some companies brand this as a "command plan"; GitLab, for example, publicly describes doing so.

### 6. Redesign deal reviews and forecast calls

Use `templates/deal-review-format.md`. Managers ask value questions first ("What is the buyer's before state? What will it cost them to do nothing? What outcome have they committed to, and how will they measure it?") before discussing close dates. Deals with no confirmed PBO or metric shouldn't be committed in the forecast.

### 7. Align handoffs

- **SDR → AE:** handoff notes capture the before scenario and consequences heard.
- **AE → customer success:** PBOs and metrics transfer as the basis for onboarding and value reviews (`pragmatic-customer-value-realization`).

### 8. Pilot and refine

Pilot with one team for a few weeks, check field completion and usefulness, remove fields nobody uses, then roll out.

## Common mistakes

- Adding a dozen fields that reps fill in with filler to pass validation.
- Stage criteria that measure rep activity rather than buyer confirmation.
- Deal reviews that discuss value only after close dates and amounts.
- Value captured in sales but not passed to customer success.

## Related skills

- `cotm-field-tools` for the questions that populate these fields.
- `cotm-coaching-reinforcement` for using the deal review as a coaching moment.
- `cotm-impact-measurement` for reporting on field completion and outcomes.
- `pragmatic-organizational-alignment` for handoffs and ops requirements.

## Using AI in this step

- Pre-fill value fields from call transcripts for rep review.
- Flag deals in commit with missing PBOs, metrics or economic buyer.
- Draft opportunity plans from CRM and call data.

Reps must confirm AI-filled fields; unverified AI summaries in the CRM pollute the forecast. Respect data access controls.

## Reference and template files

- `references/meddpicc-mapping.md` — Element-by-element mapping with CRM field suggestions and review questions.
- `templates/opportunity-plan.md` — Strategic opportunity plan.
- `templates/deal-review-format.md` — Value-first deal review and forecast call format.
