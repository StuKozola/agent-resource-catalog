# Validating Market Problems

## Why Validation Matters

Discovery (NIHITO interviews) tells you what problems exist. Validation confirms whether those problems are worth solving at scale. Without validation, product teams can invest significant time and resources into an idea that serves only a vocal minority.

Validation is about answering a specific question: **Is this problem urgent enough, pervasive enough, and painful enough that a sufficient number of people will pay to solve it?**

## The Three Validation Filters

The Pragmatic Framework provides three filters for evaluating whether a market problem is worth building a solution for:

### 1. Urgency
**Question:** Does this problem cause real pain, right now?

Urgency means the problem is active, not theoretical. Customers feel the cost of not solving it. There is a time dimension — they need a solution soon, not someday.

**How to assess urgency:**
- How frequently does the problem occur? (Daily problems are more urgent than annual ones)
- What triggers the problem? (Is the trigger increasing in frequency?)
- What is the cost of inaction? (If they do nothing, what happens?)
- Are there external forces creating urgency? (Regulatory deadlines, competitive pressure, market shifts)
- Have they already tried to solve it? (Active solution-seeking indicates urgency)

**Urgency signals from interviews:**
- "We need to figure this out by [date]"
- "This is costing us [specific amount] every month"
- "I've been trying to find a solution for months"
- Emotional intensity when describing the problem
- They bring it up unprompted (you didn't even ask about it)

### 2. Pervasiveness
**Question:** Does this problem affect enough people to support a business?

A problem that afflicts one customer is a customization request. A problem shared across a market segment is an opportunity. Pervasiveness ensures the addressable market is large enough to justify the investment.

**How to assess pervasiveness:**
- What percentage of your interview subjects mentioned this problem? (60%+ is a strong signal)
- Does the problem cross company sizes, geographies, or sub-segments?
- Can you estimate the total addressable population with this problem?
- Is the problem growing or shrinking? (Market trends, regulatory changes, technology shifts)

**Quantitative validation methods for pervasiveness:**
- **Surveys:** Send a structured survey to a larger sample. Ask respondents to rate the importance of the problem and their satisfaction with current solutions.
- **Usage data:** If you have an existing product, look at feature usage patterns, support tickets, and churn data that correlate with the problem.
- **Market sizing:** Estimate the number of potential buyers by segment using industry data, analyst reports, and public data sources.
- **Search volume analysis:** How many people are searching for solutions to this problem online?

### 3. Willingness to Pay
**Question:** Is this problem painful enough that people will spend money to make it go away?

A problem can be urgent and pervasive but if customers won't pay to solve it, it's not a viable product opportunity (though it might be a feature of a broader solution).

**How to assess willingness to pay:**
- Are customers currently spending money on workarounds? (Hiring extra staff, buying partial solutions, paying consultants)
- What is the quantifiable cost of the problem? (If it costs $100K/year, they'll pay $20K for a solution)
- Have they budgeted for a solution? (Or is this "nice to have" with no allocated budget)
- What's the price of the closest alternative or competitor? (This anchors willingness to pay)
- Can you identify a clear economic buyer? (Someone with both the pain and the budget authority)

**Important:** Price should reflect the value of making the problem go away, not what it cost to build the solution. This is a fundamental Pragmatic principle.

## The Satisfaction vs. Importance Matrix

This is a key validation tool from Pragmatic Institute's methodology. Plot market problems on a 2x2 matrix:

```
                    HIGH IMPORTANCE
                          |
    UNDERSERVED           |          APPROPRIATELY SERVED
    (High importance,     |          (High importance,
     Low satisfaction)    |           High satisfaction)
    ★ Best opportunities  |          ○ Maintain, don't reinvent
                          |
   ───────────────────────┼───────────────────────────
                          |
    OVER-INVESTED         |          TABLE STAKES
    (Low importance,      |          (Low importance,
     Low satisfaction)    |           High satisfaction)
    ✕ Deprioritize        |          △ Necessary but not 
                          |            differentiating
                    LOW IMPORTANCE
         LOW SATISFACTION             HIGH SATISFACTION
```

**How to use this matrix:**

- **Underserved (top-left):** High importance to the customer, low satisfaction with existing solutions. These are your best opportunities — customers care deeply about the problem and current solutions aren't working.

- **Appropriately served (top-right):** High importance, high satisfaction. The market has already solved this well. Competing here requires significant differentiation. Don't try to reinvent what's working.

- **Over-invested (bottom-left):** Low importance, low satisfaction. Customers don't care much and aren't satisfied, but they also don't care enough to switch. Deprioritize.

- **Table stakes (bottom-right):** Low importance, high satisfaction. These are expected capabilities — you need them to compete, but they won't differentiate you.

**To populate the matrix**, include questions in your validation survey like:
- "How important is [problem] to your work?" (Scale: 1-5)
- "How satisfied are you with your current solution for [problem]?" (Scale: 1-5)

Then plot each problem using the average scores.

## Designing a Validation Survey

After qualitative discovery, a structured survey validates findings at scale.

### Survey Design Principles

1. **Keep it short.** 5-10 minutes maximum. Respect respondents' time.
2. **Use the customer's language.** Phrase problems the way customers described them in interviews, not in your internal jargon.
3. **Don't lead.** Avoid questions that telegraph the "right" answer.
4. **Include a mix of question types:**
   - Rating scales (importance, satisfaction, frequency)
   - Ranking (force prioritization among competing problems)
   - Open text (one or two open-ended questions to capture things you missed)

### Recommended Survey Structure

**Section 1: Context** (2-3 questions)
- Role, company size, industry
- How they currently handle [relevant domain]

**Section 2: Problem Importance** (3-5 questions)
For each of the top problems from your discovery phase:
- "How important is [problem] to your work?" (1 = Not at all, 5 = Critical)
- "How frequently do you experience [problem]?" (Rarely / Monthly / Weekly / Daily)

**Section 3: Solution Satisfaction** (3-5 questions)
For each problem:
- "How satisfied are you with your current approach to [problem]?" (1 = Very dissatisfied, 5 = Very satisfied)
- "What do you currently use to address [problem]?" (Open text or multiple choice)

**Section 4: Prioritization** (1-2 questions)
- "If you could only solve ONE of these problems, which would you choose?" (Forced rank or single select)
- "How much would solving [top problem] be worth to your organization annually?" (Range brackets)

**Section 5: Open Capture** (1 question)
- "Is there anything else about [domain] that keeps you up at night that we didn't ask about?"

### Sample Size Targets
For B2B products, aim for 50-200 survey responses across relevant segments. For B2C, 200-500+. The key is having enough responses per segment to be confident in patterns.

## When a Problem Passes Validation

A market problem is validated when:

1. **Urgency confirmed:** 60%+ of survey respondents rate it "Important" or "Critical" frequency is weekly or more
2. **Pervasiveness confirmed:** The problem spans multiple sub-segments and represents a sizable addressable market
3. **Willingness to pay confirmed:** Respondents indicate they would allocate budget for a solution, or they're already spending on workarounds
4. **Solution gap confirmed:** Satisfaction with current solutions is low (plotting in the "Underserved" quadrant of the matrix)

## When a Problem Fails Validation

Not every problem that surfaces in discovery will validate. This is normal and valuable. It's far better to learn that a problem isn't pervasive before building a product than after launching one.

If a problem fails validation:
- **Low urgency:** The problem is real but not painful enough to drive purchasing behavior. Monitor it — urgency can change with market conditions.
- **Low pervasiveness:** The problem affects too few people. Consider whether it's a feature within a larger solution rather than a standalone opportunity.
- **Low willingness to pay:** The problem is painful but not enough to open wallets. Consider whether the problem could be bundled with something customers are already paying for.
- **Already solved well:** Satisfaction is high. Competing here requires 10x improvement, not incremental gains.

## Communicating Validated Problems

Once you've validated market problems, package them for organizational action:

1. **Problem statement** — Clear, customer-language description of the problem
2. **Evidence summary** — Key metrics from discovery (interview frequency) and validation (survey scores)
3. **Impact quantification** — Dollar cost, time cost, opportunity cost
4. **Market sizing** — How many potential buyers face this problem
5. **Solution gap** — What exists today and why it falls short
6. **Recommendation** — Whether to pursue, monitor, or deprioritize

Use the templates in the `templates/` directory to structure these deliverables.
