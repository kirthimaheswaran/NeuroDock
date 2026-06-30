from Bio.PDB import PDBParser

# Create a PDB parser
parser = PDBParser(QUIET=True)

# Load the protein structure
structure = parser.get_structure("AChE", "protein/4M0E.pdb")

# Basic information
print("===================================")
print("NeuroDock Protein Analysis")
print("===================================")
print("Protein Name : Acetylcholinesterase")
print("PDB ID       : 4M0E")
print()

# Count chains
chains = list(structure.get_chains())
print(f"Number of Chains   : {len(chains)}")

# Count residues
residue_count = sum(1 for residue in structure.get_residues())
print(f"Number of Residues : {residue_count}")

# Count atoms
atom_count = sum(1 for atom in structure.get_atoms())
print(f"Number of Atoms    : {atom_count}")

print()
print("Protein loaded successfully!")