import unittest
from Selenium_concepts.unitest.test_class_1 import TestClass_1
from Selenium_concepts.unitest.test_class_2 import UnitDemo

#get all tests from test_class_1 & test_class_2
tc_1 = unittest.TestLoader().loadTestsFromTestCase(TestClass_1)
tc_2 = unittest.TestLoader().loadTestsFromTestCase(UnitDemo)

#create a suite combining test_class_1 & test_class_2
test_suite = unittest.TestSuite([tc_1,tc_2])

unittest.TextTestRunner(verbosity=2).run(test_suite)