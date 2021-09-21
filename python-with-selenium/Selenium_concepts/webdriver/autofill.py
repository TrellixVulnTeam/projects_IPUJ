from selenium import webdriver
import time

class AutoComplete():
    def run(self):
        url="https://www.redbus.com/"
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(10)
        driver.find_element_by_id("src").send_keys("kada")
        time.sleep(5)
        driver.find_element_by_xpath("//ul[@class='autoFill']//li[@data-id='80336']").click()
        driver.find_element_by_id("dest").send_keys("hyd")
        time.sleep(5)
        driver.find_element_by_xpath("//ul[@class='autoFill']//li[@data-id='66341']").click()
        time.sleep(10)
        driver.find_element_by_xpath("//label[contains(text(),'Onward Date')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[@class='rb-calendar']//td[@class='wd day']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//label[contains(text(),'Return Date')]").click()
        driver.find_element_by_xpath("//div[@id='rb-calendar_return_cal']//td[@class='next']").click()
        driver.find_element_by_xpath("//div[@id='rb-calendar_return_cal']//td[starts-with(text(),5)]").click()
        time.sleep(3)
        driver.find_element_by_id("search_btn").click()
        time.sleep(2)
        print(driver.current_url)
        driver.back()
        print(driver.current_url)
        driver.forward()

        driver.close()

e=AutoComplete()
e.run()