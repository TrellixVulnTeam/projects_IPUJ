from selenium import webdriver
import time
from utililites.handywrappers import HandyWrappers

class Utily():
    def test(self):
        url="https://letskodeit.teachable.com/p/practice"
        driver=webdriver.Chrome()
        driver.maximize_window()
        hw=HandyWrappers(driver)
        driver.get(url)
        driver.implicitly_wait(10)
        text1=hw.getelement("//input[@id='bmwradio']",locatortype="xpath")
        text1.click()
        time.sleep(10)
u=Utily()
u.test()