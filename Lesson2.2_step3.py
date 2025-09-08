from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "https://suninjuly.github.io/selects1.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    v1 = browser.find_element(By.CSS_SELECTOR, "span#num1.nowrap").text
    v2 = browser.find_element(By.CSS_SELECTOR, "span#num2.nowrap").text
    v3 = int(v1) + int(v2)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(v3))
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    time.sleep(30)
    browser.quit()

# не забываем оставить пустую строку в конце файла
