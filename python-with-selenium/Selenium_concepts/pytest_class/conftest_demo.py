import pytest

@pytest.fixture()
def setUp():
    print("Running before test case")
    yield
    print("Running after test case")
