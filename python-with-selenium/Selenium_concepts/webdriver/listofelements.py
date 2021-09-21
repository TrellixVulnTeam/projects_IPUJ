from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys
class practise():
    def testing(self):
        global driver
        url = input("Enter/paste your required url : ")
        a=input("In which browser do you want test Chrome/Firefox: ")
        if a=="Firefox":
            print("OK, redirecting your ", url, "in", a,"browser")
            driver = webdriver.Firefox(executable_path="D:\Drivers\geckodriver.exe")
        elif a == "Chrome":
            print("Ok, redirecting your ", url, "in", a,"browser")
            driver = webdriver.Chrome(executable_path="D:\Drivers\chromedriver.exe")
        else:
            print("please select your option again")
        driver.maximize_window()
        driver.get(url)
        by_class_name = driver.find_elements_by_class_name("inputs")
        length1=len(by_class_name)
        print("size of the class_name is : ",length1)
        if by_class_name is not None:
            print("class_name Found")
        by_tag_name = driver.find_elements_by_tag_name("h1")
        length2=len(by_tag_name)
        print("size of the tag_name is :",length2)
        if by_tag_name is not None:
            print("tag_name found")
        time.sleep(10)
p=practise()
p.testing()