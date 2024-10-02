from trie import Trie, TrieNode

NUMBER_ANSWERS = 5

class Player:
    def __init__(self, trie: Trie) -> None:
        self.trie = trie

    def play(self, start_letter: str, target_length: int) -> list[str]:
        self.word = [start_letter] + [''] * (target_length - 1)
        self.data = [[True, False, set()] for i in range(26)]
        output = []

        self.helper(self.trie.root, output, 0)
        return output

    def helper(self, node: TrieNode, output: list[str], index: int) -> bool:
        if node is None:
            return False

        if index >= len(self.word):
            for key, (exist, count, excluded) in enumerate(self.data):
                if count > 0:
                    return False

            if node.is_word:
                output.append(''.join(self.word))
                return len(output) == NUMBER_ANSWERS
            
            return False
        
        if self.word[index] == '':
            for key, (exist, count, excluded) in enumerate(self.data):
                if exist and count > 0 and index not in excluded:
                    self.data[key][1] -= 1
                    excluded.add(index)

                    self.word[index] = key_to_char(key)
                    if self.helper(node.children[key], output, index + 1):
                        return True

                    self.data[key][1] += 1
                    excluded.remove(index)
            
            for key, (exist, count, excluded) in enumerate(self.data):
                if exist:
                    self.word[index] = key_to_char(key)
                    if self.helper(node.children[key], output, index + 1):
                        return True

            self.word[index] = ''
        else:
            key = ord(self.word[index]) - ord('a')
            if self.helper(node.children[key], output, index + 1):
                return True
        
        return False

    def update_response(self, cells: list, target_length: int, index: int) -> None:
        for i in range(index, index + target_length):
            cell_class = cells[i].get_attribute('class')
            letter = cells[i].get_attribute('textContent') 
            k = i - target_length

            match(cell_class[-1]):
                case 'r':
                    self.word[k] = letter
                    self.data[ord(letter)][1] = False

                case 'y':
                    self.data[ord(letter)][1] = True

                case '-':
                    self.data[ord(letter)][0] = False

def key_to_char(key: int) -> str:
    return chr(key + ord('a'))