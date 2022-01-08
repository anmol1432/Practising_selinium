from selenium import webdriver
from booking_bot import constant as Const
import time


class Booking(webdriver.Chrome):
    def __init__(self,
                 driver_path='C:\chrome_driver\chromedriver.exe', teardown='false'):
        self.driver_path = driver_path
        self.teardown = teardown
        super(Booking, self).__init__()
        # imimplicitly_wait(15) is going to wait until element is find
        self.implicitly_wait(15)
        self.maximize_window()

    def land_first_page(self):
        self.get(Const.BASE_URL)

    def exit(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            time.sleep(3)
            self.quit()

    def change_currency(self, currency=None):
        currency_element = self.find_element_by_css_selector(
            'button[data-tooltip-text="Choose your currency"]')
        print("hello ", currency_element)
        currency_element.click()
