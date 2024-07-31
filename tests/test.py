from selenium import webdriver
from selenium.webdriver.common.by import By

driver = None

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://localhost/en-gb?route=account/login")
driver.find_element(By.ID, "input-email").send_keys("Hello")
driver.find_element(By.ID, "input-password").send_keys("World")
elements = ["input", "input-email", "input-password", "input-confirm"]
for i in elements:
    if driver.find_elements(By.ID, str(i)):
        driver.find_element(By.ID, str(i)).clear()
    else:
        continue