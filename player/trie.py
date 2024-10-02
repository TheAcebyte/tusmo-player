CHILDREN_COUNT = 26
ENCODING = 'UTF8'

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def add_word(self, word: str) -> None:
        node = self.root

        for key in word:
            index = ord(key) - ord('a')
            if node.children[index] is None:
                node.children[index] = TrieNode()

            node = node.children[index]    

        node.is_word = True
    
    def add_words(self, file: str) -> None:
        with open(file, encoding=ENCODING) as f:
            for word in f:
                self.add_word(word.rstrip())

class TrieNode:
    def __init__(self, is_word: bool=False) -> None:
        self.children = [None] * CHILDREN_COUNT
        self.is_word = is_word
    
    def get_child(self, key: str) -> None:
        return self.children[ord(key) - ord('a')]