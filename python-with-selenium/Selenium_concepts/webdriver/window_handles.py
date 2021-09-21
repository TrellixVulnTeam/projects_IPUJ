from selenium import webdriver

import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class ScrollingElements():
    def test(self):
        url="https://letskodeit.teachable.com/p/practice"
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(10)
        parent_handle = (driver.window_handles)
        print("parent_handle :"+ str(parent_handle))
        driver.find_element_by_id("openwindow").click()
        time.sleep(5)
        print("open window is opened")
        total_handles = driver.window_handles
        print("total_handles :"+ str(total_handles))
        time.sleep(2)
#switching window handles to new window
        driver.switch_to.window(total_handles[1])
        driver.maximize_window()
        search = driver.find_element_by_id("search-courses")
        search.send_keys("python", Keys.ENTER)
        driver.close()
        time.sleep(2)
#switching window handles back to parent window u can use either total_handles[0], or parent_handle
        driver.switch_to.window(total_handles[0])
        driver.get("https://www.redbus.com")
        time.sleep(3)
        driver.execute_script("window.open('https://www.cognizant.com');")
        time.sleep(3)
e=ScrollingElements()
e.test()