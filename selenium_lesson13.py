from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def calc(x,z):
    return int(x) + int(z)


try:
    link = 'https://suninjuly.github.io/selects1.html'
    browser = webdriver.Chrome()
    browser.get(link)

    x_element1 = browser.find_element(By.CSS_SELECTOR, 'span#num1')
    x = x_element1.text

    x_element2 = browser.find_element(By.CSS_SELECTOR, 'span#num2')
    z = x_element2.text
    y = str(calc(x,z))

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(y)

    option = browser.find_element(By.CSS_SELECTOR, "button.btn")
    option.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()