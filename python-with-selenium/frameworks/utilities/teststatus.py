import frameworks.utilities.custom_logger as cl
import logging
from traceback import print_stack
from frameworks.base.base import Webdriver

class TestStatus(Webdriver):

    log = cl.customLogger(logging.INFO)

    def __init__(self, driver):
        """
        Inits CheckPoint class
        """
        super(TestStatus, self).__init__(driver)
        self.resultList = []

    def setResult(self, result, resultmessage):
        try:
            if result is not None:
                if result:
                    self.resultList.append("PASS")
                    self.log.info("TEST CASE PASSED :: + " + resultmessage)
                else:
                    self.resultList.append("FAIL")
                    self.log.error("TEST CASE FAILED :: + " + resultmessage)
                    self.take_screenshot(resultmessage)
            else:
                self.resultList.append("FAIL")
                self.log.error("TEST CASE FAILED :: + " + resultmessage)
                self.take_screenshot(resultmessage)
        except:
            self.resultList.append("FAIL")
            self.log.error("Exception Occurred")
            self.take_screenshot(resultmessage)
            print_stack()

    def mark(self, result, resultMessage):
        """
        Mark the result of the verification point in a test case
        """
        self.setResult(result, resultMessage)

    def markFinal(self, testName, result, resultmessage):
        """
        Mark the final result of the verification point in a test case
        This needs to be called at least once in a test case
        This should be final test status of the test case
        """
        self.setResult(result, resultmessage)

        if "FAIL" in self.resultList:
            self.log.error(testName +  "  TEST FAILED")
            self.resultList.clear()
            assert True == False
        else:
            self.log.info(testName + "  TEST SUCCESSFUL")
            self.resultList.clear()
            assert True == True