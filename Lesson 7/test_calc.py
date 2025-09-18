
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options
from selenium import webdriver

from page_time_change import CalculatorPage


def test_calculator():
    driver = webdriver.Edge()
    driver.maximize_window()

    calc = CalculatorPage(driver)

    calc.open()
    calc.set_delay(45)
    calc.click("7")
    calc.click("+")
    calc.click("8")
    calc.click("=")

    result = calc.get_result("15")
    assert result == "15"

    driver.quit()
