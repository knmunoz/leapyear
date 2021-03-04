def leapyear(val):
    pass

def getInput():
    while True:
        yr = input("Enter a year: ")
        try:
            val = int(yr)
            return val
        except ValueError:
            print("Please enter an integer.")

val = getInput()
leapyear(val)