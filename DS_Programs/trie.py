class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        """Insert a word into the trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    
    def search(self, word: str) -> bool:
        """Returns True if the word is in the trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word
    
    def starts_with(self, prefix: str) -> bool:
        """Returns True if there is any word in the trie that starts with the given prefix."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    
    def get_words_with_prefix(self, prefix: str) -> list[str]:
        """Returns all words in the trie that start with the given prefix."""
        words = []
        node = self.root
        
        # Traverse to the last node of prefix
        for char in prefix:
            if char not in node.children:
                return words
            node = node.children[char]
        
        # Use DFS to find all words
        self._find_words(node, prefix, words)
        return words
    
    def _find_words(self, node: TrieNode, prefix: str, words: list) -> None:
        if node.is_end_of_word:
            words.append(prefix)
        
        for char, child in node.children.items():
            self._find_words(child, prefix + char, words)

def main():
    # Example usage
    trie = Trie()
    
    # Insert some words
    words = ["apple", "app", "apricot", "banana", "bat"]
    print("Inserting words:", words)
    for word in words:
        trie.insert(word)
    
    # Search for words
    search_words = ["apple", "app", "apt", "banana"]
    print("\nSearching for words:")
    for word in search_words:
        print(f"'{word}' found: {trie.search(word)}")
    
    # Test prefix search
    prefix = "ap"
    print(f"\nWords starting with '{prefix}':")
    prefix_words = trie.get_words_with_prefix(prefix)
    print(prefix_words)

if __name__ == "__main__":
    main()