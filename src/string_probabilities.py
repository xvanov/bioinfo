import os, sys, inspect
import random
import string


currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
from src.dicts import *

def get_random_string(length, alphabet):
    """get_random_string returns random string of length using any character passed into alphabet

    Parameters
    ----------
    length :
        str
    alphabet :
        str

    Returns
        str result
    """
    result = ''.join(random.choice(alphabet) for i in range(length))
    return result

def pattern_count(text, pattern):
    """pattern_count returns number of occurences of pattern (substring) in text (string)

    Parameters
    ----------
    text :
        str
    pattern :
        str
    """
    count = 0
    T = len(text)
    P = len(pattern)
    for i in range(T-P+1):
        if text[i:i+P] == pattern:
            count+=1
    return count


def frequent_words(text, k):
    """frequent_words. Naive implementation of finding most frequent substring in string O(k*|Text|^2)

    Parameters
    ----------
    text :
        str
    k :
        int

    Returns
    -------
    list of most frequent pattern(s) in text
    """
    # TODO: improve implementation to reduce algorithmic complexity

    frequentPatterns = []
    count = []
    T = len(text)
    for i in range(T-k+1):
        pattern = text[i:i+k]
        count.append(pattern_count(text,pattern))
    maxCount = max(count)
    for i in range(T-k+1):
        if count[i]==maxCount:
            frequentPatterns.append(text[i:i+k])
    frequentPatterns = list(dict.fromkeys(frequentPatterns))
    return frequentPatterns, maxCount


def frequency_of_nucleotides(string):
    if string == '':
        return None
    else:
        length = [0,0,0,0]
        ll = len(string)
        length[0] = string.count('T')/ll
        length[1] = string.count('A')/ll
        length[2] = string.count('G')/ll
        length[3] = string.count('C')/ll
        return length;


def find_promoter(seq, promoter='TATAAAA'):
    if seq[0:7] == promoter:
        return True
    else:
        return False

def reverse_complement(seq):
    comp_seq = complement(seq)
    rev_comp_seq = reverse(comp_seq)
    return rev_comp_seq

def reverse(seq):
    rev_seq = ""
    for i in reversed(seq):
        rev_seq += i
    return rev_seq

def complement(seq):
    comp_seq=""
    for i in seq:
        if i == 'T':
            comp_seq +='A'
        elif i == 'A':
            comp_seq += 'T'
        elif i == 'G':
            comp_seq += 'C'
        else:
            comp_seq += 'G'
    return comp_seq;


def translate(rna):
    protein=[]
    for i in range(int(len(rna)/3)):
        protein.append(codon_to_AA[rna[3*i:3*i+3]])

    return protein



if __name__ == '__main__':
    N = 100
    A = '01'
    R = get_random_string(100, A)
    P = '01'
    patternCount = pattern_count(R,P)
    print(patternCount)

