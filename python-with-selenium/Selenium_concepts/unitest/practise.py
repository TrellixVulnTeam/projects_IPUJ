import pytest

class Test_Practise():

    @pytest.yield_fixture()
    def setup(self):
        print("Before every test case")
        yield
        print("After every test case")

    def test_1(setup):
        print("Good")
    def test_2(setup):
        print("Good")
