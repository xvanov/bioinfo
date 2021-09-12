# Import the sequence from the Biopython library
from Bio.Seq import *

def complement(seq):
    comp_seq=""
    mapping =  {'A':'T', "C":"G", "G":"C", "T":"A"}
    for nucleotide in gene:
        comp_seq += mapping[nucleotide]
    return comp_seq;

def reverse(seq):
    rev_seq = seq[::-1]
    return rev_seq

if __name__ == '__main__':
    gene = "TCAGACTGGTGCCGTGGTGCTCTCGCCCGATGTGACGTCGACCGCCAGCGGCGCGATGACGCCGAGGATTTCCGTGATCGTTTCGGAGGGCACGCCGGCTGCGGTCAGCGCGTCGGCCAAGTGTCCGGCGACCAGGCTGAAGTGGTGCATGGTAATTCCGCGCCCCTGATGGACTTGCTTCATCGGCGCACCGGTATAGGGCTCGGGCCCGCCAAGCGCGGCCGCGAAAAACTCCACCTGCTTGCCCTTGAGGCGGCTCATGTTCGTACCGCTGAAGAAGGCCGATAGTTGGTCATCGGCAAGCACACGAACATAGAAGTCCTCGACGACGACTTCGATGGCCTCATGCCCGCCGATCTTGTCGTAGATGCTGATCGGCTCACGTTTGCGCAAGCGTGACAGTAGTCCCATTTTTATA"
    res = reverse(complement(gene))
    print(res)
    # Define a sequence as a DNA Seq object
    seq = Seq("CCTCAGCGAGGACAGCAAGGGACTAGCC")

    # The complement() method can act just like your complement() function.
    complement = seq.complement()
    # Similarly, we can use the reverse_complement() method.
    reverse_complement = seq.reverse_complement()
    # We can even use the transcribe() method to switch alphabets to RNA
    RNA = seq.transcribe()
    print(RNA)
