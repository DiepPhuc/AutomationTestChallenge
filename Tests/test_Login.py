from Config.config import TestData
from PageObject.LoginPage import LoginPage
from PageObject.HomePage import HomePage
from Tests.test_base import BaseTest


class TestLogin(BaseTest):

    def test_log_in_with_valid_data(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = HomePage(self.driver)

        self.loginPage.set_account_info("phucdiep170794@gmail.com", "Test987654123@")
        self.loginPage.click_login()

        actual_title = self.homePage.get_home_page_title()
        assert actual_title == 'Expedia Travel: Vacation Homes, Hotels, Car Rentals, Flights & More'

    def test_log_in_with_invalid_data(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.set_account_info("asdcasdc@gmail.com", "Test987654123@")
        self.loginPage.click_login()
        self.loginPage.verify_error('You may have entered an unknown email address or an incorrect password.')

