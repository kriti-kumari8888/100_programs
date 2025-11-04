def factorial(n: int) -> int:
    """Calculate factorial of n recursively."""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    return 1 if n <= 1 else n * factorial(n - 1)

def main():
    try:
        n = int(input("Enter a non-negative integer: "))
        result = factorial(n)
        print(f"{n}! = {result}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()