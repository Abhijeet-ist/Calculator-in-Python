import math

def add():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print("Sum = ", a + b)

def sub():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print("Difference = ", a - b)

def mul():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print("Product = ", a * b)

def div():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    if b == 0:
        print("Division by zero is not possible")
    elif a == 0 and b == 0:
        print("0")
    else:
        print("Division = ", a / b)

while True:
    print("Welcome to my first calculator program made using python")
    start = input("Press Y to start or N to exit calculator: ")
    if start == "N":
        break
    elif start == "Y":
        while True:
            print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n0. Exit")
            choice = int(input("Enter your task: "))
            if choice == 1:
                add()

            elif choice == 2:
                sub()

            elif choice == 3:
                mul()

            elif choice == 4:
                div()
            elif choice == 0:
                print("Thank you")
                break
            else:
                print("This is an invalid character")
    else:
        print("Enter a valid character")