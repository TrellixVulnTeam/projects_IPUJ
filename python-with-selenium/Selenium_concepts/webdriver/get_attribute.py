from selenium import webdriver
import time

class GetValue():

    def text(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)
        search = driver.find_element_by_id("name")
        text1 = search.get_attribute("class")
        print("value of the attribute is :", text1)
        alert = driver.find_element_by_id("alertbtn")
        text2 = alert.get_attribute("value")
        print("value of the attribute is :", text2)
        show = driver.find_element_by_id("displayed-text")
        text3 = show.get_attribute("name")
        print("value of the attribute is :", text3)
        button = driver.find_element_by_xpath("//input[@id='bmwradio']")
        text4 = button.get_attribute("value")
        print("value of the attribute is :",text4)

        time.sleep(3)
t=GetValue()
t.text()