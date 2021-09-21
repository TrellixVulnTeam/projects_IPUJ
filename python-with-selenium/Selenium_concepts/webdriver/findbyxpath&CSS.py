from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys
class practise():
    def testing(self):
        driver = webdriver.Chrome(executable_path="D:\Drivers\chromedriver.exe")
        url = "https://letskodeit.teachable.com/p/practice"
        print("Navigating to the ", url)
        driver.get(url)
        by_xpath = driver.find_element_by_xpath("//input[@id='name']")
        if by_xpath is not None:
            print("xpath Found")
        by_css = driver.find_element_by_css_selector("#displayed-text")
        if by_css is not None:
            print("css_selector found")
        time.sleep(4)
p=practise()
p.testing()