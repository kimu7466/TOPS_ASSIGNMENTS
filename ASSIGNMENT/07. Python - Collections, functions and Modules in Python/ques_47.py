# Q.47 Write a Python function to calculate the factorial of a number.


import math

def calculate_factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    else:
        return math.factorial(n)

number = int(input("Enter a number: "))
print("Factorial of", number, "is:", calculate_factorial(number))
