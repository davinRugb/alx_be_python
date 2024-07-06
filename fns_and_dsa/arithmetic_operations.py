# arithmetic_operations.py

def perform_operation(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Division by zero error"
        else:
            return num1 / num2
    else:
        return "Invalid operation"

# main.py
from arithmetic_operations import perform_operation

def main():
    print("Arithmetic Operations")
    
    try:
        num1 = float(input("Enter the first number: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    try:
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    if operation not in ['add', 'subtract', 'multiply', 'divide']:
        print("Invalid operation. Please enter one of the following: add, subtract, multiply, divide.")
        return

    result = perform_operation(num1, num2, operation)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
