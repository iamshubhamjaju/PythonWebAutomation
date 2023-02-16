import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from Utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage


class TestHomePage(BaseClass):

    def test_FormSubmission(self, getData):
        log = self.getLogger()
        # ID, Xpath, CSSSelectos, Classname, name, linktext
        homePage = HomePage(self.driver)
        log.info("first name is"+ getData["Name"])
        homePage.GetInputName().send_keys(getData["Name"])
        homePage.GetEmail().send_keys(getData["Email"])
        homePage.GetPassword().send_keys(getData["Password"])
        # Static dropdown (by index, select by visible text or select by value)
        self.SelectOptionByText(homePage.GetFormControl(), getData["Gender"])

        # if you want to create Xpath for any element //tagname[@attribute='value'] -> //input[@type='submit']
        # if you want to create custom CSS for any element tagname[attribute='value'] -> //input[@type='submit'], #id, .classname
        homePage.GetSubmit().click()
        message = homePage.GetAlertMessage().text
        print(message)
        assert "Success" in message

        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def getData(self, request):
        return request.param

