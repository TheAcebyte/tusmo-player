from trie import Trie, TrieNode
import time
from settings import *

def key_to_char(key: int) -> str:
    return chr(key + ord('a'))

class Player:
    def __init__(self, trie: Trie) -> None:
        self.trie = trie

    def reset(self, target_length: int) -> list[str]:
        self.word = [''] * target_length
        self.data = [[0, set(), i] for i in range(26)]

    def play(self) -> list[str]:
        self.output = []
        data = sorted(self.data, reverse=True)
        self.helper(self.trie.root, data, 0)
        return self.output

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

    def update_response(self, cells: list, target_length: int, index: int) -> bool:
        try:
            filled = 0

            for i in range(index * target_length, index * target_length + target_length):
                classes = cells[i].get_attribute('class').split()
                letter = cells[i].text.lower()

                key = ord(letter) - ord('a')
                j = i - target_length * index

                match(classes[-1]):
                    case 'bg-blue-primary' | 'r':
                        self.word[j] = letter
                        filled += 1

                    case 'y':
                        self.data[key][0] = 1
                        self.data[key][1].add(j)

                    case '-':
                        if self.data[key][0] == 0:
                            self.data[key][0] = -1
                        else:
                            self.data[key][1].add(j)
            
            return filled == target_length

        except TypeError:
            print(f"[ERROR] Failed to retrieve letter from cell element")
            exit(1)