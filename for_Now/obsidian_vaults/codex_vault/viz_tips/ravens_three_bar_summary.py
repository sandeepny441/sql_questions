import numpy as np
import matplotlib.pyplot as plt


categories = ["Below Ravens", "On Ravens", "Above Ravens"]
locks = np.array([1015, 425, 3360])
percentages = np.array([21, 9, 70])

bg_top = np.array([10, 13, 28]) / 255
bg_bottom = np.array([4, 5, 11]) / 255
bg_warm = np.array([103, 35, 62]) / 255
bg_gold = np.array([127, 75, 27]) / 255
bg_ink = np.array([3, 4, 10]) / 255

bar_colors = ["#C75F66", "#D3A94C", "#4FA078"]
edge_colors = ["#F2A5A0", "#D7BA62", "#B9E1B2"]
label_colors = ["#F4B6B1", "#E6C56E", "#BDE5B6"]
paper_text = "#F5F1E9"
muted_text = "#B9B2A7"
y_label_text = "#FFFFFF"
grid = "#FFFFFF"

fig, ax = plt.subplots(figsize=(13, 7.2), facecolor=bg_ink)

# Dark, polished background inspired by the reference image.
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

ax.imshow(base, extent=[-0.75, 2.75, 0, 82], aspect="auto", zorder=0)
ax.set_facecolor("none")

x = np.arange(len(categories))
bars = ax.bar(
    x,
    percentages,
    width=0.62,
    color=bar_colors,
    edgecolor=edge_colors,
    linewidth=1.6,
    zorder=3,
)

for i, (bar, count, pct, color) in enumerate(zip(bars, locks, percentages, label_colors)):
    center_x = bar.get_x() + bar.get_width() / 2
    top = bar.get_height()
    ax.text(
        center_x,
        top + 3.0,
        f"{pct}%",
        ha="center",
        va="bottom",
        fontsize=24 if i == 2 else 21,
        color=color,
        weight="bold",
    )
    ax.text(
        center_x,
        top - 5.4 if top > 16 else top + 10.0,
        f"{count:,} locks",
        ha="center",
        va="top" if top > 16 else "bottom",
        fontsize=15,
        color=paper_text,
        weight="bold",
    )

ax.set_title(
    "Locks Share Around Ravens",
    fontsize=27,
    color=paper_text,
    weight="bold",
    pad=24,
)

ax.set_xticks(x, categories)
ax.tick_params(axis="x", colors=paper_text, labelsize=14, length=0, pad=14)
ax.tick_params(axis="y", colors=y_label_text, labelsize=12, length=0, pad=8)

ax.set_ylim(0, 82)
ax.set_xlim(-0.75, 2.75)
ax.yaxis.tick_right()
ax.yaxis.set_label_position("right")
ax.set_ylabel("Share of Total", color=y_label_text, fontsize=12, labelpad=18)
ax.set_yticks([0, 20, 40, 60, 80], ["0", "20%", "40%", "60%", "80%"])
ax.grid(axis="y", color=grid, alpha=0.18, linewidth=1.1, zorder=1)

for spine in ["top", "left", "right"]:
    ax.spines[spine].set_visible(False)
ax.spines["bottom"].set_color("#D7D0C5")
ax.spines["bottom"].set_alpha(0.75)
ax.spines["bottom"].set_linewidth(1.2)

plt.subplots_adjust(left=0.055, right=0.91, top=0.83, bottom=0.18)
fig.savefig("ravens_three_bar_summary.png", dpi=220, facecolor=bg_ink)
