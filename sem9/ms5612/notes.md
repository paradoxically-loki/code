# MS5612: Real Options Valuation

**Author:** Lokesh Parihar (BE22B008)

---

## Table of Contents

1. [27th July – Monday](#27th-july--monday)
2. [29th July – Wednesday](#29th-july--wednesday)
3. [3rd August – Monday](#3rd-august--monday)

---

## 27th July – Monday

Finance can broadly be divided into three parts: **Personal Finance**, **Corporate Finance**, and **Financial Markets**.

**Corporate Finance (Corp Fin)** is mostly about how businesses manage their financing. It can be broadly classified into two decision types:

- **Investment decisions** → result in **assets**
- **Financing decisions** → result in **liabilities and equity** (i.e. the firm's capital structure)

### Valuing Stocks

Stocks can be valued using any of the following methods:

- Comparative method
- Dividend Discount Model
- Free Cash Flow method
- Book Value

### Valuing Debt

Debt is valued as the present value of its cash flows (interest + principal).

### Valuing Projects (Assets)

Projects/assets are valued using the **Discounted Cash Flow (DCF)** method.

**Keywords:**
- *Fortune 500* — most Fortune 500 firms use real options in their capital budgeting.
- *Managers create shareholder value* — the core objective of corporate financial decision-making.

According to McKinsey's India head, almost no Indian company uses real options in its investment decisions — this represents an opportunity.

### DCF vs. Options Approach

- DCF assumes limited discretionary power once a decision is made, whereas an options approach explicitly values managerial **flexibility**.
- If flexibility has value to decision-makers, that flexibility itself should be valued.
- Managers can create flexibility even where none seems to exist on the surface.

---

## 29th July – Wednesday

The focus of this course is on the management of **long-term assets** (not liabilities).

Four traditional capital budgeting tools: **NPV**, **IRR**, **Profitability Index (PI)**, **Payback Period (PB)**.

| Metric | Question it answers |
|---|---|
| NPV | **How much** is the project worth? |
| IRR | **What percent** return are we making? |
| PI  | **What rank** does this project have relative to others? |
| PB  | **How long** until the investment is recovered? |

### Net Present Value (NPV)

$$NPV = \sum_{i=1}^{n} \frac{C_i}{(1+r)^i} - IO$$

where **IO** = Initial Outlay.

**Investment rule:**
- If $NPV > 0$ → accept
- If $NPV < 0$ → reject
- If $NPV = 0$ → reject, since the project doesn't create any *additional* shareholder value (it merely earns the required rate of return — in practice, firms are often indifferent at exactly zero)

### Class Discussion: Strategic Investments

What is a **strategic investment**? How do you justify one — is NPV/IRR/PB/PI really the full picture?

Some investments have a **negative NPV** under conventional analysis but are still undertaken. **Strategic investments** are those that may fail conventional investment tests (NPV, IRR) in a static/certain analysis, but pass once the value of embedded flexibility (options) is accounted for.

### Worked Example

An R&D project requires an initial outlay of **$15 million**.

If R&D succeeds, the firm can build a manufacturing plant at a cost of **$40M, $80M, or $120M** (uncertain), and the resulting market/revenue could be **$50M or $130M** (uncertain).

Under the naive "expected value" approach: expected cost = $80M, expected benefit = $90M, R&D cost = $15M.

$$NPV_{\text{naive}} = 90 - 80 - 15 = -5 \text{ million} \implies \text{Reject}$$

But this ignores the fact that management doesn't have to build the plant if conditions are unfavorable — that flexibility (an embedded **real option**) has value. The following three cases explore this.

#### Case 1: Cost certain ($80M), Revenue uncertain (50% / 50%)

- If market = $50M: cost ($80M) > revenue, so **don't build** → payoff = 0
- If market = $130M: revenue exceeds cost, so **build** → payoff = $130M − $80M = $50M

$$NPV = \frac{1}{2}(0 + 50) - 15 = 25 - 15 = \mathbf{10 \text{ million}}$$

#### Case 2: Revenue certain ($90M), Cost uncertain (1/3 each: $40M, $80M, $120M)

- Cost = $40M: profit = $90 − 40 = $50M → invest
- Cost = $80M: profit = $90 − 80 = $10M → invest
- Cost = $120M: profit = $90 − 120 = −$30M → **don't invest** → payoff = 0

$$NPV = \frac{1}{3}(50 + 10 + 0) - 15 = 20 - 15 = \mathbf{5 \text{ million}}$$

#### Case 3: Both revenue and cost uncertain (1/6 for each of 6 combinations)

| Cost | Revenue | Profit if built | Decision |
|---|---|---|---|
| 40  | 50  | 10  | Build |
| 40  | 130 | 90  | Build |
| 80  | 50  | −30 | Don't build → 0 |
| 80  | 130 | 50  | Build |
| 120 | 50  | −70 | Don't build → 0 |
| 120 | 130 | 10  | Build |

$$NPV = \frac{1}{6}(10 + 90 + 0 + 50 + 0 + 10) - 15 = \frac{160}{6} - 15 \approx 26.67 - 15 = \mathbf{11.67 \text{ million}}$$

### Takeaway

In the NPV formula, $r$ is meant to reflect the **risk** of the project. The discount rate for a project must reflect that project's own risk.

Case 3 is clearly the riskiest of the three (cost and revenue both uncertain). Comparing risk across the cases could be done more rigorously by computing the **variance** of the payoffs in each case, not just the expected value.

Across the three cases, **NPV increases as uncertainty increases** — because the R&D investment isn't just buying a plant, it's buying an **option** to build the plant only if conditions turn out favorable. The manufacturing decision itself is a **call option** on the market outcome, and — as with financial options — greater underlying volatility makes that option more valuable.

---

## 3rd August – Monday

### Summary of the Last Class

- Corporations should invest only in projects with positive NPV; otherwise they aren't creating shareholder value.
- But firms often face **strategic investments (SIs)**.
- SIs may show negative NPV under the conventional DCF method.
- Strategic investments contain embedded options; once the value of that optionality is added, true NPV may be positive.
- As uncertainty increases, the value of the initial investment (i.e., the option to expand/proceed later) increases.

### Options

- An **option** gives the holder the **right, but not the obligation**, to do something.
- **Call option:** the right to **buy** the underlying asset.
- **Put option:** the right to **sell** the underlying asset.
- Options are called **derivatives** because their value is derived from an underlying asset.
- **Option value (premium):** the price paid to acquire the option — its market price.
- **Option holder:** the buyer of the option.
- **Option writer/seller:** the party who sells (writes) the option.

### Option Payoffs

- **Stock:** payoff is a straight line of slope 1 against the value of the stock.
- **Risk-free bond:** payoff is a horizontal line, independent of the stock's value.
- **Call option:**
  - *Buyer:* payoff is $0$ while $S \le$ strike, then rises with slope 1 for $S >$ strike. Subtracting the premium paid shifts this down to get the *profit* curve.
  - *Seller (writer):* the mirror image of the buyer's payoff, reflected across the x-axis.
  - The call **buyer's upside is unlimited, downside is limited** (to the premium paid). The **seller's upside is limited** (to the premium received), **downside is unlimited**.
- Options are a **zero-sum game** — one party's gain is exactly the other's loss (ignoring transaction costs).
- **Put option:**
  - *Buyer:* the payoff is the mirror image of the call buyer's payoff, reflected about the vertical line $S = $ strike (i.e., $\max(\text{strike} - S, 0)$).
  - *Seller:* the mirror image of the put buyer's payoff, reflected across the x-axis.
  - Unlike calls, **both sides of a put have limited upside and limited downside** — since the stock price can't fall below zero, both the maximum gain and maximum loss are bounded.
- Calls and puts are "vanilla" options — combining them is where things get interesting.

### Popular Option Combinations

- **Stock + Short Call (Covered Call):** caps the upside in exchange for premium income.
- **Risk-free Bond + Short Put:** by put-call parity, this has the **same payoff** as a covered call above.
- These equivalences let us build a basket of options/securities to replicate almost any desired payoff shape.

### Getting More Creative

- **Long Call + Long Put (same strike) — a Straddle:** shaped like a "kite." This position profits when the stock moves a lot in *either* direction — the more volatile the underlying, the more valuable this position.
  - Once you net out the two premiums paid, there's a range around the strike price where the position is at a net loss.
- **Long Call @ 100 + Short 2 Calls @ 110 + Long Call @ 120 — a Butterfly Spread:** a combination that profits if the stock ends up near the middle strike, with limited risk on either side.

### Real-World Examples of Options

- Uber charges more for reservation/scheduled rides (paying for the "option" of guaranteed availability).
- Indigo charges a premium for low-cost cancellation flexibility (Indigo Fare vs. Indigo UpFront) — this cancellation right is effectively a **put option** on the ticket.
- What factors should influence the size of this cancellation premium? Interestingly, the premium appears roughly constant across flights, even after accounting for flight distance and time.
- Open question raised in class: **is insurance itself a form of put option?**

### Course Project

- **Step 1:** Propose three topics you'd like to study.
- Write a ~100-word description for each topic, explaining how it involves real options.
- Submit a hard copy by **5:00 PM, August 7th**.
- The project requires **primary data**, not desk-based research.