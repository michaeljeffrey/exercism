def distance(strand_a, strand_b):

    if len(strand_a) != len(strand_b):
        raise ValueError("Length of strands are different")

    n = 0
    distance = 0

    while n < len_a:
        if strand_a[n] != strand_b[n]:
            distance += 1
        n += 1
    return distance
