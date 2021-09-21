import logging
from frameworks.base.base import Webdriver
import frameworks.utilities.custom_logger as cl
import time

class Login_page_2(Webdriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _login="//div[contains(text(),'Sign Up or Log In')]"
    _email="email"
    _password = "password"
    _login_2 = "//input[@value='Login']"
    _all_courses = "//a[contains(text(),'All Courses')]"
    _search_course = "search"
    _search_course_button = "//button[@class='find-course search-course']"
    _java_script = "//div[@class='zen-course-author-info dynamic-text']"
    _error_message  = "//span[contains(text(), 'Your username or password is invalid. Please try again.')]"
    _all_courses_button = "//nav//a[contains(@href,'/courses') and contains(@target,'_self')]"
    _search_textbox = "course"
    _search_button = "//button[@type='submit']"
    _course_select = "//div[@class='zen-course-author-info dynamic-text']"
    _course_message = "//h1[contains(text(),'JavaScript for beginners')]"
    _enroll_button = "//button[@data-uniqid='1595290194536']"
    _payment_page = "//h2[contains(text(),'JavaScript for beginners')]"
    _payment_section = "//div[@class='margin-top-10 margin-bottom-10 agree-text']"
    _card_number = "cardnumber"
    _expiry_date = "//input[@autocomplete='cc-exp']"
    _cvv = "//input[@name='cvc']"
    _submit_button = "//button[@class='zen-subscribe sp-buy btn btn-default btn-lg btn-block btn-gtw btn-submit checkout-button dynamic-button']"
    _errormsg = "//p[@class='dynamic-text' and @style='text-align:center;color:#c00;']"
    _dynamictext="//p[@style='text-align:center;color:#c00;']"

    def login(self):
        self.click_element(locator=self._login,locator_type="xpath")
    def click_login(self):
        self.click_element(locator=self._login_2,locator_type="xpath")
    def click_all_courses(self):
        self.click_element(locator=self._all_courses, locator_type="xpath")
    def click_search(self):
        self.click_element(locator = self._search_course_button, locator_type="id")
    def click_java(self):
        self.click_element(locator=self.click_java(), locator_type="xpath")
    def enter_email(self,email):
        self.sendkeys(email, self._email,locator_type="id")
    def enter_password(self, password):
        self.sendkeys(password, self._password,locator_type="id")

    def invalid_login(self):
        self.login()
        self.enter_email(email="test@email.com")
        self.enter_password(password="sfhihfiwifiwf")
        time.sleep(3)
        self.click_login()

    def valid_login(self):
        self.enter_email(email="test@email.com")
        self.enter_password(password="abcabc")
        time.sleep(3)
        self.click_login()

    def login_failed(self):
        result = self.is_elementpresent(locator=self._error_message,locator_type="xpath")
        return result

    def cleartextfields(self):
        self.clear_element(locator="email", locator_type="id")
        self.clear_element(locator="password", locator_type="id")

    def login_successful(self):
        result = self.is_elementpresent(locator=self._search_course, locator_type="id")
        return result

    def senddata(self):
        self.click_element(locator=self._all_courses_button, locator_type="xpath")
        self.sendkeys(data="javascript", locator=self._search_textbox, locator_type="name")
        time.sleep(5)

    def clickelement(self):
        self.click_element(locator=self._search_button, locator_type="xpath")
        self.click_element(locator=self._course_select, locator_type="xpath")
        time.sleep(3)

    def enrollelement(self):
        enroll = self.is_elementdisplayed(locator=self._course_message, locator_type="xpath")
        return enroll

    def click_enroll_button(self):
        self.click_element(locator=self._enroll_button, locator_type="xpath")
        element = self.is_elementpresent(locator=self._payment_page, locator_type="xpath")
        return element

    def move_to_payment_section(self):
        self.move_to_element(locator=self._payment_section, locator_type="xpath")

    def enter_credit_card_number(self):
        self.driver.switch_to.frame(0)
        self.sendkeys(data="5125632589650588",locator=self._card_number, locator_type="name")
        self.driver.switch_to.default_content()

    def enter_credit_card_expiry(self):
        self.driver.switch_to.frame(1)
        self.sendkeys(data="0222", locator=self._expiry_date, locator_type="xpath")
        self.driver.switch_to.default_content()

    def enter_credit_card_cvv(self):
        self.driver.switch_to.frame(2)
        self.sendkeys(data="520", locator=self._cvv, locator_type="xpath")
        self.driver.switch_to.default_content()

    def click_buy_button(self):
        self.click_element(locator=self._submit_button, locator_type="xpath")

    def errormsg(self):
        error_msg = self.is_elementdisplayed(locator=self._errormsg, locator_type="xpath")
        return error_msg

    def getvalue(self):
        text = self.get_value(locator=self._dynamictext, locator_type="xpath", attribute="class")
        return text