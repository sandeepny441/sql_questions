from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


OUTPUT_DIR = Path(__file__).resolve().parent

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
SALES = np.array([118, 146, 171, 158, 192, 214, 238, 226, 251, 267, 243, 282])

BAR_COLORS = [
    "#1F77B4",
    "#FF7F0E",
    "#2CA02C",
    "#D62728",
    "#9467BD",
    "#8C564B",
    "#E377C2",
    "#7F7F7F",
    "#BCBD22",
    "#17BECF",
    "#003F5C",
    "#FFD700",
]
LABEL_COLOR_PAIRS = [
    ("#155A8A", "#438BC0"),
    ("#B85D09", "#E78A35"),
    ("#1F7A22", "#55A85A"),
    ("#9F1D20", "#D65355"),
    ("#6D4E91", "#A184C5"),
    ("#684137", "#9A7067"),
    ("#A84F8F", "#D97FC4"),
    ("#565656", "#8F8F8F"),
    ("#777818", "#AFB041"),
    ("#0F7E8D", "#48B5C1"),
    ("#002D43", "#336982"),
    ("#8A6A00", "#C29B10"),
]


def main():
    background = "#FAF0E6"
    ink = "#292421"
    grid = "#D9CDC0"
    annual_total = SALES.sum()
    percentages = SALES / annual_total * 100

    fig, ax = plt.subplots(figsize=(11.5, 7), facecolor=background)
    ax.set_facecolor(background)

    x = np.arange(len(MONTHS))
    bars = ax.bar(
        x,
        SALES,
        width=0.72,
        color=BAR_COLORS,
        edgecolor=background,
        linewidth=1.6,
        alpha=0.97,
        zorder=3,
    )

    for bar, sales, percentage, (sales_color, percent_color) in zip(
        bars, SALES, percentages, LABEL_COLOR_PAIRS
    ):
        center_x = bar.get_x() + bar.get_width() / 2
        top_y = bar.get_height()
        ax.text(
            center_x,
            top_y + 20,
            f"{sales}",
            ha="center",
            va="bottom",
            color=sales_color,
            fontsize=12.5,
            fontfamily="DejaVu Sans",
            weight="bold",
            zorder=4,
        )
        ax.text(
            center_x,
            top_y + 7,
            f"{percentage:.1f}%",
            ha="center",
            va="bottom",
            color=percent_color,
            fontsize=10.5,
            fontfamily="DejaVu Serif",
            style="italic",
            zorder=4,
        )

    ax.set_xticks(x, MONTHS)
    ax.set_ylim(0, 350)
    ax.set_yticks(np.arange(0, 351, 50))

    ax.tick_params(axis="x", colors=ink, labelsize=15, length=0, pad=12)
    ax.tick_params(axis="y", colors=ink, labelsize=13, length=0, pad=9)
    ax.grid(axis="y", color=grid, linewidth=1.05, zorder=1)
    ax.grid(axis="x", visible=False)

    for spine in ["top", "right", "left"]:
        ax.spines[spine].set_visible(False)
    ax.spines["bottom"].set_color(ink)
    ax.spines["bottom"].set_alpha(0.34)
    ax.spines["bottom"].set_linewidth(1.2)

    fig.subplots_adjust(left=0.09, right=0.965, top=0.93, bottom=0.13)
    fig.savefig(OUTPUT_DIR / "histogram_08_12_bar_colors.png", dpi=220, facecolor=background)
    plt.close(fig)


if __name__ == "__main__":
    main()
