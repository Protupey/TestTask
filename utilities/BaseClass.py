from time import sleep
from selenium.webdriver.support import expected_conditions as EC
import pytest
import random_address
import randominfo
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import random
import string

from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:
    def getPropertyBy(self, by, locatorname, propertyname):
        name = self.driver.find_element(by, locatorname).get_property(name=propertyname)
        return name

    def verifyElementPresence(self, by, locatorname):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((by, locatorname)))

    def randomFirstName(self):
        return randominfo.get_first_name(gender='male')

    def randomLastName(self):
        return randominfo.get_last_name()

    def randomEmail(self):
        user = ''.join(random.choice(string.ascii_letters) for _ in range(8))
        host = "gmail.com"
        return user + '@' + host

    def randomCompany(self):
        company = ''.join(random.choice(string.ascii_letters) for _ in range(8))
        return company

    def randomAddress(self):
        address = random_address.real_random_address()
        return address

    def randomPassword(self):
        return randominfo.random_password(length=8, special_chars=True, digits=True)

    def selectRegister(self):
        self.driver.find_element(By.XPATH, "//*[@id='top']/div/div[2]/ul/li[2]/div/a/span").click()
        self.driver.find_element(By.XPATH, "//*[@id='top']/div/div[2]/ul/li[2]/div/ul/li[1]/a").click()

    def selectLogout(self):
        self.driver.find_element(By.XPATH, "//*[@id='top']/div/div[2]/ul/li[2]/div/a/span").click()
        self.driver.find_element(By.XPATH, "//*[@id='top']/div/div[2]/ul/li[2]/div/ul/li[5]/a").click()

    def selectMyAccount(self):
        self.driver.find_element(By.XPATH, "//*[@id='top']/div/div[2]/ul/li[2]/div/a/span").click()
        self.driver.find_element(By.XPATH, "//*[@id='top']/div/div[2]/ul/li[2]/div/ul/li[1]/a").click()

    def selectOrdersHistory(self):
        self.driver.find_element(By.XPATH, "//*[@id='top']/div/div[2]/ul/li[2]/div/a/span").click()
        self.driver.find_element(By.XPATH, "//*[@id='top']/div/div[2]/ul/li[2]/div/ul/li[2]/a").click()

    def selectLogin(self):
        self.driver.find_element(By.XPATH, "//*[@id='top']/div/div[2]/ul/li[2]/div/a/span").click()
        self.driver.find_element(By.XPATH, "//*[@id='top']/div/div[2]/ul/li[2]/div/ul/li[2]/a").click()

    def login(self, email, password):
        self.driver.find_element(By.ID, "input-email").send_keys(email)
        self.driver.find_element(By.ID, "input-password").send_keys(password)
        self.driver.find_element(By.XPATH, "//*[@id='form-login']/div[3]/button").click()

    def createUser(self, firstName, lastName, email, password):
        self.driver.find_element(By.ID, "input-firstname").send_keys(firstName)
        self.driver.find_element(By.ID, "input-lastname").send_keys(lastName)
        self.driver.find_element(By.ID, "input-email").send_keys(email)
        self.driver.find_element(By.ID, "input-password").send_keys(password)
        self.driver.find_element(By.NAME, "agree").click()
        self.driver.find_element(By.XPATH, "//*[@id='form-register']/div/button").click()

    def changePassword(self, password):
        self.driver.find_element(By.ID, "input-password").send_keys(password)
        self.driver.find_element(By.ID, "input-confirm").send_keys(password)
        self.driver.find_element(By.XPATH, "//*[@id='form-password']/div/div[2]/button").click()

    def userData(self):
        firstName = self.randomFirstName()
        lastName = self.randomLastName()
        email = self.randomEmail()
        password = self.randomPassword()
        data = (firstName, lastName, email, password)
        return data

    def shippingAddData(self, firstName, lastName):
        address = self.randomAddress()
        #country = address.get('state') #could not randomize due to missing values
        #city = address.get('city') #could not randomize due to missing values
        self.driver.find_element(By.ID, "input-shipping-firstname").send_keys(firstName)
        self.driver.find_element(By.ID, "input-shipping-lastname").send_keys(lastName)
        self.driver.find_element(By.ID, "input-shipping-company").send_keys(self.randomCompany())
        self.driver.find_element(By.ID, "input-shipping-address-1").send_keys(address.get('address1'))
        self.driver.find_element(By.ID, "input-shipping-address-2").send_keys(address.get('address2'))
        self.driver.find_element(By.ID, "input-shipping-city").send_keys(address.get('city'))
        self.driver.find_element(By.ID, "input-shipping-postcode").send_keys(address.get('postalCode'))
        self.driver.find_element(By.ID, "input-shipping-country").send_keys("s") #could not randomize due to missing values
        self.driver.find_element(By.ID, "input-shipping-zone").send_keys("s") #could not randomize due to missing values


    def shippingAddMethod(self):
        self.driver.find_element(By.ID, "button-shipping-methods").click()
        self.driver.find_element(By.ID, "input-shipping-method-flat-flat").click()
        self.driver.find_element(By.ID, "button-shipping-method").click()

    def paymentAddMethod(self):
        self.driver.find_element(By.ID, "button-payment-methods").click()
        self.driver.find_element(By.ID, "input-payment-method-cod-cod").click()
        self.driver.find_element(By.ID, "button-payment-method").click()

    def goToLink(self, link):
        self.driver.get(link)

    def openHomePage(self):
        self.driver.find_element(By.XPATH, "//*[@id='logo']/a/img").click()

    def addToCartBy(self, by, element):
        self.driver.find_element(by, element).click()
        self.driver.find_element(By.ID, "button-cart").click()
        sleep(1)

    def clearTextFields(self):
        elements = ["input", "input-email", "input-password", "input-confirm", "input-firstname", "input-lasttname",
                    "input-shipping-firstname", "input-shipping-lastname", "input-shipping-company",
                    "input-shipping-address-1", "input-shipping-address-2", "input-shipping-postcode"]
        for i in elements:
            if self.driver.find_elements(By.ID, str(i)):
                self.driver.find_element(By.ID, str(i)).clear()
            else:
                continue

    def confirmOrder(self):
        iframe = self.driver.find_element(By.ID, 'button-confirm')
        ActionChains(self.driver) \
            .scroll_to_element(iframe) \
            .perform()
        self.driver.find_element(By.ID, 'button-confirm').click()
