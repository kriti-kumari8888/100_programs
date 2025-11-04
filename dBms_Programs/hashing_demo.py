"""
hashing_demo.py
Demonstrate a simple fixed-size hash file (in-memory) with chaining.
"""
from typing import Dict, List

class HashTable:
    def __init__(self, size: int = 10):
        self.size = size
        self.table: Dict[int, List[tuple]] = {i: [] for i in range(size)}

    def _hash(self, key: int) -> int:
        return key % self.size

    def insert(self, key: int, value: str):
        h = self._hash(key)
        self.table[h].append((key, value))

    def find(self, key: int):
        h = self._hash(key)
        return [v for k, v in self.table[h] if k == key]

if __name__ == "__main__":
    ht = HashTable(5)
    ht.insert(1, "Alice")
    ht.insert(6, "Bob")
    ht.insert(11, "Carol")
    print("Bucket states:")
    for b, vals in ht.table.items():
        print(b, vals)
    print("Lookup key=6 ->", ht.find(6))