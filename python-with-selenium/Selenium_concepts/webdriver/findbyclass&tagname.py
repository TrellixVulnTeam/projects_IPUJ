from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys
class practise():
    def testing(self):
        driver = webdriver.Firefox(executable_path="D:\Drivers\geckodriver.exe")
        driver.maximize_window()
        url = "https://letskodeit.teachable.com/p/practice"
        print("Navigating to the ", url)
        driver.get(url)
        by_class_name = driver.find_element_by_class_name("displayed-class")
        by_class_name.send_keys("testing")
        if by_class_name is not None:
            print("class_name Found")
        by_tag_name = driver.find_element_by_tag_name("h1")
        text=by_tag_name.text
        print("text:",text)
        # by_tag_name.send_keys("tests")
        if by_tag_name is not None:
            print("tag_name found")
        time.sleep(10)
p=practise()
p.testing()