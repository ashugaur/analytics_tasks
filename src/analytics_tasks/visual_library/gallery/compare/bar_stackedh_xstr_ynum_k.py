# %% bar_stackedh_xstr_ynum_k

## Dependencies
import pandas as pd
from analytics_tasks.automate_office.build_batch import (
    transform_data,
)
from analytics_tasks.automate_office.build_explore import (
    transform_data_explore,
)
from analytics_tasks_utils.os_functions import open_file_folder


## bar_stackedh_xstr_ynum_k
def bar_stackedh_xstr_ynum_k(
    df,
    chartTitle="bar_stackedh_xstr_ynum_k",
    studyPeriod=12,  # Keep original for context
    special_series_name=None,
    special_series_label_font_size=10,
    chart_out=None,
    chart_width=2.5,
    chart_height=1.3,
    chart_title_font_size=10,
    chart_title_color="black",
    series_label_font_size=9,
    series_label_color="white",
    xtick_label_font_size=9,
    xtick_label_color="black",
    k_value_font_size=9,
    k_value_color="#01387B",
    legend_font_size=8,
):
    import matplotlib.pyplot as plt

    # Set up the figure and axis
    fig, ax = plt.subplots(figsize=(chart_width, chart_height))

    df["value"] = round(df["value"], 1)

    # Group by x (drug) to create stacked bars
    drugs = df["x"].unique()

    # Sort drugs by total value (optional, for consistent ordering)
    drug_totals = df.groupby("x")["value"].sum().sort_values(ascending=True)
    drugs = drug_totals.index.tolist()

    y_positions = range(len(drugs))

    for i, drug in enumerate(drugs):
        drug_data = df[df["x"] == drug].sort_values(
            "y"
        )  # Sort by category for consistent stacking

        left_pos = 0  # Starting position for stacking

        for _, row in drug_data.iterrows():
            # Create stacked bar segment
            bar = ax.barh(
                i,
                row["value"],
                left=left_pos,
                height=0.6,
                color=row["color_hex"],
                edgecolor="white",
                linewidth=0.5,
            )

            # Add percentage label on each segment if it's large enough
            segment_center = left_pos + row["value"] / 2
            if row["value"] >= 8:  # Only show label if segment is wide enough
                if drug == special_series_name:
                    ax.text(
                        segment_center,
                        i,
                        f"{row['value']}%",
                        ha="center",
                        va="center",
                        color=series_label_color,
                        fontweight="bold",
                        fontsize=special_series_label_font_size,
                    )
                else:
                    ax.text(
                        segment_center,
                        i,
                        f"{row['value']}%",
                        ha="center",
                        va="center",
                        color=series_label_color,
                        fontweight="bold",
                        fontsize=series_label_font_size,
                    )

            left_pos += row["value"]  # Move to next position

        # Add K values to the right of the complete bar
        # Get the largest z value for this drug to display
        max_z_row = drug_data.loc[drug_data["z"].idxmax()]
        formatted_z = f"{max_z_row['z'] / 1000:.0f}K"
        if formatted_z.endswith(".0K"):
            formatted_z = formatted_z.replace(".0K", "K")

        if drug == special_series_name:
            ax.text(
                102,  # Position just to the right of 100%
                i,
                formatted_z,
                ha="left",
                va="center",
                color=k_value_color,
                fontweight="bold",
                fontsize=special_series_label_font_size,
            )
        else:
            ax.text(
                102,  # Position just to the right of 100%
                i,
                formatted_z,
                ha="left",
                va="center",
                color=k_value_color,
                fontsize=k_value_font_size,
            )

    # Title
    ax.set_title("")
    if chartTitle == "":
        print("NOTE: No title.")
    else:
        chartTitle = f"{chartTitle}: Percentage Distribution"
        ax.text(
            -0.19,
            1.15,
            chartTitle,
            fontsize=chart_title_font_size,
            color=chart_title_color,
            transform=ax.transAxes,
        )

    # Set y-axis
    ax.set_yticks(y_positions)
    ax.set_yticklabels(drugs, fontsize=xtick_label_font_size, color=xtick_label_color)

    # Customize special series labels
    for label in ax.get_yticklabels():
        if label.get_text() == special_series_name:
            label.set_fontweight("bold")
            label.set_fontsize(special_series_label_font_size)

    # Set x-axis limits to 0-100% plus some space for K values
    ax.set_xlim(0, 110)

    # Remove spines and ticks
    ax.set_xticks([])
    ax.xaxis.set_ticks_position("none")
    ax.yaxis.set_ticks_position("none")
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(False)

    # Create legend for y values (categories)
    y_color_map = {}
    for _, row in df.iterrows():
        if row["y"] not in y_color_map:
            y_color_map[row["y"]] = row["color_hex"]

    # Sort legend items for consistent order
    sorted_categories = sorted(y_color_map.keys())
    legend_handles = []
    legend_labels = []
    for y_val in sorted_categories:
        legend_handles.append(plt.Rectangle((0, 0), 1, 1, fc=y_color_map[y_val]))
        legend_labels.append(y_val)

    ax.legend(
        legend_handles,
        legend_labels,
        loc="upper center",
        bbox_to_anchor=(0.5, -0.15),
        ncol=len(legend_labels),
        fontsize=legend_font_size,
        frameon=False,
    )

    # Adjust layout
    plt.tight_layout()
    plt.subplots_adjust(bottom=0.25)

    if chart_out:
        plt.savefig(chart_out, bbox_inches="tight")

    plt.close()


## Run
if __name__ == "__main__":
    # Data
    df = pd.read_csv(_vl / "compare/bar_stackedh_xstr_ynum_k.csv")

    # Colors
    _colors_file = _vl / "____settings/colors.xlsm"

    # Transpose
    df = transform_data(df, x=["drug"], y=["category"], value=["proportion"], z=["pc"])

    # Add colors
    df = transform_data_explore(df, _colors_file)

    chart_out = _vl / "compare/bar_stackedh_xstr_ynum_k.png"

    bar_stackedh_xstr_ynum_k(
        df,
        chart_out=chart_out,
        chartTitle="",
        chart_title_font_size=16,
        chart_title_color="#00165E",
        studyPeriod=12,
        special_series_name="",
        special_series_label_font_size=11,
        chart_width=5,
        chart_height=2,
        series_label_font_size=12,
        xtick_label_color="#00165E",
        xtick_label_font_size=12,
        k_value_font_size=12,
        k_value_color="#00165E",
    )

    open_file_folder(chart_out)


## Self
"""
exec(open(_vl / 'compare/bar_stackedh_xstr_ynum_k.py', encoding='utf-8').read())
"""
