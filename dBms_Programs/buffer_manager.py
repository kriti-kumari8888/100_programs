"""
buffer_manager.py
Simple buffer pool with LRU eviction for page caching simulation.
"""
from collections import OrderedDict
from typing import Any

class BufferPool:
    def __init__(self, capacity: int = 3):
        self.capacity = capacity
        self.pool = OrderedDict()  # page_id -> page_data

    def get_page(self, page_id: str) -> Any:
        if page_id in self.pool:
            self.pool.move_to_end(page_id)
            return self.pool[page_id]
        return None

    def put_page(self, page_id: str, data: Any):
        if page_id in self.pool:
            self.pool.move_to_end(page_id)
            self.pool[page_id] = data
            return
        if len(self.pool) >= self.capacity:
            evicted = self.pool.popitem(last=False)
            print(f"Evicting page: {evicted[0]}")
        self.pool[page_id] = data

if __name__ == "__main__":
    bp = BufferPool(2)
    bp.put_page("p1", "data1")
    bp.put_page("p2", "data2")
    print("Get p1 ->", bp.get_page("p1"))
    bp.put_page("p3", "data3")
    print("Current pages:", list(bp.pool.keys()))
    bp.put_page("p4", "data4")
    print("Current pages after another insert:", list(bp.pool.keys()))