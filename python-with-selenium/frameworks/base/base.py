from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from traceback import print_stack
import frameworks.utilities.custom_logger as cl
from selenium.webdriver import ActionChains
import logging
import time
import os

class Webdriver():

    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        self.driver = driver

    def get_title(self):
        return self.driver.title

    def get_bytype(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type=="id":
            return By.ID
        elif locator_type=="name":
            return By.NAME
        elif locator_type=="link":
            return By.LINK_TEXT
        elif locator_type=="class":
            return By.CLASS_NAME
        elif locator_type=="xpath":
            return By.XPATH
        elif locator_type=="css":
            return By.CSS_SELECTOR
        else:
            self.log.info("Locator type",locator_type,"is not correct/supported.")
        return False

    def get_element(self,locator,locator_type):
        element = None
        try:
            locator_type = locator_type.lower()
            bytype = self.get_bytype(locator_type)
            element = self.driver.find_element(bytype,locator)
            self.log.info("Element found with locator : "+str(locator)+" with locator type : "+str(locator_type))
        except:
            self.log.info("Element not found with locator : "+str(locator)+" with locator type : "+str(locator_type))
        return element

    def get_elementlist(self, locator, locator_type="id"):
        element = None
        try:
            locator_type = locator_type.lower()
            bytype = self.get_bytype(locator_type)
            element = self.driver.find_elements(bytype, locator)
            self.log.info("Element list found with locator: " + locator +
                          " and  locatorType: " + locator_type)
        except:
            self.log.info("Element list not found with locator: " + locator +
                          " and  locatorType: " + locator_type)
        return element

    def click_element(self, locator, locator_type, element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            element.click()
            self.log.info("clicked on the element with locator : "+ str(locator) + " with locator_type : "+ str(locator_type))
        except:
            self.log.info("cannot click on the element with locator : " + str(locator) + " with locator_type : " + str(locator_type))
            print_stack()

    def sendkeys(self, data, locator, locator_type, element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            element.send_keys(data)
            self.log.info("sent data on the element with locator : " + str(locator) + " with locator_type : " + str(locator_type))
        except:
            self.log.info("cannot send data on the element with locator : " + str(locator) + " with locator_type : " + str(locator_type))
            print_stack()

    def get_text(self, locator="", locator_type="id", element=None, info=""):
        try:
            if locator:
                self.log.debug("In locator condition")
                element = self.get_element(locator, locator_type)
            self.log.debug("Before finding text")
            text = element.text
            self.log.debug("After finding element, size is: " + str(len(text)))
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on element : " + info)
                self.log.info("The text is : '" + text + "'")
                text = text.strip()
        except:
            self.log.error("Failed to get text on element " + info)
            print_stack()
            text = None
        return text

    def get_value(self, locator="", locator_type="", attribute="", element = None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            value = element.get_attribute(attribute)
            if len(value) == 0:
                self.log.info(attribute + " has no data")
            if len(value) != 0:
                self.log.info('Data of the element "' + attribute + '" is : "' + value + '"')
                value = value.strip()
        except:
            self.log.info('Failed to get value of the element "'+attribute+'"')
            value = None
        return value

    def clear_element(self, locator, locator_type):
        element = self.get_element(locator, locator_type)
        element.clear()

    def is_elementpresent(self,locator,locator_type, element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            if element is not None:
                self.log.info("Element present with locator: " + locator +
                              "with locatorType: " + locator_type)
                return True
            else:
                self.log.info("Element not present with locator: " + locator +
                              " locatorType: " + locator_type)
                return False
        except:
            print("Element not found")
            return False

    def is_elementdisplayed(self, locator, locator_type, element=None):
        is_Displayed = False
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locator_type)
            if element is not None:
                is_Displayed = element.is_displayed()
                self.log.info("Element is displayed with locator: " + locator +
                              " locatorType: " + locator_type)
            else:
                self.log.info("Element not displayed with locator: " + locator +
                              " locatorType: " + locator_type)
            return is_Displayed
        except:
            print("Element not found")
            return False

    def elementPresenceCheck(self, locator, locator_type):
        """ Check if element is present """
        try:
            locator_type = locator_type.lower()
            bytype = self.get_bytype(locator_type)
            elementList = self.driver.find_elements(bytype, locator)
            if len(elementList) > 0:
                self.log.info("Element present with locator: " + locator +
                              " locatorType: " + str(bytype))
                return True
            else:
                self.log.info("Element not present with locator: " + locator +
                              " locatorType: " + str(bytype))
                return False
        except:
            self.log.info("Element not found")
            return False

    def wait(self, locator, locator_type, timeout, poll_frequency):
        element = None
        try:
            locator_type = locator_type.lower()
            bytype = self.get_bytype(locator_type)
            wait = WebDriverWait(self.driver, timeout, poll_frequency, ignored_exceptions=[NoSuchElementException,
                                                        ElementNotVisibleException, ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((bytype, locator)))
            self.log.info("waiting for ", timeout, "seconds with interval of ", poll_frequency, "milli seconds")
        except:
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element

    def take_screenshot(self, resultmessage):
        filename = resultmessage + "." + str(round(time.time() * 1000))+".png"
        screenshot_directory = "D:\screenshots\screenshots "
        destination_folder = screenshot_directory + filename
        current_directory = os.path.dirname(__file__)
        destinationfile = os.path.join(current_directory, destination_folder)
        destination_directory = os.path.join(current_directory, screenshot_directory)
        try:
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)
            self.driver.save_screenshot(destinationfile)
            self.log.info("screenshot saved in : " + destination_folder)
        except NotADirectoryError:
            self.log.error("Exception occurred")
            print_stack()

    def web_scroll(self, direction="up"):
        if direction == "up":
            self.driver.execute_script("window.scrollBy(0, -1000);") # Scroll Up
            self.log.info("page scrolled up successfully")
        if direction == "down":
            self.driver.execute_script("window.scrollBy(0, 1000);") # Scroll Down
            self.log.info("page scrolled down successfully")

    def close_browser(self):
        return self.driver.close()

    def quit_browser(self):
        return self.driver.quit()

    def move_to_element(self, locator, locator_type, element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            ActionChains(self.driver).move_to_element(element).perform()
            self.log.info("moved to the element with locator : " + str(locator) + " with locator_type : " + str(locator_type))
        except:
            self.log.info("cannot move to the element with locator : " + str(locator) + " with locator_type : " + str(locator_type))
            print_stack()


    def move_and_send_data(self, data, locator, locator_type, element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            ActionChains(self.driver).move_to_element(element).send_keys_to_element(element, data).click().perform()
            self.log.info("moved and sent data on the element with locator : " + str(locator) + " with locator_type : " + str(locator_type))
        except:
            self.log.info("cannot move send data on the element with locator : " + str(locator) + " with locator_type : " + str(locator_type))
            print_stack()