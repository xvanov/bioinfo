#!/usr/bin/env python3


# Import the sequence and alphabet toolboxes from the Biopython library
from Bio.Seq import Seq

# Define a sequence as a DNA Seq object
seq = Seq("CCTCAGCGAGGACAGCAAGGGACTAGCC")

complement = seq.complement()
reverse_complement = seq.reverse_complement()
RNA = seq.transcribe()

print(seq)
print(complement)
print(reverse_complement)
print(RNA)
