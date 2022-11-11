from time import sleep
from Data.ExcelLib import *
from POM.Homepage import Homepage
from selenium.common.exceptions import NoSuchElementException

class Loginpage(Homepage):
    def __init__(self, driver):
        super().__init__(driver)
    
    locators = read_locators("loginpage")

    def login_enter_email(self, email):
        element = Loginpage.locators['txt_email']
        self.enter_text(element, value=email)
    
    def login_enter_password(self, password):
        element = Loginpage.locators['txt_password']
        self.enter_text(element, value=password)

    def login_click_login(self):
        element = Loginpage.locators['btn_login']
        self.click_element(element)

    def _error_message(self,error_message):
            _xpath = f"//span[text()='{error_message}']"
            for _ in range(5):
                try:
                    return self.driver.find_element("xpath",_xpath).is_displayed()
                except NoSuchElementException:
                    print("Error Message not displayed")
                    sleep(1)
                    continue
            return False
