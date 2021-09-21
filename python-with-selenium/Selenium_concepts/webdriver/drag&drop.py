from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver import ActionChains
import time

class Browsers():
    def switch(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("https://jqueryui.com/droppable/")
        driver.switch_to.frame(0)
        draggable = driver.find_element_by_id("draggable")
        droppable = driver.find_element_by_id("droppable")
        time.sleep(5)
        #there are several ways to drag and drop
        #1 ActionChains(driver).click_and_hold(draggable).release(droppable).perform()
        #2 ActionChains(driver).click_and_hold(draggable).perform()
        # ActionChains(driver).release(droppable).perform()
        #3 ActionChains(driver).click_and_hold(draggable).move_to_element(droppable).release().perform()
        #4 ActionChains(driver).drag_and_drop(draggable,droppable).perform()
        time.sleep(5)

b=Browsers()
b.switch()
