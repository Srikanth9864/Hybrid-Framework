from Data.ExcelLib import read_locators
from Library import SeleniumWrapper
from Library.SeleniumWrapper import *
class Homepage(SeleniumWrapper):
    def __int__(self):
        super().__init__()

    locators = read_locators("homepage")

    def login(self):
        element = Homepage.locators['Login_link']
        self.click_element(element)

    def shop_by_category(self):
        element = Homepage.locators['Shop_Nav']
        self.mouse_hover(element)

    def offers(self):
        element = Homepage.locators['Offers_link']
        self.click_element(element)

    def search_bar(self):
        element = Homepage.locators['Search_txt']
        self.click_element(element)

    def my_basket(self):
        element = Homepage.locators['Basket_link']
        self.click_element(element)

    def select_location(self):
        element = Homepage.locators['Location']
        self.click_element(element)

    # def is_user_logged_in(self, email):
    #     _xpath = f"//a[text()='{email}']"
    #     for _ in range(5):
    #         try:
    #             return self.driver.find_element("xpath", _xpath).is_displayed()
    #         except NoSuchElementException:
    #             print("User is not logged in yet trying after one second")
    #              sleep(1)
    #             continue
    #     return False
