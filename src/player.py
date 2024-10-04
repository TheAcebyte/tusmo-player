from trie import Trie, TrieNode
from settings import *

def key_to_char(key: int) -> str:
    return chr(key + ord('a'))

class Player:
    def __init__(self, trie: Trie) -> None:
        self.trie = trie

    def reset(self, cells: list, target_length: int) -> list[str]:
        self.word = [''] * target_length
        self.data = [[0, set(), i] for i in range(26)]
        
        first_letter = cells[0].get_attribute('textContent').lower()
        self.word[0] = first_letter

    def play(self) -> None:
        data = sorted(self.data, reverse=True)
        self.helper(self.trie.root, data, 0)

    def helper(self, node: TrieNode, data: list[int, set], index: int) -> bool:
        if node is None:
            return False

        if index >= len(self.word):
            if node.is_word:
                self.output = ''.join(self.word)
                return True
            
            return False
        
        if self.word[index] == '':
            for state, excluded, key in data:
                if state == -1:
                    break

                if index not in excluded:
                    self.word[index] = key_to_char(key)
                    if self.helper(node.children[key], data, index + 1):
                        self.word[index] = ''
                        return True
                    
            self.word[index] = ''
        else:
            key = ord(self.word[index]) - ord('a')
            if self.helper(node.children[key], data, index + 1):
                return True
            
        return False
    
    def update_response(self, cells: list, index: int) -> None:
        try:
            n = len(self.word)
            for i in range(index * n, (index + 1) * n):
                classes = cells[i].get_attribute('class').split()
                j = i - index * n
                letter = self.output[j]
                key = ord(letter) - ord('a')

                match(classes[-1]):
                    case 'r':
                        self.word[j] = letter

                    case 'y':
                        self.data[key][0] = 1
                        self.data[key][1].add(j)

                    case '-':
                        if self.data[key][0] == 0:
                            self.data[key][0] = -1
                        else:
                            self.data[key][1].add(j)
        except Exception:
            print("[ERROR] Internal error occured.")
            exit(1)

    def is_filled(self) -> bool:
        for letter in self.word:
            if letter == '':
                return False
            
        return True