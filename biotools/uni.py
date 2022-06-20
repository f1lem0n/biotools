# modules and functions
import sys


# functions

def validator(seq: str, seq_type: str) -> bool:
    """
    Checks if given string is DNA/RNA/PROTEIN sequence.

    :param seq: input sequence string
    :param seq_type: input 'DNA', 'RNA', 'PROT' or 'PROTEIN'
    :returns: False if given str is not a DNA/RNA/PROTEIN sequence, True if given str is a DNA/RNA/PROTEIN sequence
    """
    if seq_type.upper() == 'DNA':
        code = 'ATGC'
    elif seq_type.upper() == 'RNA':
        code = 'AUGC'
    elif seq_type in ('PROT', 'PROTEIN'):
        code = 'ARNDCQEGHILKMFPSTWYVBZ'
    else:
        print('[WARNING] Wrong seq_type. Please input \'DNA\', \'RNA\', \'PROT\' or \'PROTEIN\'')
        return False
    if len(seq) > 0:
        for nuc in seq.upper():
            try:
                assert nuc in code
            except AssertionError:
                print(f'[WARNING] Not a valid {seq_type.upper()} sequence.')
                return False
        return True
    else:
        print('[WARNING] Empty sequence string...')
        return False


def is_fasta(dir: str, seq_type: 'str') -> bool:
    """
    Check if the file is in FASTA format.

    :param dir: working file directory
    :param seq_type: input 'DNA', 'RNA, 'PROTEIN' or 'PROT' for short.
    :return: if the given file is in FASTA format
    """
    with open(str(dir), 'r+') as f:
        lines = f.readlines()
    headers = []
    for line in lines:
        if line.startswith('>'):
            headers.append(line)
            lines.remove(line)

    if len(headers) == 0:
        print('File does not contain headers. Not a valid FASTA file.')
        sys.exit()

    seq = ''.join(lines).replace('\n', '')
    seq_type = seq_type.upper()

    return validator(seq, seq_type)
