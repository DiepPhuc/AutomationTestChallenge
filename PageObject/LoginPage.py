from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as e

from Config.config import TestData
from PageObject.BasePage import BasePage


class LoginPage(BasePage):
    email_locator = (By.XPATH, '//*[@type="email"]')
    password_locator = (By.XPATH, '//*[@type="password"]')
    login_btn = (By.XPATH, '//*[@class="col-login__btn"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def get_login_page_title(self, title):
        return self.get_title(title)

    def set_account_info(self, email, password):
        self.send_keys_action(self.email_locator, email)
        self.send_keys_action(self.password_locator, password)

    def click_login(self):
        self.click_action(self.login_btn, 10)

