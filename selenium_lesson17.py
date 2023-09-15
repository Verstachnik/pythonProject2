from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()

    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    option1 = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    option1.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element(By.CSS_SELECTOR, 'span#input_value.nowrap')
    x = x_element.text
    y = calc(x)

    option2 = browser.find_element(By.CSS_SELECTOR, 'input#answer')
    option2.send_keys(y)

    option3 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    option3.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()