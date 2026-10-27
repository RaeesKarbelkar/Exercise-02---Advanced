num1 = int(input("input num1: "))
num2 = int(input("input num2: "))
# TODO: Input operation
operation = input("input (+, -, *, /, %, **)")
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