
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_form_zip():
    driver = webdriver.Edge()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+79858999987")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA Engineer")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    zip_input = driver.find_element(By.NAME, "zip-code")
    zip_input.clear()

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(5)

    WebDriverWait(driver, 5).until(
        EC.url_contains("data-types-submitted.html"))
    
    zip_code_result = driver.find_element(By.ID, "zip-code")

    assert zip_code_result.text == "N/A"

    driver.quit()
