def slices(series, length):
    #       self.assertEqual(slices("9142", 2), ["91", "14", "42"])
    #   slice(start, stop, step)

    print(series, length)

    n = 0
    strings = []

    for n in range(0, len(series)):
        print("loop", n)
        string = ""
        sObject = slice(n, n + length)
        print(sObject)
        print()
        if len(series[sObject]) == length:
            strings.append(series[sObject])
        
    return strings

# print(slices("9142", 2))