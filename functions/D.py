def add(a, b):
    return a + b
def subtract(a, b): 
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b != 0 :
        return a / b
    else:
        print("Cannot divide by zero")

num1 = float(input("Enter first number: "))

num2 = float(input("Enter second number: "))

op = input("Enter operation (+, -, *, /): ")

if op == "+":
    print(add(num1, num2))
elif op == "-":
    print(subtract(num1, num2))
elif op == "*":
    print(multiply(num1, num2))
elif op == "/":
    print(divide(num1, num2))
else:
    print("Invalid operator")
