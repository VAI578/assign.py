       
# Task 1: Calculate Factorial Using a Function

def factorial(n):
    """Function to calculate factorial using a loop"""
    if n < 0:
        return "Factorial is not defined for negative numbers"
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


num = 5
print("Factorial of", num, "is:", factorial(num))

# task 2
# Task 2: Using the Math Module for Calculations

import math

try:
    # Taking input from user
    num = float(input("Enter a number: "))

    if num < 0:
        print("Square root and logarithm are not defined for negative numbers.")
    else:
        # Calculations
        square_root = math.sqrt(num)
        logarithm = math.log(num)
        sine_value = math.sin(num)

        # Display results
        print("\nResults:")
        print("Square Root:", square_root)
        print("Natural Logarithm (log base e):", logarithm)
        print("Sine (in radians):", sine_value)

except ValueError:
    print("Invalid input! Please enter a valid number.")


