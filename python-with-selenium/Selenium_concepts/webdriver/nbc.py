from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains
import time

class Order():
    def order(self):
        url = "https://stage-www.nbc.com/"
        driver = webdriver.Chrome(executable_path="D:\chromedriver_win32\chromedriver.exe") #Give chromedriverPath
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("//a[@href='/shows/all/popular']").click()
        ActionChains(driver).move_to_element(driver.find_element_by_xpath("//a[@aria-label='Chicago Fire, NBC']")).click().perform()
        time.sleep(10)

O=Order()
O.order()