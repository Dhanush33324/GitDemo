from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome("./chromedriver")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
search_item = "Apple"
driver.find_element_by_xpath("//input[@placeholder='Search for Vegetables and Fruits']").send_keys(search_item)
driver.find_element_by_xpath("//button[@class='search-button']").click()

driver.find_element_by_xpath(f"//h4[text()='{search_item} - 1 Kg']/..//a[@class='increment']").click()

driver.find_element_by_xpath(f"//h4[text()='{search_item} - 1 Kg']/..//button[text()='ADD TO CART']").click()
driver.find_element_by_xpath("//img[@alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located(("xpath","//button[text()='Place Order']")))
amounts = driver.find_elements_by_xpath("//p[@class='amount']")
# print(len(amounts))
a = []
for index, amount in enumerate(amounts):
    print(index)
    if index%2 != 0:
        print(int(amount.text))
        a.append(int(amount.text))
total = sum(a)
if int(driver.find_element_by_xpath("//span[@class='discountAmt']").text) == total:
    driver.find_element_by_xpath("//button[text()='Place Order']").click()

select = Select(driver.find_element_by_xpath("//option[text()='Select']"))
select.select_by_visible_text("India")
driver.find_element_by_xpath("//input[@type='checkbox']").click()
driver.find_element_by_xpath("//button[text()='Proceed']").click()
Successful_message = driver.find_element_by_xpath()


