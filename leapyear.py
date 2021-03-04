def leapyear(val):
    if (val % 4) == 0:
        if (val % 100) == 0:
            if (val % 400) == 0:
                return "{0} is a leap year".format(val)
            else:
                return "{0} is not a leap year".format(val)
        else:
            return "{0} is a leap year".format(val)
    else:
        return "{0} is not a leap year".format(val)

def getInput():
    while True:
        yr = input("Enter a year: ")
        try:
            val = int(yr)
            return val
        except ValueError:
            print("Please enter an integer.")

val = getInput()
print(leapyear(val))