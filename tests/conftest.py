import pytest
from selenium import webdriver
driver = None


@pytest.fixture(scope="class")
def setup(request):
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("http://localhost")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()