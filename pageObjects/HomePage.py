from selenium.webdriver.common.by import By

from pageObjects.CheckOutPage import checkoutpage


class HomePage:

    def __init__(self, driver):
        self.driver = driver  # constructor for driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")  # Tuple, declared shop locator

    # find_element(By.CSS_SELECTOR, "input[name='name']")
    InputName = (By.CSS_SELECTOR, "input[name='name']")

    # find_element(By.NAME, "email")
    Email = (By.NAME, "email")

    # find_element(By.ID, "exampleInputPassword1")
    Password = (By.ID, "exampleInputPassword1")

    # find_element(By.ID, "exampleFormControlSelect1")
    FormControl = (By.ID, "exampleFormControlSelect1")

    # find_element(By.XPATH, "//input[@type='submit']")
    Submit = (By.XPATH, "//input[@type='submit']")

    # driver.find_element(By.CLASS_NAME, "alert-success")
    Alert = (By.CLASS_NAME, "alert-success")

    def shopItems(self):

        self.driver.find_element(*HomePage.shop).click()
        Checkoutpage = checkoutpage(self.driver)
        return Checkoutpage

        # Shop link is interlinked to homepage and checkout page
        # self.driver is instance variable
        # driver.find_element(By.CSS_SELECTOR, "a[href*='shop']")

    def GetInputName(self):
        return self.driver.find_element(*HomePage.InputName)

    def GetEmail(self):
        return self.driver.find_element(*HomePage.Email)

    def GetPassword(self):
        return self.driver.find_element(*HomePage.Password)

    def GetFormControl(self):
        return self.driver.find_element(*HomePage.FormControl)

    def GetSubmit(self):
        return self.driver.find_element(*HomePage.Submit)

    def GetAlertMessage(self):
        return self.driver.find_element(*HomePage.Alert)








