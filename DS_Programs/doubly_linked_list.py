class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_front(self, data):
        """Insert a node at the beginning of the list."""
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head.prev = new_node
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
        new_node.prev = current
    
    def delete(self, key):
        """Delete the first occurrence of key in the list."""
        if not self.head:
            return
        
        current = self.head
        
        # If head node itself holds the key
        if current.data == key:
            self.head = current.next
            if self.head:
                self.head.prev = None
            return
        
        # Search for the key
        while current and current.data != key:
            current = current.next
        
        if not current:
            return
        
        # Unlink the node
        if current.next:
            current.next.prev = current.prev
        current.prev.next = current.next
    
    def display_forward(self):
        """Display the list from head to tail."""
        current = self.head
        print("Forward:", end=" ")
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")
    
    def display_backward(self):
        """Display the list from tail to head."""
        if not self.head:
            print("Backward: None")
            return
        
        current = self.head
        while current.next:
            current = current.next
        
        print("Backward:", end=" ")
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")

def main():
    # Example usage
    dll = DoublyLinkedList()
    
    # Insert some elements
    print("Inserting elements: 1, 2, 3, 4")
    dll.insert_end(1)
    dll.insert_end(2)
    dll.insert_end(3)
    dll.insert_front(0)
    dll.insert_end(4)
    
    # Display the list in both directions
    dll.display_forward()
    dll.display_backward()
    
    # Delete an element
    print("\nDeleting element: 2")
    dll.delete(2)
    
    # Display the updated list
    dll.display_forward()
    dll.display_backward()

if __name__ == "__main__":
    main()