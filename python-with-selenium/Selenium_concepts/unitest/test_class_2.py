import unittest

class UnitDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("---"*30)
        print("i will run only once before test execution")
        print("---" * 30)

    def setUp(self):
        print("starting test")
    def test_method1(self):
        print("method1 is ran success")
    def test_method2(self):
        print("method2 is ran success")
    def tearDown(self):
        print("test ended")

    @classmethod
    def tearDownClass(cls):
        print("---" * 30)
        print("i will run only once after test execution")
        print("---" * 30)

if __name__ == '__main__':
    unittest.main(verbosity=2)