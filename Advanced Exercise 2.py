# -------------------------------------------
# Advanced Python Challenge: Exercise 02 Operators and Conditionals
# -------------------------------------------

# Overview:
# This exercise challenges your understanding of Python operators, conditionals, and input handling.
# Complete each section with the required logic, using good variable names and adding comments where necessary.

# -------------------------------------------
# Question 1: Multi-Step Arithmetic Operations
# -------------------------------------------

# Task:
# Use compound arithmetic operators to modify values of a, b, and c.
# Then calculate the square root of the sum of their squares.
# Tip: Use the math module.

import math

# Start with some base values
a = 5
b = 10
c = 7

# TODO: Add 3 to a using +=
a+=3

# TODO: Multiply b by 2 using *=
b*=2
# TODO: Modulo c by 4 using %=
c%=4
# TODO: Calculate the square root of (a^2 + b^2 + c^2)
result =(math.sqrt(a)+math.sqrt(b)+math.sqrt(c))
# TODO: Print the final result rounded to 2 decimal places
print(f"The result of the operation is: {result:.2f}")

# -------------------------------------------
# Question 2: Complex Conditional Evaluation
# -------------------------------------------

# Task:
# Ask the user to input three integers (x, y, z).
# Then evaluate and print whether:
# - x is even
# - y is positive
# - z is between 10 and 50
# Use logical operators to combine the conditions.

# Tip: Use and/or to join conditions.

# TODO: Input x, y, z
x=int(input("input x: "))
y=int(input("input y: "))
z=int(input("input z: "))
# TODO: Create conditions:
if x%2 == 0:
  print("x is even is true") 
  if y>0 :
    print("y is postive") 
    if z >= 10 and z <= 50 :
      print(" z is between 10 and 50")
#   is_even = True if x is even
#   is_positive = True if y > 0
#   is_in_range = True if z between 10 and 50
# TODO: Create final_condition = is_even and is_positive and is_in_range
condition1 = False
condition2 = False
condition3 = False

if x%2 == 0:
  condition1 = True
  if y>0 :
    condition2 = True
    if z >= 10 and z <= 50 :
      condition3 = True
    if condition1 and condition2 and condition3:
      Create_final_condition = "is_even and is_positive and is_in_range"
# TODO: Print final_condition
print(Create_final_condition)

# -------------------------------------------
# Question 3: Grading with Adjustments
# -------------------------------------------

# Task:
# Ask the user for their base score, then apply:
score = int(input("input score: "))
# - bonus points (+5)
score +=5
# - late penalty (-10)
score -= 10
# Final score must not exceed 100 or drop below 0.
if score > 100 or score < 0:
    print("error")
# Then assign a grade.
if score <100 or score> 80:
  print("Great")
elif score <79 or 50:
  print("Good")
elif score <49: 
  print("Low")
# Tip: Use min() and max() to constrain the score.
score = max(0, min(score, 100))

# TODO: Input score from user
# TODO: Apply adjustments
# TODO: Clamp score between 0 and 100
# TODO: Use if-elif-else to determine grade and print it


# -------------------------------------------
# Question 4: Advanced Calculator
# -------------------------------------------

# Task:
# Ask the user to input two numbers and an operation (+, -, *, /, %, **).
# Handle division/modulus by zero with error checking.
# Perform the operation and print the result.

# Tip: Use try-except and elif branches for each operation.

# TODO: Input num1, num2
num1 = int(input("input num1: "))
num2 = int(input("input num2: "))
# TODO: Input operation
operation = input("input (+, -, *, /, %, **): ")
# TODO: Match operation using if-elif
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 == 0:
        result = "Error: Cannot divide by zero"
    else:
        result = num1 / num2
elif operation == "%":
    if num2 == 0:
        result = "Error: Cannot divide by zero"
    else:
        result = num1 % num2
elif operation == "**":
    result = num1 ** num2  
else:
    result = "Invalid operation"
# TODO: Handle division/modulus by zero with try-except
    
# TODO: Print result
print(f"The result is: {result}")

