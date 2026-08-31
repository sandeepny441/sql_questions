import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch


# Placeholder data for concept review.
# Replace these lock counts with production values when available.
labels = [
    "-60",
    "-50",
    "-40",
    "-30",
    "-20",
    "-10",
    "Ravens",
    "+10",
    "+20",
    "+30",
    "+40",
    "+50",
    "+60",
]

group_labels = [
    "Below Ravens",
    "Below Ravens",
    "Below Ravens",
    "Below Ravens",
    "Below Ravens",
    "Below Ravens",
    "Ravens",
    "Evo Ravens",
    "Evo Ravens",
    "Evo Ravens",
    "Evo Ravens",
    "Evo Ravens",
    "Evo Ravens",
]

# Placeholder data for concept review.
# Evo Ravens intentionally carries 70% of the total lock volume.
locks = np.array([65, 95, 125, 165, 230, 335, 425, 520, 620, 690, 650, 500, 380])
percentages = locks / locks.sum() * 100


def rounded_percentages_that_sum_to_100(values):
    raw = values / values.sum() * 100
    floored = np.floor(raw).astype(int)
    remaining = 100 - floored.sum()
    order = np.argsort(raw - floored)[::-1]
    floored[order[:remaining]] += 1
    return floored


rounded_percentages = rounded_percentages_that_sum_to_100(locks)
below_total = locks[:6].sum()
ravens_total = locks[6]
evo_total = locks[7:].sum()
total_locks = locks.sum()
below_pct = rounded_percentages[:6].sum()
ravens_pct = rounded_percentages[6]
evo_pct = rounded_percentages[7:].sum()


def catmull_rom_curve(xs, ys, samples_per_segment=28):
    points = np.column_stack([xs, ys]).astype(float)
    padded = np.vstack([points[0], points, points[-1]])
    curve = []
    for i in range(1, len(padded) - 2):
        p0, p1, p2, p3 = padded[i - 1], padded[i], padded[i + 1], padded[i + 2]
        for t in np.linspace(0, 1, samples_per_segment, endpoint=False):
            t2 = t * t
            t3 = t2 * t
            point = 0.5 * (
                (2 * p1)
                + (-p0 + p2) * t
                + (2 * p0 - 5 * p1 + 4 * p2 - p3) * t2
                + (-p0 + 3 * p1 - 3 * p2 + p3) * t3
            )
            curve.append(point)
    curve.append(points[-1])
    curve = np.array(curve)
    return curve[:, 0], curve[:, 1]


# Restrained Japanese-inspired gradients:
# Below Ravens gets darker as it moves farther left from Ravens.
# Evo Ravens gets darker as it moves farther right from Ravens.
colors = [
    "#7F263A",
    "#A93C4C",
    "#C95E61",
    "#DF8280",
    "#EFAAA2",
    "#F7D5CE",
    "#1E2F5F",  # Ravens indigo
    "#DDECD4",
    "#BFDDB8",
    "#97C996",
    "#6CAD78",
    "#3F8F66",
    "#1D6F5E",
]

paper = "#F8F5EF"
ink = "#242424"
muted = "#68635C"
grid = "#DED8CB"
gold = "#C7A24A"
count_color = "#232323"
percent_color = "#5B3A8E"

fig, ax = plt.subplots(figsize=(16, 8.5), facecolor=paper)
ax.set_facecolor(paper)

x = np.arange(len(labels))
bars = ax.bar(
    x,
    locks,
    width=0.68,
    color=colors,
    edgecolor=paper,
    linewidth=2,
    zorder=3,
)

ravens_idx = labels.index("Ravens")
bars[ravens_idx].set_edgecolor(gold)
bars[ravens_idx].set_linewidth(3.2)

curve_x, curve_y = catmull_rom_curve(x, locks)
ax.plot(
    curve_x,
    curve_y,
    color="#5B3A8E",
    linewidth=3.2,
    alpha=0.92,
    zorder=4,
)
ax.scatter(
    x,
    locks,
    s=34,
    color=paper,
    edgecolor="#5B3A8E",
    linewidth=1.8,
    zorder=4.2,
)

ax.set_ylim(0, locks.max() * 1.78)
summary_y = locks.max() * 1.38
arrow_y = locks.max() * 1.60

below_box = (
    f"{below_total:,} locks\n"
    f"{below_pct}% of total"
)
ravens_box = (
    "On Ravens\n"
    f"{ravens_total:,} locks\n"
    f"{ravens_pct}% of total"
)
evo_box = (
    f"{evo_total:,} locks\n"
    f"{evo_pct}% of total"
)

ax.text(
    2.05,
    summary_y,
    below_box,
    ha="center",
    va="center",
    fontsize=18,
    color="#6F1F32",
    weight="bold",
    linespacing=1.24,
    bbox=dict(
        boxstyle="round,pad=0.52,rounding_size=0.18",
        facecolor="#F6D7D2",
        edgecolor="#8B263B",
        linewidth=2.2,
    ),
    zorder=6,
)

ax.text(
    6.0,
    summary_y,
    ravens_box,
    ha="center",
    va="center",
    fontsize=17,
    color="#1E2F5F",
    weight="bold",
    linespacing=1.24,
    bbox=dict(
        boxstyle="round,pad=0.50,rounding_size=0.18",
        facecolor="#ECE6D8",
        edgecolor=gold,
        linewidth=2.2,
    ),
    zorder=6,
)

ax.text(
    10.15,
    summary_y,
    evo_box,
    ha="center",
    va="center",
    fontsize=20,
    color="#175B4E",
    weight="bold",
    linespacing=1.24,
    bbox=dict(
        boxstyle="round,pad=0.52,rounding_size=0.18",
        facecolor="#DCEFD5",
        edgecolor="#1D6F5E",
        linewidth=2.2,
    ),
    zorder=6,
)

left_arrow = FancyArrowPatch(
    (5.2, arrow_y),
    (0.75, arrow_y),
    arrowstyle="Simple,head_width=18,head_length=24,tail_width=7",
    color="#8B263B",
    alpha=0.78,
    linewidth=0,
    zorder=5,
)
right_arrow = FancyArrowPatch(
    (6.8, arrow_y),
    (12.25, arrow_y),
    arrowstyle="Simple,head_width=18,head_length=24,tail_width=7",
    color="#1D6F5E",
    alpha=0.78,
    linewidth=0,
    zorder=5,
)
ax.add_patch(left_arrow)
ax.add_patch(right_arrow)

ravens_connector = FancyArrowPatch(
    (ravens_idx, locks[ravens_idx] + locks.max() * 0.18),
    (ravens_idx, summary_y - locks.max() * 0.17),
    arrowstyle="Simple,head_width=14,head_length=18,tail_width=4",
    color=gold,
    alpha=0.9,
    linewidth=0,
    zorder=5,
)
ax.add_patch(ravens_connector)

ax.text(
    2.95,
    arrow_y + locks.max() * 0.045,
    "Below Ravens",
    ha="center",
    va="bottom",
    fontsize=15,
    color="#7F263A",
    weight="bold",
)
ax.text(
    9.55,
    arrow_y + locks.max() * 0.045,
    "Above Ravens",
    ha="center",
    va="bottom",
    fontsize=15,
    color="#1D6F5E",
    weight="bold",
)

for i, (bar, count, pct) in enumerate(zip(bars, locks, rounded_percentages)):
    y = bar.get_height()
    center_x = bar.get_x() + bar.get_width() / 2
    pct_y = y + 36
    count_y = y + 78
    ax.text(
        center_x,
        count_y,
        f"{count:,}",
        ha="center",
        va="bottom",
        fontsize=14 if i == ravens_idx else 13,
        color="#1E2F5F" if i == ravens_idx else count_color,
        weight="bold",
    )
    ax.text(
        center_x,
        pct_y,
        f"{pct}%",
        ha="center",
        va="bottom",
        fontsize=13 if i == ravens_idx else 12,
        color=percent_color,
        weight="bold",
    )

ax.set_title(
    "Locks Distribution Around Ravens",
    fontsize=25,
    weight="bold",
    color=ink,
    pad=24,
)

ax.set_ylabel("Locks", fontsize=12, color=ink, labelpad=12)
tick_labels = [
    "Below\n-60 bps",
    "Below\n-50 bps",
    "Below\n-40 bps",
    "Below\n-30 bps",
    "Below\n-20 bps",
    "Below\n-10 bps",
    "Ravens",
    "Evo\n+10 bps",
    "Evo\n+20 bps",
    "Evo\n+30 bps",
    "Evo\n+40 bps",
    "Evo\n+50 bps",
    "Evo\n+60 bps",
]
ax.set_xticks(x, tick_labels)

ax.set_xlim(-0.75, len(labels) - 0.25)
ax.grid(axis="y", color=grid, linewidth=0.8, alpha=0.9, zorder=0)
ax.tick_params(axis="x", length=0, labelsize=10, colors=ink, pad=10)
ax.tick_params(axis="y", length=0, labelsize=10, colors=muted)

for spine in ["top", "right", "left"]:
    ax.spines[spine].set_visible(False)
ax.spines["bottom"].set_color("#C9C1B4")

plt.subplots_adjust(left=0.07, right=0.985, top=0.84, bottom=0.16)
fig.savefig("ravens_histogram_concept.png", dpi=220, facecolor=paper)
