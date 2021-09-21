from selenium import webdriver
class Test():
    def firefox(self):
        driver=webdriver.Firefox(executable_path="D:\Drivers\geckodriver.exe")
        driver.maximize_window()
        driver.get("https://www.facebook.com")
t=Test()
t.firefox()
