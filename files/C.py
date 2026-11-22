try:
    number = float(input("Enter an integer: "))
    print(f"You entered: {number}")
except ValueError:
    print("Invalid input! ")
