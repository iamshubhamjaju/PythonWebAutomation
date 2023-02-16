from selenium.webdriver.common.by import By


class ConfirmationPage:

    def __init__(self, driver):
        self.driver= driver

    # driver.find_element(By.ID, "country")
    Country = (By.ID, "country")
    # driver.find_element(By.LINK_TEXT, "India")
    CountrySelect = (By.LINK_TEXT, "India")
    # driver.find_element(By.XPATH, "//div[@class= 'checkbox checkbox-primary']")
    Checkbox = (By.XPATH, "//div[@class= 'checkbox checkbox-primary']")
    # driver.find_element(By.XPATH, "//input[@class= 'btn btn-success btn-lg']")
    Purchase = (By.XPATH, "//input[@class= 'btn btn-success btn-lg']")
    # driver.find_element(By.CLASS_NAME, "alert-success")
    Success = (By.CLASS_NAME, "alert-success")

    def getCountry(self):
        return self.driver.find_element(*ConfirmationPage.Country)

    def getCountrySelect(self):
        return self.driver.find_element(*ConfirmationPage.CountrySelect)

    def getCheckbox(self):
        return self.driver.find_element(*ConfirmationPage.Checkbox)

    def getPurchase(self):
        return self.driver.find_element(*ConfirmationPage.Purchase)

    def getSuccess(self):
        return self.driver.find_element(*ConfirmationPage.Success)
