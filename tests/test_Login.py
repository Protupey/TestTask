from time import sleep
from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_registartionValidation(self):
        data = self.userData()
        self.selectRegister()
        self.createUser(firstName=data[0], lastName=data[1], email=data[2], password=data[3])
        sleep(1)
        self.selectLogout()
        sleep(1)
        self.selectLogin()
        self.login(email=data[2], password=data[3])
        self.driver.find_element(By.XPATH, "//*[@id='content']/ul[1]/li[1]/a").click()
        assert self.getPropertyBy(by=By.ID, locatorname="input-firstname", propertyname="value") == data[0]
        assert self.getPropertyBy(by=By.ID, locatorname="input-lastname", propertyname="value") == data[1]
        assert self.getPropertyBy(by=By.ID, locatorname="input-email", propertyname="value") == data[2]