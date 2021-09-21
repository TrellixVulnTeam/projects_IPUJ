from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys
class practise():
    def testing(self):
        driver=webdriver.Chrome(executable_path="D:\Drivers\chromedriver.exe")
        url="https://letskodeit.teachable.com/p/practice"
        print("Navigating to the ",url)
        driver.get(url)
        by_id=driver.find_element_by_id("name")
        if by_id is not None:
            print("ID Found")
        by_name=driver.find_element_by_name("show-hide")
        if by_name is not None:
            print("Name found")
        time.sleep(4)
p=practise()
p.testing()