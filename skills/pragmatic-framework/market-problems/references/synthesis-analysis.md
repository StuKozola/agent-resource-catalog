# Synthesizing and Analyzing Market Problems Findings

## From Interviews to Insights

Individual NIHITO interviews are data points. The real value emerges when you look across multiple interviews for **patterns**. A single customer mentioning a problem is an anecdote. When 10 of 15 customers independently describe the same pain point, you have an insight worth acting on.

## Step 1: Organize Your Raw Data

After completing your interview cycle (typically 15-30 interviews), gather all your notes, transcripts, and recordings into a single workspace. For each interview, ensure you have:

- Date and participant info (role, company type, segment, customer status)
- Key quotes (verbatim language from the customer)
- Problems mentioned (in the customer's words)
- Workarounds described
- Emotional intensity markers (where did they get animated, frustrated, or emphatic?)
- Competitive mentions
- Buying process details (if applicable)

## Step 2: Theme Identification

Read through all interview notes and begin grouping related problems into themes. This is an inductive process — let the themes emerge from the data rather than forcing interviews into pre-existing categories.

### How to Identify Themes

1. **First pass — open coding:** Go through each interview and highlight every distinct problem mentioned. Write each one on a separate note (physical sticky notes or digital equivalent).

2. **Second pass — grouping:** Start clustering related problems together. Problems that describe different facets of the same underlying challenge belong in the same group. Give each cluster a descriptive name using customer language where possible.

3. **Third pass — hierarchy:** Within each theme, identify sub-themes. A large theme like "data quality issues" might break down into "duplicate records," "stale data from manual entry," and "inconsistent formats across sources."

4. **Fourth pass — frequency and intensity:** For each theme, note how many interviews mentioned it and how emotionally charged the responses were. High frequency + high intensity = strong signal.

### Theme Naming
Name themes using the customer's language, not your internal jargon. If customers say "I spend all day chasing down numbers," the theme isn't "data accessibility optimization" — it's "chasing down numbers" or "time wasted on data gathering." This customer language will be invaluable for positioning later.

## Step 3: Distinguish Symptoms from Root Causes

Customers describe symptoms. Your job is to find root causes. Multiple symptoms often trace back to a single root cause, and solving the root cause addresses all of them.

**Example:**
- Symptom: "Reports take too long to generate"
- Symptom: "I can't get the data I need for meetings"
- Symptom: "I have to ask IT every time I need a custom query"
- Root cause: **Users lack self-service access to the data they need for their workflows**

Solving any one symptom in isolation misses the bigger picture. Solving the root cause addresses all three.

### How to Find Root Causes
- **Ask "why" repeatedly.** If a customer says reports take too long, ask why. If the answer is "because the data has to be pulled manually," ask why that's the case. Keep going until you hit something structural.
- **Look for convergence.** When multiple symptoms from different interviews point to the same underlying issue, you've likely found a root cause.
- **Validate with follow-up questions.** If you suspect a root cause, test it in subsequent interviews: "Other people have told us that [root cause] is a challenge. Does that resonate with you?"

## Step 4: Build a Problem Inventory

Create a structured catalog of the problems you've identified. For each problem, document:

### Problem Record Structure

**Problem Name:** Use customer language (e.g., "Chasing down numbers for month-end close")

**Problem Description:** 2-3 sentences describing the problem in the customer's context. What's happening, who's affected, and what the impact is.

**Evidence:**
- Number of interviews where this was mentioned (e.g., "12 of 18 interviews")
- Representative quotes (2-3 verbatim quotes that capture the problem well)
- Personas affected (which roles experience this problem)

**Current Workarounds:** How do customers currently cope? Workarounds indicate real pain — nobody builds elaborate workarounds for trivial problems.

**Impact:**
- Time cost (hours/week wasted)
- Financial cost (if quantifiable)
- Opportunity cost (what they can't do because of this problem)
- Emotional cost (frustration, stress, career risk)

**Urgency Indicators:**
- How often does this problem occur? (daily, weekly, quarterly)
- What triggers it?
- What happens if it's not solved?

**Related Problems:** Which other problems in your inventory are connected to this one?

## Step 5: Prioritize the Problem Inventory

Not all problems are equally worth solving. Before moving to validation, do an initial prioritization based on your qualitative findings:

### Prioritization Criteria

| Criterion | High Signal | Low Signal |
|-----------|------------|------------|
| Frequency | Mentioned in 60%+ of interviews | Mentioned in <20% of interviews |
| Intensity | Customers get visibly frustrated or animated | Mentioned in passing, low emotion |
| Workaround complexity | Elaborate workarounds exist | Simple workarounds or "we just live with it" |
| Financial impact | Customers can quantify the cost | Vague or unquantifiable |
| Breadth | Affects multiple personas/segments | Narrow to one niche |
| Strategic fit | Aligns with your distinctive competencies | Would require building entirely new capabilities |

Problems that score highly across multiple criteria are your strongest candidates for validation.

## Step 6: Share Findings with Stakeholders

Before proceeding to formal validation, share your synthesized findings with the cross-functional stakeholders who provided input during planning (see research-planning.md). This serves multiple purposes:

- **Builds credibility.** You went out, talked to the market, and came back with evidence.
- **Surfaces blind spots.** Others may connect your findings to data or patterns you didn't see.
- **Creates alignment.** When the entire team has seen the same market evidence, prioritization discussions become grounded in data rather than opinion.
- **Generates momentum.** When developers hear customers describe problems in their own words (especially through direct quotes), it inspires better solutions.

### Presentation Format
Lead with the top 3-5 problems. For each:
1. State the problem in customer language
2. Share 2-3 representative quotes
3. Note frequency (how many interviews mentioned it)
4. Describe current workarounds
5. Quantify impact where possible

Resist the urge to jump to solutions during this presentation. The goal is shared understanding of problems. Solutions come later, informed by this understanding.

## Anti-Patterns to Avoid

- **Cherry-picking quotes to support a predetermined conclusion.** Let the data lead.
- **Ignoring problems that are inconvenient.** If the market is telling you something you don't want to hear, that's the most important thing to pay attention to.
- **Over-weighting vocal customers.** The loudest 20% of customers don't represent the quiet 80%. Ensure your synthesis reflects the broader pattern.
- **Confusing correlation with causation.** Just because two problems co-occur doesn't mean one causes the other.
- **Analysis paralysis.** You don't need perfect synthesis. You need to be directionally right and move to validation.
