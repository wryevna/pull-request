
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

def test_third_image_src():
    driver = webdriver.Chrome() 
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html") 
    
    wait = WebDriverWait(driver, 20)
    wait.until(lambda d: len(d.find_elements(By.TAG_NAME, "img")) >= 3)
    
    images = driver.find_elements(By.TAG_NAME, "img")
    third_img = images[2] 
    
    wait.until(lambda d: third_img.get_attribute("src") not in (None, "")) 
    src_value = third_img.get_attribute("src")
    
    print("SRC 3й картинки:", src_value)
    driver.quit()

