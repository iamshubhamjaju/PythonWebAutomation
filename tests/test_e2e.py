from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Utilities.BaseClass import BaseClass
from pageObjects.CheckOutPage import checkoutpage
from pageObjects.ConfirmationPage import ConfirmationPage
from pageObjects.HomePage import HomePage


class TestOne(BaseClass):

    def test_e2e(self):
        # //a[contains(@href,'shop')]- Regular expression (a is tag name, @href is attribute , shop is value)
        # a[href*='shop'] - css expression
        log = self.getLogger()
        homePage = HomePage(self.driver)
        Checkoutpage = homePage.shopItems()
        log.info("Getting all the card items")
        products = Checkoutpage.getCardTitles()
        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            log.info(productName)
            if productName == "Blackberry":
                product.find_element(By.XPATH, "div/button").click()

        Checkoutpage.getCheckout().click()
        confirmPage = Checkoutpage.getCheckoutItems()
        log.info("Entering Country Name as ind")
        confirmPage.getCountry().send_keys("ind")
        self.verifyLinkPresence("India")
        confirmPage.getCountrySelect().click()
        confirmPage.getCheckbox().click()
        confirmPage.getPurchase().click()
        successText = confirmPage.getSuccess().text
        log.info("Text received from application is" + successText)

        assert "Success! Thank you!" in successText
        self.driver.close()









