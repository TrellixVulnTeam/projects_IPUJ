from selenium import webdriver
from frameworks.base.important import Imp

class Text():

    def function1(self):
        url = "https://courses.letskodeit.com/courses/javascript-for-beginners/buy/plan/9883"
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(url)

        global imp
        imp = Imp(self.driver)

    def function2(self):
        self.function1()
        imp.get_value(locator="header5", locator_type="id", attribute="data-yummy")
        imp.get_value(locator="//img[@class='img-responsive center-block']", locator_type="xpath", attribute="style")

    def function3(self):
        a = imp.get_text(locator="//h2[@class='dynamic-heading text-white chkout-letter-sp']", locator_type="xpath")
        return a

t=Text()
t.function2()
