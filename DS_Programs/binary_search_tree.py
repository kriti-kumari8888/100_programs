class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        """Insert a key into the BST."""
        self.root = self._insert_recursive(self.root, key)
    
    def _insert_recursive(self, root, key):
        if not root:
            return Node(key)
        
        if key < root.key:
            root.left = self._insert_recursive(root.left, key)
        elif key > root.key:
            root.right = self._insert_recursive(root.right, key)
        
        return root
    
    def search(self, key):
        """Search for a key in the BST."""
        return self._search_recursive(self.root, key)
    
    def _search_recursive(self, root, key):
        if not root or root.key == key:
            return root
        
        if key < root.key:
            return self._search_recursive(root.left, key)
        return self._search_recursive(root.right, key)
    
    def inorder(self):
        """Perform inorder traversal of the BST."""
        self._inorder_recursive(self.root)
        print()
    
    def _inorder_recursive(self, root):
        if root:
            self._inorder_recursive(root.left)
            print(root.key, end=" ")
            self._inorder_recursive(root.right)

def main():
    # Example usage
    bst = BinarySearchTree()
    
    # Insert some elements
    keys = [50, 30, 70, 20, 40, 60, 80]
    for key in keys:
        bst.insert(key)
    
    print("Inorder traversal of the BST:")
    bst.inorder()
    
    # Search for elements
    search_keys = [40, 90]
    for key in search_keys:
        if bst.search(key):
            print(f"\n{key} found in the BST")
        else:
            print(f"\n{key} not found in the BST")

if __name__ == "__main__":
    main()