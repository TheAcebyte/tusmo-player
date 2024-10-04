from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from settings import *

class Driver:
    def __init__(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(IMPLICIT_WAIT)
    
    def launch(self) -> None:
        self.driver.get(URL)
    
    def start(self, mode: int) -> None:
        buttons = self.driver.find_elements(By.CSS_SELECTOR, BUTTON_SELECTOR)
        buttons[mode].click()

    def refresh(self) -> None:
        self.driver.refresh()

    def check_lost(self) -> bool:
        middle_elements = self.driver.find_elements(By.CSS_SELECTOR, LOST_SELECTOR)
        return len(middle_elements) == 1

    def fetch_cells(self):
        return self.driver.find_elements(By.CSS_SELECTOR, CELL_SELECTOR)

    def fetch_length(self, cells) -> int:
        return len(cells) // NUM_ROWS

    def press_key(self, key: str) -> None:
        self.driver.execute_script("""
            const event = new KeyboardEvent('keypress', {keyCode: arguments[0]});
            window.dispatchEvent(event);
            """, ord(key))
    
    def press_enter(self) -> None:
        keycode = 13
        self.driver.execute_script("""
            const event = new KeyboardEvent('keypress', {keyCode: arguments[0]});
            window.dispatchEvent(event);
            """, keycode)