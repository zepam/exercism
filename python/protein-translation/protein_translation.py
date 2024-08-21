def proteins(strand):

    RNA = {
        'Methionine': ('AUG'),
        'Phenylalanine': ('UUU', 'UUC'),
        'Leucine': ('UUA', 'UUG'),
        'Serine': ('UCU', 'UCC', 'UCA', 'UCG'),
        'Tyrosine': ('UAU', 'UAC'),
        'Cysteine': ('UGU', 'UGC'),
        'Tryptophan': ('UGG'),
        'stop_sequence': ('UAA', 'UAG', 'UGA')
    }

    STEPS = 3   # size of codons

    proteins = []   # list of all proteins in sequence before stop
    codon_list = [strand[i:i+STEPS] for i in range(0, len(strand), STEPS)]

    for c in codon_list:
        if c in RNA['stop_sequence']:   # find a stop codon
            break
        for k, v in RNA.items():        # find key and value in RNA
            if c in v:                  # if the value is in there
                proteins.append(k)      # append the key
    return proteins
