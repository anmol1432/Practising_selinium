"""
This .py file is created for.
entring values in html input useing selinium.
find_element_by_cssSelector (button[onclick="total()"]) gives you more control
over html element.
https://www.w3schools.com/cssref/css_selectors.asp link
"""
from typing import KeysView
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.support import expected_conditions as EC, select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
import os

path = "C:/workspace/py_projects/kochar/selinium/chrome_driver/chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://www.opencart.com/")
driver.implicitly_wait(4)

try:
    email_input = driver.find_element_by_name('newsletter')
    enter_btn = driver.find_element_by_class_name('subscribe')
    email_input.send_keys('xyz@gmail.com')
    driver.implicitly_wait(4)
    enter_btn.click()
except:
    print("NO INUT ELEMENT FIND")
