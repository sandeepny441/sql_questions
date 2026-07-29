from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


OUTPUT_DIR = Path(__file__).resolve().parent
RNG = np.random.default_rng(20260711)

GROUPS = ["North", "East", "South", "West", "Central"]
COLORS = ["#305CDE", "#E66B2E", "#1E9B72", "#B64C8B", "#D5A21F"]
BACKGROUND = "#F8F4EC"
PANEL = "#FCFAF4"
INK = "#23211D"
MUTED = "#6B665E"
GRID = "#D9D1C4"


def build_sales_data():
    base_specs = [
        (142, 17, [215, 229, 236]),
        (166, 22, [243, 258, 271, 286]),
        (128, 14, [194, 205]),
        (181, 28, [78, 295, 312]),
        (153, 19, [232, 246, 260]),
    ]
    data = []
    for mean, spread, outliers in base_specs:
        values = RNG.normal(mean, spread, 84)
        values = np.clip(values, 70, None)
        data.append(np.concatenate([values, np.array(outliers)]))
    return data


def tukey_outliers(values):
    q1, q3 = np.percentile(values, [25, 75])
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    mask = (values < lower) | (values > upper)
    return mask, q1, q3, iqr


def draw_horizontal_violin_chart():
    data = build_sales_data()
    positions = np.arange(len(data), 0, -1)

    fig, ax = plt.subplots(figsize=(16, 9), facecolor=BACKGROUND)
    ax.set_facecolor(PANEL)

    violins = ax.violinplot(
        data,
        positions=positions,
        vert=False,
        widths=0.72,
        showmeans=False,
        showmedians=False,
        showextrema=False,
    )
    for body, color in zip(violins["bodies"], COLORS):
        body.set_facecolor(color)
        body.set_edgecolor(color)
        body.set_alpha(0.24)
        body.set_linewidth(1.2)
        body.set_zorder(1)

    box = ax.boxplot(
        data,
        positions=positions,
        vert=False,
        widths=0.24,
        patch_artist=True,
        showfliers=False,
        medianprops={"color": INK, "linewidth": 2.4},
        whiskerprops={"color": INK, "linewidth": 1.45},
        capprops={"color": INK, "linewidth": 1.45},
        boxprops={"edgecolor": INK, "linewidth": 1.25},
    )
    for patch, color in zip(box["boxes"], COLORS):
        patch.set_facecolor(color)
        patch.set_alpha(0.88)
        patch.set_zorder(3)

    for position, group, values, color in zip(positions, GROUPS, data, COLORS):
        outlier_mask, q1, q3, iqr = tukey_outliers(values)
        outliers = values[outlier_mask]
        regular_values = values[~outlier_mask]
        median = np.median(values)
        outlier_pct = len(outliers) / len(values) * 100

        ax.scatter(
            regular_values,
            np.full(len(regular_values), position) + RNG.uniform(-0.13, 0.13, len(regular_values)),
            s=14,
            color=color,
            alpha=0.18,
            linewidth=0,
            zorder=2,
        )
        ax.scatter(
            outliers,
            np.full(len(outliers), position) + RNG.uniform(-0.055, 0.055, len(outliers)),
            s=74,
            color=PANEL,
            edgecolor=color,
            linewidth=2.2,
            zorder=5,
        )

        ax.plot([median, median], [position - 0.34, position + 0.34], color=color, linewidth=1.8, alpha=0.9)

        ax.text(
            323,
            position + 0.17,
            f"Median {median:.0f}",
            ha="left",
            va="center",
            fontsize=12.7,
            fontfamily="DejaVu Sans",
            color=color,
            weight="bold",
        )
        ax.text(
            323,
            position - 0.03,
            f"Outliers {outlier_pct:.1f}%",
            ha="left",
            va="center",
            fontsize=10.7,
            fontfamily="DejaVu Serif",
            style="italic",
            color=color,
        )
        ax.text(
            323,
            position - 0.23,
            f"IQR {iqr:.0f}",
            ha="left",
            va="center",
            fontsize=9.8,
            fontfamily="DejaVu Sans",
            color=MUTED,
        )

    ax.annotate(
        "Open rings are Tukey outliers",
        xy=(312, positions[1] + 0.05),
        xytext=(245, positions[0] + 0.42),
        arrowprops={"arrowstyle": "->", "color": MUTED, "linewidth": 1.25},
        fontsize=11.5,
        color=MUTED,
        ha="left",
        va="center",
    )

    ax.set_title(
        "Regional Sales Spread",
        loc="left",
        fontsize=26,
        weight="bold",
        color=INK,
        pad=18,
    )
    ax.text(
        0,
        1.012,
        "Horizontal violin plots with box ranges, median markers, and outlier percentages",
        transform=ax.transAxes,
        ha="left",
        va="bottom",
        fontsize=12.6,
        color=MUTED,
    )

    ax.set_yticks(positions, GROUPS)
    ax.set_xlabel("Sales", color=INK, fontsize=13, labelpad=14)
    ax.set_xlim(55, 365)
    ax.set_xticks(np.arange(50, 351, 50))
    ax.tick_params(axis="y", colors=INK, labelsize=15, length=0, pad=15)
    ax.tick_params(axis="x", colors=INK, labelsize=12.5, length=0, pad=9)
    ax.grid(axis="x", color=GRID, linewidth=1.05, zorder=0)
    ax.grid(axis="y", visible=False)

    for spine in ["top", "right", "left"]:
        ax.spines[spine].set_visible(False)
    ax.spines["bottom"].set_color(INK)
    ax.spines["bottom"].set_alpha(0.34)
    ax.spines["bottom"].set_linewidth(1.2)

    fig.subplots_adjust(left=0.105, right=0.95, top=0.84, bottom=0.14)
    output_file = OUTPUT_DIR / "horizontal_violin_sales.png"
    fig.savefig(output_file, dpi=220, facecolor=BACKGROUND)
    plt.close(fig)
    return output_file


def main():
    output_file = draw_horizontal_violin_chart()
    print(output_file.name)


if __name__ == "__main__":
    main()
