import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
       driver=webdriver.Chrome()
       print("launching chrome browser.....")
    elif browser=='Firefox':
        driver=webdriver.Firefox()
        print("launching firefox browser.....")
    return driver






    