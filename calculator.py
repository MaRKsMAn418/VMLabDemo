# Calculator

num1= input("Enter first number :")
num2 = input("Enter second number :")
op = input("Enter the operator (+, -, *, /): ")

# Functions (+ , - , * , /)
def sum():
    result = float(num1) + float(num2)
    print(result)
def diff():
    result = float(num1) - float(num2)
    print(result)
def product():
    result = float(num1) * float(num2)
    print(result)
def divide():
    result = float(num1) / float(num2)
    print(result)
    
if op == "+":
    sum()
elif op == "-":
    diff()
elif op == "*":
    product()
elif op == "/":
    divide()
else:
    print("Invalid operator. Please enter a valid operator (+, -, *, /).")

