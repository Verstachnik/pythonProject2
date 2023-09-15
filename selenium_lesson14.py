from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    x_element1 = browser.find_element(By.CSS_SELECTOR, "[id = 'input_value']")
    x = x_element1.text
    y = calc(x)

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    button = browser.find_element(By.CSS_SELECTOR, "input#answer.form-control")
    button.send_keys(y)

    option1 = browser.find_element(By.CSS_SELECTOR, "input#robotCheckbox")
    option1.click()

    option2 = browser.find_element(By.CSS_SELECTOR, "input#robotsRule")
    option2.click()

    option3 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    option3.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()