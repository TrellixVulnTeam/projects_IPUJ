from selenium import webdriver
import time
class Chrome():
    def test(self):
        driver=webdriver.Chrome()
        url=input("Enter the URl = ")
        print("Navigating to the "+str(url))
        driver.get(url)
        driver.maximize_window()
        time.sleep(5)
c=Chrome()
c.test()