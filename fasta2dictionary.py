#python3

def fasta_dictionary(infile):

    dict = {}
    headers, sequences = '', ''

    lines = infile.read().splitlines()
    for f in lines:
        if f.startswith(">"):
            count = 0
            headers = f
        else:
            count += 1
            if count == 1:
                sequences = f
            else:
                sequences = sequences + f
        dict[headers] = sequences
    return dict
