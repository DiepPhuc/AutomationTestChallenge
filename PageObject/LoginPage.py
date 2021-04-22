from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as e

from Config.config import TestData
from PageObject.BasePage import BasePage


class LoginPage(BasePage):
    email_locator = (By.XPATH, '//*[@id="user_email"]')
    password_locator = (By.XPATH, '//*[@id="user_password"]')
    login_btn = (By.XPATH, '//*[@value="Submit"]')
    status = (By.XPATH, '//*[@class="panel-body"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def set_account_info(self, email, password):
        self.send_keys_action(self.email_locator, email)
        self.send_keys_action(self.password_locator, password)

    def click_login(self):
        self.click_action(self.login_btn, 10)

    def verify_status(self, expected_status):
        actual_status = self.get_element_text(self.status)
        assert actual_status in expected_status

