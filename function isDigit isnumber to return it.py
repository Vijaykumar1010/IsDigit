# function isDigit isnumber to return it is a digit
def isNumber(number: int):

    isInteger = True # set a flag

    if number.startswith('-'): 
        number = number[1:] # Remove the '-' for checking digits

    for eachcharacter in number:

        if (eachcharacter >='0' and eachcharacter <= '9'):

            continue
        else:
            isInteger = False
        break
    
    return isInteger

# invocation code

result = isNumber('0123')

if result:
    print("Yes it is an integer")

else:
    print("No it is not an integer")
