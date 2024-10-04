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
    count = -1

    while not lost:
        cells = driver.fetch_cells()
        length = driver.fetch_length(cells)
        player.reset(cells, length)

        for i in range(NUM_ROWS):
            player.play()
            for letter in player.output:
                driver.press_key(letter)
            driver.press_enter()
            time.sleep(PLAY_DELAY)

            cells = driver.fetch_cells()
            player.update_response(cells, i)
            if player.is_filled():
                break
            time.sleep(ITERATION_DELAY)
        
        driver.refresh()
        time.sleep(ROUND_DELAY)
        lost = driver.check_lost()
        count += 1
    
    print(f"\nWords Found: {count}")

if __name__ == '__main__':
    main()