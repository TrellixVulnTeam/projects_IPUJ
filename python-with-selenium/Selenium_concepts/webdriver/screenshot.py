from selenium import webdriver
from python_concepts.utilities.handywrappers import HandyWrappers
import time

class ScreenShot():
    def run(self):
        url="https://letskodeit.teachable.com/"
        driver=webdriver.Chrome()
        driver.maximize_window()
        hw=HandyWrappers(driver)
        driver.get(url)
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("//a[contains(text(),'Login')]").click()
        driver.find_element_by_id("user_email").send_keys("abc@emailcom")
        driver.find_element_by_id("user_password").send_keys("abc")
        driver.find_element_by_xpath("//input[@value='Log In']").click()
        time.sleep(10)
        driver.get_screenshot_as_file()
        # destination_name="D:\screenshots\check.png"
        # try:
        #     driver.save_screenshot(destination_name)
        #     print("saving screenshot in "+destination_name)
        # except NotADirectoryError:
        #     print("directory issue")
        #use the below generic method
        hw.take_screeshot(driver)

e=ScreenShot()
e.run()