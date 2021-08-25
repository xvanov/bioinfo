def seq_diff(seq1, seq2, dont_count=['_']):
    """
    return number of characters that are in common
    and different between 2 strings
    doesn't count defined characters
    :param seq1: string 1
    :param seq2: string 2
    :return common, diff: number of common characters
    and different characters
    """
    seq1 = seq1.replace(" ", "")
    seq2 = seq2.replace(" ", "")
    l1, l2 = list(seq1), list(seq2)
    n1, n2 = len(l1), len(l2)
    assert n1 == n2
    common = 0
    diff = 0
    for i in range(n1):
        if l1[i] in dont_count:
            if l2[i] not in dont_count:
                print(i, l1, l2)
            assert l2[i] == l1[i]
        elif l1[i] == l2[i]:
            common += 1
        else:
            diff += 1
    return common, diff

def compare_one_to_many(original, compare_to):
    """
    compares one sequence to many finding in common and different characters
    :param original: string to compare to
    :param compare_to: list of strings to compare original to
    :return results: dictionary of tuples with number in common and number different
    """
    original_k = list(original.items())[0][0]
    original_v = list(original.items())[0][1]
    results = {}
    for k, v in compare_to.items():
        print(k)
        com, dif = seq_diff(original_v, v, dont_count=[])
        results[k] = (com, dif)
    results = {k: v for k, v in sorted(results.items(), key=lambda item: item[1][0])}
    return results


if __name__ == '__main__':
    # single comparison
    aphid = 'IKIIIIGSGV  GGTAAAARLS  KKGFQVEVYE  KNSYNGGRCS  IIR_HNGHRF  DQGPSL__YL'
    bacte = 'KRTFVIGAGF  GGLALAIRLQ  AAGIATTVLE  QHDKPGGRAY  VWQ_DQGFTF  DAGPTV__IT'
    common, diff = seq_diff(aphid, bacte)
    print(f"common: {common}")
    print(f"different: {diff}")

    # multiple comparisons
    original = {'Acyrthosiphon':    'IKIIIIGSGV GGTAAAARLS KKGFQVEVYE KNSYNGGRCS IIR_HNGHRF DQHPSL__YL'}
    compare_to = {
        'Pantoea':                  'KRTFVIGAGF GGLALAIRLQ AAGIATTVLE QHDKPGGRAY VWQ_DQGFTF DAGPTV__IT',
        'Staphylococcus':           'MKIAVIGAGV TGLAAAARIA SQGHEVTIFE KNNNVGGRMN QLK_KDGFTF DMGPTI__VM',
        'Ustilago':                 'KKVVIIGAGA GGTALAARLG RRGYSVTVLE KNSFGGGRCS LIH_HDGHRW DQGPSL__YL',
        'Gibberella':               'KSVIVIGAGV GGVSTAARLA KAGFKVTILE KNDFTGGRCS LIH_NDGHRF DQGPSL__LL',
        'Arabidopsis':              'WDAVVIGGGH NGLTAAAYLA RGGLSVAVLE RRHVIGGAAV TEEIVPGFKF SRCSYLQGLL'}

    results = compare_one_to_many(original, compare_to)
    print(f"results:\n{results}")
