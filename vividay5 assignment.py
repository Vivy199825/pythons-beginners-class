Write a simple program for a simple calculator or atm machine based on all the knowledge you have learnt so far, 
which must include the use of the def function, and if/else/elif statement.

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    operation = int(input("Enter your option: "))

    if operation == 5:
        print("Exiting the calculator.")
        return
    
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if operation == 1:
        print("Result:", num1 + num2)
    elif operation == 2:
        print("Result:", num1 - num2)
    elif operation == 3:
        print("Result:", num1 * num2)
    elif operation == 4:
        if num2 == 0:
            print("Error! Division by zero is not allowed.")
        else:
            print("Result:", num1 / num2)
    else:
        print("Invalid operation. Please choose a valid operation.")

    calculator()

calculator()