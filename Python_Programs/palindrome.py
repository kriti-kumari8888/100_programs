def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome (case-insensitive)."""
    # Remove spaces and convert to lowercase
    s = ''.join(s.lower().split())
    return s == s[::-1]

def main():
    text = input("Enter a string: ")
    if is_palindrome(text):
        print(f'"{text}" is a palindrome')
    else:
        print(f'"{text}" is not a palindrome')

if __name__ == "__main__":
    main()