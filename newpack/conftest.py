from selenium import webdriver
import pytest
from newpack.data import MAIN_PAGE_URL


@pytest.fixture(scope="session")
def chrome_drv():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get(MAIN_PAGE_URL)
    return driver




