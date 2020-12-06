def is_armstrong_number(number):
    
    # convert number to string
    number_string = str(number)

    # get the number of digits in number
    number_of_digits = len(number_string)

    # initialize armstrong number
    armstrong_num = 0

    # loop through each digit and raise the number to the power of the number of digits and sum
    for n in number_string:
        armstrong_num = armstrong_num + int(n)**number_of_digits

    # final check to see if it's an armstrong number and return correct value
    if armstrong_num == number:
        return True
    else:
        return False


