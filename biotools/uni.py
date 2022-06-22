# modules and functions
import sys


# functions

def validate(seq: str, seq_type: str) -> bool:
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
        print('[ERROR] Wrong seq_type. Please input \'DNA\', \'RNA\', \'PROT\' or \'PROTEIN\'')
        return False
    if len(seq) > 0:
        for nuc in seq.upper():
            try:
                assert nuc in code
            except AssertionError:
                print(f'[ERROR] Not a valid {seq_type.upper()} sequence.')
                return False
        return True
    else:
        print('[ERROR] Empty sequence string...')
        return False


def is_fasta(dir: str, seq_type: 'str') -> bool:
    """
    Check if the file is in FASTA format.

    :param dir: working file directory
    :param seq_type: input 'DNA', 'RNA, 'PROT' or 'PROTEIN'
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
        print('[ERROR] File does not contain headers. Not a valid FASTA file.')
        sys.exit()
    seq = ''.join(lines).replace('\n', '')
    seq_type = seq_type.upper()
    return validate(seq, seq_type)


def read_fasta(dir: str, seq_type: str) -> dict:
    """
    Allows to read FASTA files containing one or more sequences (headers).

    :param dir: working file directory
    :param seq_type: input 'DNA', 'RNA', 'PROT' or 'PROTEIN'
    :return: dictionary in {header: sequence} format
    """
    if is_fasta(dir, seq_type):
        with open(dir, 'r+') as f:
            lines = f.readlines()
        headers = []
        seqs = ''
        for line in lines:
            if line.startswith('>'):
                line = line.replace('\n', '')
                if line not in headers:
                    headers.append(line)
                else:
                    print('[ERROR] Identical headers found!')
                    sys.exit()
                if len(seqs) > 0:
                    seqs += ';'
            else:
                seqs += (line.replace('\n', ''))
        seqs = seqs.split(sep=';')
        return {headers[i]: seqs[i] for i in range(len(headers))}
