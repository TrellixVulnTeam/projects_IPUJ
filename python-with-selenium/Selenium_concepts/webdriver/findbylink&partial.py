from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys
class practise():
    def testing(self):
        driver = webdriver.Chrome(executable_path="D:\Drivers\chromedriver.exe")
        url = "https://letskodeit.teachable.com/pages/practice"
        print("Navigating to the ", url)
        driver.get(url)
        by_link = driver.find_element_by_link_text("Login") #link text means full name of the anchor(starts with a)
        if by_link is not None:
            print("link Found")
        by_partial_link_text = driver.find_element_by_partial_link_text("Prac") #partial means partial name of the anchor
        if by_partial_link_text is not None:
            print("partial_link_text found")
        time.sleep(4)
p=practise()
p.testing()