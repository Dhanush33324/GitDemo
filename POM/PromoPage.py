from selenium.webdriver.common.by import By


class PromoPage:
    def __init__(self, driver):
        self.driver = driver

    amounts = (By.XPATH, "//p[@class='amount']")
    discount_amount = (By.XPATH, "//span[@class='discountAmt']")
    button_placeOrder = (By.XPATH, "//button[text()='Place Order']")
    select_locator = (By.XPATH, "//option[text()='Select']/..")
    check_box = (By.XPATH, "//input[@type='checkbox']")
    button_proceed = (By.XPATH, "//button[text()='Proceed']")


    def get_amounts(self):
        return self.driver.find_elements(*PromoPage.amounts)

    def get_discount_amounts(self):
        return self.driver.find_element(*PromoPage.discount_amount)

    def click_place_Order(self):
        return self.driver.find_element(*PromoPage.button_placeOrder)

    def get_select_locator(self):
        return self.driver.find_element(*PromoPage.select_locator)

    def click_check_box(self):
        return self.driver.find_element(*PromoPage.check_box)

    def click_button_proceed(self):
        return self.driver.find_element(*PromoPage.button_proceed)