from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import time

class WaitTypes():
    def types(self):
        # #implicit_wait
        # url="https://www.expedia.co.in/"
        # driver=webdriver.Chrome()
        # driver.maximize_window()
        # driver.get(url)
        # driver.implicitly_wait(10)
        # flights=driver.find_element_by_xpath("//a[@aria-controls='wizard-flight-pwa']")
        # flights.click()
        # leaving=driver.find_element_by_xpath("//button[@aria-label='Leaving from']")
        # leaving.send_keys("SFO",Keys.ENTER)
        # leaving.send_keys(Keys.ENTER)
        # time.sleep(10)
        # going=driver.find_element_by_xpath("//button[@aria-label='Going to']")
        # going.send_keys("NYC",Keys.ENTER)
        # time.sleep(10)
        # submit=driver.find_element_by_xpath("//button[@type='submit']")
        # submit.click()
        # time.sleep(20)

        url = "https://www.expedia.co.in/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(10)
        flights = driver.find_element_by_xpath("//a[@aria-controls='wizard-flight-pwa']")
        flights.click()
        leaving = driver.find_element_by_xpath("//button[@aria-label='Leaving from']")
        leaving.send_keys("SFO", Keys.ENTER)
        leaving.send_keys(Keys.ENTER)
        going = driver.find_element_by_xpath("//button[@aria-label='Going to']")
        going.send_keys("NYC", Keys.ENTER)
        submit = driver.find_element_by_xpath("//button[@type='submit']")
        submit.click()
        wait=WebDriverWait(driver,timeout=10,poll_frequency=1,ignored_exceptions=[NoSuchElementException,ElementNotVisibleException,ElementNotSelectableException])
        element=wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='airlineRowContainer_AS']")))
        element.click()
        time.sleep(10)


w=WaitTypes()
w.types()