import unittest

class UnitTestdemo(unittest.TestCase):

    def setUp(self):
        print("starting test")
    def test_method1(self):
        print("method1 is ran success")
    def test_method2(self):
        print("method2 is ran success")
    def tearDown(self):
        print("test ended")
if __name__ == '__main__':
    unittest.main(verbosity=2)