seq1 = 'TCTGCTTTAACTTAT'
seq2 = 'AGTGCGCTGACCTAC'
gdh_seq = gdh = 'AUGGAUCAGACAUAUUCUCUGGAGUCAUUCCUCAACCAUGUCCAAAAGCGCGACCCGAAUCAAACCGAGUUCGCGCAAGCCGUUCGUGAAGUAAUGACCACACUCUGGCCUUUUCUUGAACAAAAUCCAAAAUAUCGCCAGAUGUCAUUACUGGAGCGUCUGGUUGAACCGGAGCGCGUGAUCCAGUUUCGCGUGGUAUGGGUUGAUGAUCGCAACCAGAUACAGGUCAACCGUGCAUGGCGUGUGCAGUUCAGCUCUGCCAUCGGCCCGUACAAAGGCGGUAUGCGCUUCCAUCCGUCAGUUAACCUUUCCAUUCUCAAAUUCCUCGGCUUUGAACAAACCUUCAAAAAUGCCCUGACUACUCUGCCGAUGGGCGGUGGUAAAGGCGGCAGCGAUUUCGAUCCGAAAGGAAAAAGCGAAGGUGAAGUGAUGCGUUUUUGCCAGGCGCUGAUGACUGAACUGUAUCGCCACCUGGGCGCGGAUACCGACGUUCCGGCAGGUGAUAUCGGGGUUGGUGGUCGUGAAGUCGGCUUUAUGGCGGGGAUGAUGAAAAAGCUCUCCAACAAUACCGCCUGCGUCUUCACCGGUAAGGGCCUUUCAUUUGGCGGCAGUCUUAUUCGCCCGGAAGCUACCGGCUACGGUCUGGUUUAUUUCACAGAAGCAAUGCUAAAACGCCACGGUAUGGGUUUUGAAGGGAUGCGCGUUUCCGUUUCUGGCUCCGGCAACGUCGCCCAGUACGCUAUCGAAAAAGCGAUGGAAUUUGGUGCUCGUGUGAUCACUGCGUCAGACUCCAGCGGCACUGUAGUUGAUGAAAGCGGAUUCACGAAAGAGAAACUGGCACGUCUUAUCGAAAUCAAAGCCAGCCGCGAUGGUCGAGUGGCAGAUUACGCCAAAGAAUUUGGUCUGGUCUAUCUCGAAGGCCAACAGCCGUGGUCUCUACCGGUUGAUAUCGCCCUGCCUUGCGCCACCCAGAAUGAACUGGAUGUUGACGCCGCGCAUCAGCUUAUCGCUAAUGGCGUUAAAGCCGUCGCCGAAGGGGCAAAUAUGCCGACCACCAUCGAAGCGACUGAACUGUUCCAGCAGGCAGGCGUACUAUUUGCACCGGGUAAAGCGGCUAAUGCUGGUGGCGUCGCUACAUCGGGCCUGGAAAUGGCACAAAACGCUGCGCGCCUGGGCUGGAAAGCCGAGAAAGUUGACGCACGUUUGCAUCACAUCAUGCUGGAUAUCCACCAUGCCUGUGUUGAGCAUGGUGGUGAAGGUGAGCAAACCAACUACGUGCAGGGCGCGAACAUUGCCGGUUUUGUGAAGGUUGCCGAUGCGAUGCUGGCGCAGGGUGUGAUUUAA'



# A function that translates DNA into a protein sequence.
def translate(DNA):
    # A python dictionary data structure to translate.
    dna_to_pro = {'ATG': 'M', 'GCG': 'A', 'TCA': 'S', 'GAA': 'E', 'GGG': 'G', 'GGT': 'G', 'AAA': 'K', 'GAG': 'E', 'AAT': 'N', 'CTA': 'L', 
                  'CAT': 'H', 'TCG': 'S', 'TAG': 'STOP', 'GTG': 'V', 'TAT': 'Y', 'CCT': 'P', 'ACT': 'T', 'TCC': 's', 'CAG': 'Q', 'CCA': 'P', 
                  'TAA': 'STOP', 'AGA': 'R', 'ACG': 'T', 'CAA': 'Q', 'TGT': 'C', 'GCT': 'A', 'TTC': 'F', 'AGT': 'S', 'ATA': 'I', 'TTA': 'L', 
                  'CCG': 'P', 'ATC': 'I', 'TTT': 'F', 'CGT': 'R', 'TGA': 'STOP', 'GTA': 'V', 'TCT': 'S', 'CAC': 'H', 'GTT': 'V', 'GAT': 'D', 
                  'CGA': 'R', 'GGA': 'G', 'GTC': 'V', 'GGC': 'G', 'TGC': 'C', 'CTG': 'L', 'CTC': 'L', 'CGC': 'R', 'CGG': 'R', 'AAC': 'N', 
                  'GCC': 'A', 'ATT': 'I', 'AGG': 'R', 'GAC': 'D', 'ACC': 'T', 'AGC': 'S', 'TAC': 'Y', 'ACA': 'T', 'AAG': 'K', 'GCA': 'A', 
                  'TTG': 'L', 'CCC': 'P', 'CTT': 'L', 'TGG': 'W'}
    protein = []
    start = 0
    # Step through the DNA sequence and translate.
    while start + 2 < len(DNA):
        codon = DNA[start:start + 3]
        protein.append(dna_to_pro[codon])
        start += 3
    return ''.join(protein)


def rna_translate(RNA):
    # A python dictionary data structure to translate.
    rna_to_pro = {'AUG': 'M', 'GCG': 'A', 'UCA': 'S', 'GAA': 'E', 'GGG': 'G', 'GGU': 'G', 'AAA': 'K', 'GAG': 'E', 'AAU': 'N', 'CUA': 'L', 'CAU': 'H', 'UCG': 'S', 'UAG': 'STOP', 'GUG': 'V', 'UAU': 'Y', 'CCU': 'P', 'ACU': 'T', 'UCC': 's', 'CAG': 'Q', 'CCA': 'P', 'UAA': 'STOP', 'AGA': 'R', 'ACG': 'T', 'CAA': 'Q', 'UGU': 'C', 'GCU': 'A', 'UUC': 'F', 'AGU': 'S', 'AUA': 'I', 'UUA': 'L', 'CCG': 'P', 'AUC': 'I', 'UUU': 'F', 'CGU': 'R', 'UGA': 'STOP', 'GUA': 'V', 'UCU': 'S', 'CAC': 'H', 'GUU': 'V', 'GAU': 'D', 'CGA': 'R', 'GGA': 'G', 'GUC': 'V', 'GGC': 'G', 'UGC': 'C', 'CUG': 'L', 'CUC': 'L', 'CGC': 'R', 'CGG': 'R', 'AAC': 'N', 'GCC': 'A', 'AUU': 'I', 'AGG': 'R', 'GAC': 'D', 'ACC': 'T', 'AGC': 'S', 'UAC': 'Y', 'ACA': 'T', 'AAG': 'K', 'GCA': 'A', 'UUG': 'L', 'CCC': 'P', 'CUU': 'L', 'UGG': 'W'}
    protein = []
    start = 0
    # Step through the DNA sequence and translate.
    while start + 2 < len(RNA):
        codon = RNA[start:start + 3]
        protein.append(rna_to_pro[codon])
        start += 3
    return ''.join(protein)

# Print the translated sequences.
print("Seq1: ", seq1, "Translated: ", translate(seq1))
print("Seq2: ", seq2, "Translated: ", translate(seq2))
print("Seq2: ", gdh_seq, "Translated: ", rna_translate(gdh_seq))
