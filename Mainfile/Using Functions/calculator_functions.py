def add(x, y):
    """Addition"""
    return x + y

def subtract(x, y):
    """Subtraction"""
    return x - y

def multiply(x, y):
    """Multiplication"""
    return x * y

def divide(x, y):
    """Division"""
    try:
        result = x / y
        if result == float('inf') or result == float('-inf'):
            raise ZeroDivisionError
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero."
    except SyntaxError:
        return "Syntax error in input."

def get_valid_number(prompt):
    """Helper function to get a valid number input"""
    while True:
        try:
            num = float(input(prompt))
            return num
        except ValueError:
            print("Invalid input. Please enter a number.")
import os
def main():
    os.system('cls')
    print("Select operation.")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    while True:
        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '5':
            print("Exiting...")
            break

        if choice not in ('1', '2', '3', '4'):
            print("Invalid Input")
            continue

        num1 = get_valid_number("Enter first number: ")
        num2 = get_valid_number("Enter second number: ")

        if choice == '4' and num2 == 0:
            print("Cannot divide by zero.")
            continue

        try:
            if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))
            elif choice == '2':
                print(num1, "-", num2, "=", subtract(num1, num2))
            elif choice == '3':
                print(num1, "*", num2, "=", multiply(num1, num2))
            elif choice == '4':
                print(num1, "/", num2, "=", divide(num1, num2))
        except SyntaxError:
            print("Syntax error in input.")

        while True:
            next_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
            if next_calculation == "yes" or next_calculation == "no":
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

        if next_calculation != "yes":
            print("Exiting...")
            break

if __name__ == "__main__":
    main()
