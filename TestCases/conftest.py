import pytest
from selenium import webdriver


@pytest.fixture()
def setup():

    driver = webdriver.Chrome(executable_path="C:/Driver/chromedriver_win32/chromedriver.exe")
    print("Launching Chrome browser.....")
    return driver



