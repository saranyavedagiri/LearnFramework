import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage

class Test_001_Login:
    URL = "http://admin-demo.nopcommerce.com/"
    useremail = "admin@yourstore.com"
    password = "admin"

    def test_homePageTitle(self, setup):
        self.driver = setup
        self.driver.get(self.URL)
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Your store. Login":
            assert True
        else:
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.URL)
        self.lp=LoginPage(self.driver)
        self.lp.enteruseremail(self.useremail)
        self.lp.enterpassword(self.password)
        self.lp.clicklogin()
        act_title = self.driver.title
       # self.driver.close()
        if act_title == "Dashboard / nopCommerce administration":
            assert True
        else:
            assert False

