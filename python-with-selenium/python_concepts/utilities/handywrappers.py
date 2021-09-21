from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from traceback import print_stack
import time

class HandyWrappers():
    def __init__(self,driver):
        self.driver=driver
    def getbytype(self,locatortype):
        locatortype = locatortype.lower()
        if locatortype=="id":
            return By.ID
        elif locatortype=="name":
            return By.NAME
        elif locatortype=="linktext":
            return By.LINK_TEXT
        elif locatortype=="classname":
            return By.CLASS_NAME
        elif locatortype=="xpath":
            return By.XPATH
        elif locatortype=="css":
            return By.CSS_SELECTOR
        else:
            print("Locator type",locatortype,"is not correct/supported.")
        return False

    def getelement(self,locator,locatortype):
        element = None
        try:
            bytype = self.getbytype(locatortype)
            element = self.driver.find_element(bytype,locator)
            print("element found")
        except:
            print("Element not found")
        return element

    def iselementpresent(self,locator,locatortype):
        try:
            bytype=self.getbytype(locatortype)
            element= self.driver.find_element(bytype,locator)
            if element is not None:
                print("element found")
                return True
            else:
                return False
        except:
            print("element not found")
            return False

    def wait(self,locator,locatortype,timeout,poll_frequency):
        element = None
        try:
            bytype = self.getbytype(locatortype)
            wait = WebDriverWait(self.driver, timeout, poll_frequency, ignored_exceptions=[NoSuchElementException,
                                                        ElementNotVisibleException, ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((bytype,locator)))
            print("waiting for ",timeout,"seconds with interval of ",poll_frequency," milli seconds")
        except:
            print("Element not appeared on the web page")
            print_stack()
        return element

    def take_screeshot(self, driver):
        filename=str(round(time.time()*100))+".png"
        screenshot_directory="D:\screenshots\screenshots"
        destination_folder=screenshot_directory+filename
        try:
            driver.save_screenshot(destination_folder)
            print("screenshot saved in :: "+ destination_folder)
        except NotADirectoryError:
            print("Not a directory issue")