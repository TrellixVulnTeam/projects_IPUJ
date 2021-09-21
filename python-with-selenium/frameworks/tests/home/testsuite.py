import unittest, logging
from frameworks.tests.home.login_tests import Frame
from frameworks.tests.home.login_tests_2 import Login_tests_2

tc_1 = unittest.TestLoader().loadTestsFromTestCase(Frame)
tc_2 = unittest.TestLoader().loadTestsFromTestCase(Login_tests_2)

smoke_test = unittest.TestSuite([tc_1])

unittest.TextTestRunner(verbosity=2).run(smoke_test)