from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    a = browser.find_element(By.XPATH, '//button[@class="btn btn-primary"]')
    a.click()
    confirm = browser.switch_to.alert
    confirm.accept()

    def calc(x):
        return math.log(math.fabs(12 * math.sin(x)))

    x_element = browser.find_element(By.CSS_SELECTOR, 'span[id="input_value"]')
    x = x_element.text
    y = calc(float(x))
    input1 = browser.find_element(By.CSS_SELECTOR, "input#answer.form-control")
    input1.send_keys(y)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
