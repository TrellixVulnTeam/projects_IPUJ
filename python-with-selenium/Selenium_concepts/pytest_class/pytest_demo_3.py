import pytest
from selenium import webdriver
from frameworks.base.base import Webdriver
import frameworks.utilities.excel_extract_load as excel
import time

class Test():

    @pytest.fixture()
    def setUp(self):
        url = "https://letskodeit.com/"
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        global driver, hw, rows, columns, path
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(url)
        path = "D:\sample.xlsx"
        rows = excel.get_row_count(path, "Sheet3")
        print(rows)
        columns = excel.get_column_count(path, "Sheet3")
        print(columns)
        hw = Webdriver(driver)
        yield
        driver.quit()

    def test_case_1(self):
        hw.click_element(locator="//div[contains(text(),'Sign')]", locator_type="xpath")

    def test_case_2(self):
        for r in range(2, rows+1):
            user_name = excel.read_data(path, "Sheet3", r, 1 )
            pass_word = excel.read_data(path, "Sheet3", r, 2)
            time.sleep(5)
            hw.sendkeys(locator="email", locator_type="id", data=user_name)
            time.sleep(5)
            hw.sendkeys(locator="password", locator_type="id", data=pass_word)
            hw.click_element(locator="//input[@value='Login']", locator_type="xpath")
            if hw.is_elementdisplayed(locator="//span[starts-with(text(),'Your')]", locator_type="xpath"):
                excel.write_data(path, "Sheet3", r, 3, "test case failed")
                hw.clear_element(locator="email", locator_type="id")
                driver.refresh()
            elif driver.title=="All Courses":
                excel.write_data(path, "Sheet3", r, 3, "test case Passed")
                hw.click_element(locator="dropdownMenu1", locator_type="id")
                hw.click_element(locator="//a[starts-with(text(), 'Logout')]", locator_type="xpath")
                hw.click_element(locator="//a[starts-with(text(), 'Sign In')]", locator_type="xpath")
            pass