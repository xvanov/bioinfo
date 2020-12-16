import random
import string

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




if __name__ == '__main__':
    N = 100
    A = '01'
    R = get_random_string(100, A)
    P = '01'
    patternCount = pattern_count(R,P)
    print(patternCount)

