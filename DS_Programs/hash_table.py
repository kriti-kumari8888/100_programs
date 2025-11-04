class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(self.size)]
    
    def _hash(self, key):
        """Simple hash function."""
        return hash(key) % self.size
    
    def insert(self, key, value):
        """Insert a key-value pair into the hash table."""
        hash_key = self._hash(key)
        
        # Check if key exists and update value
        for item in self.table[hash_key]:
            if item[0] == key:
                item[1] = value
                return
        
        # If key doesn't exist, append new key-value pair
        self.table[hash_key].append([key, value])
    
    def get(self, key):
        """Retrieve value for a given key."""
        hash_key = self._hash(key)
        
        for item in self.table[hash_key]:
            if item[0] == key:
                return item[1]
        
        raise KeyError(f"Key '{key}' not found")
    
    def remove(self, key):
        """Remove a key-value pair from the hash table."""
        hash_key = self._hash(key)
        
        for i, item in enumerate(self.table[hash_key]):
            if item[0] == key:
                del self.table[hash_key][i]
                return
        
        raise KeyError(f"Key '{key}' not found")
    
    def display(self):
        """Display the hash table."""
        for i, bucket in enumerate(self.table):
            if bucket:  # only show non-empty buckets
                print(f"Bucket {i}: {bucket}")

def main():
    # Example usage
    ht = HashTable()
    
    # Insert some key-value pairs
    print("Inserting key-value pairs:")
    ht.insert("apple", 5)
    ht.insert("banana", 8)
    ht.insert("orange", 3)
    ht.insert("grape", 2)
    
    print("\nHash Table contents:")
    ht.display()
    
    # Retrieve values
    print(f"\nValue for 'apple': {ht.get('apple')}")
    print(f"Value for 'banana': {ht.get('banana')}")
    
    # Remove a key-value pair
    print("\nRemoving 'orange'")
    ht.remove("orange")
    
    print("\nUpdated Hash Table contents:")
    ht.display()

if __name__ == "__main__":
    main()