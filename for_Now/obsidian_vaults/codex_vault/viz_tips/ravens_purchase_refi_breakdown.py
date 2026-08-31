import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch


categories = ["Below Ravens", "On Ravens", "Above Ravens"]

# Placeholder split data. Each group adds back to the pillar totals used before:
# Below = 1,015, On = 425, Above = 3,360.
purchase_locks = np.array([660, 285, 2420])
refi_locks = np.array([355, 140, 940])
totals = purchase_locks + refi_locks
grand_total = totals.sum()

pillar_share = totals / grand_total * 100
purchase_mix = purchase_locks / totals * 100
refi_mix = refi_locks / totals * 100

bg_top = np.array([10, 13, 28]) / 255
bg_bottom = np.array([4, 5, 11]) / 255
bg_warm = np.array([103, 35, 62]) / 255
bg_gold = np.array([127, 75, 27]) / 255
bg_ink = np.array([3, 4, 10]) / 255

purchase_color = "#E0B85D"
refi_color = "#7657A8"
pillar_colors = ["#F2A5A0", "#D7BA62", "#B9E1B2"]
paper_text = "#F5F1E9"
white_text = "#FFFFFF"
grid = "#FFFFFF"

fig, ax = plt.subplots(figsize=(13, 7.2), facecolor=bg_ink)

# Dark editorial glow background, matching the previous summary chart.
w, h = 1300, 720
yy, xx = np.mgrid[0:h, 0:w]
base = np.zeros((h, w, 3))
vertical = yy / (h - 1)
for c in range(3):
    base[:, :, c] = bg_top[c] * (1 - vertical) + bg_bottom[c] * vertical

warm_glow = np.exp(-(((xx - 180) / 430) ** 2 + ((yy - 80) / 270) ** 2))
gold_glow = np.exp(-(((xx - 830) / 520) ** 2 + ((yy - 560) / 310) ** 2))
for c in range(3):
    base[:, :, c] = (
        base[:, :, c]
        + warm_glow * bg_warm[c] * 0.46
        + gold_glow * bg_gold[c] * 0.18
    )
base = np.clip(base, 0, 1)

ax.imshow(base, extent=[-0.75, 4.15, 0, 2850], aspect="auto", zorder=0)
ax.set_facecolor("none")

group_x = np.array([0.0, 1.7, 3.4])
bar_width = 0.36
offset = 0.23
purchase_x = group_x - offset
refi_x = group_x + offset

purchase_bars = ax.bar(
    purchase_x,
    purchase_locks,
    width=bar_width,
    color=purchase_color,
    edgecolor="#F1D385",
    linewidth=1.5,
    zorder=3,
)
refi_bars = ax.bar(
    refi_x,
    refi_locks,
    width=bar_width,
    color=refi_color,
    edgecolor="#BCA7E6",
    linewidth=1.5,
    zorder=3,
)

for i, center_x in enumerate(group_x):
    group_top = max(purchase_locks[i], refi_locks[i])
    if i == 0:
        total_y = group_top + 360
        share_y = group_top + 250
    elif i == 1:
        total_y = group_top + 360
        share_y = group_top + 255
    else:
        total_y = group_top + 210
        share_y = group_top + 115
    ax.text(
        center_x,
        total_y,
        f"{totals[i]:,} total",
        ha="center",
        va="bottom",
        fontsize=15 if i == 2 else 13,
        color=pillar_colors[i],
        weight="bold",
    )
    ax.text(
        center_x,
        share_y,
        f"{round(pillar_share[i]):.0f}% of all locks",
        ha="center",
        va="bottom",
        fontsize=10.5,
        color=paper_text,
        weight="bold",
    )

for bars, values, mix, label_color in [
    (purchase_bars, purchase_locks, purchase_mix, "#17140B"),
    (refi_bars, refi_locks, refi_mix, white_text),
]:
    for bar, value, pct in zip(bars, values, mix):
        x_pos = bar.get_x() + bar.get_width() / 2
        y = bar.get_height()
        inside = y > 600
        ax.text(
            x_pos,
            y - 110 if inside else y + 48,
            f"{value:,}\n{pct:.0f}%",
            ha="center",
            va="top" if inside else "bottom",
            fontsize=11.5 if inside else 10.5,
            color=label_color if inside else paper_text,
            weight="bold",
            linespacing=1.15,
            zorder=5,
        )

ax.set_title(
    "Purchase vs Refi Breakdown Around Ravens",
    fontsize=23,
    color=paper_text,
    weight="bold",
    pad=24,
)

ax.set_xticks(group_x, categories)
ax.tick_params(axis="x", colors=paper_text, labelsize=12.5, length=0, pad=14)
ax.tick_params(axis="y", colors=white_text, labelsize=10.5, length=0, pad=8)

ax.set_ylim(0, 2850)
ax.set_xlim(-0.75, 4.15)
ax.yaxis.tick_right()
ax.yaxis.set_label_position("right")
ax.set_ylabel("Locks", color=white_text, fontsize=11, labelpad=18)
ax.set_yticks([0, 500, 1000, 1500, 2000, 2500], ["0", "500", "1,000", "1,500", "2,000", "2,500"])
ax.grid(axis="y", color=grid, alpha=0.18, linewidth=1.1, zorder=1)

for spine in ["top", "left", "right"]:
    ax.spines[spine].set_visible(False)
ax.spines["bottom"].set_color("#D7D0C5")
ax.spines["bottom"].set_alpha(0.75)
ax.spines["bottom"].set_linewidth(1.2)

ax.legend(
    handles=[
        Patch(facecolor=purchase_color, edgecolor="none", label="Purchase"),
        Patch(facecolor=refi_color, edgecolor="none", label="Refi"),
    ],
    loc="upper left",
    bbox_to_anchor=(0.02, 0.98),
    ncol=2,
    frameon=False,
    fontsize=11.5,
    labelcolor=paper_text,
)

plt.subplots_adjust(left=0.055, right=0.91, top=0.83, bottom=0.15)
fig.savefig("ravens_purchase_refi_breakdown.png", dpi=220, facecolor=bg_ink)
