from Data.ExcelLib import *
from POM.Homepage import Homepage


class FfvPage(Homepage):
    FfvPage_Objects = read_locators("F&VPage")

    def organic_fruits_vegetables(self):
        element = FfvPage.FfvPage_Objects['organic_fruits&vegetables']
        self.mouse_hover(element)

    def fresh_fruit(self):
        element= FfvPage.FfvPage_Objects['fresh_fruits']
        self.click_element(element)

    def fresh_vegetable(self):
        element = FfvPage.FfvPage_Objects['fresh_vegeteables']
        self.click_element(element)

    def type_sort_option(self):
        item_locator = FfvPage.FfvPage_Objects['item_option']
        self.select_list_item(item_locator)

    def brand_checkbox(self):
        cbx = FfvPage.FfvPage_Objects['brand']
        self.click_element(cbx)

    def seasonal_checkbox(self):
        cbx = FfvPage.FfvPage_Objects['seasonal']
        self.click_element(cbx)

    def country_origin(self):
        cbx = FfvPage.FfvPage_Objects['country_origin']
        self.click_element(cbx)
