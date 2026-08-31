from pathlib import Path

import xlsxwriter


OUTPUT = Path("/Users/san/Documents/ai_1001/codex_files/003_epo/linear_regression_interactive.xlsx")


def build_workbook(path: Path) -> None:
    workbook = xlsxwriter.Workbook(path)
    sheet = workbook.add_worksheet("Regression Demo")
    lists = workbook.add_worksheet("Lists")
    lists.hide()

    title = workbook.add_format(
        {
            "bold": True,
            "font_size": 22,
            "font_name": "Aptos Display",
            "font_color": "#1f2937",
            "align": "left",
            "valign": "vcenter",
        }
    )
    subtitle = workbook.add_format(
        {
            "font_size": 11,
            "font_name": "Aptos",
            "font_color": "#5b6475",
            "text_wrap": True,
        }
    )
    block = workbook.add_format(
        {
            "bg_color": "#f7f0ff",
            "border": 1,
            "border_color": "#dac7f3",
        }
    )
    label = workbook.add_format(
        {
            "bold": True,
            "font_name": "Aptos",
            "font_color": "#4c1d95",
            "bg_color": "#f7f0ff",
            "border": 1,
            "border_color": "#dac7f3",
        }
    )
    value = workbook.add_format(
        {
            "font_name": "Aptos",
            "num_format": "0.0",
            "align": "center",
            "bg_color": "#ffffff",
            "border": 1,
            "border_color": "#dac7f3",
        }
    )
    hint = workbook.add_format(
        {
            "font_name": "Aptos",
            "font_color": "#5b6475",
            "bg_color": "#f7f0ff",
            "border": 1,
            "border_color": "#dac7f3",
            "text_wrap": True,
            "valign": "top",
        }
    )
    metric_label = workbook.add_format(
        {
            "bold": True,
            "font_name": "Aptos",
            "font_color": "#1f2937",
            "bg_color": "#fef3c7",
            "border": 1,
            "border_color": "#f6d88e",
        }
    )
    metric_value = workbook.add_format(
        {
            "bold": True,
            "font_name": "Aptos",
            "font_color": "#92400e",
            "bg_color": "#fff8dc",
            "border": 1,
            "border_color": "#f6d88e",
            "num_format": "0.00",
            "align": "center",
        }
    )
    formula_box = workbook.add_format(
        {
            "bold": True,
            "font_name": "Aptos",
            "font_color": "#9d174d",
            "bg_color": "#fdf2f8",
            "border": 1,
            "border_color": "#f3c4d7",
            "align": "center",
        }
    )
    section_title = workbook.add_format(
        {
            "bold": True,
            "font_name": "Aptos",
            "font_color": "#111827",
            "bottom": 1,
            "bottom_color": "#e5e7eb",
        }
    )
    note = workbook.add_format(
        {
            "font_name": "Aptos",
            "font_color": "#4b5563",
            "text_wrap": True,
            "valign": "top",
        }
    )
    header = workbook.add_format(
        {
            "bold": True,
            "font_name": "Aptos",
            "bg_color": "#ede9fe",
            "border": 1,
            "border_color": "#ddd6fe",
            "font_color": "#312e81",
            "align": "center",
        }
    )
    number = workbook.add_format(
        {
            "font_name": "Aptos",
            "border": 1,
            "border_color": "#e5e7eb",
            "num_format": "0.00",
        }
    )
    integer = workbook.add_format(
        {
            "font_name": "Aptos",
            "border": 1,
            "border_color": "#e5e7eb",
            "num_format": "0",
        }
    )

    sheet.hide_gridlines(2)
    sheet.set_zoom(115)
    sheet.set_default_row(22)
    sheet.set_column("A:A", 14)
    sheet.set_column("B:B", 13)
    sheet.set_column("C:C", 13)
    sheet.set_column("D:E", 12)
    sheet.set_column("F:H", 15)
    sheet.set_column("I:I", 3)
    sheet.set_column("J:N", 12)

    sheet.merge_range("A1:H1", "Linear Regression, Visually", title)
    sheet.merge_range(
        "A2:H2",
        "Use the purple controls to change the line. The chart updates instantly so you can explain slope, intercept, and why a better-fitting line produces smaller errors.",
        subtitle,
    )

    for row in range(3, 7):
        sheet.write_blank(row, 0, None, block)
        sheet.write_blank(row, 1, None, block)
        sheet.write_blank(row, 2, None, block)
        sheet.write_blank(row, 3, None, block)

    sheet.write("A4", "Slope", label)
    sheet.write("A5", "Intercept", label)
    sheet.write("A6", "Your line", label)
    sheet.write("A7", "Squared error", metric_label)

    sheet.write_number("B4", 1.8, value)
    sheet.write_number("B5", 3.0, value)
    sheet.write_formula("B6", '="y = " & TEXT(B4,"0.0") & "x + " & TEXT(B5,"0.0")', formula_box)
    sheet.write_formula("B7", "=SUM(E13:E24)", metric_value)

    sheet.merge_range(
        "C4:D5",
        "Try a steeper slope to rotate the line.\nChange the intercept to move the line up or down.",
        hint,
    )
    sheet.merge_range(
        "C6:D7",
        "A smaller squared error means your line is closer to the points.\nThat is the basic idea behind least squares regression.",
        hint,
    )

    sheet.write("F4", "How to explain it", section_title)
    sheet.merge_range(
        "F5:H7",
        "1. Start with the red line.\n2. Change slope to make it flatter or steeper.\n3. Change intercept to shift it up or down.\n4. Watch how the gap between the dots and the line changes.\n5. The best regression line is the one that makes the total squared error as small as possible.",
        note,
    )
    sheet.write("F9", "Excel's best-fit reference", section_title)
    sheet.write("F10", "Best slope", label)
    sheet.write_formula("G10", "=SLOPE(B13:B24,A13:A24)", value)
    sheet.write("F11", "Best intercept", label)
    sheet.write_formula("G11", "=INTERCEPT(B13:B24,A13:A24)", value)

    x_values = list(range(1, 13))
    y_values = [5, 8, 8, 10, 14, 14, 17, 18, 22, 22, 25, 27]

    sheet.write_row("A12", ["X", "Observed Y", "Predicted Y", "Residual", "Squared Error"], header)
    for row_index, (x_val, y_val) in enumerate(zip(x_values, y_values), start=13):
        sheet.write_number(row_index - 1, 0, x_val, integer)
        sheet.write_number(row_index - 1, 1, y_val, number)
        sheet.write_formula(row_index - 1, 2, f"=$B$4*A{row_index}+$B$5", number)
        sheet.write_formula(row_index - 1, 3, f"=B{row_index}-C{row_index}", number)
        sheet.write_formula(row_index - 1, 4, f"=D{row_index}^2", number)

    slope_values = [round(-1.0 + step * 0.2, 1) for step in range(31)]
    intercept_values = [round(-5.0 + step * 0.5, 1) for step in range(31)]
    for idx, val in enumerate(slope_values, start=1):
        lists.write_number(idx - 1, 0, val)
    for idx, val in enumerate(intercept_values, start=1):
        lists.write_number(idx - 1, 1, val)

    sheet.data_validation(
        "B4",
        {
            "validate": "list",
            "source": "=Lists!$A$1:$A$31",
            "input_title": "Slope",
            "input_message": "Pick a slope. Bigger means steeper.",
        },
    )
    sheet.data_validation(
        "B5",
        {
            "validate": "list",
            "source": "=Lists!$B$1:$B$31",
            "input_title": "Intercept",
            "input_message": "Pick an intercept. This moves the line up or down.",
        },
    )

    chart = workbook.add_chart({"type": "scatter", "subtype": "straight_with_markers"})
    chart.add_series(
        {
            "name": "Observed points",
            "categories": "=\'Regression Demo\'!$A$13:$A$24",
            "values": "=\'Regression Demo\'!$B$13:$B$24",
            "line": {"none": True},
            "marker": {
                "type": "circle",
                "size": 7,
                "border": {"color": "#4338ca"},
                "fill": {"color": "#a78bfa"},
            },
        }
    )
    chart.add_series(
        {
            "name": "Your line",
            "categories": "=\'Regression Demo\'!$A$13:$A$24",
            "values": "=\'Regression Demo\'!$C$13:$C$24",
            "line": {"color": "#e11d48", "width": 2.75},
            "marker": {"type": "none"},
        }
    )
    chart.set_title({"name": "One Graph: Data + Adjustable Regression Line"})
    chart.set_x_axis(
        {
            "name": "X",
            "major_gridlines": {"visible": False},
            "min": 1,
            "max": 12,
        }
    )
    chart.set_y_axis(
        {
            "name": "Y",
            "major_gridlines": {"visible": True, "line": {"color": "#ece8ff"}},
            "min": 0,
            "max": 30,
        }
    )
    chart.set_legend({"position": "bottom"})
    chart.set_plotarea(
        {
            "fill": {"color": "#fffefe"},
            "border": {"color": "#ede9fe"},
        }
    )
    chart.set_chartarea(
        {
            "fill": {"color": "#ffffff"},
            "border": {"color": "#d7d9e0"},
        }
    )
    chart.set_size({"width": 760, "height": 420})

    sheet.insert_chart("J2", chart)
    sheet.freeze_panes(12, 0)

    workbook.close()


if __name__ == "__main__":
    build_workbook(OUTPUT)
    print(OUTPUT)
