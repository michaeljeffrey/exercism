def is_isogram(phrase):
    
    char_set = set()
    for char in phrase.lower():
        if char.isalpha():
            if char not in char_set:
                char_set.add(char)
            else:
                return False
    
    return True
