from selenium import webdriver
from time import sleep

class ScrollingElements():
    def test(self):
        url="https://courses.letskodeit.com/practice"
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(10)
        element = driver.find_element_by_id("name")
        print(element.is_displayed())
        element.send_keys("Mahesh")
        sleep(10)
        driver.find_element_by_id("alertbtn").click()
        sleep(5)
        alertpopup = driver.switch_to.alert
        alertpopup.accept()
        sleep(5)
        confirm  = driver.find_element_by_id("confirmbtn")
        confirm.click()
        confirmbtn = driver.switch_to.alert
        sleep(5)
        confirmbtn.dismiss()
        sleep(5)
        confirm.click()
        sleep(5)
        confirmbtn.accept()
        sleep(5)
e=ScrollingElements()
e.test()