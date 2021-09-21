import unittest
#if assert fails at one step then it will not perform the next step in the same method so it will skip to next method
class AssertClassDemo(unittest.TestCase):

    def test_assertequalnotequal(self):
        a = "Hello"
        b = "Hello"
        c = "python"
        self.assertEqual(a,b, msg="a & b is not equal")
        self.assertNotEqual(a,c, msg='a & c is equal')
    def test_truefalse(self):
        a = True
        self.assertTrue(a,"a is not true")
        a = False
        self.assertFalse(a,"a is not false")


if __name__ == '__main__':
    unittest.main(verbosity=2)
