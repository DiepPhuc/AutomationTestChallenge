from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# This class contains generic methods and utilities for all pages


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def count_element_action(self, by_locator):
        count_element = len(WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(by_locator)))
        return count_element

    def click_action(self, by_locator, time_out):
        WebDriverWait(self.driver, time_out).until(EC.element_to_be_clickable(by_locator)).click()

    def send_keys_action(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def get_title(self, title, main_region):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(main_region))
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title
