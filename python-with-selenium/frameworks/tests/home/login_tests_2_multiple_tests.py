from selenium import webdriver
from frameworks.pages.home.login_page_2_multiple_data import Login_page_2_multiple_data
from frameworks.utilities.teststatus import TestStatus
import unittest, logging
import frameworks.utilities.custom_logger as cl
from ddt import ddt, data, unpack

@ddt
class Login_tests_2_mutliple_tests(unittest.TestCase):

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
    lp = Login_page_2_multiple_data(driver)
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
        self.lp.click_all_courses()

    @data(("JavaScript","5125632589650588","0222","520"), ("Learn Python","5125632589650588","0222","520"), ("Complete Test","5125632589650588","0222","520"))
    @unpack
    def test_case_3(self, course_name, card_number, expiry, cvv):
        self.lp.senddata(course_name)
        self.lp.click_course(course_name)
        element = self.lp.enrollelement(course_name)
        self.ts.mark(element, "Test select course")
        course = self.lp.click_enroll_button(course_name)
        self.ts.mark(course, "Test payment detailed page")
        self.lp.move_to_payment_section()
        self.lp.enter_credit_card_details(card_number, expiry, cvv)
        self.lp.click_buy_button()
        error = self.lp.errormsg()
        self.ts.mark(error, "test invalid_card_details")
        text = self.lp.getvalue()
        self.ts.mark(text, "Error message display")
        self.lp.click_all_courses_again()

    def test_case_4(self):
        self.driver.quit()