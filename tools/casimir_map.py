"""
Figures for the website, computed with casimir_core.energy():
  images/casimir-map.png     homepage (Fig. 1): slice n1 = 0, for a dark background
  images/casimir-slices.png  research page: slices n1 = 0, 1/3, 2/3, 1, for a light background
Run from the project root:  python tools/casimir_map.py   (needs numpy and matplotlib)
"""
import os, sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Polygon
from matplotlib import font_manager as fm

sys.path.insert(0, os.path.dirname(__file__))
from casimir_core import energy

pi = np.pi
for f in fm.findSystemFonts():
    if "Spectral" in f:
        fm.fontManager.addfont(f)
SERIF = "Spectral" if any(f.name == "Spectral" for f in fm.fontManager.ttflist) else "serif"

def field(n1, n=420):
    b = np.linspace(-pi / 2, pi / 2, n)          # horizontal: β
    a = np.linspace(0, pi, n)                    # vertical:   α
    B, A = np.meshgrid(b, a)
    inside = (A >= np.abs(B)) & (A <= pi - np.abs(B))
    E = np.full(A.shape, np.nan)
    E[inside] = energy(A[inside], B[inside], n1)
    return B, A, E

def shade(E, emax):
    # signed square-root compression keeps the faint regions visible
    return np.sign(E) * np.sqrt(np.abs(E) / emax)

def cmap(dark):
    if dark:
        stops = [(0, "#0b1f6b"), (.22, "#1f5fd6"), (.45, "#38b6e0"), (.5, "#f6efe0"),
                 (.55, "#ffd23a"), (.78, "#f07a12"), (1, "#8f1406")]
    else:
        stops = [(0, "#123d7a"), (.25, "#2a7bc4"), (.46, "#9fd3ec"), (.5, "#fbf7ee"),
                 (.54, "#f6d48a"), (.75, "#e0842b"), (1, "#8a2d0b")]
    return LinearSegmentedColormap.from_list("casimir", stops)

def rhombus(ax, n1, emax, dark, labels=None, lw_zero=2.0, label_size=14):
    B, A, E = field(n1)
    S = shade(E, emax)
    poly = Polygon([(0, 0), (pi / 2, pi / 2), (0, pi), (-pi / 2, pi / 2)], closed=True,
                   facecolor="none", edgecolor="none")
    ax.add_patch(poly)
    im = ax.imshow(S, extent=[-pi / 2, pi / 2, 0, pi], origin="lower", cmap=cmap(dark),
                   vmin=-1, vmax=1, interpolation="bicubic")
    im.set_clip_path(poly)
    line = "#fbf3e2" if dark else "#17354d"
    cs = ax.contour(B, A, S, levels=np.linspace(-0.95, 0.95, 20), colors=line,
                    linewidths=0.5, alpha=0.32 if dark else 0.28,
                    negative_linestyles="solid")
    z = ax.contour(B, A, E, levels=[0], colors=line, linewidths=lw_zero)
    for c in (cs, z):
        c.set_clip_path(poly)
    ax.plot([0, pi / 2, 0, -pi / 2, 0], [0, pi / 2, pi, pi / 2, 0], color=line, lw=0.8, alpha=0.6)
    ax.set_xlim(-pi / 2 - 0.01, pi / 2 + 0.01); ax.set_ylim(-0.01, pi + 0.01)
    ax.set_aspect("equal"); ax.axis("off")
    if labels:   # (top, bottom, left, right) vertex names
        c = "#fbf3e2" if dark else "#17354d"
        kw = dict(color=c, fontfamily=SERIF, fontstyle="italic", fontsize=label_size, alpha=0.9)
        top, bottom, left, right = labels
        ax.text(0, pi + 0.1, top, ha="center", va="bottom", **kw)
        ax.text(0, -0.1, bottom, ha="center", va="top", **kw)
        ax.text(-pi / 2 + 0.02, pi / 2 + 0.12, left, ha="center", va="bottom", linespacing=1.1, **kw)
        ax.text(pi / 2 - 0.02, pi / 2 + 0.12, right, ha="center", va="bottom", linespacing=1.1, **kw)

root = os.path.join(os.path.dirname(__file__), "..")
emax = abs(energy(pi / 2, -pi / 2, 1.0))         # strongest attraction (periodic)

# Homepage figure: the slice n1 = 0, normalised to its own extremes.
# Its side vertices are the mixed Dirichlet-Neumann conditions (repulsive).
HERO_N1 = 0.0
_, _, E0 = field(HERO_N1)
fig = plt.figure(figsize=(7.2, 7.2), dpi=200)
ax = fig.add_axes([0, 0, 1, 1])
rhombus(ax, HERO_N1, np.nanmax(np.abs(E0)), dark=True, lw_zero=3.0)
fig.savefig(os.path.join(root, "images", "casimir-map.png"), transparent=True)
plt.close(fig)

# Research page: four slices
vals = [0, 1 / 3, 2 / 3, 1]
fig, axs = plt.subplots(1, 4, figsize=(12, 3.0), dpi=200)
for ax, v in zip(axs, vals):
    rhombus(ax, v, emax, dark=False, lw_zero=1.6)
fig.subplots_adjust(left=0.005, right=0.995, top=0.99, bottom=0.01, wspace=0.1)
fig.savefig(os.path.join(root, "images", "casimir-slices.png"), transparent=True)
plt.close(fig)
print("done")
