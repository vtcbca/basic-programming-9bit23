import math

def factorial_builtin(n):
    return math.factorial(n)

number = int(input("Enter a number: "))
print(f"The factorial of {number} is {factorial_builtin(number)}")
