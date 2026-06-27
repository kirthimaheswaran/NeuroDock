import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load docking scores
df = pd.read_csv("data/docking_scores.csv")

print("NeuroDock Dataset")
print(df)

# Calculate consensus score
df["Consensus_Score"] = df[
    ["AutoDock_Vina", "Glide", "GOLD"]
].mean(axis=1)

# Rank ligands
ranked = df.sort_values("Consensus_Score")

print("\nTop Ranked Ligands:")
print(ranked[["Ligand", "Consensus_Score"]])

# Create graph
plt.figure(figsize=(8,5))
plt.bar(ranked["Ligand"], ranked["Consensus_Score"])

plt.title("Consensus Docking Scores")
plt.xlabel("Ligands")
plt.ylabel("Consensus Score")

plt.tight_layout()

plt.savefig("figures/consensus_scores.png")

plt.show()
# Save ranked ligands
ranked.to_csv("results/ranked_ligands.csv", index=False)

print("\nResults saved to results/ranked_ligands.csv")
# Heatmap of docking scores

scores = df[["AutoDock_Vina", "Glide", "GOLD"]]

plt.figure(figsize=(6,5))
plt.imshow(scores, aspect="auto")

plt.colorbar(label="Docking Score")

plt.xticks(
    np.arange(3),
    ["AutoDock Vina", "Glide", "GOLD"]
)

plt.yticks(
    np.arange(len(df)),
    df["Ligand"]
)

plt.title("Docking Score Heatmap")

plt.tight_layout()

plt.savefig("figures/docking_heatmap.png")

plt.show()
# Scatter plot comparing AutoDock Vina and Glide

plt.figure(figsize=(6,6))

plt.scatter(df["AutoDock_Vina"], df["Glide"], s=80)

for i, ligand in enumerate(df["Ligand"]):
    plt.text(
        df["AutoDock_Vina"][i],
        df["Glide"][i],
        ligand,
        fontsize=8
    )

plt.title("AutoDock Vina vs Glide Scores")
plt.xlabel("AutoDock Vina")
plt.ylabel("Glide")

plt.grid(True)

plt.tight_layout()

plt.savefig("figures/docking_comparison.png")

plt.show()
# Generate analysis report

best = ranked.iloc[0]

report = f"""
NeuroDock Analysis Report
=========================

Target Protein:
Acetylcholinesterase (AChE)

Best Ligand:
{best['Ligand']}

Consensus Score:
{best['Consensus_Score']:.2f}

Interpretation:
The ligand {best['Ligand']} achieved the best average docking score
across AutoDock Vina, Glide, and GOLD, suggesting consistent predicted
binding affinity.

Number of ligands analysed:
{len(df)}

Analysis completed successfully.
"""

with open("results/analysis_report.txt", "w") as file:
    file.write(report)

print("\nAnalysis report saved to results/analysis_report.txt")