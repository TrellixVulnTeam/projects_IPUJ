from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
import time

from selenium.common.exceptions import NoSuchElementException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Expedia():
    def run(self):
        url="https://www.redbus.com/"
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(10)
        onward=driver.find_element_by_xpath("//label[contains(text(),'Onward Date')]")
        onward.click()
        time.sleep(3)
        date=driver.find_element_by_xpath("//div[@id='rb-calendar_onward_cal']")
        disable=date.find_elements(By.TAG_NAME,"td")
        for x in disable:
                if x.text == "30":
                    x.click()
                    break
        # date.click()
        # wait=WebDriverWait(driver,10,1,ignored_exceptions=[NoSuchElementException,ElementNotSelectableException])
        # date=wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Nov 26, 2020, date disabled']")))
        print(date.is_enabled())
        time.sleep(10)
        driver.quit()

e=Expedia()
e.run()