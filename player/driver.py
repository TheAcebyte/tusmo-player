from selenium import webdriver
from selenium.webdriver.common.by import By

URL = 'https://www.tusmo.xyz'
BUTTON_SELECTOR = '.menu-button'
GRID_SELECTOR = '.motus-grid'
CELL_SELECTOR = '.cell-content'

LOADING_WAIT = 10

class Driver:
    def __init__(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(LOADING_WAIT)
    
    def launch(self) -> None:
        self.driver.get(URL)
    
    def start(self, mode: int) -> None:
        buttons = self.driver.find_elements(By.CSS_SELECTOR, BUTTON_SELECTOR)
        buttons[mode].click()

    def fetch_length(self) -> None:
        grid = self.driver.find_element(By.CSS_SELECTOR, GRID_SELECTOR)
        length = len(grid.value_of_css_property('grid-template-columns').split())
        return length

    def fetch_cells(self):
        return self.driver.find_element(By.CSS_SELECTOR, CELL_SELECTOR)

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
