from time import sleep
from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_ChangePassword(self):
        data = self.userData()
        newpassword = self.randomPassword()
        self.selectRegister()
        self.createUser(firstName=data[0], lastName=data[1], email=data[2], password=data[3])
        sleep(1)
        self.selectMyAccount()
        self.driver.find_element(By.XPATH, "//*[@id='content']/ul[1]/li[2]/a").click()
        self.changePassword(password=newpassword)
        sleep(1)
        self.selectLogout()
        sleep(1)
        self.selectLogin()
        # User can not login under old password
        self.login(email=data[2], password=data[3])
        assert self.driver.find_element(By.ID, "form-login")
        # User can login under new password
        self.driver.find_element(By.ID, "input-email").clear()
        self.driver.find_element(By.ID, "input-password").clear()
        #self.clearTextFields()
        self.login(email=data[2], password=newpassword)
        self.driver.find_element(By.XPATH, "//*[@id='content']/ul[1]/li[1]/a").click()
        assert self.getPropertyBy(by=By.ID, locatorname="input-firstname", propertyname="value") == data[0]
        assert self.getPropertyBy(by=By.ID, locatorname="input-lastname", propertyname="value") == data[1]
        assert self.getPropertyBy(by=By.ID, locatorname="input-email", propertyname="value") == data[2]
