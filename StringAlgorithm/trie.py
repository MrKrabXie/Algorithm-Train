class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.is_end_of_word = True

    def search(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return current_node.is_end_of_word

    def starts_with(self, prefix):
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return True

# Example usage:
trie = Trie()
words = ["apple", "app", "application", "banana", "bat", "cat"]
for word in words:
    trie.insert(word)

print(trie.search("app"))  # True
print(trie.search("banana"))  # True
print(trie.search("application"))  # True
print(trie.search("b"))  # False

print(trie.starts_with("app"))  # True
print(trie.starts_with("ba"))  # True
print(trie.starts_with("c"))  # True
print(trie.starts_with("d"))  # False
