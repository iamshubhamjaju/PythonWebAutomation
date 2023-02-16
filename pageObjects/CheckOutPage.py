from selenium.webdriver.common.by import By

from pageObjects.ConfirmationPage import ConfirmationPage


class checkoutpage:

    def __init__(self, driver):
        self.driver = driver  # constructor for driver

    # driver.find_elements(By.XPATH, "//div[@class='card h-100']")
    cardTitle = (By.XPATH, "//div[@class='card h-100']")
    # driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']")
    Checkout = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    # driver.find_element(By.XPATH, "//button[@class='btn btn-success']")
    CheckoutItems = (By.XPATH, "//button[@class='btn btn-success']")

    def getCardTitles(self):
        return self.driver.find_elements(*checkoutpage.cardTitle)

    def getCheckout(self):
        return self.driver.find_element(*checkoutpage.Checkout)

    def getCheckoutItems(self):
        self.driver.find_element(*checkoutpage.CheckoutItems).click()
        confirmPage = ConfirmationPage(self.driver)
        return confirmPage
