"""
initial	name  	total_km	first_50	consistency
ab     	Radha 	1       	2       	1          
lp     	Atul  	2       	3       	4          
mn     	Shyam 	3       	1       	3          
zl     	Kishan	4       	4       	2          
"""


# %% composition_heatmap

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data
data = {
    "initial": ["ab", "lp", "mn", "zl"],
    "name": ["Radha", "Atul", "Shyam", "Kishan"],
    "total_km": [1, 2, 3, 4],
    "first_50": [2, 3, 1, 4],
    "consistency": [1, 4, 3, 2]
}

# Convert to DataFrame
df = pd.DataFrame(data)
#df.head(5).to_clipboard(index=False)
df["label"] = df["name"] + " [" + df["initial"] + "]"
df = df.set_index("label").drop(columns=["initial", "name"])  # Set index and drop redundant cols

# Set main color (RED in this case)
main_color = np.array([1, 56, 123]) / 255  # RGB -> Red shade

# Generate colors with reversed alpha values (higher values → lighter, lower values → darker)
unique_values = sorted(set(df.values.ravel()))  # Unique sorted values
alphas = np.linspace(1, 0.3, len(unique_values))  # Reverse order: high values are lighter
color_map = {val: (*main_color, alpha) for val, alpha in zip(unique_values, alphas)}

# Create a colormap from the generated colors
custom_cmap = sns.color_palette([color_map[val] for val in unique_values], as_cmap=True)

# Create figure with enforced white background
fig, ax = plt.subplots(figsize=(4, 4), facecolor="white")

# Remove index name to avoid "label" appearing on the y-axis
df.index.name = None  

# ✅ **Bring back borders with white lines (without gridlines)**
sns.heatmap(df, annot=True, fmt="d", cmap=custom_cmap, cbar=False, 
#            annot_kws={"fontsize": 12}, square=True, linewidths=1.5, linecolor="white", ax=ax)
             annot_kws={"fontsize": 12}, linewidths=1.5, linecolor="white", ax=ax) #auto adjust box size

# Left-align title manually
fig.text(0, 1.1, "correlation_heatmap", fontsize=14, fontweight='bold', ha='left', va='center', color="navy")
plt.subplots_adjust(top=0.75)  # Adjust spacing as needed
ax.margins(y=0)                 # Removes extra padding
plt.tight_layout()               # Auto-optimizes spacing

# Move x-axis labels to the top
ax.xaxis.tick_top()
ax.set_xticklabels(ax.get_xticklabels(), fontsize=11, fontweight="bold", color="navy")
ax.set_yticklabels(ax.get_yticklabels(), fontsize=11, fontweight="bold", rotation=0, color="navy")

# ✅ Remove tick marks but KEEP labels
ax.tick_params(left=False, bottom=False, top=False, right=False)

# ✅ Keep the x and y labels
ax.set_xlabel("Metrics", fontsize=12, fontweight="bold", labelpad=10, color="navy")
#ax.set_ylabel("Name (Initial)", fontsize=12, fontweight="bold", labelpad=10, color="navy")

# Turn off the y-axis label explicitly (optional)
ax.set_ylabel("")

# ✅ Forcefully remove all spines to avoid hidden gridlines
for spine in ax.spines.values():
    spine.set_visible(False)

# ✅ Manually disable Seaborn's automatic gridlines (Just in case)
ax.grid(False)

# ✅ Add footnote below the chart
fig.text(0, -0.05, "Note: This heatmap represents XYZ metrics. Data as of 2025.\nNote2",
         fontsize=7, color="gray", ha="left", va="top")

# Show plot
#plt.show()

# Display the chart
chart_out = _vl + r'\correlation\correlation_heatmap.png'
plt.savefig(chart_out, dpi=300, bbox_inches='tight')
#sp.Popen(chart_out, shell=True) #open file
#plt.show()

#exec(open(_vl+r'\correlation\correlation_heatmap.py').read())
