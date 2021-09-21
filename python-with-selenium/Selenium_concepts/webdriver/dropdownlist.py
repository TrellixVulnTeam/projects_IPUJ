from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
class Practise():
    def test1(self):
        url=input("Enter your url : ")
        browser=input("In which browser you want to open select 1 or 2 \n1.Chrome 2.Firefox \n")
        if browser==str(1) or browser=="Chrome":
            print("OK redirecting your "+url+" in Chrome browser")
            driver=webdriver.Chrome()
        elif browser==str(2) or browser=="Firefox":
            print("OK redirecting your " + url + " in Firefox browser")
            driver = webdriver.Firefox()
        pass
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(10)
        dropdown=driver.find_element_by_id("carselect")
        print("dropdown :",dropdown)
        value=Select(dropdown)
        print(value)
        value.select_by_value("benz")
        print("select benz by value")
        time.sleep(3)
        value.select_by_index("2")
        print("select honda by index")
        time.sleep(3)
        value.select_by_visible_text("BMW")
        print("select BMW by visible_text")
        time.sleep(3)
        value.select_by_index(2)
        print("select honda by index")
        time.sleep(3)
        # dropdown=driver.find_element_by_xpath("//option[@value='honda']")
        # dropdown.click()
        # time.sleep(3)

p = Practise()
p.test1()
#https://www.google.com/
#https://letskodeit.teachable.com/p/practice