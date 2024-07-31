from time import sleep
from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass


class TestTwo(BaseClass):

    def test_confirmCreatedOrder(self):
        data = self.userData()
        self.selectRegister()
        self.createUser(firstName=data[0], lastName=data[1], email=data[2], password=data[3])
        sleep(1)
        self.openHomePage()
        self.addToCartBy(by=By.XPATH, element="//*[@id='content']/div[2]/div[1]/div/div[1]")
        self.openHomePage()
        sleep(1)
        self.addToCartBy(by=By.XPATH, element="//*[@id='content']/div[2]/div[2]/div/div[1]")
        self.goToLink(link='http://localhost/en-gb?route=checkout/cart')
        self.goToLink(link='http://localhost/en-gb?route=checkout/checkout')
        self.shippingAddData(firstName=data[0], lastName=data[1])
        self.driver.find_element(By.XPATH, "//*[@id='button-shipping-address']").click()
        self.shippingAddMethod()
        self.paymentAddMethod()
        self.confirmOrder()
        sleep(1)
        self.selectOrdersHistory()
        assert self.driver.find_element(By.XPATH, "//*[@id='content']/div[1]/table/tbody/tr/td[4]").text == "Pending"
