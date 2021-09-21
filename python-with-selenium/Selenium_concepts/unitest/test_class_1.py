import unittest

class TestClass_1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("--"*30)
        print("execution started")
        print("--" * 30)
    def setUp(self):
        print("printed before test case")
    def test_class1(self):
        print("class 1 printed successfully")
    def test_class2(self):
        print("class 2 printed successfully")
    def test_class3(self):
        print("class 3 printed successfully")
    def tearDown(self):
        print("printed before test case")

    @classmethod
    def tearDownClass(cls):
        print("--" * 30)
        print("execution completed")
        print("--" * 30)

if __name__ == '__main__':
    if __name__ == '__main__':
        unittest.main(verbosity=2)
