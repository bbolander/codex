
import sys

def collatz(number):
    if number % 2 == 0:
        number = number // 2
        print str(number)
        return number
    else:
        number = number * 3 + 1
        print str(number)
        return number

while True:
    try:
        number = int(input("Please enter a number: "))
        break
    #except (ValueError, RuntimeError, TypeError, NameError):
    except (TypeError):
        print "Value needs to be a number."

while number != 1:
    number = collatz(number)
