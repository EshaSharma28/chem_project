from rdkit import Chem # type: ignore
from rdkit.Chem import AllChem # type: ignore

# 1. Define the molecule (using Aspirin as an example)
smiles = "CC(=O)OC1=CC=CC=C1C(=O)O"
molecule = Chem.MolFromSmiles(smiles)

# 2. Add Hydrogen atoms (SMILES usually hides them for simplicity)
molecule_with_h = Chem.AddHs(molecule)

# 3. Generate 3D Coordinates
AllChem.EmbedMolecule(molecule_with_h, AllChem.ETKDG())

# 4. Save it as a .pdb file (Standard 3D format)
Chem.MolToPDBFile(molecule_with_h, "aspirin.pdb")

print("Success! Your 3D molecule is saved as aspirin.pdb")