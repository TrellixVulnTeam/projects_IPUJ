from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver import ActionChains
import time


class Browsers():
    def switch(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)

        driver.get("https://letskodeit.teachable.com/p/practice")
        # search = driver.find_element_by_xpath("//input[@class='form-control search input-lg']")
        driver.execute_script("window.scrollBy(0,900)")
        time.sleep(5)
        element = driver.find_element_by_id("mousehover")
        webdriver.ActionChains(driver).move_to_element(element).perform()
        time.sleep(5)
        top_link = driver.find_element_by_xpath("//a[text()='Top']")
        webdriver.ActionChains(driver).move_to_element(top_link).click().perform()
        time.sleep(5)
        ActionChains(driver).move_to_element(element).perform()
        time.sleep(5)
        reload_link = driver.find_element_by_xpath("//a[text()='Reload']")
        webdriver.ActionChains(driver).move_to_element(reload_link).click().perform()
        time.sleep(5)
        driver.quit()
        webdriver.ActionChains(driver)
        # ActionChains(driver).move_to_element(search).send_keys_to_element(search,"mahesh").click().perform()
        # time.sleep(10)
        # time.sleep(10)

b=Browsers()
b.switch()
