from selenium.webdriver.common.by import By

from POM.PromoPage import PromoPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    search_field = (By.XPATH, "//input[@placeholder='Search for Vegetables and Fruits']")
    search_button = (By.XPATH, "//button[@class='search-button']")
    # add_product = (By.XPATH, f"//h4[text()='{search_item} - 1 Kg']/..//button[text()='ADD TO CART']")
    button_Img_cart = (By.XPATH, "//img[@alt='Cart']")
    button_proceed_to_checkout =(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']")

    def search_product(self):
        self.driver.find_element(*HomePage.search_field).clear()
        return self.driver.find_element(*HomePage.search_field)

    def click_search_button(self):
        return self.driver.find_element(*HomePage.search_button)

    def click_add_product(self, search_item):
        return self.driver.find_element("xpath", f"//h4[text()='{search_item} - 1 Kg']/..//a[@class='increment']")

    def click_add_to_cart(self, search_item):
        return self.driver.find_element("xpath", f"//h4[text()='{search_item} - 1 Kg']/..//button[text()='ADD TO CART']")

    def click_cart_img(self):
        return self.driver.find_element(*HomePage.button_Img_cart)

    def click_proceed_to_checkout(self):
        self.driver.find_element(*HomePage.button_proceed_to_checkout).click()
        return PromoPage(self.driver)
