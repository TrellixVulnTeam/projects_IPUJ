from selenium import webdriver
import time

class GetText():

    def text(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)
        openwindow=driver.find_element_by_id("openwindow")
        text1=openwindow.text
        print("Text of the open window is :",text1)
        opentab = driver.find_element_by_id("opentab")
        text2 = opentab.text
        print("Text of the open tab is :", text2)
        mouse=driver.find_element_by_id("mousehover")
        text3=mouse.text
        print("Text of the mousehover is :",text3)
        time.sleep(3)
t=GetText()
t.text()