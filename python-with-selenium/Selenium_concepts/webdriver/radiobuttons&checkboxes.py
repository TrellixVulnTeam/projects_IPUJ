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
        bmwbtn=driver.find_element_by_id("bmwradio")
        bmwbtn.click()
        benzbtn=driver.find_element_by_id("benzradio")
        benzbtn.click()
        hondabtn=driver.find_element_by_id("hondaradio")
        hondabtn.click()
        bmwchk = driver.find_element_by_id("bmwcheck")
        bmwchk.click()
        benzchk = driver.find_element_by_id("benzcheck")
        benzchk.click()
        hondachk = driver.find_element_by_id("hondacheck")
        hondachk.click()
        time.sleep(5)
        print("bmw button is enabled"+str(bmwbtn.is_selected()))
        print("benz button is enabled" + str(benzbtn.is_selected()))
        print("honda button is enabled" + str(hondabtn.is_selected()))
        print("bmw checkbox is enabled" + str(bmwchk.is_selected()))
        print("benz checkbox is enabled" + str(benzchk.is_selected()))
        print("honda checkbox is enabled" + str(hondachk.is_selected()))

p = Practise()
p.test1()
#https://www.google.com/
#https://letskodeit.teachable.com/p/practice