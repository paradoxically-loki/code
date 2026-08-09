# MS5610: Security Analysis and Portfolio Management

**Author:** Lokesh Parihar

---

## Table of Contents

1. [28th July – Thursday](#28th-july--thursday)
2. [31st July – Friday](#31st-july--friday)
3. [4th August – Tuesday](#4th-august--tuesday)

---

## 28th July – Thursday

*(No notes recorded for this session.)*

---

## 31st July – Friday

- The **52-week high/low** range is a decent reference band for a security's price.
- Key valuation questions: what could the value be in the future? Is the security **overvalued** or **undervalued** relative to our future projections?

### Security Valuation

- **Debt Instruments**
  - Coupon Instruments
  - Treasury Instruments
  - Zero Coupon Instruments
  - Flexi Coupon Instruments
  - Deep Discount Instruments
- **Equity Instruments**
  - Common Equity Instruments
  - Preferred Equity Instruments
  - Convertible Instruments
  - Derivative Instruments

### Coupon Instruments

- **LTP** = Last Traded Price.
- The interest accrued on a coupon between payment dates is not itself "traded" as a separate instrument.
- Three related concepts: **clean price**, **dirty price**, and **accrued interest**.
  - Dirty price = clean price + accrued interest.
- Trades are quoted at the **clean price**, and accrued interest is paid separately to the seller by the new buyer.
- In practice, this is more commonly handled by having the buyer pay a price that already nets out (deducts) the accrued interest owed.

### Valuation of Coupon Instruments

$$\text{Running Yield} = \frac{\text{Coupon Amount}}{\text{Clean Price}}$$

$$\text{Simple Yield to Maturity} = \frac{C}{CP} + \frac{P - CP}{n \times CP}$$

$$\text{Price} = \sum_{i=1}^{n} \frac{C_i}{(1+YTM)^i} + \frac{P}{(1+YTM)^n}$$

> *(Corrected the last term above — the original had the exponent $n$ sitting outside the fraction, i.e. $\frac{P}{1+YTM}^n$, which isn't valid; it should be $\frac{P}{(1+YTM)^n}$, discounting the face value back n periods like the coupons.)*

Where:
- $C$ = Coupon Amount
- $P$ = Face Value
- $CP$ = Clean Price
- $K$ = discount rate/required return (*how do we find K? — flagged as open question in the original notes*)

$$\text{Accrued Interest} = \frac{C}{m}\left(\frac{d_{xi} - d_{xc}}{T_d}\right)$$

- $d_{xi}$ = number of days since the last coupon payment
- $d_{xc}$ = number of days between book closure dates

> **Note:** this formula and the exact definitions of $d_{xi}$, $d_{xc}$, and $T_d$ were flagged in the original notes as needing double-checking — I've left it as recorded rather than guessing at a "corrected" version, since accrued-interest conventions vary by market and instrument (and India's book-closure convention for G-Secs is a special case worth confirming against the course material).

**Other terms to follow up on** (as flagged in original notes):
- Term structure of interest rates
- **Book closure date** — the date announced by the exchange/issuer on which dividend or interest eligibility is determined
- **Ex-coupon** vs **cum-coupon** dates

### Equity Valuation: Multiplier Method

Broad categories of multiplier-based valuation:
- Earnings Valuation
- Revenue Valuation
- Cash Flow Valuation
- Economic Value Added
- Accounting Value
- Yield Valuation
- Members' Valuation

> *(Left "Members' Valuation" as written — this term wasn't standard enough for me to confidently rename it. If it's meant to be something like "embedded value" (common in insurance/mutual company valuation), worth confirming with your instructor or the course reading.)*

$$\text{PE Multiplier} = \frac{\text{Market Price}}{\text{Earnings Per Share}}$$

### Multiplier Method

**Price-Earnings Ratio (PE):**

$$PEG \text{ Ratio} = \frac{PE \text{ Multiplier}}{\text{Growth Rate}}$$

> *(Renamed "PE Growth Rate" to its standard name, the **PEG ratio**, since that's what this formula computes.)*

$$PE_{\text{Relative}} = \frac{\text{Share PE}}{\text{Index PE}}$$

**Price to Sales Ratio (PSR):**

$$PSR = \frac{\text{Market Capitalisation}}{\text{One-Year Total Revenue}}$$

**Price to Book Value Ratio (PBV):**

$$PBV = \frac{\text{Market Price}}{\text{Book Value per Share}}$$

---

## 4th August – Tuesday

### Security Valuation (continued)

### Class Exercise

**Price to Sales Ratio (PSR):**

$$PSR = \frac{\text{Share Price}}{\text{Revenue per Share}} = \frac{\text{Market Cap}}{\text{Annual Revenue}}$$