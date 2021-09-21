from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class Practise():
    def test1(self):
        global driver
        url=input("Enter your url : ")
        browser=input("In which browser you want to open select 1 or 2 \n1.Chrome 2.Firefox \n")
        if browser==str(1) or browser=="Chrome":
            print("OK redirecting your "+url+" in Chrome browser")
            driver=webdriver.Chrome()
        elif browser==str(2) or browser=="Firefox":
            print("OK redirecting your " + url + " in Firefox browser")
            driver = webdriver.Firefox()
        pass
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(10)
        login=driver.find_element(By.XPATH, "//a[@href='/sign_in']")
        login.click()
        email=driver.find_element(By.XPATH, "//input[@id='user_email']")
        email.send_keys("email")
        password=driver.find_element(By.XPATH, "//input[@id='user_password']")
        password.send_keys("password")
        time.sleep(5)
        email.clear()
        password.clear()
        time.sleep(2)
p = Practise()
p.test1()