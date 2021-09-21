import pytest

@pytest.fixture()
def setUp():
    print("print once before every test test case")
    yield
    print("print once after every test test case")
    
def test_1(setUp):
    print("Test_1 executed successfully")
def test_2(setUp):
    print("Test_2 executed successfully")