
from selenium import webdriver
import pytest


@pytest.fixture(params=['Browser Chrome', 'Browser FireFox'], scope="class")
def driver(request):
    global driver
    if request.param == 'Browser FireFox':
        driver = webdriver.Firefox()
        driver.maximize_window()

    elif request.param == 'Browser Chrome':
        driver = webdriver.Chrome()
        driver.maximize_window()

    yield driver
    driver.quit()


