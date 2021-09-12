import pathlib
import os

def length(string):
    length = 0;
    # Make a function here that counts the number of nucleotides in the input 
    # sequence, return as variable "length".
    length = len(string)
    a = string.count('A')
    t = string.count('T')
    c = string.count('C')
    g = string.count('G')
    print(f"length: {length}")
    print(f"A: {a}, {a/length}")
    print(f"T: {t}, {t/length}")
    print(f"C: {c}, {c/length}")
    print(f"G: {g}, {g/length}")
    return length

if __name__ == '__main__':
    test_sequence = "ACAACATACAAAGGGCCACAGATACATCAAAAAATGCTCAACATCACTATTTGTCAGGGAAGTACTAATTAAAACCAAAATGAGATGTCCCCTCAAACCTGTTAGAATGGCTATTATCAAAAAGATGAAAGATAGCAACTATCAGAGAGGATGATAGAAAAGGGAACCCTTGCATCATGTACAAATTAAAAATAGAACTATCACATGATCCAAGAATCCTACTTCTGGGTATATAGCCAAAGGAATTGAAATCAATATGTCAAAGGGATATCTGCACTCCTATGTTATTGCAGCATGTTCACAATGGCCAAGATATAGAATCAACCTAACTGTTCATAGACAGATGAATGGATAAATGAAATGTGATATGGAAAATTATTCAGCCTTAAAAACAGTAGGAAATTCTGTCATTTGAGACAACGTGGATGAACCTAGAGGACATTAAGCTAAGTGAAATAAGCTAGACACAGAAAGACAAATATTGCATGATCTCACTTAGAATCTAAAAAATCTGAACTCATAGAAGCAGAGAATAGTATGATGGTTACTAGGGTTATCTGGCAGGGAGAGGATGAGGAAATGGGACATTGTTAATAAAAGGAAAAAAATTCAATTAGTAGG"
    #print(length(test_sequence))
    dpath = str(os.path.join(pathlib.Path(__file__).parent.absolute().parent, 'data'))
    files = [os.path.join(dpath, f) for f in os.listdir(dpath) if os.path.isfile(os.path.join(dpath, f))]
    for f in files:
        print(f)
        seq = open(f).readlines()[1:]
        seq = ''.join(seq)
        length(seq)

