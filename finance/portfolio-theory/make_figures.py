"""Figures for Chapter 5 (Portfolio Management) notes - Capinski & Zastawniak.
All data are the book's own examples unless stated otherwise."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = "/home/claude/ch5/figures/"
B, O, A, Y, M, G, V, R = "#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300", "#6250d6", "#e34948"
INK, INK2, GRID = "#0b0b0b", "#52514e", "#e4e3df"
plt.rcParams.update({
    "svg.fonttype": "path", "font.family": "DejaVu Sans", "font.size": 10,
    "axes.edgecolor": INK2, "axes.labelcolor": INK, "axes.titlesize": 11,
    "axes.titleweight": "bold", "axes.spines.top": False, "axes.spines.right": False,
    "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.7,
    "xtick.color": INK2, "ytick.color": INK2, "legend.frameon": False,
    "figure.facecolor": "white", "axes.facecolor": "white", "lines.linewidth": 2,
})
def save(fig, name):
    fig.tight_layout(); fig.savefig(OUT + name, format="svg", bbox_inches="tight"); fig.savefig("/tmp/claude-0/-home-claude/327c6f50-71de-5337-b96a-a34486cccd5a/scratchpad/" + name.replace(".svg", ".png"), dpi=90, bbox_inches="tight"); plt.close(fig)

# ---------------------------------------------------------------- 1. two securities, varying rho
mu1, s1, mu2, s2 = 0.10, 0.15, 0.20, 0.30   # illustrative; sigma1/sigma2 = 0.5
rhos = [(-1, B), (-0.5, O), (0.5, A), (0.8, V), (1, R)]
s = np.linspace(-0.6, 1.6, 600)
fig, ax = plt.subplots(figsize=(7.2, 4.6))
for rho, c in rhos:
    sig = np.sqrt(np.maximum((1-s)**2*s1**2 + s**2*s2**2 + 2*s*(1-s)*rho*s1*s2, 0))
    mu = (1-s)*mu1 + s*mu2
    ax.plot(sig, mu, color=c, lw=1, alpha=.55, ls="--")
    k = (s >= 0) & (s <= 1)
    ax.plot(sig[k], mu[k], color=c, lw=2.4, label=fr"$\rho_{{12}}={rho}$")
ax.scatter([s1, s2], [mu1, mu2], s=60, color=INK, zorder=5, edgecolor="white", lw=2)
ax.annotate(r"$(\sigma_1,\mu_1)$", (s1, mu1), xytext=(8, -14), textcoords="offset points")
ax.annotate(r"$(\sigma_2,\mu_2)$", (s2, mu2), xytext=(8, -4), textcoords="offset points")
ax.axvline(s1, color=INK2, lw=.8, ls=":")
ax.text(s1+.003, 0.235, r"$\sigma_1$", color=INK2)
ax.set_xlim(0, 0.45); ax.set_ylim(0.06, 0.26)
ax.set_xlabel(r"risk  $\sigma_V$"); ax.set_ylabel(r"expected return  $\mu_V$")
ax.set_title("Two-security portfolio lines for different correlations (cf. Fig 5.1, 5.3, 5.4)")
ax.legend(loc="upper left", fontsize=9)
ax.text(0.30, 0.075, "solid = no short selling (0 ≤ s ≤ 1)\ndashed = with short selling\n"
        r"threshold: $\rho_{12}=\sigma_1/\sigma_2=0.5$", fontsize=8.5, color=INK2)
save(fig, "fig1_two_security_rho.svg")

# ---------------------------------------------------------------- 2. variance vs s : three cases
fig, axs = plt.subplots(1, 3, figsize=(10, 3.3), sharey=False)
cases = [(0.9, "case 3: ρ > σ₁/σ₂  →  s₀ < 0, s_min = 0"),
         (0.2, "case 1: ρ < σ₁/σ₂  →  0 < s₀ < 1"),
         (None, "σ₂ < σ₁ with high ρ  →  s₀ > 1, s_min = 1")]
for ax, (rho, title) in zip(axs, cases):
    if rho is None:
        a1, a2, r = 0.30, 0.15, 0.9
    else:
        a1, a2, r = s1, s2, rho
    ss = np.linspace(-0.8, 1.8, 400)
    var = (1-ss)**2*a1**2 + ss**2*a2**2 + 2*ss*(1-ss)*r*a1*a2
    s0 = (a1**2 - r*a1*a2)/(a1**2 + a2**2 - 2*r*a1*a2)
    smin = min(max(s0, 0), 1)
    ax.plot(ss, var, color=INK2, lw=1)
    k = (ss >= 0) & (ss <= 1)
    ax.plot(ss[k], var[k], color=B, lw=2.6)
    v0 = (1-s0)**2*a1**2 + s0**2*a2**2 + 2*s0*(1-s0)*r*a1*a2
    vm = (1-smin)**2*a1**2 + smin**2*a2**2 + 2*smin*(1-smin)*r*a1*a2
    ax.scatter([s0], [v0], color=O, s=50, zorder=5, edgecolor="white", lw=1.5, label=f"$s_0$={s0:.2f}")
    ax.scatter([smin], [vm], color=A, s=70, marker="D", zorder=6, edgecolor="white", lw=1.5, label=f"$s_{{min}}$={smin:.2f}")
    for x in (0, 1): ax.axvline(x, color=INK2, lw=.7, ls=":")
    ax.set_title(title, fontsize=9, fontweight="normal")
    ax.set_xlabel(r"$s=w_2$"); ax.legend(fontsize=8, loc="upper center")
    ax.set_ylim(0, None)
axs[0].set_ylabel(r"$\sigma_V^2$")
fig.suptitle(r"Minimising $\sigma_V^2(s)$ — Theorem 5.5 (cf. Fig 5.2). Bold = no short selling", fontsize=11, fontweight="bold")
save(fig, "fig2_variance_vs_s.svg")

# ---------------------------------------------------------------- 3. one risky + risk-free
rF, m1, sg1 = 0.05, 0.15, 0.20
w = np.linspace(-1, 2, 300)
fig, ax = plt.subplots(figsize=(6, 4))
sig, mu = np.abs(w)*sg1, rF + w*(m1-rF)
ax.plot(sig[w < 0], mu[w < 0], color=INK2, lw=1, ls="--", label="short the risky asset (w₁ < 0)")
ax.plot(sig[(w >= 0) & (w <= 1)], mu[(w >= 0) & (w <= 1)], color=B, lw=2.6, label="0 ≤ w₁ ≤ 1 (lend at r_F)")
ax.plot(sig[w > 1], mu[w > 1], color=O, lw=2, label="w₁ > 1 (borrow at r_F, leverage)")
ax.scatter([0, sg1], [rF, m1], color=INK, s=55, zorder=5, edgecolor="white", lw=2)
ax.annotate(r"$(0, r_F)$", (0, rF), xytext=(8, 8), textcoords="offset points")
ax.annotate(r"$(\sigma_1,\mu_1)$", (sg1, m1), xytext=(6, -14), textcoords="offset points")
ax.set_xlabel(r"$\sigma_V=|w_1|\sigma_1$"); ax.set_ylabel(r"$\mu_V$")
ax.set_title("One risky + one risk-free security (Prop 5.7, Fig 5.5)")
ax.legend(fontsize=8.5, loc="upper left"); ax.set_xlim(0, .42)
save(fig, "fig3_risky_plus_riskfree.svg")

# ---------------------------------------------------------------- Example 5.10 data
m = np.array([.10, .15, .20]); sd = np.array([.28, .24, .25])
Rm = np.array([[1, -.1, .25], [-.1, 1, .2], [.25, .2, 1]])
C = Rm*np.outer(sd, sd); Ci = np.linalg.inv(C); u = np.ones(3)
a_, b_, c_ = u@Ci@u, u@Ci@m, m@Ci@m          # uC^-1u^T, uC^-1m^T, mC^-1m^T
det = a_*c_ - b_**2
def w_line(muV):  # Prop 5.10
    return ((c_ - b_*muV)*(u@Ci) + (a_*muV - b_)*(m@Ci))/det
w_mvp = u@Ci/a_
mu_mvp, sd_mvp = m@w_mvp, np.sqrt(w_mvp@C@w_mvp)


def no_short_band(mu_grid):
    """min/max sigma over the segment {w>=0, sum w=1, m.w=mu} (exact via fine grid)."""
    lo, hi = [], []
    for mv in mu_grid:
        pts = []
        for i, j in [(0, 1), (1, 2), (0, 2)]:
            if (m[i]-mv)*(m[j]-mv) <= 0 and m[i] != m[j]:
                t_ = (mv-m[j])/(m[i]-m[j]); w_ = np.zeros(3); w_[i], w_[j] = t_, 1-t_; pts.append(w_)
        if len(pts) < 2: lo.append(np.nan); hi.append(np.nan); continue
        P, Q = pts[0], pts[-1]; tt = np.linspace(0, 1, 400)[:, None]; Ws = P*(1-tt)+Q*tt
        v = np.sqrt(np.einsum("ij,jk,ik->i", Ws, C, Ws)); lo.append(v.min()); hi.append(v.max())
    return np.array(lo), np.array(hi)

# ---------------------------------------------------------------- 4. Markowitz bullet
fig, ax = plt.subplots(figsize=(7.2, 5))
muV = np.linspace(0.02, 0.30, 400)
sdV = np.sqrt((a_*muV**2 - 2*b_*muV + c_)/det)
ax.fill_betweenx(muV, sdV, 0.5, color="#e6e5e0", label="attainable (short selling allowed)")
mg = np.linspace(0.1, 0.2, 300); lo_, hi_ = no_short_band(mg)
ax.fill_betweenx(mg, lo_, hi_, color="#9cc3ef", alpha=.8, label="attainable without short selling")
ax.plot(lo_, mg, color=V, lw=1.6, label="min-variance line, no short selling")
ax.plot(sdV[muV < mu_mvp], muV[muV < mu_mvp], color=INK2, lw=1.6, ls="--", label="minimum variance line (inefficient half)")
ax.plot(sdV[muV >= mu_mvp], muV[muV >= mu_mvp], color=B, lw=2.8, label="efficient frontier")
ax.scatter(sd, m, color=INK, s=55, zorder=5, edgecolor="white", lw=2)
for i in range(3):
    ax.annotate(f"Security {i+1}\n({sd[i]:.2f}, {m[i]:.2f})", (sd[i], m[i]), xytext=(7, -6), textcoords="offset points", fontsize=8)
ax.scatter([sd_mvp], [mu_mvp], color=O, s=80, marker="D", zorder=6, edgecolor="white", lw=1.5)
ax.annotate(f"MVP\nσ={sd_mvp:.3f}, μ={mu_mvp:.3f}", (sd_mvp, mu_mvp), xytext=(-62, -34), textcoords="offset points", fontsize=8.5, color=INK)
ax.set_xlim(0.10, 0.36); ax.set_ylim(0.04, 0.26)
ax.set_xlabel(r"$\sigma_V$"); ax.set_ylabel(r"$\mu_V$")
ax.set_title("Markowitz bullet — Example 5.10 / 5.11 data (cf. Fig 5.7, 5.10)")
ax.legend(fontsize=8, loc="upper center", bbox_to_anchor=(0.5, -0.13), ncol=2)
save(fig, "fig4_markowitz_bullet.svg")

# ---------------------------------------------------------------- 5. weight plane w2,w3
fig, ax = plt.subplots(figsize=(5.4, 5))
ax.fill([0, 1, 0], [0, 0, 1], color="#9cc3ef", alpha=.5, label="no short selling (triangle)")
ax.plot([0, 1, 0, 0], [0, 0, 1, 0], color=INK2, lw=1)
xs = np.linspace(-0.6, 1.6, 10)
for line in ([xs, 0*xs], [0*xs, xs], [xs, 1-xs]):
    ax.plot(*line, color=INK2, lw=.6, ls=":")
mv = np.linspace(-0.05, 0.40, 50); WL = np.array([w_line(x) for x in mv])
ax.plot(WL[:, 1], WL[:, 2], color=B, lw=2.8, label="minimum variance line (Prop 5.10)")
ax.scatter([w_mvp[1]], [w_mvp[2]], color=O, s=70, marker="D", zorder=5, edgecolor="white", lw=1.5, label="MVP")
for (x, y, t) in [(0, 0, "only sec 1"), (1, 0, "only sec 2"), (0, 1, "only sec 3")]:
    ax.scatter([x], [y], color=INK, s=30, zorder=5); ax.annotate(t, (x, y), xytext=(5, 5), textcoords="offset points", fontsize=8)
ax.set_xlim(-0.4, 1.4); ax.set_ylim(-0.4, 1.4); ax.set_aspect("equal")
ax.set_xlabel(r"$w_2$"); ax.set_ylabel(r"$w_3$   ($w_1=1-w_2-w_3$)")
ax.set_title("Attainable portfolios on the $w_2,w_3$ plane (Fig 5.6)")
ax.legend(fontsize=8, loc="upper right")
save(fig, "fig5_weight_plane.svg")

# ---------------------------------------------------------------- 6. CML + market portfolio
rF = 0.05
gw = (m - rF*u)@Ci; wM = gw/gw.sum(); muM, sdM = m@wM, np.sqrt(wM@C@wM)
fig, ax = plt.subplots(figsize=(7.2, 5))
ax.fill_betweenx(muV, sdV, 0.5, color="#eeede9")
ax.plot(sdV, muV, color=INK2, lw=1.4, label="minimum variance line (risky assets only)")
x = np.linspace(0, 0.34, 50)
ax.plot(x, rF + (muM-rF)/sdM*x, color=B, lw=2.8, label=r"CML: $\mu=r_F+\frac{\mu_M-r_F}{\sigma_M}\sigma$")
ax.plot(x, rF - (muM-rF)/sdM*x, color=INK2, lw=1, ls="--")
ax.scatter([0], [rF], color=INK, s=55, zorder=5, edgecolor="white", lw=2)
ax.scatter([sdM], [muM], color=O, s=260, marker="*", zorder=6, edgecolor="white", lw=.8)
ax.annotate(f"market portfolio M\nσ_M={sdM:.3f}, μ_M={muM:.3f}\nw_M=[{wM[0]:.3f}, {wM[1]:.3f}, {wM[2]:.3f}]",
            (sdM, muM), xytext=(10, -40), textcoords="offset points", fontsize=8.5)
ax.annotate(r"$(0,r_F)$, $r_F=5\%$", (0, rF), xytext=(6, 6), textcoords="offset points")
ax.annotate("lending\n(r_F + M)", (sdM*.45, rF+(muM-rF)*.45), xytext=(-5, 18), textcoords="offset points", fontsize=8, color=INK2)
ax.annotate("borrowing\n(leveraged M)", (sdM*1.45, rF+(muM-rF)*1.45), xytext=(-60, 10), textcoords="offset points", fontsize=8, color=INK2)
ax.set_xlim(0, 0.34); ax.set_ylim(0, 0.28)
ax.set_xlabel(r"$\sigma$"); ax.set_ylabel(r"$\mu$")
ax.set_title("Capital Market Line — Example 5.13 (cf. Fig 5.11)")
ax.legend(fontsize=8.5, loc="upper left")
save(fig, "fig6_cml.svg")

# ---------------------------------------------------------------- 7. characteristic line (simulated)
rng = np.random.default_rng(3)
KM = rng.normal(0.01, 0.045, 60); beta_true, alpha_true = 1.3, 0.002
KV = alpha_true + beta_true*KM + rng.normal(0, 0.025, 60)
beta_hat = np.cov(KV, KM, ddof=0)[0, 1]/np.var(KM); alpha_hat = KV.mean() - beta_hat*KM.mean()
fig, ax = plt.subplots(figsize=(6.2, 4.4))
ax.axhline(0, color=INK2, lw=.8); ax.axvline(0, color=INK2, lw=.8)
ax.scatter(KM, KV, s=28, color=B, alpha=.8, edgecolor="white", lw=.8, label="scenarios / observations")
xx = np.linspace(KM.min(), KM.max(), 10)
ax.plot(xx, alpha_hat + beta_hat*xx, color=O, lw=2.4,
        label=fr"$y=\beta_V x+\alpha_V$:  $\beta_V$={beta_hat:.2f}, $\alpha_V$={alpha_hat:.4f}")
i = np.argmax(np.abs(KV - (alpha_hat+beta_hat*KM)))
ax.plot([KM[i], KM[i]], [KV[i], alpha_hat+beta_hat*KM[i]], color=R, lw=1.4, ls=":")
ax.annotate(r"residual $\varepsilon_V$", (KM[i], KV[i]), xytext=(8, 0), textcoords="offset points", fontsize=8.5, color=INK)
ax.set_xlabel(r"market return $K_M$"); ax.set_ylabel(r"portfolio return $K_V$")
ax.set_title("Characteristic line / beta (Fig 5.12) — simulated data")
ax.legend(fontsize=8.5, loc="upper left")
save(fig, "fig7_characteristic_line.svg")

# ---------------------------------------------------------------- 8. CML vs SML
rng = np.random.default_rng(11)
fig, (a1, a2) = plt.subplots(1, 2, figsize=(10, 4.2))
# securities + random portfolios on the CAPM: mu = rF + (muM-rF) beta
betas_pts = np.concatenate([[(wM@C@np.eye(3)[i])/sdM**2 for i in range(3)]])
Wp = rng.dirichlet([1, 1, 1], 8)
pts_mu = np.r_[m, Wp@m]; pts_sd = np.r_[sd, np.sqrt(np.einsum("ij,jk,ik->i", Wp, C, Wp))]
pts_beta = np.r_[[(np.eye(3)[i]@C@wM)/sdM**2 for i in range(3)], (Wp@C@wM)/sdM**2]
a1.plot(sdV, muV, color=INK2, lw=1.2)
a1.plot(x, rF + (muM-rF)/sdM*x, color=B, lw=2.6, label="CML (efficient portfolios only)")
a1.scatter(pts_sd, pts_mu, s=30, color=V, zorder=5, edgecolor="white", label="securities & portfolios")
a1.scatter([sdM], [muM], color=O, s=110, marker="*", zorder=6)
a1.set_xlim(0, .34); a1.set_ylim(0, .26); a1.set_xlabel(r"$\sigma$"); a1.set_ylabel(r"$\mu$")
a1.set_title("Capital Market Line (σ, μ plane)"); a1.legend(fontsize=8, loc="upper left")
bb = np.linspace(-0.2, 1.6, 10)
a2.plot(bb, rF + (muM-rF)*bb, color=B, lw=2.6, label=r"SML: $\mu_V=r_F+(\mu_M-r_F)\beta_V$")
a2.scatter(pts_beta, pts_mu, s=30, color=V, zorder=5, edgecolor="white", label="same securities & portfolios")
a2.scatter([1], [muM], color=O, s=110, marker="*", zorder=6)
a2.annotate(r"M: $\beta_M=1$", (1, muM), xytext=(10, -14), textcoords="offset points", fontsize=8.5)
a2.scatter([0], [rF], color=INK, s=40, zorder=6); a2.annotate(r"$r_F$ ($\beta=0$)", (0, rF), xytext=(6, -12), textcoords="offset points", fontsize=8.5)
a2.scatter([0.55], [0.17], color=A, s=70, marker="^", zorder=6); a2.annotate("above SML →\nunderpriced (buy)", (0.55, .17), xytext=(-40, 10), textcoords="offset points", fontsize=8)
a2.scatter([1.35], [0.15], color=R, s=70, marker="v", zorder=6); a2.annotate("below SML →\noverpriced (sell)", (1.35, .15), xytext=(-40, -30), textcoords="offset points", fontsize=8)
a2.set_xlim(-0.2, 1.6); a2.set_ylim(0, .26); a2.set_xlabel(r"$\beta$"); a2.set_ylabel(r"$\mu$")
a2.set_title("Security Market Line (β, μ plane)"); a2.legend(fontsize=8, loc="upper left")
fig.suptitle("CML applies only to efficient portfolios; SML applies to every security (Fig 5.13, Example 5.13 data)", fontsize=10.5, fontweight="bold")
save(fig, "fig8_cml_vs_sml.svg")

# ---------------------------------------------------------------- 9. diversification (beyond book)
n = np.arange(1, 51); sig_i, rho = 0.30, 0.25
var_n = sig_i**2/n + (1-1/n)*rho*sig_i**2
fig, ax = plt.subplots(figsize=(6.4, 4))
ax.plot(n, np.sqrt(var_n), color=B, lw=2.4, label=r"total risk $\sigma_V$ (equal weights)")
ax.axhline(np.sqrt(rho)*sig_i, color=O, lw=2, ls="--", label=r"systematic floor $\sqrt{\rho}\,\sigma$")
ax.fill_between(n, np.sqrt(rho)*sig_i, np.sqrt(var_n), color="#9cc3ef", alpha=.4, label="diversifiable risk")
ax.set_xlabel("number of securities n"); ax.set_ylabel(r"$\sigma_V$"); ax.set_ylim(0, .32)
ax.set_title("Why diversify: risk falls to a systematic floor\n(σ = 30% each, pairwise ρ = 0.25; illustrative)", fontsize=10)
ax.legend(fontsize=8.5)
save(fig, "fig9_diversification.svg")

print("MVP", w_mvp.round(3), round(mu_mvp, 3), round(sd_mvp, 3))
print("market", wM.round(3), round(muM, 4), round(sdM, 4), "beta_hat", beta_hat)
print("line coefs a,b,c", a_, b_, c_)
