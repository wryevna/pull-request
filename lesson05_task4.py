
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("https://the-internet.herokuapp.com/login")

username = driver.find_element(By.CSS_SELECTOR, "#username")
username.send_keys("tomsmith")

password = driver.find_element(By.CSS_SELECTOR, "#password")
password.send_keys("SuperSecretPassword!")

button = driver.find_element(By.CSS_SELECTOR, ".fa-2x.fa-sign-in")
button.click()

green_message = driver.find_element(By.CSS_SELECTOR, ".flash.success")
print("Сообщение с плашки:", green_message.text)

sleep(3)

driver.quit()




