from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    driver = webdriver.Chrome()
    driver.get(link)
    driver.implicitly_wait(5)

    # button_book = driver.find_element(By.CSS, "button[onclick='checkPrice();']")
    button_book = driver.find_element(By.CSS_SELECTOR, "button[onclick='checkPrice();']")

    price = WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button_book.click()

    driver.execute_script("window.scrollBy(0, 800)")

    x_element = driver.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    time.sleep(1)

    pole_vvoda = driver.find_element(By.ID, "answer").send_keys(y)

    button_submit = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button_submit.click()

finally:
    time.sleep(3)
    driver.quit()
