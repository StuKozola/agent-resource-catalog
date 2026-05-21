# Use Scenario Examples Library

Annotated examples across multiple domains. Each example is followed by analysis notes explaining what makes it effective (or what to watch out for).

---

## How to Read These Examples

Each entry shows:
- **Persona snapshot** — brief context for the persona used
- **Requirement** — the parent requirement this scenario expands
- **Use Scenario(s)** — the narrative(s)
- **Analysis** — what the scenario does well and any cautions

---

## Example 1: Education / Course Registration (Official Pragmatic Example)

**Persona:** Jessica, a psychology major at a mid-size university  
**Requirement:** "Jessica, a college student, registers for college classes each semester."

**Use Scenario A:**  
Jessica feels overwhelmed scrolling through a long list of irrelevant classes, struggling to find the ones she needs for her psychology major.

**Use Scenario B:**  
Jessica can't easily identify which courses fulfill her graduation requirements, leaving her confused and frustrated as she tries to plan her semester schedule.

**Analysis:**  
✅ One persona, one problem each  
✅ Solution-free — no mention of filters, search, or any feature  
✅ Emotional stakes clear (overwhelmed, confused, frustrated)  
✅ Each scenario illuminates a different facet of the same core problem  
✅ Concise but vivid  

---

## Example 2: Consumer / Meal Planning (LinkedIn/Pragmatic Example)

**Persona:** Sam, a mid-level marketing manager with a young family, works 9–5 from home  
**Requirement:** Sam needs to plan and purchase groceries for her family on a busy weekly schedule.

**Use Scenario A:**  
After a full day of back-to-back video calls, Sam realizes at 5:30 p.m. that she has no plan for dinner and no idea what's in the refrigerator. She opens her laptop to search for ideas, but after 20 minutes of browsing, she still hasn't landed on anything that matches what she thinks (but isn't sure) she has at home. She orders delivery again, frustrated by the cost.

**Use Scenario B:**  
Sam does get to the grocery store on a Saturday, but without a list she wanders the aisles buying things that look good in the moment. Later that week she throws out produce she forgot she bought. The wasted food and wasted money bother her, but she never finds time to approach grocery shopping differently.

**Analysis:**  
✅ Rich context — time of day, emotional state, competing pressures all present  
✅ Solution-free throughout  
✅ Consequence is concrete (wasted money, recurring frustration)  
✅ Two scenarios show different moments when the problem surfaces  
⚠️ Could be slightly tightened — watch for scenarios that become too long  

---

## Example 3: B2B SaaS / Financial Reporting

**Persona:** David, a CFO at a 150-person manufacturing company, runs monthly board reporting  
**Requirement:** David needs to compile and present accurate monthly financial reports to the board.

**Use Scenario A:**  
The week before each board meeting, David's team spends three days pulling data from four different systems — their ERP, their CRM, a legacy Excel model, and the HR platform. Each handoff introduces errors that aren't caught until David is reviewing the final deck the night before the meeting. He routinely finds inconsistencies in the numbers at 10 p.m. and has no reliable way to trace them back to their source.

**Use Scenario B:**  
During the board meeting itself, a director asks David how a specific line item compares to the same period two years ago. David doesn't have that data in the room. He commits to following up, but the extra research eats two hours the following day and leaves the board waiting for answers they expected in real time.

**Analysis:**  
✅ Specific enough to resonate with anyone who has run board reporting  
✅ Emotional stakes high (night-before anxiety, public exposure)  
✅ Frequency is embedded ("week before each board meeting," "each board meeting")  
✅ Solution-free — no mention of dashboards, integrations, or reports  
✅ Two scenarios show different phases where the problem manifests  

---

## Example 4: Healthcare / Clinical Workflow

**Persona:** Dr. Reyes, an ER physician at a regional hospital  
**Requirement:** Dr. Reyes needs to review a patient's complete medication history before making a treatment decision.

**Use Scenario A:**  
A patient arrives in the ER unable to communicate. Dr. Reyes needs to know what medications the patient is currently taking before administering treatment. She checks the hospital's system — the patient was seen here two years ago, but the record doesn't include prescriptions from the patient's primary care physician at a different clinic. She calls the clinic but reaches voicemail. She makes a treatment decision with incomplete information, documenting the uncertainty in the record.

**Analysis:**  
✅ High stakes make the scenario immediately compelling  
✅ The gap between what the user needs and what's available is concrete  
✅ The workaround (phone call, voicemail) is noted as context, not as a solution  
✅ Consequence of the problem (decision under uncertainty) is explicit  
⚠️ "Documenting the uncertainty" borders on a process outcome — acceptable here as it conveys stakes, not a solution  

---

## Example 5: What a BAD Use Scenario Looks Like

**Use Scenario (Flawed):**  
Maria is a project manager who needs better task tracking. She wishes the system had a way to filter tasks by assignee and due date. It would also help if she could export a list to share with her team. The current lack of filtering makes her work harder.

**Analysis:**  
❌ "Needs better task tracking" — vague, no specific problem  
❌ "Wishes the system had a way to filter" — solution embedded in sentence 2  
❌ "Export a list" — feature request, not a problem narrative  
❌ No persona context (who is Maria? what is her role? what is she trying to accomplish?)  
❌ No emotional or business consequence beyond "makes her work harder"  

**Revised:**  
Maria is a project manager coordinating a 12-person engineering team. Every Friday she pulls together a status update for her director, manually scanning each team member's tasks to identify what's overdue. When team members update their tasks on Thursday evening, she doesn't catch the changes in time. Her director gets an outdated picture of project health, and Maria spends Friday morning fielding questions about discrepancies she wasn't aware of.

---

## Tips for Generating Scenarios in Bulk

When a team needs to cover many persona/problem pairs quickly:

1. **Matrix approach:** List personas across the top, key problems down the side. Each cell is a scenario opportunity.
2. **NIHITO mining:** Review interview notes for moments customers said "I have to..." or "I end up..." — these are scenario seeds.
3. **Day-in-the-life walk:** Walk through the persona's typical day and note every friction point that touches your product's domain.
4. **Edge vs. core:** Write one scenario for the most common occurrence of the problem, and one for a high-stakes edge case.
