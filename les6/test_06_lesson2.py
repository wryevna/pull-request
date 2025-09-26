
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_button_text_changes():
    driver = webdriver.Chrome()
    try:
        driver.get("http://uitestingplayground.com/textinput")

        input_field = driver.find_element(By.ID, "newButtonName")
        input_field.send_keys("SkyPro")

        button = driver.find_element(By.ID, "updatingButton")
        button.click()

        assert button.text == "SkyPro"
        print(button.text)

    finally:
        driver.quit()
