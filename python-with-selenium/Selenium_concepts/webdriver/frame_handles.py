from selenium import webdriver

import time


class ScrollingElements():
    def test(self):
        url="https://letskodeit.teachable.com/p/practice"
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(10)
# switching to frame using id , name, numbers
        #driver.switch_to.frame("courses-iframe") #by id
 #       driver.switch_to.frame("iframe-name")  # by name
        driver.switch_to.frame(0) #in the given url only one frame so frame is 0
        element = driver.find_element_by_xpath("//body[@marginheight='0']//button[@class='navbar-toggle']")
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(10)
        driver.find_element_by_id("search-courses").send_keys("python")
        time.sleep(10)
# switching to default content
        driver.switch_to.default_content() #use either parent_frame or default_content both will work
  #      driver.switch_to.parent_frame()
        element1 = driver.find_element_by_xpath("//legend[contains(text(),'Checkbox Example')]")
        driver.execute_script("arguments[0].scrollIntoView(true);",element1)
        time.sleep(2)
        checkbox = driver.find_elements_by_xpath("//input[@type='checkbox']")
        for check in checkbox:
            is_selected = check.is_selected()
            if not is_selected:
                check.click()
                time.sleep(3)
        
e=ScrollingElements()
e.test()