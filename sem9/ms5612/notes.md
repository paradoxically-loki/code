# MS5612: Real Options Valuation

**Author:** Lokesh Parihar (BE22B008)

---

## Table of Contents

1. [27th July - Monday](#27th-july--monday)
2. [29th July - Wednesday](#29th-july--wednesday)
3. [3rd August - Monday](#3rd-august--monday)
4. [10th August - Monday](#10th-august---monday)
5. [12th August - Wednesday](#12th-august---wednesday)
5. [17th August - Monday](#17th-august---monday)

---

## 27th July - Monday

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

## 29th July - Wednesday

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

## 3rd August - Monday

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


## 10th August - Monday
### Summary of the last classes
- Financial Engg: Figuring out the options required to get a certain payoff.
- Characterization of options: Strike price, time to expiry, stock price.
- Put-Call Parity: $P + S = B + C$, where $S$ is the security, and $B$ is zero-coupon bond with face value equal to the strike of both options.
- This can be seen by drawing the payoff curves.
- We may also rearrange the equation and get the following: $S = C + B - P$.
- We may estimate the stock price this way.

### On Field Visit
- If the payoff from a feature or an offer resembles that of an option, then the cost of the feature should be the same as that of an option.

### The Black-Scholes Model
- Options: European, and American
- Discussion in this class, mostly on European.
- For call option, the value decreases with the increase in Strike Price.
- For call option, the value increases with the increase in time to maturity.
- For call option, the value increases with the increase in underlying price.
 $$C = S N(d_1) - e^{-rT} K N(d_2)$$
- Here, $r$ is the risk-free rate.
- $d_1 = \frac{\ln{S/K} + (r + \sigma^2/2)T}{\sigma \sqrt{T}}$
- $d_2 = d_1 - \sigma \sqrt{T}$
- T, time to expiry, must be in years, the same as $\sigma$.
- $\sigma$, volatility is the annualised,which is also the standard deviation.
- $\sigma^2$ is variance.
- Technically, $\sigma$ should be the expected volatility from now to the time of expiry.
---

## 12th August - Wednesday
### Key Assumptions of the Black-Sholes
- No dividends are paid out during the life of the options.
- Markets are random.
- There are no transaction costs in buying and selling the options.
- The risk-free rate and volatility of the underlying are known and constant.
- The returns of the underlying asset are normally distributed.
- The option is European.
- The underlying is liquid.


| Factor | Call Option | Put Option |
|------------|---------|-----------|
| Stock Price | + | -|
| Strike Price | - | + |
| Stock Volatility | + | + |
| Interest Rate | + | - |
| Time to Expiry | + | + |

### Report Submission
- Follow report writing conventions.
- Start with an introduction.
- Focus should be on what did we interpret from what we saw.
- High Standards.

### Binomial Model for the Valuation of Options
- After each time step, the price of the asset could be in either of the two possible states, i.e, upstate or downstate.
- There is an opportunity of investing in a Chemical plant.
- In year 0, 60 million needs to be invested in getting permits/clearances.
- In year 1, 400 million needs to be invested in getting the designs ready.
- In year 2, or year 3, 800 million needs to be invested in actual construction.
- For DCF Analysis, the discount rate in 10%.
- Value of a similar asset in the market is 1 billion.
- $NPV = 1000 - 60 - 400/1.1 - 800/1.1^3 = -25$
- Let's construct a binomial tree.
- If we have $S$ at the start, the value of the upstate is $e^{\sigma \sqrt{T}}$, and that of the downstate is $e^{-\sigma \sqrt{T}}$.
- In our example, we are using $\sigma = 18.23%$.
- The upstate is $1200$, and the downstate is $833$.
- At second state, we get $1440$, $1000$, and $684$.
- At third state, we get $1728$, $1200$, $833$, and $578$.
- Binomial model becomes much more realistic when the time period is very small, as the terminal values are almost continuous.
- The $400$ million at year 1 is a compound option as it is an option on another option (the $800$ million option).
- It's better to start analysis from the extreme right. 
- We shall invest at the $1728$ leaf as it's more than $800$.

### Replicating Portfolio Method to Value Options
- Assume a stock with current price $50$. 
- At the end of an year, it could either be $60$, or $40$.
- Also, assume a call option with strike 50.
- Payoff of Call option is $10$ if $S = 60$, else 0
- Also consider the following portfolio: $0.5 Stock  + 18.18 @10\% $
- Payoff of the call option, is equal to the payoff of this portfolio.
- What is the value of this portfolio today is $0.5*50 - 18.18 = 6.82$ = value of the call option.
- The above numbers can be derived from the following set of equations:
$$ 60m - 1.1B = 10 \\
40m - 1.1B = 0$$
- Do the above example by hand, and calculate the option value at each state.

---
## 17th August - Monday
### Summary of the previous class
- Revisiting the previous example.
```
                928
          699
    514         400
71        259
    168         33
          21
                0
```
- We can also find the probability of the project being abandoned in year n by using Pascal's triangle.

### Risk Neutrality
- Assume a gas distributor, 
```
September 1      December 1
                 1.37

1.00 

                 0.73
```
- A consumer is willing to pay 0.5 million to buy 6 million unit at a price of 1.05.
- The consumer is buying a call option.
- Percentage raise = $1.37/1.00 - 1 = 37\%$
- Percentage fall = $0.73/1.00 - 1 = -27\%$
- Risk free interest rate, $R_f = 8\%$.
- $P_R$: probability of raise
- $$P_R * (\text{\% of rise}) + (1-P_R)*(\text{\% of fall}) = 2\%$$
- $2\%$ reflects the interest rate of the quarter.
- In our example, $P_R = 45\%$.
- Consumer is paying $0.5/6$ premium per unit of gas.
- Payoff for the distributor: $$(45\% (1.05 - 1.37)*6 + 55\% *0)/1.02  + 0.5$$
- The minimum price for this contract must be 0.847 million, which is 0.14 per unit.
#### Calculations using  the replicating portfolio method
$$
1.37m - 1.02b = 0.32 \\
0.73m - 1.02b = 0
$$
- m = 0.5, b = 0.36. premium = 0.5*1 - 0.36 = 0.14.

#### Option Delta
$$\text{Option Delta} = \frac{\text{swing of the call}}{\text{swing of the stock}}$$
- In our example, this comes out to be $\frac{0.32 - 0}{1.37 - 0.73} = 0.5$.
- How much shall we borrow so that we'll be able to repay?
- Delta can't be more than 1.
---

