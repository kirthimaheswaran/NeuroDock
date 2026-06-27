import pandas as pd
import matplotlib.pyplot as plt

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