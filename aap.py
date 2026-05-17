def addition(a, b):
    return a + b

def subtraction(a, b, c):
    return a - b - c

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print(f"Addition: {addition(num1, num2)}")
    print(f"Subtraction: {subtraction(num1, num2)}")
    print(f"Multiplication: {multiplication(num1, num2)}")
    print(f"Division: {division(num1, num2)}")

if __name__ == "__main__":
    main()