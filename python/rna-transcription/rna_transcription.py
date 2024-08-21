def to_rna(dna_strand):
    rna_strand = ""
    dna_rna_conversion = {'G':'C', 'C':'G', 'T':'A', 'A':'U'}
    for c in dna_strand:
        rna_strand += dna_rna_conversion[c]
    return rna_strand
