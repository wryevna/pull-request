
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_zip_red_and_others_green():
    driver = webdriver.Edge()
    wait = WebDriverWait(driver, 10)
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    driver.find_element(By.NAME, "zip-code").clear()

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    wait.until(EC.url_contains("data-types-submitted.html"))

    zip_field = driver.find_element(By.ID, "zip-code")
    red_colors = ["rgba(132, 32, 41, 1)", "rgb(132, 32, 41)"]
    assert zip_field.value_of_css_property("color") in red_colors, \
        f"Zip code должен быть красным, а сейчас {zip_field.value_of_css_property('color')}"

    green_fields = [
        "first-name",
        "last-name",
        "address",
        "e-mail",
        "phone",
        "city",
        "country",
        "job-position",
        "company"
    ]
    green_colors = [
        "rgba(0, 128, 0, 1)", "rgb(0, 128, 0)",
        "rgba(15, 81, 50, 1)", "rgb(15, 81, 50)"
    ]
    for field_id in green_fields:
        elem = driver.find_element(By.ID, field_id)
        color = elem.value_of_css_property("color")
        assert color in green_colors, f"{field_id} не зелёный! Сейчас {color}"

    driver.quit()
