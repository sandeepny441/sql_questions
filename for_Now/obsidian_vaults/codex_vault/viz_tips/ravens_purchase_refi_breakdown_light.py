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

paper_top = np.array([251, 248, 240]) / 255
paper_bottom = np.array([239, 235, 226]) / 255
blush = np.array([238, 176, 170]) / 255
sage = np.array([183, 215, 188]) / 255
gold_glow_color = np.array([218, 185, 106]) / 255

purchase_color = "#D9AD45"
refi_color = "#7560A8"
purchase_edge = "#AE8429"
refi_edge = "#5D4A8C"
pillar_colors = ["#A43B4C", "#A9852E", "#2F765F"]
ink = "#232323"
muted = "#6D675F"
grid = "#D8D0C3"

fig, ax = plt.subplots(figsize=(13, 7.2), facecolor="#F6F2EA")

# Soft paper background with restrained warm/cool glow.
w, h = 1300, 720
yy, xx = np.mgrid[0:h, 0:w]
base = np.zeros((h, w, 3))
vertical = yy / (h - 1)
for c in range(3):
    base[:, :, c] = paper_top[c] * (1 - vertical) + paper_bottom[c] * vertical

blush_glow = np.exp(-(((xx - 190) / 430) ** 2 + ((yy - 85) / 270) ** 2))
sage_glow = np.exp(-(((xx - 1060) / 470) ** 2 + ((yy - 210) / 300) ** 2))
gold_glow = np.exp(-(((xx - 700) / 470) ** 2 + ((yy - 570) / 260) ** 2))
for c in range(3):
    base[:, :, c] = (
        base[:, :, c]
        + blush_glow * blush[c] * 0.16
        + sage_glow * sage[c] * 0.18
        + gold_glow * gold_glow_color[c] * 0.10
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
    edgecolor=purchase_edge,
    linewidth=1.4,
    zorder=3,
)
refi_bars = ax.bar(
    refi_x,
    refi_locks,
    width=bar_width,
    color=refi_color,
    edgecolor=refi_edge,
    linewidth=1.4,
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
        color=muted,
        weight="bold",
    )

for bars, values, mix, inside_color in [
    (purchase_bars, purchase_locks, purchase_mix, "#1F1B12"),
    (refi_bars, refi_locks, refi_mix, "#FFFFFF"),
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
            color=inside_color if inside else ink,
            weight="bold",
            linespacing=1.15,
            zorder=5,
        )

ax.set_title(
    "Purchase vs Refi Breakdown Around Ravens",
    fontsize=23,
    color=ink,
    weight="bold",
    pad=24,
)

ax.set_xticks(group_x, categories)
ax.tick_params(axis="x", colors=ink, labelsize=12.5, length=0, pad=14)
ax.tick_params(axis="y", colors=ink, labelsize=10.5, length=0, pad=8)

ax.set_ylim(0, 2850)
ax.set_xlim(-0.75, 4.15)
ax.yaxis.tick_right()
ax.yaxis.set_label_position("right")
ax.set_ylabel("Locks", color=ink, fontsize=11, labelpad=18)
ax.set_yticks([0, 500, 1000, 1500, 2000, 2500], ["0", "500", "1,000", "1,500", "2,000", "2,500"])
ax.grid(axis="y", color=grid, alpha=0.92, linewidth=1.0, zorder=1)

for spine in ["top", "left", "right"]:
    ax.spines[spine].set_visible(False)
ax.spines["bottom"].set_color("#BEB5A7")
ax.spines["bottom"].set_alpha(0.95)
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
    labelcolor=ink,
)

plt.subplots_adjust(left=0.055, right=0.91, top=0.83, bottom=0.15)
fig.savefig("ravens_purchase_refi_breakdown_light.png", dpi=220, facecolor="#F6F2EA")
