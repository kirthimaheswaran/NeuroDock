from Bio.PDB import PDBParser

# Create parser
parser = PDBParser(QUIET=True)

# Load protein structure
structure = parser.get_structure("AChE", "protein/4M0E.pdb")

# Count information
chains = list(structure.get_chains())
residue_count = sum(1 for residue in structure.get_residues())
atom_count = sum(1 for atom in structure.get_atoms())

# Print results
print("===================================")
print("NeuroDock Protein Analysis")
print("===================================")
print("Protein Name : Acetylcholinesterase")
print("PDB ID       : 4M0E")
print(f"Number of Chains   : {len(chains)}")
print(f"Number of Residues : {residue_count}")
print(f"Number of Atoms    : {atom_count}")

# Save report
report = f"""
NeuroDock Protein Analysis
==========================

Protein Name : Acetylcholinesterase
PDB ID       : 4M0E

Number of Chains   : {len(chains)}
Number of Residues : {residue_count}
Number of Atoms    : {atom_count}
"""

with open("results/protein_analysis_report.txt", "w") as file:
    file.write(report)

print("\nProtein analysis report saved to results/protein_analysis_report.txt")