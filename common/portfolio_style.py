"""Shared plot style and brand palette for portfolio projects.

Import this module from notebooks instead of hardcoding colors:

    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path("../..").resolve()))  # repo root from notebooks/

    from common.portfolio_style import PALETTE, CLASS_COLORS, apply_mpl_style
    apply_mpl_style()
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterable, Sequence

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.metrics import confusion_matrix

# Brand palette (alternating light/dark pairs)
PALETTE = {
    "light_blue": "#8fd7d7",
    "med_blue": "#00b0be",
    "light_pink": "#ff8ca1",
    "med_pink": "#f45f74",
    "light_green": "#bdd373",
    "med_green": "#98c127",
    "light_orange": "#ffcd8e",
    "med_orange": "#ffb255",
    # Neutrals for text / axes (not brand accents)
    "ink": "#1F2933",
    "slate": "#52606D",
    "grid": "#E4E7EB",
}

# Default two-class / primary–secondary accents
CLASS_COLORS = [PALETTE["med_blue"], PALETTE["med_pink"]]

# Extra series colors when more than two groups are needed
ACCENT_COLORS = [
    PALETTE["med_blue"],
    PALETTE["med_pink"],
    PALETTE["med_green"],
    PALETTE["med_orange"],
    PALETTE["light_blue"],
    PALETTE["light_pink"],
    PALETTE["light_green"],
    PALETTE["light_orange"],
]


def apply_mpl_style() -> None:
    """Apply the portfolio matplotlib style globally."""
    plt.rcParams.update(
        {
            "figure.facecolor": "white",
            "axes.facecolor": "white",
            "axes.edgecolor": PALETTE["grid"],
            "axes.labelcolor": PALETTE["ink"],
            "axes.titlecolor": PALETTE["ink"],
            "axes.titlesize": 13,
            "axes.labelsize": 11,
            "xtick.color": PALETTE["slate"],
            "ytick.color": PALETTE["slate"],
            "text.color": PALETTE["ink"],
            "font.family": "DejaVu Sans",
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.grid": False,
            "legend.frameon": False,
            "figure.dpi": 120,
        }
    )


def plot_confusion(
    y_true,
    y_pred,
    title: str,
    class_names: Sequence[str] | None = None,
    save_as: str | Path | None = None,
    cmap_color: str | None = None,
):
    """Draw a clean confusion-matrix heatmap in portfolio colors."""
    cm = confusion_matrix(y_true, y_pred)
    if class_names is None:
        labels = sorted(np.unique(np.concatenate([np.asarray(y_true), np.asarray(y_pred)])))
        class_names = [str(x) for x in labels]

    color = cmap_color or PALETTE["med_blue"]
    fig, ax = plt.subplots(figsize=(4.2, 3.6))
    sns.heatmap(
        cm,
        annot=True,
        fmt="d",
        cmap=sns.light_palette(color, as_cmap=True),
        xticklabels=list(class_names),
        yticklabels=list(class_names),
        cbar=False,
        linewidths=1,
        linecolor="white",
        ax=ax,
    )
    ax.set_xlabel("Predicted")
    ax.set_ylabel("Actual")
    ax.set_title(title)
    fig.tight_layout()
    if save_as:
        fig.savefig(save_as, bbox_inches="tight")
    plt.show()
    return cm


def line_accuracy_chart(
    x: Iterable,
    y: Iterable,
    title: str,
    xlabel: str = "Components",
    save_as: str | Path | None = None,
    line_color: str | None = None,
    highlight_color: str | None = None,
):
    """Plot validation accuracy vs a hyperparameter with portfolio styling."""
    xs = list(x)
    ys = list(y)
    line = line_color or PALETTE["med_blue"]
    highlight = highlight_color or PALETTE["med_pink"]

    fig, ax = plt.subplots(figsize=(7, 3.8))
    ax.plot(xs, ys, color=line, marker="o", linewidth=2, markersize=5)
    ax.fill_between(xs, ys, alpha=0.15, color=line)
    ax.set_xlabel(xlabel)
    ax.set_ylabel("Validation accuracy")
    ax.set_title(title)
    ymin = max(0.0, min(ys) - 0.02)
    ymax = min(1.0, max(ys) + 0.02)
    ax.set_ylim(ymin, ymax)
    ax.axhline(max(ys), color=highlight, linestyle="--", linewidth=1, alpha=0.8)
    fig.tight_layout()
    if save_as:
        fig.savefig(save_as, bbox_inches="tight")
    plt.show()
