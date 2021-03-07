from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser== 'chrome':
    driver=webdriver.Chrome()
    print("Launching Chrome browser.....")
    elif browser == 'Firefox':
    driver = webdriver.Firefox()
    print("Launching Firefox browser.....")
    else:
        driver= webdriver.Ie
    return driver

def pytest_addoption(parser): # This will get the value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): #This will return the browser value to setup method
    return request .config.getoption("--browser")

############# Pytest HTML Report#############
# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadeta['Project Name'] = 'nop Commerce'
    config._metadeta['Module Name'] = 'Customers'
    config._metadeta['Tester'] = 'Saranya'

# it is hook for delete/modify environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugin",None)

