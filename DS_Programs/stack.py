class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        """Check if stack is empty."""
        return len(self.items) == 0
    
    def push(self, item):
        """Push an item onto the stack."""
        self.items.append(item)
    
    def pop(self):
        """Remove and return the top item from the stack."""
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Stack is empty")
    
    def peek(self):
        """Return the top item without removing it."""
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Stack is empty")
    
    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)

def main():
    # Example usage
    stack = Stack()
    
    # Push some elements
    print("Pushing elements: 1, 2, 3")
    stack.push(1)
    stack.push(2)
    stack.push(3)
    
    print(f"Stack size: {stack.size()}")
    print(f"Top element: {stack.peek()}")
    
    # Pop elements
    print("\nPopping elements:")
    while not stack.is_empty():
        print(f"Popped: {stack.pop()}")

if __name__ == "__main__":
    main()