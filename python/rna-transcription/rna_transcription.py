def to_rna(dna_strand):
    
    transcription = { "C" : "G", \
                      "G" : "C", \
                      "T" : "A", \
                      "A" : "U"}

    rna_strand = ''

    for letter in dna_strand:
        rna_strand += transcription[letter]

    return rna_strand
