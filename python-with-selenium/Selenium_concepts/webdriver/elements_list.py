from selenium import webdriver
from selenium.webdriver.common.by import By
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
        radio_buttons_list=driver.find_elements_by_xpath("//input[@type='radio']")
        print("length of the string is : ",len(radio_buttons_list))
        for buttons in radio_buttons_list:
            is_selected=buttons.is_selected()
            print(is_selected)
            if not is_selected:
                buttons.click()
                time.sleep(3)

p = Practise()
p.test1()
#https://www.google.com/
#https://letskodeit.teachable.com/p/practice