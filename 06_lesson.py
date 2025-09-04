
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#Перейдите на страницу http://uitestingplayground.com/ajax.
#Нажмите на синюю кнопку.
#Получите текст из зеленой плашки.
#Выведите его в консоль 
#("Data loaded with AJAX get request.")

driver = webdriver.Chrome()
driver.get('http://uitestingplayground.com/ajax')

button = driver.find_element(By.ID, "ajaxButton")
button.click()

wait = WebDriverWait(driver, 20)
green_box = wait.until(
    EC.visibility_of_element_located((By.CLASS_NAME, "bg-success"))
)

print(green_box.text)

driver.quit()
