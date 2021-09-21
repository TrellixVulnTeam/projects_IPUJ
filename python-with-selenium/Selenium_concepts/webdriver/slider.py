from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver import ActionChains
import time

class Slider():
    def move(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("https://jqueryui.com/")
        slider = driver.find_element_by_xpath("//a[text()='Slider']")
        webdriver.ActionChains(driver).move_to_element(slider).click().perform()
        time.sleep(5)
        driver.switch_to.frame(0)
        slider_element = driver.find_element_by_xpath("//span[@tabindex='0']")
        ActionChains(driver).drag_and_drop_by_offset(slider_element, 200, 0).perform()

        print("slider moved successfully")
        time.sleep(10)

b=Slider()
b.move()
