from selenium.webdriver.common.by import By

class Imp():

    def __init__(self, driver):
        self.driver = driver

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
            print("Locator type",locator_type,"is not correct/supported.")
        return False

    def get_element(self,locator,locator_type, element = None):
        try:
            locator_type = locator_type.lower()
            bytype = self.get_bytype(locator_type)
            element = self.driver.find_element(bytype,locator)
            print("Element found with locator : "+str(locator)+" with locator type : "+str(locator_type))
        except:
            print("Element not found with locator : "+str(locator)+" with locator type : "+str(locator_type))
        return element

    def get_text(self, locator="", locator_type="id", element=None, info=""):
        try:
            if locator:
                print("In locator condition")
                element = self.get_element(locator, locator_type)
            print("Before finding text")
            text = element.text
            print("After finding element, size is : " + str(text))
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                print("Getting text on element : " + info)
                print("The text is : '" + text + "'")
                text = text.strip()
        except:
            print("Failed to get text on element " + info)
            text = None
        return text

    def get_value(self, locator="", locator_type="", attribute="", element = None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            value = element.get_attribute(attribute)
            if len(value) == 0:
                print(attribute + " has no data")
            if len(value) != 0:
                print('Data of the element "' + attribute + '" is : "' + value + '"')
                value = value.strip()
        except:
            print("Failed to get value of the element "+attribute)
            value = None
        return value