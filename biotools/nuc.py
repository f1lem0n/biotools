# modules and functions
import sys

import biotools.uni as uni


# functions


def nuc_freq(seq: str, seq_type: str) -> dict:
    """
    Counts how many of A, T, C, G nucleotides are in the sequence.

    :param seq: input sequence string
    :param seq_type: input 'DNA' or 'RNA'
    :returns: dictionary with counted nucleotides
    """
    count = {"A": 0, "T": 0, "C": 0, "G": 0}
    if uni.validate(seq, seq_type):
        for nuc in seq.upper():
            count[nuc] += 1
    else:
        print(f'[ERROR] Not a valid {seq_type.upper()} sequence.')
        sys.exit()
    return count


def trans(seq: str) -> str:
    """
    Transcribes DNA to RNA.

    :param seq: input DNA sequence string
    :returns: RNA sequence
    """
    if uni.validate(seq, 'dna') == 'DNA':
        return seq.upper().replace('T', 'U')


def reverse(seq: str, seq_type: str) -> str:
    """
    Reverse DNA/RNA sequence.

    :param seq: input sequence string
    :param seq_type: input 'DNA' or 'RNA'
    :returns: reversed sequence
    """
    if uni.validate(seq, seq_type):
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
    if uni.validate(seq, seq_type):
        for nuc in seq.upper():
            cseq += code[nuc]
    return cseq


def gc_content(seq: str) -> float:
    """
    Get GC content in DNA/RNA sequence.

    :param seq: input sequence string
    :return: ratio of GC pairs to all pairs
    """
    seq = seq.upper()
    if uni.validate(seq, 'DNA') or uni.validate(seq, 'RNA'):
        gc = seq.count('G') + seq.count('C')
        return gc / len(seq)
    else:
        print('[ERROR] Not a valid sequence.')
        sys.exit()


def pmc(seq1: str, seq2: str, mode: str, print_output: bool = False) -> int:
    """
    Point mutation counter.

    :param seq1: first sequence
    :param seq2: second sequence
    :param mode: 'ignore indels' or 'best match'
    :param print_output: print compared sequences (default: False)
    :return: number of point mutations
    """

    def output(seq1, seq2, matches, count):
        print(
            '-------------------------\n' +
            f'point mutation count: {count}\n' +
            '-------------------------\n'
        )
        previouslen = 0
        while min(len(seq1), len(seq2)):
            matcheslen = len(matches[:20])
            print(
                seq1[:20] + '\n' +
                f'{matches[:20]:22}{matcheslen + previouslen}' + '\n' +
                seq2[:20]
            )
            previouslen += 20
            seq1, seq2, matches = seq1[20:], seq2[20:], matches[20:]

    if mode == 'ignore indels':
        count = 0
        matches = ''
        for i in range(min(len(seq1), len(seq2))):
            if seq1[i] != seq2[i]:
                count += 1
                matches += ' '
            else:
                matches += '|'
        if print_output:
            output(seq1, seq2, matches, count)
        return count

    elif mode == 'best match':
        print('i am too stupid yet')
        if print_output:
            output(seq1, seq2, matches='', count=0)
