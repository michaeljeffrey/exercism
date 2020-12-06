# trying to write this DRY-ly

def convert(number):
    '''convert number to sounds if evenly divisible by certain values'''
    # mod values and sounds
    ppp = [(3, 'Pling'),(5, 'Plang'),(7, 'Plong')]
    
    # init variable
    string = ''

    # loop and append sound to string
    for p in ppp:
        # print(p) 
        string += mod_me(number, *p)

    # final check to see if loop above appended nothing
    if not string:
        string = str(number)
    return string


def mod_me(number, mod, sound):
    ''' check number if mod is zero and return sound or empty string'''
    if number % mod == 0:
        return sound 
    else:
        return ''