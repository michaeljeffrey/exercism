def is_valid(isbn):
    # (x1 * 10 + x2 * 9 + x3 * 8 + x4 * 7 + x5 * 6 + x6 * 5 + x7 * 4 + x8 * 3 + x9 * 2 + x10 * 1) mod 11 == 0
  
    valid = ['1','2','3','4','5','6','7','8','9','0','X'] # valids
    
    i = list(filter(lambda x: (x in valid), list(isbn))) # filter out all but valids
    
    if len(i) != 10: # only 10 is a valid isbn
        return False 
    elif 'X' in [i[x] for x in range(0,9)]: # check to make sure X isn't non-last
        return False
    else: # flip X to 10 if it's there
        if i[9] == 'X':
            i[9] = '10'

    # apply the forumula
    i_formula = int(i[0]) * 10 + int(i[1]) * 9 + int(i[2]) * 8 + int(i[3]) * 7 + \
        int(i[4]) * 6 + int(i[5]) * 5 + int(i[6]) * 4 + int(i[7]) * 3 + \
        int(i[8]) * 2 + int(i[9]) * 1
    
    # mod 11 check
    if i_formula % 11 == 0:
        return True
    else: 
        return False