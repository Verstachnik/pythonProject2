from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()

    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)


    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'h5#price'),'$100'))

    option = browser.find_element(By.CSS_SELECTOR, "button.btn")
    option.click()

    x_element = browser.find_element(By.CSS_SELECTOR, 'span#input_value.nowrap')
    x = x_element.text
    y = calc(x)

    option2 = browser.find_element(By.CSS_SELECTOR, 'input#answer')
    option2.send_keys(y)

    option3 = browser.find_element(By.CSS_SELECTOR, "button#solve")
    option3.click()




finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
  # не забывает оптавлять одну пустую строку
  


