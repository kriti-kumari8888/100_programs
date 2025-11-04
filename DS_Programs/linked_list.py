class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_front(self, data):
        """Insert a node at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_end(self, data):
        """Insert a node at the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def delete(self, key):
        """Delete the first occurrence of key in linked list."""
        current = self.head
        
        if current and current.data == key:
            self.head = current.next
            return
        
        while current and current.next:
            if current.next.data == key:
                current.next = current.next.next
                return
            current = current.next
    
    def display(self):
        """Print the linked list."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

def main():
    # Example usage
    llist = LinkedList()
    
    # Insert some elements
    llist.insert_end(1)
    llist.insert_end(2)
    llist.insert_front(0)
    llist.insert_end(3)
    
    print("Original linked list:")
    llist.display()
    
    # Delete an element
    llist.delete(2)
    print("\nAfter deleting 2:")
    llist.display()

if __name__ == "__main__":
    main()