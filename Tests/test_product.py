from time import sleep
from POM.Fresh_Fruits_and_Vegetables_ import FfvPage
from POM.Homepage import Homepage
from conftest import driver


def test_product():
    hp = Homepage(driver)
    hp.shop_by_category()
    fp = FfvPage(driver)
    fp.organic_fruits_vegetables()
    fp.fresh_fruit()
