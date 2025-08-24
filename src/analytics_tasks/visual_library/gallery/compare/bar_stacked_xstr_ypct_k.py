# %% bar_stacked_xstr_ypct_k


## About
"""
transform_data(df, x=['date'], y=['source'], value=['nbr_of_patients'])

cat       drug   source nbr_of_patients
2022-01-31 Drug A New    1243
2022-01-31 Drug A Old    19518
2022-01-31 Drug A Mature 47570
"""

## Dependencies
import matplotlib.pyplot as plt
import pandas as pd
from analytics_tasks.utils.functions import open_file_folder
from analytics_tasks.automate_office.build_batch import (
    transform_data,
)
from analytics_tasks.automate_office.build_explore import (
    transform_data_explore,
)

_colors_file = _vl / "____settings/colors.xlsm"


## Filter data
df_monthly = pd.read_csv(_vl / "compare/bar_stacked_xstr_ypct_k.csv")
df = df_monthly[df_monthly["drug"] == "Drug A"]


## Transpose data
df = transform_data(df, x=["cat"], y=["source"], value=["nbr_of_patients"])
df = transform_data_explore(df, _colors_file)


# Calculate percentages and totals
df_pct = df.pivot_table(index="x", columns="y", values="value", aggfunc="sum")
df_totals = df_pct.sum(axis=1)
df_pct = df_pct.div(df_totals, axis=0) * 100

# Create the stacked bar chart
plt.figure()
ax = plt.gca()
plt.gcf()

# Plot stacked bars
colors = df[["y", "color_hex"]].drop_duplicates().set_index("y")["color_hex"].to_dict()
df_pct.plot(kind="bar", stacked=True, ax=ax, color=[colors[y] for y in df_pct.columns])

# Customize the plot
ax.grid(False)  # Remove gridlines
ax.set_yticks([])  # Remove y-axis ticks
ax.set_ylabel("")  # Remove y-axis label

# Format x-axis
x_labels = [d for d in df_pct.index]
ax.set_xticklabels(x_labels, rotation=0)

# Set x-axis title
ax.set_xlabel("Category")

# Add total values on top of bars
for i, total in enumerate(df_totals):
    plt.text(i, 100, f"{int(total / 1000)}K", ha="center", va="bottom")

# Add percentage labels
for c in ax.containers:
    ax.bar_label(c, fmt="%.0f%%", label_type="center", color="white")

# Customize apperance
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)

# Add legend
plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left", frameon=False)

plt.tight_layout()
# plt.show()

chart_out = _vl / 'compare/bar_stacked_xstr_ypct_k.png'
plt.savefig(chart_out)
open_file_folder(chart_out)


## Self
"""
exec(open(_vl / 'compare/bar_stacked_xstr_ypct_k.py', encoding='utf-8').read())
"""
