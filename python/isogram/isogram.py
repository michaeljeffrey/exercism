def is_isogram(phrase):
    
    char_set = set()
    for char in phrase:
        if char.isalpha():
            if char.lower() not in char_set:
                char_set.add(char.lower())
            else:
                return False
    
    return True
