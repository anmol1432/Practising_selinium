from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import os

driver = webdriver.Chrome(
    "C:/workspace/py_projects/kochar/selinium/chrome_driver/chromedriver.exe")
driver.get("https://www.flipkart.com/")

# we can wait until this condition return
# driver.implicitly_wait(4)
# login_btn = driver.find_element_by_class_name('_28p97w')
# login_btn.click()

WebDriverWait(driver, 3).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, '_28p97w'),  # 1 arg element filtration
        'Login'  # arg element text
    )
)
