# Import the sequence and alphabet toolboxes from the Biopython library
import os
import pathlib
from Bio.Seq import Seq
form Bio import SeqIO
import warnings
warnings.filterwarnings("ignore")


# Define an ORF finding function
def orf_finder(seq):
    output = []
    # The function can search the RNA sequence offset by 0, 1 or 2
    for frame in range(3):
        # From the first frame on, the sequence is translated using the translate() method
        for pro in seq[frame:].translate(table).split("*"):
            # Modify the function here:
			# If the protein is longer than 100 amino acids, and it starts with 
			# the starting codon M, record it. Right now it records everything.
            print(str(pro.seq))
            if pro[0] == 'M' and len(pro) > 100:
                output.append(f'{pro[:30]}...{pro[-3:]}')
    return output


if __name__ == "__main__":
    dpath = str(os.path.join(pathlib.Path(__file__).absolute().parent.parent.parent, 'dat/ncbi_dataset/data/GCF_006051015.1'))
    print(pathlib.Path(dpath).exists())
    fpath = os.path.join(dpath, 'GCF_006051015.1_ASM605101v2_genomic.fna')
    # Import the sequence of a bacterial DNA genome (called a plasmid) as a Seq object.
    plasmid = open(fpath).readlines()[1:]
    plasmid = ''.join(plasmid)
    table = 1
    seq = Seq(plasmid)

    orfs = orf_finder(seq)

for i in range(25):
    print("ORF ",i+1, " ",orfs[i])
