from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as e

from Config.config import TestData
from PageObject.BasePage import BasePage


class LoginPage(BasePage):
    email_locator = (By.XPATH, '//*[@id="signin-loginid"]')
    password_locator = (By.XPATH, '//*[@id="signin-password"]')
    login_btn = (By.XPATH, '//*[@id="submitButton"]')
    email_error = (By.XPATH, '//*[@class="alert-message""]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def set_account_info(self, email, password):
        self.send_keys_action(self.email_locator, email)
        self.send_keys_action(self.password_locator, password)

    def click_login(self):
        self.click_action(self.login_btn, 10)

    def verify_error(self, expected_error):
        actual_error = self.BasePage.get_element_text(self.email_error)
        assert expected_error in actual_error, "Text not found %s" % expected_error

