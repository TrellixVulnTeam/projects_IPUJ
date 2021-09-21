from selenium import webdriver
from frameworks.pages.home.login_page_2 import Login_page_2
from frameworks.utilities.teststatus import TestStatus
import unittest
import logging
import frameworks.utilities.custom_logger as cl

class Login_tests_2(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        log = cl.customLogger(logging.DEBUG)
        log.info("Execution Started")

    @classmethod
    def tearDownClass(cls) -> None:
        log = cl.customLogger(logging.DEBUG)
        log.info("Execution Completed")

    url = "https://letskodeit.com/"
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(url)
    lp = Login_page_2(driver)
    ts = TestStatus(driver)

    def test_case_1(self):
        self.lp.invalid_login()
        result = self.lp.login_failed()
        self.ts.mark(result, "Test invalid credentials")
        self.lp.cleartextfields()

    def test_case_2(self):
        self.lp.valid_login()
        result1 = self.lp.login_successful()
        self.ts.mark(result1, "Test valid credentials")

    def test_case_3(self):
        self.lp.senddata()
        self.lp.clickelement()
        element = self.lp.enrollelement()
        self.ts.mark(element, "Test select course")

    def test_case_4(self):
        course = self.lp.click_enroll_button()
        self.ts.mark(course, "Test payment detailed page")

    def test_case_5(self):
        self.lp.move_to_payment_section()
        self.lp.enter_credit_card_number()
        self.lp.enter_credit_card_expiry()
        self.lp.enter_credit_card_cvv()
        self.lp.click_buy_button()
        error = self.lp.errormsg()
        self.ts.mark(error, "test invalid_card_details")

    def test_case_6(self):
        text = self.lp.getvalue()
        self.ts.mark(text, "Error message display")
        self.driver.quit()