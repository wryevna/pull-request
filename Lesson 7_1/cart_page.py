
from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def checkout(self):
        self.driver.find_element(By.ID, "checkout").click()

    def get_cart_items(self):
        return [el.text for el in self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")]