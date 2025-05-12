from Bio.Seq import Seq

# Sample DNA
dna_seq = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")

# Translate
protein_seq = dna_seq.translate()

print("DNA Sequence:", dna_seq)
print("Protein Sequence:", protein_seq)
