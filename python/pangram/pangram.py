# improrting string for alphabet list
import string

def is_pangram(sentence):

    # init empty list to populate with letters
    sentence_has = []
    
    # loop through each letter in the sentence
    for letter in sentence:
        # drop the case to lower to make everything homogenous
        lower_letter = letter.lower()
        # loop through each letter and make sure it's a letter
        if lower_letter in string.ascii_lowercase:
            # see if it's not already in the list of letters used
            if lower_letter not in sentence_has:
                # add it to list of existing letters
                sentence_has.append(lower_letter)

    # assuming we're staying with the English alphabet, see if there are 26 chars
    if len(sentence_has) == 26:
        return True
    else:
        return False