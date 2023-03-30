"""
Define a method which returns the square of the given number if it is an even, 
return cube of the given number if it is an odd number.

CONDITIONS:
if the given number is negative or zero, return -1.
if the given number is even, return square of the number.
if the given number is odd, return cube of the given number.
"""


def calculate(number):
    if number <=0:
        return -1
    elif number%2==0:
        return number**2
    else:
        return number**3
try:
    user_input = int(input("Enter an Integer Number: "))
except:
    print("Please Enter Integer Only!")
else:
    print(calculate(user_input))
