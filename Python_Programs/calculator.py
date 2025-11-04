def calculate(a: float, b: float, op: str) -> float:
    """Perform basic arithmetic operations."""
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            raise ValueError("Division by zero")
        return a / b
    else:
        raise ValueError(f"Unsupported operator: {op}")

def main():
    try:
        print("Simple Calculator")
        print("Supported operations: +, -, *, /")
        a = float(input("Enter first number: "))
        op = input("Enter operator: ")
        b = float(input("Enter second number: "))
        
        result = calculate(a, b, op)
        print(f"\n{a} {op} {b} = {result}")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()