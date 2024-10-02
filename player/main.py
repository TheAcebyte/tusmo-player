from driver import Driver
from player import Player
from trie import *
import time

from timeit import default_timer

DICTIONARY_FILE = 'data/dictionary.txt'

def main() -> None:
    trie = Trie()
    trie.add_words(DICTIONARY_FILE)

    player = Player(trie)
    print(player.play('c', 8))

    driver = Driver()
    driver.launch()
    driver.start(2)

    time.sleep(30)

if __name__ == '__main__':
    main()