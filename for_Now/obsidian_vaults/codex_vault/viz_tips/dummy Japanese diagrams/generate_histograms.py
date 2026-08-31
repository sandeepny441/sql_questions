from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


OUTPUT_DIR = Path(__file__).resolve().parent

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
SALES = np.array([118, 146, 171, 158, 192, 214, 238, 226, 251, 267, 243, 282])

THEMES = [
    {
        "id": "01",
        "name": "coastal_blues",
        "background": "#F7F2E8",
        "ink": "#17324D",
        "grid": "#D6D0C3",
        "bars": [
            "#0B1F3A",
            "#123C69",
            "#1769AA",
            "#1C91C0",
            "#11A7A9",
            "#3BA99C",
            "#62B6A7",
            "#84C7B5",
            "#A7D3C3",
            "#6B8FBF",
            "#345995",
            "#0E4D64",
        ],
    },
    {
        "id": "02",
        "name": "sunset_citrus",
        "background": "#FFF3E8",
        "ink": "#3B1E16",
        "grid": "#E7D2C4",
        "bars": [
            "#7A1E2B",
            "#A8323C",
            "#D14B42",
            "#EF6F4C",
            "#F38D2C",
            "#F7B32B",
            "#E6A157",
            "#C97D60",
            "#B45A3C",
            "#8E3B46",
            "#D95D75",
            "#FF9E80",
        ],
    },
    {
        "id": "03",
        "name": "forest_moss",
        "background": "#F4F1E7",
        "ink": "#203322",
        "grid": "#D4D8C8",
        "bars": [
            "#123524",
            "#1D5C35",
            "#2E7D3E",
            "#4F9D58",
            "#74A662",
            "#99B76D",
            "#B6C472",
            "#8B9A46",
            "#657B3B",
            "#3F5F3A",
            "#6DAF8B",
            "#2A6F5A",
        ],
    },
    {
        "id": "04",
        "name": "orchid_berry",
        "background": "#F8F0F6",
        "ink": "#2E1C3D",
        "grid": "#DDD0DD",
        "bars": [
            "#32145A",
            "#512B81",
            "#6B46A1",
            "#8B5FBF",
            "#AA6BC8",
            "#C35AA8",
            "#D94E8F",
            "#B83F75",
            "#8E2A5E",
            "#6A1B4D",
            "#A77DB7",
            "#E08CCB",
        ],
    },
    {
        "id": "05",
        "name": "desert_earth",
        "background": "#FAF0E6",
        "ink": "#3C2A21",
        "grid": "#DFD0C2",
        "bars": [
            "#5A2E1F",
            "#7B3F2A",
            "#9C5134",
            "#BD6740",
            "#D9824B",
            "#E2A154",
            "#C99A5B",
            "#A87C4F",
            "#8B6F47",
            "#6F5A3E",
            "#B65F45",
            "#D9B68C",
        ],
    },
    {
        "id": "06",
        "name": "nordic_cool",
        "background": "#F4F7F8",
        "ink": "#1E2B33",
        "grid": "#D0D9DD",
        "bars": [
            "#1B263B",
            "#30455C",
            "#486581",
            "#5C7C99",
            "#78A1BB",
            "#A9C6D9",
            "#6EA8A1",
            "#4B8F8C",
            "#7B8EA3",
            "#A2AAB5",
            "#325D79",
            "#223D55",
        ],
    },
    {
        "id": "07",
        "name": "citrus_grove",
        "background": "#FFF9E6",
        "ink": "#3B3317",
        "grid": "#E7DEBF",
        "bars": [
            "#6B8E23",
            "#8AA62D",
            "#B5BD22",
            "#D7C51E",
            "#FFD23F",
            "#F9A620",
            "#F27A1A",
            "#D95D39",
            "#A4B43F",
            "#7CA66A",
            "#C0CA33",
            "#FFB000",
        ],
    },
    {
        "id": "08",
        "name": "jewel_box",
        "background": "#F6F1EA",
        "ink": "#221D35",
        "grid": "#D8CFCA",
        "bars": [
            "#003F5C",
            "#2F4B7C",
            "#665191",
            "#A05195",
            "#D45087",
            "#F95D6A",
            "#FF7C43",
            "#FFA600",
            "#1B9E77",
            "#00798C",
            "#7A5195",
            "#B22A2E",
        ],
    },
    {
        "id": "09",
        "name": "vintage_print",
        "background": "#F5EFE2",
        "ink": "#24211D",
        "grid": "#D8CEBE",
        "bars": [
            "#264653",
            "#2A9D8F",
            "#E9C46A",
            "#F4A261",
            "#E76F51",
            "#8AB17D",
            "#577590",
            "#B56576",
            "#6D597A",
            "#355070",
            "#CB997E",
            "#A5A58D",
        ],
    },
    {
        "id": "10",
        "name": "editorial_contrast",
        "background": "#F7F5EF",
        "ink": "#1F1F1F",
        "grid": "#D8D4C8",
        "bars": [
            "#005F73",
            "#0A9396",
            "#94D2BD",
            "#E9D8A6",
            "#EE9B00",
            "#CA6702",
            "#BB3E03",
            "#AE2012",
            "#9B2226",
            "#3D405B",
            "#81B29A",
            "#F2CC8F",
        ],
    },
]


def hex_to_rgb(color):
    color = color.lstrip("#")
    return np.array([int(color[i : i + 2], 16) for i in (0, 2, 4)]) / 255


def rgb_to_hex(rgb):
    rgb = np.clip(np.round(rgb * 255), 0, 255).astype(int)
    return "#{:02X}{:02X}{:02X}".format(*rgb)


def mix(first_color, second_color, weight):
    first = hex_to_rgb(first_color)
    second = hex_to_rgb(second_color)
    return rgb_to_hex(first * (1 - weight) + second * weight)


def relative_luminance(color):
    rgb = hex_to_rgb(color)
    linear = np.where(rgb <= 0.03928, rgb / 12.92, ((rgb + 0.055) / 1.055) ** 2.4)
    return 0.2126 * linear[0] + 0.7152 * linear[1] + 0.0722 * linear[2]


def contrast_ratio(first_color, second_color):
    first = relative_luminance(first_color)
    second = relative_luminance(second_color)
    lighter, darker = max(first, second), min(first, second)
    return (lighter + 0.05) / (darker + 0.05)


def readable_label_color(color, background, ink):
    if contrast_ratio(color, background) >= 3.3:
        return color
    return mix(color, ink, 0.58)


def draw_sales_chart(theme):
    background = theme["background"]
    ink = theme["ink"]
    grid = theme["grid"]
    bar_colors = theme["bars"]
    annual_total = SALES.sum()
    percentages = SALES / annual_total * 100

    fig, ax = plt.subplots(figsize=(11.5, 7), facecolor=background)
    ax.set_facecolor(background)

    x = np.arange(len(MONTHS))
    bars = ax.bar(
        x,
        SALES,
        width=0.72,
        color=bar_colors,
        edgecolor=background,
        linewidth=1.6,
        alpha=0.97,
        zorder=3,
    )

    for bar, sales, percentage, bar_color in zip(bars, SALES, percentages, bar_colors):
        sales_color = readable_label_color(bar_color, background, ink)
        percent_color = mix(sales_color, background, 0.27)
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
    filename = OUTPUT_DIR / f"histogram_{theme['id']}.png"
    fig.savefig(filename, dpi=220, facecolor=background)
    plt.close(fig)
    return filename


def main():
    for theme in THEMES:
        output_file = draw_sales_chart(theme)
        print(f"{output_file.name} - {theme['name']}")


if __name__ == "__main__":
    main()
