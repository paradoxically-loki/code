"""Numerical checks and figure data for the booklet.

Every number quoted in a table of the booklet comes from this script; run
    python3 make_data.py
from this folder. It writes ../data/*.dat (read by pgfplots) and ../data/results.txt.
Only numpy and the standard library are needed.
"""
import math
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "data")
os.makedirs(OUT, exist_ok=True)
rng = np.random.default_rng(20261102)
_erfc = np.vectorize(math.erfc)
LOG = open(os.path.join(OUT, "results.txt"), "w")


def say(*a):
    s = " ".join(str(x) for x in a)
    print(s, flush=True)
    LOG.write(s + "\n")
    LOG.flush()


def N(x):
    return 0.5 * _erfc(-np.asarray(x, float) / math.sqrt(2))


def phi(x):
    return np.exp(-0.5 * np.asarray(x, float) ** 2) / math.sqrt(2 * math.pi)


def bs_call(S, K, T, r, s):
    d1 = (np.log(S / K) + (r + 0.5 * s * s) * T) / (s * math.sqrt(T))
    return S * N(d1) - K * np.exp(-r * T) * N(d1 - s * math.sqrt(T))


def bs_vega(S, K, T, r, s):
    d1 = (np.log(S / K) + (r + 0.5 * s * s) * T) / (s * math.sqrt(T))
    return S * phi(d1) * math.sqrt(T)


def implied_vol(price, S, K, T, r):
    lo, hi = 1e-4, 5.0
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if bs_call(S, K, T, r, mid) > price:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


def save(name, header, *cols):
    arr = np.column_stack(cols)
    np.savetxt(os.path.join(OUT, name), arr, header=header, comments="", fmt="%.8g")


# ---------------------------------------------------------------- Brownian paths
say("== Variation of a Brownian path ==")
n = 2**16
dW = rng.normal(0, math.sqrt(1 / n), n)
W = np.concatenate([[0], np.cumsum(dW)])
step = 2**6
save("bm_path.dat", "t W", np.arange(0, n + 1, step) / n, W[::step])
ms, tv, qv = [], [], []
for k in range(2, 17):
    W_k = W[:: 2 ** (16 - k)]
    d = np.diff(W_k)
    ms.append(2.0 ** (-k))
    tv.append(np.abs(d).sum())
    qv.append((d**2).sum())
    say(f"mesh 2^-{k}: sum|dW|={tv[-1]:.3f} sum dW^2={qv[-1]:.4f}")
save("bm_var.dat", "mesh tv qv", ms, tv, qv)

# ---------------------------------------------------------------- reflection picture
n = 2000
a = 0.6
for _ in range(1000):
    dW = rng.normal(0, math.sqrt(1 / n), n)
    W = np.concatenate([[0], np.cumsum(dW)])
    hit = np.argmax(W >= a)
    if W.max() >= a and 0.2 < hit / n < 0.5 and 0.1 < W[-1] < 0.5:
        break
R = W.copy()
R[hit:] = 2 * a - W[hit:]
t = np.arange(n + 1) / n
save("reflect.dat", "t W R", t[::4], W[::4], R[::4])
say(f"reflection figure: hit at t={hit / n:.3f}, W1={W[-1]:.3f}, a={a}")

# reflection principle check
paths, n = 200000, 1000
W = np.zeros(paths)
M = np.zeros(paths)
for _ in range(n):
    W += rng.normal(0, math.sqrt(1 / n), paths)
    M = np.maximum(M, W)
for a in [0.5, 1.0, 2.0]:
    say(f"P(M_1>={a}): MC(n=1000) {np.mean(M >= a):.4f}  exact 2P(W>={a}) {2 * float(N(-a)):.4f}")

# ---------------------------------------------------------------- barrier option
say("== Down-and-out call ==")
S0, K, B, r, s, T = 100.0, 100.0, 90.0, 0.05, 0.2, 1.0
exact = bs_call(S0, K, T, r, s) - (S0 / B) ** (1 - 2 * r / s**2) * bs_call(B**2 / S0, K, T, r, s)
paths, n = 400000, 250
dt = T / n
X = np.full(paths, math.log(S0))
alive = np.ones(paths, bool)
alive_d = np.ones(paths, bool)
logB = math.log(B)
for _ in range(n):
    Xn = X + (r - 0.5 * s * s) * dt + s * math.sqrt(dt) * rng.standard_normal(paths)
    pknock = np.exp(-2 * np.maximum(X - logB, 0) * np.maximum(Xn - logB, 0) / (s * s * dt))
    alive &= rng.random(paths) > pknock
    alive_d &= Xn > logB
    X = Xn
pay = np.exp(-r * T) * np.maximum(np.exp(X) - K, 0)
v1, v2 = pay * alive_d, pay * alive
say(f"vanilla {float(bs_call(S0, K, T, r, s)):.4f} closed-form DO {float(exact):.4f}")
say(f"MC daily monitoring {v1.mean():.4f} +- {v1.std() / math.sqrt(paths):.4f}")
say(f"MC with bridge correction {v2.mean():.4f} +- {v2.std() / math.sqrt(paths):.4f}")


# ---------------------------------------------------------------- Fourier machinery
def lewis_call(cf, S, K, T, r, umax=200.0, nu=4000):
    """cf(u) is the characteristic function of ln(S_T/F); u may be complex."""
    F = S * math.exp(r * T)
    u = (np.arange(nu) + 0.5) * umax / nu
    cfv = cf(u - 0.5j)
    Ks = np.atleast_1d(K).astype(float)
    res = np.empty(len(Ks))
    for i, Ki in enumerate(Ks):
        k = math.log(F / Ki)
        val = np.sum(np.real(np.exp(1j * u * k) * cfv) / (u * u + 0.25)) * umax / nu
        res[i] = math.exp(-r * T) * (F - math.sqrt(F * Ki) / math.pi * val)
    return res


def cf_bs(s, T):
    return lambda u: np.exp(-0.5 * s * s * T * (1j * u + u * u))


def cf_heston(T, v0, kappa, theta, xi, rho):
    def f(u):
        a = kappa - rho * xi * 1j * u
        d = np.sqrt(a * a + xi * xi * (1j * u + u * u))
        g = (a - d) / (a + d)
        e = np.exp(-d * T)
        C = (kappa * theta / xi**2) * ((a - d) * T - 2 * np.log((1 - g * e) / (1 - g)))
        D = (v0 / xi**2) * (a - d) * (1 - e) / (1 - g * e)
        return np.exp(C + D)

    return f


def cf_merton(T, s, lam, muJ, delJ):
    mbar = math.exp(muJ + 0.5 * delJ**2) - 1

    def f(u):
        return np.exp(
            T * (-0.5 * s * s * (1j * u + u * u) - 1j * u * lam * mbar
                 + lam * (np.exp(1j * u * muJ - 0.5 * delJ**2 * u * u) - 1))
        )

    return f


say("== Fourier pricer sanity check against Black-Scholes ==")
say("Lewis:", lewis_call(cf_bs(0.2, 1.0), 100, 110.0, 1.0, 0.03), " BS:", float(bs_call(100, 110, 1, 0.03, 0.2)))

say("== Heston ==")
H = dict(v0=0.04, kappa=2.0, theta=0.04, xi=0.5, rho=-0.7)
S0, r = 100.0, 0.0
T = 1.0
Ks_chk = np.array([80.0, 100.0, 120.0])
ex = lewis_call(cf_heston(T, **H), S0, Ks_chk, T, r)
paths, n = 400000, 400
dt = T / n
x = np.full(paths, math.log(S0))
v = np.full(paths, H["v0"])
rho = H["rho"]
for _ in range(n):
    z1 = rng.standard_normal(paths)
    z2 = rho * z1 + math.sqrt(1 - rho * rho) * rng.standard_normal(paths)
    vp = np.maximum(v, 0)
    x += -0.5 * vp * dt + np.sqrt(vp * dt) * z1
    v += H["kappa"] * (H["theta"] - vp) * dt + H["xi"] * np.sqrt(vp * dt) * z2
for Ki, e in zip(Ks_chk, ex):
    p = np.maximum(np.exp(x) - Ki, 0)
    say(f"K={Ki}: Fourier {e:.4f}  MC {p.mean():.4f} +- {p.std() / math.sqrt(paths):.4f}")
say(f"Feller 2 kappa theta - xi^2 = {2 * H['kappa'] * H['theta'] - H['xi'] ** 2:.3f}")

M_par = dict(s=0.15, lam=0.5, muJ=-0.15, delJ=0.15)


def merton_series(S, K, T, r, s, lam, muJ, delJ):
    mbar = math.exp(muJ + 0.5 * delJ**2) - 1
    lp = lam * (1 + mbar)
    total = 0.0
    for k in range(60):
        w = math.exp(-lp * T) * (lp * T) ** k / math.factorial(k)
        sk = math.sqrt(s * s + k * delJ**2 / T)
        rk = r - lam * mbar + k * math.log(1 + mbar) / T
        total += w * bs_call(S, K, T, rk, sk)
    return float(total)


say("== Merton ==")
for Ki in [80.0, 100.0, 120.0]:
    say(f"K={Ki}: series {merton_series(100, Ki, 1.0, 0.0, **M_par):.4f} Fourier "
        f"{lewis_call(cf_merton(1.0, **M_par), 100, Ki, 1.0, 0.0)[0]:.4f}")

# smiles
mny = np.linspace(-0.35, 0.3, 40)
for name, T in [("025", 0.25), ("100", 1.0)]:
    Ks = 100 * np.exp(mny * math.sqrt(T))
    he = lewis_call(cf_heston(T, **H), 100.0, Ks, T, 0.0)
    me = lewis_call(cf_merton(T, **M_par), 100.0, Ks, T, 0.0)
    ivh = [implied_vol(p, 100.0, k, T, 0.0) for p, k in zip(he, Ks)]
    ivm = [implied_vol(p, 100.0, k, T, 0.0) for p, k in zip(me, Ks)]
    save(f"smile_{name}.dat", "m K heston merton", mny, Ks, ivh, ivm)
    i = np.argmin(np.abs(mny))
    say(f"T={T}: ATM-ish IV Heston {ivh[i]:.4f} Merton {ivm[i]:.4f}")

# Breeden-Litzenberger density
T = 1.0
Ks = np.linspace(40, 180, 281)
C = lewis_call(cf_heston(T, **H), 100.0, Ks, T, 0.0, umax=300, nu=8000)
h = Ks[1] - Ks[0]
dens = (C[2:] - 2 * C[1:-1] + C[:-2]) / h**2
Km = Ks[1:-1]
sg = implied_vol(lewis_call(cf_heston(T, **H), 100.0, np.array([100.0]), T, 0.0)[0], 100.0, 100.0, T, 0.0)
lognorm = phi((np.log(Km / 100) + 0.5 * sg**2 * T) / (sg * math.sqrt(T))) / (Km * sg * math.sqrt(T))
save("density.dat", "K heston lognormal", Km, dens, lognorm)
say(f"Implied density integrates to {dens.sum() * h:.4f}; mean {(dens * Km).sum() * h:.3f}; ATM vol {sg:.4f}")

# variance swap strip
say("== Variance swap replication ==")
T = 1.0
Ks = np.exp(np.linspace(math.log(5), math.log(1000), 3000))
Cs = lewis_call(cf_heston(T, **H), 100.0, Ks, T, 0.0, umax=300, nu=6000)
Ps = Cs - 100.0 + Ks
otm = np.where(Ks < 100.0, Ps, Cs)
strip = (2 / T) * np.trapezoid(otm / Ks**2, Ks)
true = H["theta"] + (H["v0"] - H["theta"]) * (1 - math.exp(-H["kappa"] * T)) / (H["kappa"] * T)
say(f"Heston: strip fair variance {strip:.5f} vs theoretical {true:.5f}")
H2 = dict(H, v0=0.09)
Cs = lewis_call(cf_heston(T, **H2), 100.0, Ks, T, 0.0, umax=300, nu=6000)
Ps = Cs - 100.0 + Ks
otm = np.where(Ks < 100.0, Ps, Cs)
strip = (2 / T) * np.trapezoid(otm / Ks**2, Ks)
true = H2["theta"] + (H2["v0"] - H2["theta"]) * (1 - math.exp(-H2["kappa"] * T)) / (H2["kappa"] * T)
atm = implied_vol(lewis_call(cf_heston(T, **H2), 100.0, np.array([100.0]), T, 0.0)[0], 100.0, 100.0, T, 0.0)
say(f"Heston v0=.09: strip {strip:.5f} theoretical {true:.5f}; ATM implied var {atm**2:.5f}")

# Dupire check
say("== Dupire vs Gatheral form, skew rule ==")


def iv_surf(k, T):
    return 0.20 - 0.10 * k + 0.15 * k * k + 0.0 * T


def call_surf(K, T):
    return bs_call(100.0, K, T, 0.0, iv_surf(math.log(K / 100.0), T))


def w(k, T):
    return iv_surf(k, T) ** 2 * T


def dup(K, T):
    h, e = 0.05, 0.001
    dT = (call_surf(K, T + e) - call_surf(K, T - e)) / (2 * e)
    dKK = (call_surf(K + h, T) - 2 * call_surf(K, T) + call_surf(K - h, T)) / h**2
    return math.sqrt(float(2 * dT / (K * K * dKK)))


def gat(k, T):
    h, e = 1e-3, 1e-4
    W = w(k, T)
    wT = (w(k, T + e) - w(k, T - e)) / (2 * e)
    wk = (w(k + h, T) - w(k - h, T)) / (2 * h)
    wkk = (w(k + h, T) - 2 * W + w(k - h, T)) / h**2
    den = 1 - k / W * wk + 0.25 * (-0.25 - 1 / W + k * k / W**2) * wk**2 + 0.5 * wkk
    return math.sqrt(wT / den)


for K in [90.0, 100.0, 110.0]:
    say(f"T=0.5 K={K}: Dupire {dup(K, 0.5):.4f}, Gatheral {gat(math.log(K / 100), 0.5):.4f}, implied {iv_surf(math.log(K / 100), 0.5):.4f}")
for T in [0.02, 0.5]:
    h = 0.005
    sl = (gat(h, T) - gat(-h, T)) / (2 * h)
    say(f"T={T}: local-vol slope at ATM {sl:.4f}; implied slope -0.1000; ratio {sl / -0.1:.3f}")

# SABR
say("== SABR Hagan vs MC ==")


def hagan(F, K, T, a, b, rho, nu):
    if abs(F - K) < 1e-12:
        z_x = 1.0
        pre = a / F ** (1 - b)
        fk = F * F
    else:
        fk = F * K
        lg = math.log(F / K)
        z = (nu / a) * fk ** ((1 - b) / 2) * lg
        x = math.log((math.sqrt(1 - 2 * rho * z + z * z) + z - rho) / (1 - rho))
        z_x = z / x
        pre = a / (fk ** ((1 - b) / 2) * (1 + (1 - b) ** 2 / 24 * lg**2 + (1 - b) ** 4 / 1920 * lg**4))
    cor = 1 + ((1 - b) ** 2 / 24 * a * a / fk ** (1 - b) + rho * b * nu * a / (4 * fk ** ((1 - b) / 2)) + (2 - 3 * rho * rho) / 24 * nu * nu) * T
    return pre * z_x * cor


F0, a0, b, rho, nu, T = 1.0, 0.3, 0.5, -0.3, 0.4, 1.0
paths, n = 400000, 500
dt = T / n
f = np.full(paths, F0)
al = np.full(paths, a0)
for _ in range(n):
    z1 = rng.standard_normal(paths)
    z2 = rho * z1 + math.sqrt(1 - rho * rho) * rng.standard_normal(paths)
    f = np.maximum(f + al * f**b * math.sqrt(dt) * z1, 0.0)
    al = al * np.exp(nu * math.sqrt(dt) * z2 - 0.5 * nu * nu * dt)
for K in [0.7, 0.85, 1.0, 1.2, 1.4]:
    p = np.maximum(f - K, 0)
    iv = implied_vol(p.mean(), F0, K, T, 0.0)
    say(f"K={K}: Hagan {hagan(F0, K, T, a0, b, rho, nu):.4f} MC {iv:.4f} (price se {p.std() / math.sqrt(paths):.5f})")

# ---------------------------------------------------------------- rates
say("== Short rates ==")
kap, th, sg, r0 = 0.5, 0.04, 0.01, 0.02
Tb = 5.0


def vas_B(tau):
    return (1 - math.exp(-kap * tau)) / kap


def vas_P(tau, r):
    B = vas_B(tau)
    A = (th - sg**2 / (2 * kap**2)) * (B - tau) - sg**2 * B**2 / (4 * kap)
    return math.exp(A - B * r)


paths, n = 200000, 1000
dt = Tb / n
rr = np.full(paths, r0)
integ = np.zeros(paths)
e = math.exp(-kap * dt)
sd = sg * math.sqrt((1 - e * e) / (2 * kap))
snap = None
for i in range(n):
    rn = th + (rr - th) * e + sd * rng.standard_normal(paths)
    integ += 0.5 * (rr + rn) * dt
    rr = rn
    if i == n // 5 - 1:
        snap = (rr.copy(), integ.copy())
dd = np.exp(-integ)
say(f"Vasicek P(0,5): formula {vas_P(Tb, r0):.5f} MC {dd.mean():.5f} +- {dd.std() / math.sqrt(paths):.5f}")
# option on bond: expiry 1y on 5y bond
T0, K0 = 1.0, vas_P(4.0, r0) * 1.0
rT, iT = snap
sp = sg * math.sqrt((1 - math.exp(-2 * kap * T0)) / (2 * kap)) * vas_B(Tb - T0)
h0 = math.log(vas_P(Tb, r0) / (vas_P(T0, r0) * K0)) / sp + sp / 2
cf_val = vas_P(Tb, r0) * float(N(h0)) - K0 * vas_P(T0, r0) * float(N(h0 - sp))
pT = np.array([0.0])
B4 = vas_B(4.0)
A4 = (th - sg**2 / (2 * kap**2)) * (B4 - 4.0) - sg**2 * B4**2 / (4 * kap)
pay = np.exp(-iT) * np.maximum(np.exp(A4 - B4 * rT) - K0, 0)
say(f"Vasicek bond call (Jamshidian) {cf_val:.6f}  MC {pay.mean():.6f} +- {pay.std() / math.sqrt(paths):.6f}")

kap, th, sg, r0, Tb = 0.5, 0.04, 0.1, 0.02, 5.0
gam = math.sqrt(kap**2 + 2 * sg**2)
den = (gam + kap) * (math.exp(gam * Tb) - 1) + 2 * gam
B = 2 * (math.exp(gam * Tb) - 1) / den
A = (2 * gam * math.exp((kap + gam) * Tb / 2) / den) ** (2 * kap * th / sg**2)
paths, n = 200000, 2000
dt = Tb / n
rr = np.full(paths, r0)
integ = np.zeros(paths)
for _ in range(n):
    rp = np.maximum(rr, 0)
    integ += rp * dt
    rr += kap * (th - rp) * dt + sg * np.sqrt(rp * dt) * rng.standard_normal(paths)
dd = np.exp(-integ)
say(f"CIR P(0,5): formula {A * math.exp(-B * r0):.5f} MC {dd.mean():.5f} +- {dd.std() / math.sqrt(paths):.5f}")
say(f"CIR Feller 2*kappa*theta - sigma^2 = {2 * kap * th - sg**2:.4f}")

say("== Margrabe ==")
S1, S2, s1, s2, rho, T = 100.0, 95.0, 0.3, 0.2, 0.5, 1.0
sm = math.sqrt(s1**2 + s2**2 - 2 * rho * s1 * s2)
ex = float(bs_call(S1, S2, T, 0.0, sm))
paths = 2000000
z1 = rng.standard_normal(paths)
z2 = rho * z1 + math.sqrt(1 - rho**2) * rng.standard_normal(paths)
A1 = S1 * np.exp(0.03 - 0.5 * s1**2 + s1 * z1)
A2 = S2 * np.exp(0.03 - 0.5 * s2**2 + s2 * z2)
p = math.exp(-0.03) * np.maximum(A1 - A2, 0)
say(f"Margrabe formula {ex:.4f}, MC (r=3%) {p.mean():.4f} +- {p.std() / math.sqrt(paths):.4f}")
# a separate, larger run on its own stream, so the main stream's later numbers are unaffected
rng2 = np.random.default_rng(7)
z1 = rng2.standard_normal(8000000)
z2 = rho * z1 + math.sqrt(1 - rho**2) * rng2.standard_normal(8000000)
p = math.exp(-0.03) * np.maximum(S1 * np.exp(0.03 - 0.5 * s1**2 + s1 * z1) - S2 * np.exp(0.03 - 0.5 * s2**2 + s2 * z2), 0)
say(f"Margrabe larger run (8m paths) {p.mean():.4f} +- {p.std() / math.sqrt(8000000):.4f}")

# ---------------------------------------------------------------- Euler / Milstein
say("== Euler and Milstein ==")
mu, sg, S0, T = 0.05, 0.5, 100.0, 1.0
paths = 100000
fine = 2**12
dWf = rng.normal(0, math.sqrt(T / fine), (paths // 20, fine))
hs, se, sm = [], [], []
exactT = S0 * np.exp((mu - 0.5 * sg**2) * T + sg * dWf.sum(1))
for k in range(2, 11):
    m = 2**k
    block = fine // m
    dW = dWf.reshape(paths // 20, m, block).sum(2)
    Xe = np.full(paths // 20, S0)
    Xm = np.full(paths // 20, S0)
    h = T / m
    for j in range(m):
        d = dW[:, j]
        Xe = Xe * (1 + mu * h + sg * d)
        Xm = Xm * (1 + mu * h + sg * d + 0.5 * sg**2 * (d * d - h))
    hs.append(h)
    se.append(np.mean(np.abs(Xe - exactT)))
    sm.append(np.mean(np.abs(Xm - exactT)))
    w_exact = S0**2 * math.exp((2 * mu + sg**2) * T)
    w_euler = S0**2 * ((1 + mu * h) ** 2 + sg**2 * h) ** m
    say(f"h=2^-{k}: strong Euler {se[-1]:.4f} Milstein {sm[-1]:.4f}; weak Euler E[X^2] err {abs(w_euler - w_exact):.3f}")
save("strong.dat", "h euler milstein", hs, se, sm)
pe = np.polyfit(np.log(hs), np.log(se), 1)[0]
pm = np.polyfit(np.log(hs), np.log(sm), 1)[0]
say(f"fitted slopes: Euler {pe:.3f} Milstein {pm:.3f}")

# ---------------------------------------------------------------- variance reduction
say("== Variance reduction ==")
S0, K, r, s, T = 100.0, 100.0, 0.05, 0.2, 1.0
ex = float(bs_call(S0, K, T, r, s))
paths = 100000
z = rng.standard_normal(paths)
drift = (r - 0.5 * s * s) * T
ST = S0 * np.exp(drift + s * math.sqrt(T) * z)
disc = math.exp(-r * T)
plain = disc * np.maximum(ST - K, 0)
ST2 = S0 * np.exp(drift - s * math.sqrt(T) * z)
anti = 0.5 * (plain + disc * np.maximum(ST2 - K, 0))
b = np.cov(plain, ST)[0, 1] / ST.var()
cv = plain - b * (ST - S0 * math.exp(r * T))
say(f"Exact {ex:.4f}")
say(f"Plain {plain.mean():.4f} se {plain.std() / math.sqrt(paths):.4f}")
say(f"Antithetic {anti.mean():.4f} se {anti.std() / math.sqrt(paths):.4f} (uses 2x the payoff evaluations)")
say(f"Control ST {cv.mean():.4f} se {cv.std() / math.sqrt(paths):.4f} b={b:.3f} corr={np.corrcoef(plain, ST)[0, 1]:.3f}")
# stratified
u = (np.arange(paths) + rng.random(paths)) / paths
# inverse normal by bisection-free Acklam approximation


def norminv(p):
    a = [-3.969683028665376e01, 2.209460984245205e02, -2.759285104469687e02, 1.383577518672690e02, -3.066479806614716e01, 2.506628277459239e00]
    b_ = [-5.447609879822406e01, 1.615858368580409e02, -1.556989798598866e02, 6.680131188771972e01, -1.328068155288572e01]
    c = [-7.784894002430293e-03, -3.223964580411365e-01, -2.400758277161838e00, -2.549732539343734e00, 4.374664141464968e00, 2.938163982698783e00]
    d = [7.784695709041462e-03, 3.224671290700398e-01, 2.445134137142996e00, 3.754408661907416e00]
    p = np.asarray(p)
    x = np.empty_like(p)
    lo = p < 0.02425
    hi = p > 1 - 0.02425
    mid = ~(lo | hi)
    q = np.sqrt(-2 * np.log(p[lo]))
    x[lo] = (((((c[0] * q + c[1]) * q + c[2]) * q + c[3]) * q + c[4]) * q + c[5]) / ((((d[0] * q + d[1]) * q + d[2]) * q + d[3]) * q + 1)
    q = np.sqrt(-2 * np.log(1 - p[hi]))
    x[hi] = -(((((c[0] * q + c[1]) * q + c[2]) * q + c[3]) * q + c[4]) * q + c[5]) / ((((d[0] * q + d[1]) * q + d[2]) * q + d[3]) * q + 1)
    q = p[mid] - 0.5
    t_ = q * q
    x[mid] = (((((a[0] * t_ + a[1]) * t_ + a[2]) * t_ + a[3]) * t_ + a[4]) * t_ + a[5]) * q / (((((b_[0] * t_ + b_[1]) * t_ + b_[2]) * t_ + b_[3]) * t_ + b_[4]) * t_ + 1)
    return x


reps = []
for _ in range(40):
    u = (np.arange(5000) + rng.random(5000)) / 5000
    zz = norminv(u)
    reps.append(np.mean(disc * np.maximum(S0 * np.exp(drift + s * math.sqrt(T) * zz) - K, 0)))
say(f"Stratified (40 reps of 5000, 200k total): {np.mean(reps):.4f} se of mean {np.std(reps, ddof=1) / math.sqrt(40):.5f}")

# importance sampling deep OTM
K2 = 200.0
ex2 = float(bs_call(S0, K2, T, r, s))
zz = rng.standard_normal(paths)
plain2 = disc * np.maximum(S0 * np.exp(drift + s * math.sqrt(T) * zz) - K2, 0)
theta = (math.log(K2 / S0) - drift) / (s * math.sqrt(T))
y = zz + theta
LR = np.exp(-theta * y + 0.5 * theta**2)
isv = disc * np.maximum(S0 * np.exp(drift + s * math.sqrt(T) * y) - K2, 0) * LR
say(f"K=200 exact {ex2:.6f}; plain {plain2.mean():.6f} se {plain2.std() / math.sqrt(paths):.6f}; IS (theta={theta:.3f}) {isv.mean():.6f} se {isv.std() / math.sqrt(paths):.6f}")

# Asian with geometric control
n_as = 12
paths = 1000000
dt = T / n_as
Z = rng.standard_normal((paths, n_as))
logS = np.log(S0) + np.cumsum((r - 0.5 * s * s) * dt + s * math.sqrt(dt) * Z, axis=1)
arith = np.exp(logS).mean(1)
geo = np.exp(logS.mean(1))
pa = disc * np.maximum(arith - K, 0)
pg = disc * np.maximum(geo - K, 0)
tb = dt * (n_as + 1) / 2
vb = s * s * dt * (n_as + 1) * (2 * n_as + 1) / (6 * n_as)
Fg = S0 * math.exp((r - 0.5 * s * s) * tb + 0.5 * vb)
d1 = (math.log(Fg / K) + 0.5 * vb) / math.sqrt(vb)
ge = disc * (Fg * float(N(d1)) - K * float(N(d1 - math.sqrt(vb))))
b = np.cov(pa, pg)[0, 1] / pg.var()
cv = pa - b * (pg - ge)
say(f"Asian (12 fixings): geo exact {ge:.4f}, geo MC {pg.mean():.4f}; plain {pa.mean():.4f} se {pa.std() / math.sqrt(paths):.4f}; CV {cv.mean():.4f} se {cv.std() / math.sqrt(paths):.5f}; corr {np.corrcoef(pa, pg)[0, 1]:.4f}")

# Greeks
paths = 400000
zz = rng.standard_normal(paths)
ST = S0 * np.exp(drift + s * math.sqrt(T) * zz)
path = disc * (ST > K) * ST / S0
lr = disc * np.maximum(ST - K, 0) * zz / (S0 * s * math.sqrt(T))
eps = 1.0
bump = disc * (np.maximum((S0 + eps) / S0 * ST - K, 0) - np.maximum((S0 - eps) / S0 * ST - K, 0)) / (2 * eps)
d1 = (math.log(S0 / K) + (r + 0.5 * s * s) * T) / (s * math.sqrt(T))
say(f"Delta exact {float(N(d1)):.4f}; pathwise {path.mean():.4f} se {path.std() / math.sqrt(paths):.4f}; LR {lr.mean():.4f} se {lr.std() / math.sqrt(paths):.4f}; bump(common z) {bump.mean():.4f} se {bump.std() / math.sqrt(paths):.4f}")


# ---------------------------------------------------------------- trees and American
def crr(S, K, T, r, s, n, american=True, put=True):
    h = T / n
    u = math.exp(s * math.sqrt(h))
    d = 1 / u
    p = (math.exp(r * h) - d) / (u - d)
    df = math.exp(-r * h)
    ST = S * u ** (2.0 * np.arange(n + 1) - n)
    V = np.maximum(K - ST, 0) if put else np.maximum(ST - K, 0)
    for i in range(n, 0, -1):
        V = df * (p * V[1:] + (1 - p) * V[:-1])
        if american:
            Si = S * u ** (2.0 * np.arange(i) - (i - 1))
            V = np.maximum(V, K - Si if put else Si - K)
    return float(V[0])


say("== CRR ==")
ex = float(bs_call(100, 100, 1, 0.05, 0.2))
for n in [10, 11, 50, 51, 100, 101, 500, 501, 1000]:
    say(f"n={n}: Euro call {crr(100, 100, 1, 0.05, 0.2, n, False, False):.4f} err {crr(100, 100, 1, 0.05, 0.2, n, False, False) - ex:+.4f}")
am = crr(100, 100, 1, 0.05, 0.2, 5000, True, True)
eu = crr(100, 100, 1, 0.05, 0.2, 5000, False, True)
say(f"American put (n=5000) {am:.4f}; European {eu:.4f}; premium {am - eu:.4f}")
L = 2 * 0.05 * 100 / (2 * 0.05 + 0.04)
perp = (100 - L) * (100 / L) ** (-2 * 0.05 / 0.04)
say(f"Perpetual put K=100,r=5%,sig=20%: L*={L:.3f}, V(100)={perp:.4f}; CRR T=100y (n=20000) {crr(100, 100, 100, 0.05, 0.2, 20000):.4f}")

# LSM
say("== Longstaff-Schwartz ==")
paths, n = 200000, 50
dt = 1.0 / n
Z = rng.standard_normal((paths // 2, n))
Z = np.concatenate([Z, -Z])
S = 100 * np.exp(np.cumsum((0.05 - 0.02) * dt + 0.2 * math.sqrt(dt) * Z, axis=1))
disc1 = math.exp(-0.05 * dt)
cash = np.maximum(100 - S[:, -1], 0)
for j in range(n - 2, -1, -1):
    cash *= disc1
    itm = S[:, j] < 100
    x = S[itm, j] / 100
    A = np.column_stack([np.ones_like(x), x, x**2, x**3])
    beta = np.linalg.lstsq(A, cash[itm], rcond=None)[0]
    cont = A @ beta
    ex = 100 - S[itm, j]
    idx = np.where(itm)[0][ex > cont]
    cash[idx] = 100 - S[idx, j]
cash *= disc1
say(f"LSM American put {cash.mean():.4f} se {cash.std() / math.sqrt(paths):.4f} (50 exercise dates; low-biased relative to continuous exercise)")
say(f"Continuous-exercise CRR value {am:.4f}")


# ---------------------------------------------------------------- finite differences
def fd_call(scheme, Nx, Nt, S0=100.0, K=100.0, r=0.05, s=0.2, T=1.0, L=4.0, rannacher=False):
    x0 = math.log(S0 / K)
    x = np.linspace(x0 - L, x0 + L, Nx + 1)
    h = x[1] - x[0]
    dt = T / Nt
    a = 0.5 * s * s / h**2
    b = (r - 0.5 * s * s) / (2 * h)
    lo, di, up = a - b, -2 * a - r, a + b
    S = K * np.exp(x)
    V = np.maximum(S - K, 0)

    def bc(tau):
        return K * np.exp(x[-1]) - K * math.exp(-r * tau)

    def solve_tri(l, d, u, rhs):
        n = len(rhs)
        c = np.zeros(n)
        g = np.zeros(n)
        c[0] = u / d
        g[0] = rhs[0] / d
        for i in range(1, n):
            m = d - l * c[i - 1]
            c[i] = u / m
            g[i] = (rhs[i] - l * g[i - 1]) / m
        y = np.zeros(n)
        y[-1] = g[-1]
        for i in range(n - 2, -1, -1):
            y[i] = g[i] - c[i] * y[i + 1]
        return y

    for m in range(Nt):
        tau0, tau1 = m * dt, (m + 1) * dt
        th = {"explicit": 0.0, "implicit": 1.0, "cn": 0.5}[scheme]
        sub = 1
        if rannacher and m < 2:
            th = 1.0
            sub = 2
        ddt = dt / sub
        for q in range(sub):
            ta = tau0 + q * ddt
            tb = ta + ddt
            rhs = V[1:-1] + (1 - th) * ddt * (lo * V[:-2] + di * V[1:-1] + up * V[2:])
            ub = bc(tb)
            if th == 0.0:
                V[1:-1] = rhs
            else:
                rhs[-1] += th * ddt * up * ub
                V[1:-1] = solve_tri(-th * ddt * lo, 1 - th * ddt * di, -th * ddt * up, rhs)
            V[0] = 0.0
            V[-1] = ub
    return float(V[Nx // 2]), V, x


say("== Finite differences (error = FD - BS, ATM call) ==")
ex = float(bs_call(100, 100, 1, 0.05, 0.2))
say(f"exact {ex:.5f}")
for Nx, Nt in [(100, 25), (200, 100), (400, 400), (800, 1600)]:
    i = fd_call("implicit", Nx, Nt)[0]
    c = fd_call("cn", Nx, Nt)[0]
    r_ = fd_call("cn", Nx, Nt, rannacher=True)[0]
    say(f"Nx={Nx} Nt={Nt}: implicit {i - ex:+.5f} CN {c - ex:+.5f} CN-Rann {r_ - ex:+.5f}")
h = 8.0 / 200
lim = h * h / 0.04
say(f"explicit stability dt <= h^2/sigma^2 = {lim:.4f} (Nx=200) -> Nt>={1 / lim:.0f}")
for Nt in [20, 23, 24, 25, 26, 30]:
    v = fd_call("explicit", 200, Nt)[0]
    say(f"explicit Nx=200 Nt={Nt}: dt/limit={1 / Nt / lim:.3f} error {v - ex:+.5g}")

say("Time refinement at fixed Nx=1600 (price error), and gamma at the strike with a large step")
for Nt in [25, 50, 100, 200, 400]:
    i = fd_call("implicit", 1600, Nt)[0]
    c = fd_call("cn", 1600, Nt)[0]
    say(f"Nx=1600 Nt={Nt}: implicit {i - ex:+.5f} CN {c - ex:+.5f}")
d1_ = (math.log(100 / 100) + (0.05 + 0.02) * 1) / 0.2
gam_ex = float(phi(d1_)) / (100 * 0.2)
for name, sc, ra in [("implicit", "implicit", False), ("CN", "cn", False), ("CN+Rannacher", "cn", True)]:
    _, V, x = fd_call(sc, 1600, 10, rannacher=ra)
    j = 800
    hh = x[1] - x[0]
    Vx = (V[j + 1] - V[j - 1]) / (2 * hh)
    Vxx = (V[j + 1] - 2 * V[j] + V[j - 1]) / hh**2
    say(f"{name}: gamma at strike {(Vxx - Vx) / 100**2:.5f} (exact {gam_ex:.5f}), neighbours", [round(float(((V[k + 1] - 2 * V[k] + V[k - 1]) / hh**2 - (V[k + 1] - V[k - 1]) / (2 * hh)) / (100 * math.exp(x[k])) ** 2), 5) for k in (798, 799, 801, 802)])

# ---------------------------------------------------------------- hedging error
say("== Discrete delta hedging ==")
S0, K, r, s, T = 100.0, 100.0, 0.0, 0.2, 1.0
vega = float(bs_vega(S0, K, T, r, s))
paths = 50000
ns, stds, theo, means = [], [], [], []
for n in [6, 13, 26, 52, 104, 252, 504]:
    dt = T / n
    S = np.full(paths, S0)
    C0 = float(bs_call(S0, K, T, r, s))
    cash = np.full(paths, C0)
    delta_old = np.zeros(paths)
    for j in range(n):
        tau = T - j * dt
        d1 = (np.log(S / K) + 0.5 * s * s * tau) / (s * math.sqrt(tau))
        delta = N(d1)
        cash -= (delta - delta_old) * S
        delta_old = delta
        S = S * np.exp(-0.5 * s * s * dt + s * math.sqrt(dt) * rng.standard_normal(paths))
    pl = cash + delta_old * S - np.maximum(S - K, 0)
    ns.append(n)
    stds.append(pl.std())
    theo.append(math.sqrt(math.pi / 4) * vega * s / math.sqrt(n))
    means.append(pl.mean())
    say(f"N={n}: std P&L {pl.std():.3f}  theory {theo[-1]:.3f}  mean {pl.mean():+.3f}")
save("hedge.dat", "n sim theory", ns, stds, theo)

# vol mis-specification: hedge at implied with realised different
say("Gamma P&L: sell at 20%, hedge at 20%, realised 25%")
n = 252
dt = T / n
sr = 0.25
S = np.full(paths, S0)
cash = np.full(paths, float(bs_call(S0, K, T, r, s)))
delta_old = np.zeros(paths)
for j in range(n):
    tau = T - j * dt
    d1 = (np.log(S / K) + 0.5 * s * s * tau) / (s * math.sqrt(tau))
    delta = N(d1)
    cash -= (delta - delta_old) * S
    delta_old = delta
    S = S * np.exp(-0.5 * sr * sr * dt + sr * math.sqrt(dt) * rng.standard_normal(paths))
pl = cash + delta_old * S - np.maximum(S - K, 0)
say(f"mean P&L {pl.mean():.3f} std {pl.std():.3f}; BS(25%)-BS(20%) = {float(bs_call(S0, K, T, r, sr) - bs_call(S0, K, T, r, s)):.3f}")

# ---------------------------------------------------------------- GARCH
say("== GARCH(1,1) ==")
om, al, be = 2e-6, 0.08, 0.90
n = 2000000
z = rng.standard_normal(n)
h_ = om / (1 - al - be)
ret = np.empty(n)
hs_ = np.empty(n)
for i in range(n):
    hs_[i] = h_
    ret[i] = math.sqrt(h_) * z[i]
    h_ = om + al * ret[i] ** 2 + be * h_
uv = om / (1 - al - be)
kurt = np.mean(ret**4) / np.mean(ret**2) ** 2
p = al + be
kurt_th = 3 * (1 - p**2) / (1 - p**2 - 2 * al**2)
r2 = ret**2 - np.mean(ret**2)
ac = [np.mean(r2[:-k] * r2[k:]) / np.mean(r2**2) for k in (1, 2, 5, 10)]
rho1 = al * (1 - al * be - be**2) / (1 - 2 * al * be - be**2)
say(f"uncond var sim {np.mean(ret**2):.3e} theory {uv:.3e}; ann vol {math.sqrt(252 * uv):.3f}")
say(f"kurtosis sim {kurt:.2f} theory {kurt_th:.2f}")
say("acf r^2 lag 1,2,5,10 sim:", [round(x, 4) for x in ac], " theory:", [round(rho1 * p ** (k - 1), 4) for k in (1, 2, 5, 10)])
sub = 1000
start = 5000
save("garch.dat", "t garch iid", np.arange(sub), 100 * ret[start:start + sub], 100 * math.sqrt(uv) * rng.standard_normal(sub))

# ---------------------------------------------------------------- Kalman: local level
say("== Kalman filter, local level ==")
T_ = 500
q, R = 0.01, 0.25
state = np.cumsum(rng.normal(0, math.sqrt(q), T_))
obs = state + rng.normal(0, math.sqrt(R), T_)
m, P = 0.0, 10.0
out = []
for y_ in obs:
    P = P + q
    Kg = P / (P + R)
    m = m + Kg * (y_ - m)
    P = (1 - Kg) * P
    out.append(m)
out = np.array(out)
Pss = 0.5 * (-q + math.sqrt(q * q + 4 * q * R))
Kss = (Pss + q) / (Pss + q + R)
say(f"steady gain sim {Kg:.4f} theory {Kss:.4f}; rmse obs {np.sqrt(np.mean((obs - state) ** 2)):.3f} filter {np.sqrt(np.mean((out - state) ** 2)):.3f}")

# ---------------------------------------------------------------- Merton portfolio / Kelly
say("== Kelly ==")
mu_, sg_, r_ = 0.08, 0.2, 0.02
f_star = (mu_ - r_) / sg_**2
for mult in [0.5, 1.0, 2.0, 3.0]:
    f_ = mult * f_star
    g = r_ + f_ * (mu_ - r_) - 0.5 * f_**2 * sg_**2
    say(f"f = {mult} x Kelly = {f_:.2f}: growth {g * 100:.3f}%")

# ---------------------------------------------------------------- Markowitz example
say("== Markowitz three assets ==")
mu = np.array([0.06, 0.09, 0.12])
vol = np.array([0.10, 0.18, 0.25])
Corr = np.array([[1, 0.2, 0.1], [0.2, 1, 0.4], [0.1, 0.4, 1]])
Cov = np.outer(vol, vol) * Corr
Inv = np.linalg.inv(Cov)
one = np.ones(3)
A = one @ Inv @ one
Bm = one @ Inv @ mu
Cm = mu @ Inv @ mu
D = A * Cm - Bm**2
say(f"A={A:.4f} B={Bm:.4f} C={Cm:.4f} D={D:.4f}; GMV mean {Bm / A:.4f} vol {math.sqrt(1 / A):.4f}")
m_grid = np.linspace(Bm / A - 0.06, 0.16, 80)
sd = np.sqrt((A * m_grid**2 - 2 * Bm * m_grid + Cm) / D)
rf = 0.02
wt = Inv @ (mu - rf)
wt = wt / wt.sum()
mt, st = wt @ mu, math.sqrt(wt @ Cov @ wt)
say(f"tangency weights {np.round(wt, 3)}, mean {mt:.4f}, vol {st:.4f}, Sharpe {(mt - rf) / st:.4f}; sqrt(H) {math.sqrt((mu - rf) @ Inv @ (mu - rf)):.4f}")
save("frontier.dat", "sd m", sd, m_grid)
save("assets.dat", "sd m", vol, mu)
save("cml.dat", "sd m", np.array([0, st, 0.3]), np.array([rf, mt, rf + (mt - rf) / st * 0.3]))

# estimation error
T_obs = 60
true_w = Inv @ (mu - rf)
wts = []
for _ in range(5000):
    Rr = rng.multivariate_normal(mu / 12, Cov / 12, T_obs)
    mh = Rr.mean(0) * 12
    ww = Inv @ (mh - rf)
    wts.append(ww / ww.sum())
wts = np.array(wts)
say(f"tangency weights from 5y monthly returns, known cov: 5% {np.round(np.quantile(wts, 0.05, axis=0), 2)} median {np.round(np.median(wts, 0), 2)} 95% {np.round(np.quantile(wts, 0.95, axis=0), 2)}")

# ---------------------------------------------------------------- VaR
say("== VaR ES ==")
z99 = 2.3263
say(f"Normal 99% VaR {z99:.3f} sigma; ES {float(phi(z99)) / 0.01:.3f} sigma")
nu = 4
# t(4) quantile & ES by simulation scaled to unit variance
x = rng.standard_t(nu, 5000000) * math.sqrt((nu - 2) / nu)
qs = np.quantile(-x, 0.99)
say(f"t4 unit variance 99% VaR {qs:.3f}; ES {(-x)[-x >= qs].mean():.3f}")

LOG.close()
