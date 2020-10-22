from Config.config import TestData
from PageObject.LoginPage import LoginPage
from PageObject.HomePage import HomePage
from Tests.test_base import BaseTest


class TestSortColumnData(BaseTest):

    def test_sort_first_name_with_descending(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = HomePage(self.driver)
        # Login Action
        self.loginPage.set_account_info(TestData.USER_NAME, TestData.PASSWORD)
        self.loginPage.click_login()
        # Get first name list before sorting
        first_name_list = self.homePage.get_first_name_list()
        # Sort expected list to ascending to verify with actual list
        expected_first_name_list = sorted(first_name_list, reverse=True)
        print(expected_first_name_list)
        # Verify sorting ascending function
        actual_first_name_list = self.homePage.verify_sorting_first_name('Descending')
        assert expected_first_name_list == actual_first_name_list, "The first name doesn't sort as expected"

    def test_sort_first_name_with_ascending(self):
        self.homePage = HomePage(self.driver)
        # Get first name list before sorting
        first_name_list = self.homePage.get_first_name_list()
        # Sort expected list to ascending to verify with actual list
        expected_first_name_list = sorted(first_name_list)
        print(expected_first_name_list)
        # Verify sorting ascending function
        actual_first_name_list = self.homePage.verify_sorting_first_name('Ascending')
        assert expected_first_name_list == actual_first_name_list, "The first name doesn't sort as expected"
