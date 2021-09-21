from selenium import webdriver
from frameworks.base.base import Webdriver
from selenium.webdriver.common.keys import Keys
import time


class Expedia():
    def run(self):
        url="https://www.expedia.co.in/"
        driver=webdriver.Chrome()
        hw=Webdriver(driver)
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(10)
        flights=hw.get_element("//a[@aria-controls='wizard-flight-pwa']","xpath")
        flights.click()
        leaving = hw.get_element("//button[@aria-label='Leaving from']","xpath")
        leaving.send_keys("SFO",Keys.ENTER)
        time.sleep(3)
        going = hw.get_element("//button[@aria-label='Going to']","xpath")
        going.send_keys("NYC", Keys.ENTER)
        time.sleep(3)
        submit = hw.get_element("//button[@type='submit']","xpath")
        submit.click()
        change = hw.wait("//input[@id='changeOptionFilter-0']","xpath",10,1)
        change.click()
        time.sleep(10)
e=Expedia()
e.run()