from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()
    
    def is_empty(self):
        """Check if queue is empty."""
        return len(self.items) == 0
    
    def enqueue(self, item):
        """Add an item to the end of the queue."""
        self.items.append(item)
    
    def dequeue(self):
        """Remove and return the first item in the queue."""
        if not self.is_empty():
            return self.items.popleft()
        raise IndexError("Queue is empty")
    
    def front(self):
        """Return the first item without removing it."""
        if not self.is_empty():
            return self.items[0]
        raise IndexError("Queue is empty")
    
    def size(self):
        """Return the number of items in the queue."""
        return len(self.items)

def main():
    # Example usage
    queue = Queue()
    
    # Enqueue some elements
    print("Enqueuing elements: 1, 2, 3")
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    
    print(f"Queue size: {queue.size()}")
    print(f"Front element: {queue.front()}")
    
    # Dequeue elements
    print("\nDequeuing elements:")
    while not queue.is_empty():
        print(f"Dequeued: {queue.dequeue()}")

if __name__ == "__main__":
    main()