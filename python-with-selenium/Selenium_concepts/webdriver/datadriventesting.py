import python_concepts.utilities.excel_extract_load as excel
from selenium import webdriver
from frameworks.base.base import Webdriver
import time

path = "D:\sample.xlsx"
rows = excel.get_row_count(path, "Sheet3")
columns = excel.get_column_count(path, "Sheet3")
url = "https://letskodeit.com/"
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get(url)
wb = Webdriver(driver)

wb.click_element(locator="//div[contains(text(),'Sign Up or Log In')]",locator_type="xpath")
for r in range(2, rows+1):
    user_name = excel.read_data(path, "Sheet3", r, 1)
    wb.sendkeys(locator="email", locator_type="id", data = user_name)
    password = excel.read_data(path, "Sheet3", r, 2)
    wb.sendkeys(locator="password", locator_type="id", data = password)
    wb.click_element(locator="//input[@value='Login']", locator_type="xpath")
    if wb.is_elementpresent(locator="//span[contains(text(), 'Your username or password is invalid. Please try again.')]",locator_type="xpath"):
        excel.write_data(path, "Sheet3", r, 3, "Login failed")
        wb.clear_element(locator="email", locator_type="id")
        driver.refresh()
        time.sleep(5)
    else :
        excel.write_data(path, "Sheet3", r, 3, "Login successful")