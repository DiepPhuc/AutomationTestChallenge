from Config.config import TestData
from PageObject.LoginPage import LoginPage
from PageObject.HomePage import HomePage
from Tests.test_base import BaseTest


class TestFilter(BaseTest):

    def test_filter_inactive_status(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = HomePage(self.driver)

        # Login Action
        self.loginPage.set_account_info(TestData.USER_NAME, TestData.PASSWORD)
        self.loginPage.click_login()

        # Filter Inactive status and verify
        self.homePage.click_filter_btn()
        self.homePage.select_filter_status(TestData.INACTIVE_STATUS)
        self.homePage.apply_filter()
        status_list = self.homePage.verify_filter_status()
        for actual_status in status_list:
            assert actual_status == TestData.INACTIVE_STATUS, "Status doesn't contain only Inactive"

