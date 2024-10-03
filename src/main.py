from driver import Driver
from player import Player
from trie import Trie
import time

from settings import *

def main() -> None:
    trie = Trie()
    trie.add_words(DICTIONARY_FILE)
    driver = Driver()
    player = Player(trie)

    start(driver, player)
    while input("Continue? [Y/N]: ") == 'Y':
        start(driver, player) 

def start(driver: Driver, player: Player) -> None:
    driver.launch()
    driver.start(SOLO_MODE)
    lost = False
    count = 0

    while not lost:
        length = driver.fetch_length()
        player.reset(length)

        for i in range(6):
            cells = driver.fetch_cells()
            valid = player.update_response(cells, length, max(0, i - 1))
            
            if valid:
                break

            output = player.play()
            for char in output:
                driver.press_key(char)

            driver.press_enter()
            time.sleep(ITERATION_DELAY)
        
        driver.refresh()
        time.sleep(ROUND_DELAY)
        lost = driver.check_lost()
        count += 1
    
    print(f"\nFound words: {count}")

if __name__ == '__main__':
    main()