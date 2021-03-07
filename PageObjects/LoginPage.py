class LoginPage:
    textbox_useremail_id = "Email"
    textbox_password_id = "Password"
    Button_login_Xpath = "//body/div[6]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[3]/input[1]"
    link_logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def enteruseremail(self, useremail):
        self.driver.find_element_by_id(self.textbox_useremail_id).clear()
        self.driver.find_element_by_id(self.textbox_useremail_id).send_keys(useremail)

    def enterpassword(self,password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clicklogin(self):
        self.driver.find_element_by_xpath(self.Button_login_Xpath).click()

    def clicklogout(self):
        self.driver.find_element_by_xpath(self.link_logout_linktext).click()

