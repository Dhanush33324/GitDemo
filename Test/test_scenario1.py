import pytest

from POM.HomePage import HomePage
from TestData.HomePageData import HomePageData
from utility.BaseClass import BaseClass


class TestScenario1(BaseClass):
    def test_scenario1(self, getData):
        homepage = HomePage(self.driver)
        homepage.search_product().send_keys(getData["search_item"])
        homepage.click_search_button().click()
        homepage.click_add_product(getData["search_item"]).click()
        # homepage.click_add_product(getData["search_item"]).click()
        homepage.click_add_to_cart(getData["search_item"]).click()
        homepage.click_cart_img().click()
        promopage = homepage.click_proceed_to_checkout()
        self.verifylinkpresence(("xpath","//button[text()='Place Order']"))
        amounts = promopage.get_amounts()
        a = []
        for index, amount in enumerate(amounts):
            print(index)
            if index % 2 != 0:
                print(int(amount.text))
                a.append(int(amount.text))
        total = sum(a)
        if int(promopage.get_discount_amounts().text) == total:
            promopage.click_place_Order().click()

        self.selectOptionByText(promopage.get_select_locator(), "India")

        promopage.click_check_box().click()
        promopage.click_button_proceed().click()
        


    @pytest.fixture(params=HomePageData.test_homepage_data)
    def getData(self, request):
        return request.param
