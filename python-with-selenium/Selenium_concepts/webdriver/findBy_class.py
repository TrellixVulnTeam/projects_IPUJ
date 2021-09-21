from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class By_class():
    def test_by(self):
        driver=webdriver.Firefox()
        print("Firefox opened successfully")
        driver.maximize_window()
        url="https://letskodeit.teachable.com/pages/practice"
        print("redirecting to", url)
        driver.get(url)
        driver.maximize_window()
        by_id=driver.find_element(By.ID,"name")
        if by_id is not None:
            print("by_id found")
        by_name=driver.find_element(By.NAME,"show-hide")
        if by_name is not None:
            print("by_name is found")
        by_link_text=driver.find_element(By.LINK_TEXT,"Login")
        if by_link_text is not None:
            print("by_link_name is found")
        by_partial_link_text=driver.find_element(By.PARTIAL_LINK_TEXT,"Pract")
        if by_partial_link_text is not None:
            print("by_partial_link_name is found")
        by_xpath = driver.find_element(By.XPATH,"//input[@id='name']")
        if by_xpath is not None:
            print("xpath Found")
        by_css = driver.find_element(By.CSS_SELECTOR,"#displayed-text")
        if by_css is not None:
            print("css_selector found")
        by_class_name = driver.find_element(By.CLASS_NAME,"displayed-class")
        if by_class_name is not None:
            print("class_name Found")
        by_tag_name = driver.find_element(By.TAG_NAME,"h1")
        if by_tag_name is not None:
            print("tag_name found")
b=By_class()
b.test_by()
print("Code executed successfully")