
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_calculator():
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    driver.find_element(By.ID, "delay").clear()
    driver.find_element(By.ID, "delay").send_keys(45)
    time.sleep(3)

    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()
    
    result = WebDriverWait(driver, 50).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))

    assert result, "Результат - 15"

    driver.quit()