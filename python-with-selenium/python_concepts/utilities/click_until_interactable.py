#move to element and click the same button
#important

from selenium import webdriver
import time
from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains


class ScrollingElements():
    def test(self):
        url="https://letskodeit.teachable.com/p/practice"
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(10)

        time.sleep(10)
        try:
            element = driver.find_element_by_id("mousehover")
            webdriver.ActionChains(driver).move_to_element(element).click(element).perform()
            time.sleep(10)
            print("action performed")
        except [ElementClickInterceptedException]:
            print("element click intercepted exception")
        time.sleep(10)

e=ScrollingElements()
e.test()