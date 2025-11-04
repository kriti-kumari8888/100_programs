def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    return all(n % i != 0 for i in range(3, int(n ** 0.5) + 1, 2))

def main():
    try:
        n = int(input("Enter an integer: "))
        if is_prime(n):
            print(f"{n} is prime")
        else:
            print(f"{n} is not prime")
    except ValueError:
        print("Error: Please enter a valid integer")

if __name__ == "__main__":
    main()