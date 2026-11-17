# Exception Log and Pattern Review — [Product]

*Exceptions focus area (Operations), 2027 Pragmatic Framework. Log every request, approved or declined.*

## Part 1: Exception log

| ID | Date | Customer / team | Segment | Type | Requested (solution) | Underlying problem (tag) | Decision | Approver | Est. one-time cost | Est. ongoing cost / yr | Revenue at stake | Owner | Sunset / review date | Related IDs | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| EX-001 | | | | Product | | e.g., `erp-reconciliation` | Approve one-off | | | | | | | | Active |
| EX-002 | | | | Commercial | | e.g., `annual-budget-cycle` | Decline + alt | | | | | | | | Closed |

**Tagging rules**
- Tag by underlying problem, using a short controlled vocabulary maintained by the log owner.
- Add a second tag for the affected persona (per `pragmatic-user-personas` / `pragmatic-buyer-personas`).
- Status values: Pending, Active, Sunset, Migrated to standard, Closed (declined).

## Part 2: Pattern review (monthly or quarterly)

**Period:**  **Reviewers:** product, sales/deal desk, CS, support, finance
**Totals:** requests ___ | approved ___ | declined ___ | routed to product ___ | active exceptions ___ | total ongoing cost ___

### Patterns found (threshold: e.g., 3+ accounts in 12 months on the same problem tag)

| Problem tag | # requests | # accounts | Segments | Revenue affected | Cost of exceptions so far | Validated beyond requesters? | Decision | Routed to | Owner |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | Y/N | Productize / Change policy or packaging / Standard service offering / Keep declining | `pragmatic-requirements` / `pragmatic-pricing` / `pragmatic-market-problems` | |

### Problem statement for each pattern routed to product
- **Problem:** (in market terms)
- **Who has it:** (personas, segments)
- **How often:** (frequency in the customer's work)
- **Evidence:** (request IDs, quotes, revenue, cost of exceptions)
- **Validation plan:** customers/prospects who did not ask
- **Existing exceptions to migrate if built:**

### Active exception health
| ID | Owner | Sunset date passed? | Still needed? | Action |
|---|---|---|---|---|
| | | | | Extend / Retire / Migrate to standard |

### Policy and alignment updates
- Changes to approval matrix or criteria:
- Messages for sales, CS and support (`pragmatic-organizational-alignment`):
- Inputs to `pragmatic-scaling` (manual work) and `pragmatic-business-outcomes` (margin impact):
