import os
from rdkit import Chem
from rdkit.Chem import AllChem

def make_aspirin_pdbqt():
    # 1. Create Aspirin molecule
    smiles = 'CC(=O)OC1=CC=CC=C1C(=O)O'
    mol = Chem.MolFromSmiles(smiles)
    mol = Chem.AddHs(mol)
    
    # 2. Generate 3D coordinates
    AllChem.EmbedMolecule(mol, AllChem.ETKDG())
    
    # 3. Create the file path
    file_path = "aspirin.pdbqt"
    
    # 4. Write the file in the exact format Vina wants
    with open(file_path, "w") as f:
        # PDBQT header for Vina
        f.write("REMARK  Name = Aspirin\n")
        f.write("ROOT\n")
        for i, atom in enumerate(mol.GetAtoms()):
            pos = mol.GetConformer().GetAtomPosition(i)
            # This is the strict PDBQT spacing Vina requires
            f.write(f"HETATM {i+1:>4} {atom.GetSymbol():<2}  UNL     1    {pos.x:>8.3f}{pos.y:>8.3f}{pos.z:>8.3f}  1.00  0.00          {atom.GetSymbol()}\n")
        f.write("ENDROOT\n")
        f.write("TORSDOF 0\n")
    
    if os.path.exists(file_path):
        print(f"SUCCESS: {file_path} created with size {os.path.getsize(file_path)} bytes.")
    else:
        print("ERROR: File was not created.")

if __name__ == "__main__":
    make_aspirin_pdbqt()