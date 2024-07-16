#Defined a function here for each operation

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

#Function to display the calculator operations
def calculator():
    print("Welcome to my Very Simple Calculator called PyCalc")
    print("Select your desired operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter your choice (1 or 2 or 3 or 4): ")

    num1 = float(input("Enter your first number please: "))
    num2 = float(input("Enter your second number please: "))

    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid input")

#Calling the calculator function to run the program
calculator()
