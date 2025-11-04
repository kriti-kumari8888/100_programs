"""
btree_demo.py
A very small, illustrative (not production) B-tree-like structure using a simple node split policy.
This is intentionally tiny and educational only.
"""
from __future__ import annotations
from typing import List, Optional

class Node:
    def __init__(self, leaf: bool = True):
        self.keys: List[int] = []
        self.children: List[Node] = []
        self.leaf = leaf

    def __repr__(self):
        return f"Node(keys={self.keys}, leaf={self.leaf})"

class TinyBTree:
    def __init__(self, t: int = 2):
        self.root = Node(True)
        self.t = t  # minimum degree (very small demo)

    def insert(self, key: int):
        root = self.root
        if len(root.keys) == (2 * self.t - 1):
            new_root = Node(False)
            new_root.children.append(root)
            self._split_child(new_root, 0)
            self.root = new_root
            self._insert_nonfull(new_root, key)
        else:
            self._insert_nonfull(root, key)

    def _split_child(self, parent: Node, i: int):
        t = self.t
        y = parent.children[i]
        z = Node(y.leaf)
        z.keys = y.keys[t:]
        y.keys = y.keys[:t-1]
        if not y.leaf:
            z.children = y.children[t:]
            y.children = y.children[:t]
        parent.children.insert(i + 1, z)
        parent.keys.insert(i, y.keys.pop())

    def _insert_nonfull(self, node: Node, key: int):
        if node.leaf:
            node.keys.append(key)
            node.keys.sort()
        else:
            i = len(node.keys) - 1
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == (2 * self.t - 1):
                self._split_child(node, i)
                if key > node.keys[i]:
                    i += 1
            self._insert_nonfull(node.children[i], key)

    def __repr__(self):
        return repr(self.root)

if __name__ == "__main__":
    bt = TinyBTree(t=2)
    for k in [10, 20, 5, 6, 12, 30, 7, 17]:
        bt.insert(k)
    print("Tiny B-Tree root:", bt)
    print("(This is a tiny, illustrative structure, not a full B-tree implementation.)")