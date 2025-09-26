
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    def open_browser(self):
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )

    def set_delay(self, seconds):
        delay = self.driver.find_element(By.ID, "delay")
        delay.clear()
        delay.send_keys(str(seconds))

    def click(self, value):
        self.driver.find_element(By.XPATH, f"//span[text()='{value}']").click()

    def get_result(self, expected):
        self.wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"),
                expected
            )
        )
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text
