def demonstrate_list_comprehension():
    """Show various examples of list comprehension."""
    # Basic square numbers
    squares = [x**2 for x in range(10)]
    print(f"Squares 0-9: {squares}")
    
    # Even numbers only
    evens = [x for x in range(20) if x % 2 == 0]
    print(f"Even numbers 0-19: {evens}")
    
    # Nested comprehension (multiplication table)
    mult_table = [[i*j for j in range(1, 6)] for i in range(1, 6)]
    print("\nMultiplication table 1-5:")
    for row in mult_table:
        print(row)
    
    # String manipulation
    words = ["hello", "world", "python", "programming"]
    caps = [w.upper() for w in words if len(w) > 5]
    print(f"\nCapitalized words > 5 chars: {caps}")

if __name__ == "__main__":
    demonstrate_list_comprehension()