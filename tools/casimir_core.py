"""
Casimir energy between two parallel plates (3+1 dimensions, complex massless scalar)
for the boundary conditions U(α, β, n) = e^{iα}(I cos β + i n·σ sin β) of
M. Asorey & J. M. Muñoz-Castañeda, Nucl. Phys. B 874 (2013) 852-876.

Spectral function, eq. (2.20), with δ = L = 1:
  h_U(k) ∝ sin k ((k²-1) cos β + (k²+1) cos α) - 2k sin α cos k - 2k n1 sin β
Rotated to imaginary momentum k = iκ and normalised by its large-L limit, it gives
  F(κ) = [(1-e^{-2κ}) Q - 2κ sin α (1+e^{-2κ}) - 4κ n1 sin β e^{-κ}] / (Q - 2κ sin α),
  Q = (1-κ²) cos α - (1+κ²) cos β,
and the Casimir energy per unit plate area
  E/S = (1 / 2π²) ∫_0^∞ κ² log F(κ) dκ.
Consistent (non-negative) boundary conditions fill the rhombus |β| ≤ α ≤ π - |β|.
"""
import numpy as np

# Gauss-Legendre quadrature on κ ∈ (0, 45]; the integrand decays like e^{-κ}
_x, _w = np.polynomial.legendre.leggauss(400)
_split = 8.0
K = np.concatenate([(_x + 1) / 2 * _split, _split + (_x + 1) / 2 * (45 - _split)])
W = np.concatenate([_w / 2 * _split, _w / 2 * (45 - _split)])

def energy(alpha, beta, n1):
    a = np.asarray(alpha, float)[..., None]
    b = np.asarray(beta, float)[..., None]
    k = K
    Q = (1 - k**2) * np.cos(a) - (1 + k**2) * np.cos(b)
    e1, e2 = np.exp(-k), np.exp(-2 * k)
    num = (1 - e2) * Q - 2 * k * np.sin(a) * (1 + e2) - 4 * k * n1 * np.sin(b) * e1
    den = Q - 2 * k * np.sin(a)
    with np.errstate(divide="ignore", invalid="ignore"):
        F = num / den
        integrand = k**2 * np.log(F)
    return (integrand * W).sum(-1) / (2 * np.pi**2)

if __name__ == "__main__":
    pi = np.pi
    th = lambda t: -pi**2/45 + t**2/6 - t**3/(6*pi) + t**4/(24*pi**2)   # eq. (3.21)
    checks = [
        ("Dirichlet  α=π, β=0", energy(pi, 0, 0), -pi**2/720),
        ("Neumann    α→0, β=0", energy(1e-6, 0, 0), -pi**2/720),
        ("periodic   α=π/2, β=-π/2, n1=1", energy(pi/2, -pi/2, 1), th(0)),
        ("antiperiod α=π/2, β=+π/2, n1=1", energy(pi/2, pi/2, 1), th(pi)),
        ("quasi-per. θ=2π/3 (n1=-1/2 at β=-π/2)", energy(pi/2, -pi/2, -0.5), th(2*pi/3)),
        ("Dirichlet–Neumann α=π/2, β=π/2, n1=0", energy(pi/2, pi/2, 0), 7/8*pi**2/720),
    ]
    for name, got, exact in checks:
        print(f"{name:42s} computed {float(got): .6f}   exact {exact: .6f}")
