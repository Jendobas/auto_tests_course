import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


def calc(x):
    return math.log(abs(12 * math.sin(int(x))))


link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CLASS_NAME, "trollface.btn.btn-primary")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    res_x = calc(x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(res_x)

    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
