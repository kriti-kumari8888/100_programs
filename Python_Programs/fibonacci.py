def fibonacci(n: int) -> list[int]:
    """Generate first n Fibonacci numbers."""
    if n < 1:
        raise ValueError("N must be >= 1")
    fib = [0, 1]
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

def main():
    try:
        n = int(input("Enter N (>=1): "))
        result = fibonacci(n)
        print(f"Fibonacci sequence: {' '.join(map(str, result))}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()