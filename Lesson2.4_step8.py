from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time, math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button1 = browser.find_element(By.ID, "book")
    button1.click()

    def calc(x):
        return math.log(math.fabs(12 * math.sin(x)))

    x_element = browser.find_element(By.CSS_SELECTOR, 'span[id="input_value"]')
    x = x_element.text
    y = calc(float(x))
    input1 = browser.find_element(By.CSS_SELECTOR, "input#answer.form-control")
    input1.send_keys(y)
    button2 = browser.find_element(By.ID, "solve")
    button2.click()
finally:
    time.sleep(10)
    browser.quit()
