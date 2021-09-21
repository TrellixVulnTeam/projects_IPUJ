from selenium import webdriver
import time
import logging
"""
logging levels - 
DEBUG
INFO
WARNING
ERROR
CRITICAL
logging formats - 
https://docs.python.org/3/library/logging.html#logrecord-attributes
https://docs.python.org/3/library/time.html#time.strftime
"""

class Logging():
    def test(self):
        logging.basicConfig(filename='D:\screenshots\cest.log', format='%(asctime)s: %(levelname)s: %(message)s',
                             datefmt='%d-%m-%Y %I:%M:%S %p', level=logging.DEBUG)

        logging.info("info message")
        logging.warning("warning message")
        logging.error("error message")
        logging.critical("critical message")
        #D:\screenshots\cest.log"

b = Logging()
b.test()