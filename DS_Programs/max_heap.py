class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def parent(self, i):
        return (i - 1) // 2
    
    def left_child(self, i):
        return 2 * i + 1
    
    def right_child(self, i):
        return 2 * i + 2
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def insert(self, key):
        """Insert a new key into the max heap."""
        self.heap.append(key)
        self._sift_up(len(self.heap) - 1)
    
    def _sift_up(self, i):
        parent = self.parent(i)
        if i > 0 and self.heap[i] > self.heap[parent]:
            self.swap(i, parent)
            self._sift_up(parent)
    
    def extract_max(self):
        """Remove and return the maximum element from the heap."""
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        
        return max_val
    
    def _sift_down(self, i):
        max_index = i
        left = self.left_child(i)
        right = self.right_child(i)
        
        if left < len(self.heap) and self.heap[left] > self.heap[max_index]:
            max_index = left
        
        if right < len(self.heap) and self.heap[right] > self.heap[max_index]:
            max_index = right
        
        if i != max_index:
            self.swap(i, max_index)
            self._sift_down(max_index)
    
    def get_max(self):
        """Return the maximum element without removing it."""
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")
        return self.heap[0]

def main():
    # Example usage
    heap = MaxHeap()
    
    # Insert some elements
    print("Inserting elements: 4, 10, 8, 5, 1")
    elements = [4, 10, 8, 5, 1]
    for elem in elements:
        heap.insert(elem)
    
    print(f"\nCurrent heap array: {heap.heap}")
    print(f"Maximum element: {heap.get_max()}")
    
    # Extract elements in order
    print("\nExtracting elements:")
    while heap.heap:
        print(f"Extracted: {heap.extract_max()}")

if __name__ == "__main__":
    main()