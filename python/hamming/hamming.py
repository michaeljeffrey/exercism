def distance(strand_a, strand_b):

    if len(strand_a) != len(strand_b):
        raise ValueError("Length of strands are different")

    x = zip(strand_a, strand_b)

    return(sum([i[0] != i[1] for i in tuple(x)]))
