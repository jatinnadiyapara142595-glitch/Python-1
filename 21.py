# 1. Write a Function to Perform Arithmetic Operations
#  Create separate functions for addition,
# subtraction, multiplication, and division.
#  Call them based on user input.

def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b if b != 0 else "Error! Division by zero"

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

op = input("Choose (+, -, *, /): ")

if op == '+':
    print("Result:", add(a, b))
elif op == '-':
    print("Result:", sub(a, b))
elif op == '*':
    print("Result:", mul(a, b))
elif op == '/':
    print("Result:", div(a, b))
else:
    print("Invalid choice")
