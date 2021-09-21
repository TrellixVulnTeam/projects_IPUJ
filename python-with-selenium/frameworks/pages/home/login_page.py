import frameworks.utilities.custom_logger as cl
import logging
import time
from frameworks.utilities.fortitle import BasePage

class Login_page(BasePage):

    log = cl.customLogger(logging.DEBUG)
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators
    _sign_in = "//div[@class='ast-button']"
    _email = "email"
    _password = "password"
    _login = "//input[@type='submit']"

    def click_sign_in(self):
        self.click_element(self._sign_in, locator_type="xpath")
    def enter_email(self,email):
        self.sendkeys(email, self._email,locator_type="id")
    def enter_password(self, password):
        self.sendkeys(password, self._password,locator_type="id")
    def click_login(self):
        self.click_element(self._login,locator_type="xpath")
    def login_in(self, email='', password=''):
        self.click_sign_in()
        self.enter_email(email)
        time.sleep(5)
        self.enter_password(password)
        self.click_login()

    def verify_login_successful(self, locator, locatortype):
        result = self.is_elementpresent(locator, locatortype)
        return result

    def verify_login_failed(self, locator, locatortype):
        result = self.is_elementpresent(locator, locatortype)
        return result

    def verifytitle(self):
        return self.verifyPageTitle("All Courses")