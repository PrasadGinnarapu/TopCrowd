"""
Write a program that iterates the integers from 1 to 100. 
But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". 
For numbers that are multiples of both three and five print "FizzBuzz".
"""

def fizz_buzz():
    """
    This function prints "Fizz" for all the 3 multiples,
    prints "Buzz" for all the 5 multiples,
    prints "FizzBuzz" for all the 3 and 5 multiples.
    """
    for digit in range(1,101):
        if (digit % 3 == 0 and digit % 5==0):
            print("FizzBuzz")
        elif digit % 5 == 0:
            print("Buzz")
        elif digit % 3 == 0:
            print("Fizz")
        else:
            continue
fizz_buzz()