# modules and functions
import sys
from typing import Union


# functions

def is_nucleic(seq: str, acid: str) -> Union[bool, str]:
    """
    Checks if given string is DNA/RNA sequence.

    :param seq: input sequence string
    :param acid: input 'DNA' or 'RNA'
    :returns:
    False if given str is not a DNA/RNA sequence,
    'DNA' if str is DNA sequence,
    'RNA' if str is RNA sequence
    """
    if acid.upper() == 'DNA':
        code = ('A', 'T', 'G', 'C')
    elif acid.upper() == 'RNA':
        code = ('A', 'U', 'G', 'C')
    else:
        print('Wrong acid type. Please input \'DNA\' or \'RNA\'')
        return False

    for nuc in seq.upper():
        try:
            assert nuc in code
        except AssertionError:
            print(f'Not a valid {acid.upper()} sequence.')
            return False
    return f'{acid.upper()}'


def nuc_freq(seq: str, acid: str) -> dict:
    """
    Counts how many of A, T, C, G nucleotides are in the sequence.

    :param seq: input sequence string
    :param acid: input 'DNA' or 'RNA'
    :returns: dictionary with counted nucleotides
    """
    count = {"A": 0, "T": 0, "C": 0, "G": 0}
    if is_nucleic(seq, acid):
        for nuc in seq.upper():
            count[nuc] += 1
    else:
        print(f'Not a valid {acid.upper()} sequence.')
        sys.exit()
    return count


def trans(seq: str) -> str:
    """
    Transcribes DNA to RNA.

    :param seq: input DNA sequence string
    :returns: RNA sequence
    """
    if is_nucleic(seq, 'dna') == 'DNA':
        return seq.upper().replace('T', 'U')


def reverse(seq: str, acid: str) -> str:
    """
    Reverse DNA/RNA sequence.

    :param seq: input sequence string
    :param acid: input 'DNA' or 'RNA'
    :returns: reversed sequence
    """
    if is_nucleic(seq, acid):
        ls = list(reversed(seq.upper()))
        return ''.join(ls)


def complement(seq: str, acid: str) -> str:
    """
    Complement DNA/RNA sequence.

    :param seq: input sequence string
    :param acid: input 'DNA' or 'RNA'
    :returns: complementary sequence
    """
    code = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C', 'U': 'A'}
    cseq = ''
    if is_nucleic(seq, acid):
        for nuc in seq.upper():
            cseq += code[nuc]
    return cseq
