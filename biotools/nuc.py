# modules and functions
import sys
import biotools.uni as u


# functions


def nuc_freq(seq: str, seq_type: str) -> dict:
    """
    Counts how many of A, T, C, G nucleotides are in the sequence.

    :param seq: input sequence string
    :param seq_type: input 'DNA' or 'RNA'
    :returns: dictionary with counted nucleotides
    """
    count = {"A": 0, "T": 0, "C": 0, "G": 0}
    if u.validator(seq, seq_type):
        for nuc in seq.upper():
            count[nuc] += 1
    else:
        print(f'Not a valid {seq_type.upper()} sequence.')
        sys.exit()
    return count


def trans(seq: str) -> str:
    """
    Transcribes DNA to RNA.

    :param seq: input DNA sequence string
    :returns: RNA sequence
    """
    if u.validator(seq, 'dna') == 'DNA':
        return seq.upper().replace('T', 'U')


def reverse(seq: str, seq_type: str) -> str:
    """
    Reverse DNA/RNA sequence.

    :param seq: input sequence string
    :param seq_type: input 'DNA' or 'RNA'
    :returns: reversed sequence
    """
    if u.validator(seq, seq_type):
        ls = list(reversed(seq.upper()))
        return ''.join(ls)


def complement(seq: str, seq_type: str) -> str:
    """
    Complement DNA/RNA sequence.

    :param seq: input sequence string
    :param seq_type: input 'DNA' or 'RNA'
    :returns: complementary sequence
    """
    code = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C', 'U': 'A'}
    cseq = ''
    if u.validator(seq, seq_type):
        for nuc in seq.upper():
            cseq += code[nuc]
    return cseq
