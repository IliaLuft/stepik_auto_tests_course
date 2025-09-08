import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return math.log(math.fabs(12 * math.sin(x)))

    x_element = browser.find_element(By.CSS_SELECTOR, 'span[id="input_value"]')
    x = x_element.text
    y = calc(float(x))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    input1 = browser.find_element(By.CSS_SELECTOR, "input#answer.form-control")
    input1.send_keys(y)
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()
    button1 = browser.find_element(By.CSS_SELECTOR, "#robotsRule.form-check-input")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button1)
    option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule.form-check-input")
    option2.click()
    button.click()

finally:
    time.sleep(10)
    browser.quit()
