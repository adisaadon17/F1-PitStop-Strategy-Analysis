import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load efficiency dataset
efficiency = pd.read_csv(
    r"C:\Users\adisa\OneDrive\שולחן העבודה\Adi\Personal Project\F1 Project\Python\View CSV\PitEfficiency_vs_Results.csv",
    header=None,
    names=["constructorName", "raceYear", "avgPitLaneSec", "avgFinishPos"]
)

# Select numeric columns
numeric_df = efficiency[["raceYear", "avgPitLaneSec", "avgFinishPos"]]
correlation_matrix = numeric_df.corr()

# ----------- STYLE SETTINGS -------------
# Create figure with soft Ice-Blue background (30% transparency)
fig = plt.figure(figsize=(6, 6))
fig.patch.set_facecolor('#CFE9FF')      # Ice Blue
fig.patch.set_alpha(0.3)                # 30% transparency

# Build the square-perfect heatmap
cmap = sns.color_palette(
    ["#002A5C", "#4A7EBB", "#FFFFFF"],  # Dark Blue → Soft Blue → White
    as_cmap=True
)

sns.set_style("white")
ax = sns.heatmap(
    correlation_matrix,
    annot=True,
    fmt=".2f",
    cmap=cmap,
    linewidths=0.8,
    linecolor="#B2C7D9",
    square=True,
    cbar_kws={"shrink": 0.75}
)

# Title + Text Styling
plt.title("Correlation Heatmap", fontsize=16, pad=15, color="#002A5C")
plt.xticks(rotation=45, fontsize=11, color="#002A5C")
plt.yticks(rotation=0, fontsize=11, color="#002A5C")

plt.tight_layout()

# Save if needed
plt.savefig("soft_blue_heatmap.png", dpi=300, facecolor=fig.get_facecolor(), bbox_inches="tight")

plt.show()
