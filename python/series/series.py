def slices(series, length):
    if not (0 < length <= len(series)):
        raise ValueError("Invalid")
    return([series[i:length+i] for i in range(len(series)) if i <= len(series)-length])

