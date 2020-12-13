import os,sys,inspect
import pytest
import re

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
from src.string_probabilities import *

def test_get_random_string():
    length = 100
    alphabet = '01'
    randomString = get_random_string(length, alphabet)
    assert len(randomString) == length
    matches = re.findall(r'[^01]', randomString)
    assert len(matches) == 0

@pytest.mark.parametrize("text, pattern, expected",
                         [('ACAACTATGCATACTATCGGGAACTATCCT','ACTAT', 3),
                          ('ACTGACTCCCACCCC','CCC',3)])
def test_pattern_count(text, pattern, expected):
    count = pattern_count(text, pattern)
    assert count == expected


def test_frequent_words():
    text = 'ACTGACTCCCACCCC'
    k = 3
    patterns, maxCount = frequent_words(text, k)
    print(patterns)
    print(maxCount)
    assert patterns == ['CCC']
    assert maxCount == 3


