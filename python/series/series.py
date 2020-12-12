def slices(series, length):
    series_length = len(series)
    if not (0 < length <= series_length):
        raise ValueError("Invalid")
    slices = []
    start = 0
    while length <= series_length:
        slices.append(series[start:length])
        start += 1
        length += 1
    return slices
