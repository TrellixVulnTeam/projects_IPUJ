from selenium import webdriver
from frameworks.pages.home.login_page import Login_page
from frameworks.utilities.teststatus import TestStatus
import unittest
import pytest

class Frame(unittest.TestCase):

    url = "https://letskodeit.com/"
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(url)
    lp = Login_page(driver)
    ts = TestStatus(driver)

    @pytest.mark.run(order=2)
    def test_valid_login(self):
        self.lp.login_in(email="test@email.com",password="abcabc")
        title = self.lp.verifytitle()
        self.ts.mark(title, "Title Verification")
        login = self.lp.verify_login_successful("search", locatortype="id")
        self.ts.markFinal("test_valid_login",login, "Login verification")
        self.driver.close()

    @pytest.mark.run(order=1)
    def test_invalid_login(self):
        self.lp.login_in(email="test@email.com", password="abcsbjwbfjwjcjwabc")
        status = self.lp.verify_login_failed(
                "//span[contains(text(),'Your username or password is invalid. Please try again.')]",
                "xpath")
        self.ts.mark(status, "sign_in verication")
        # assert status == True
        # self.lp.clear_element("email", locatortype="id")
        # self.lp.clear_element("password", locatortype="id")
        self.driver.find_element_by_id("email").clear()
        self.driver.find_element_by_id("password").clear()




