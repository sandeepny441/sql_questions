from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


OUTPUT_DIR = Path(__file__).resolve().parent
RNG = np.random.default_rng(20260711)

GROUPS = ["North", "East", "South", "West", "Central"]
COLORS = ["#0072B2", "#D55E00", "#009E73", "#CC79A7", "#E69F00"]
BACKGROUND = "#F7F2E8"
INK = "#25221E"
MUTED = "#6C655D"
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
    return mask, q1, q3, lower, upper


def draw_chart():
    data = build_sales_data()
    positions = np.arange(1, len(data) + 1) * 1.55

    fig, ax = plt.subplots(figsize=(15.5, 8.8), facecolor=BACKGROUND)
    ax.set_facecolor(BACKGROUND)

    violins = ax.violinplot(
        data,
        positions=positions,
        widths=0.96,
        showmeans=False,
        showmedians=False,
        showextrema=False,
    )
    for body, color in zip(violins["bodies"], COLORS):
        body.set_facecolor(color)
        body.set_edgecolor("none")
        body.set_alpha(0.22)
        body.set_zorder(1)

    box = ax.boxplot(
        data,
        positions=positions,
        widths=0.42,
        patch_artist=True,
        showfliers=False,
        medianprops={"color": INK, "linewidth": 2.2},
        whiskerprops={"color": INK, "linewidth": 1.4},
        capprops={"color": INK, "linewidth": 1.4},
        boxprops={"edgecolor": INK, "linewidth": 1.3},
    )
    for patch, color in zip(box["boxes"], COLORS):
        patch.set_facecolor(color)
        patch.set_alpha(0.88)
        patch.set_zorder(3)

    for index, (position, values, color) in enumerate(zip(positions, data, COLORS)):
        outlier_mask, q1, q3, lower, upper = tukey_outliers(values)
        outliers = values[outlier_mask]
        regular_values = values[~outlier_mask]
        median = np.median(values)
        outlier_pct = len(outliers) / len(values) * 100
        iqr = q3 - q1

        jitter = RNG.uniform(-0.08, 0.08, len(outliers))
        ax.scatter(
            np.full(len(outliers), position) + jitter,
            outliers,
            s=62,
            color=BACKGROUND,
            edgecolor=color,
            linewidth=2.0,
            zorder=5,
        )

        ax.scatter(
            np.full(len(regular_values), position) + RNG.uniform(-0.19, 0.19, len(regular_values)),
            regular_values,
            s=12,
            color=color,
            alpha=0.13,
            linewidth=0,
            zorder=2,
        )

        ax.text(
            position,
            341,
            f"Median {median:.0f}",
            ha="center",
            va="bottom",
            fontsize=12.5,
            fontfamily="DejaVu Sans",
            color=color,
            weight="bold",
        )
        ax.text(
            position,
            326,
            f"Outliers {outlier_pct:.1f}%",
            ha="center",
            va="bottom",
            fontsize=10.8,
            fontfamily="DejaVu Serif",
            style="italic",
            color=color,
        )
        ax.text(
            position,
            311,
            f"IQR {iqr:.0f}",
            ha="center",
            va="bottom",
            fontsize=9.8,
            fontfamily="DejaVu Sans",
            color=MUTED,
        )

    ax.annotate(
        "Open circles mark Tukey outliers",
        xy=(positions[-1] + 0.02, max(data[-1])),
        xytext=(positions[-1] - 1.45, 292),
        arrowprops={"arrowstyle": "->", "color": MUTED, "linewidth": 1.2},
        fontsize=11.5,
        color=MUTED,
        ha="left",
        va="center",
    )

    ax.set_title(
        "Sales Distribution by Region",
        loc="left",
        fontsize=25,
        weight="bold",
        color=INK,
        pad=18,
    )
    ax.text(
        0,
        1.012,
        "Five box-and-whisker plots with violin distributions and outlier percentages",
        transform=ax.transAxes,
        ha="left",
        va="bottom",
        fontsize=12.5,
        color=MUTED,
    )

    ax.set_xticks(positions, GROUPS)
    ax.set_ylabel("Sales", color=INK, fontsize=13, labelpad=15)
    ax.set_ylim(55, 360)
    ax.set_yticks(np.arange(50, 361, 50))
    ax.tick_params(axis="x", colors=INK, labelsize=14.5, length=0, pad=14)
    ax.tick_params(axis="y", colors=INK, labelsize=12.5, length=0, pad=9)
    ax.grid(axis="y", color=GRID, linewidth=1.05, zorder=0)
    ax.grid(axis="x", visible=False)

    ax.set_xlim(positions[0] - 0.9, positions[-1] + 0.9)
    for spine in ["top", "right", "left"]:
        ax.spines[spine].set_visible(False)
    ax.spines["bottom"].set_color(INK)
    ax.spines["bottom"].set_alpha(0.34)
    ax.spines["bottom"].set_linewidth(1.2)

    fig.subplots_adjust(left=0.075, right=0.965, top=0.84, bottom=0.14)
    output_file = OUTPUT_DIR / "five_box_violin_sales.png"
    fig.savefig(output_file, dpi=220, facecolor=BACKGROUND)
    plt.close(fig)
    return output_file


def main():
    output_file = draw_chart()
    print(output_file.name)


if __name__ == "__main__":
    main()
