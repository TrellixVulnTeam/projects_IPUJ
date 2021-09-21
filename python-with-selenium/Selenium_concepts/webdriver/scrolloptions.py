from selenium import webdriver
import time

class ScrollingElements():
    def test(self):
        url="https://letskodeit.teachable.com/p/practice"
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(10)
        print(driver.get_window_size())
        # Scroll Down
        driver.execute_script("window.scrollBy(0,1600);")
        time.sleep(10)
        #Scroll Up
        driver.execute_script("window.scrollBy(0,-1600);")
        time.sleep(10)
        #Scroll element to view
        element=driver.find_element_by_id("mousehover")
        driver.execute_script("arguments[0].scrollIntoView(true);",element) #return element into view
        time.sleep(10)
        driver.execute_script("window.scrollBy(0,-250);")
        time.sleep(10)
        # Native way  to scroll element into view
        location = element.location_once_scrolled_into_view #returns the element to topleftcorner of the screen
        print(location)
        time.sleep(10)

e=ScrollingElements()
e.test()