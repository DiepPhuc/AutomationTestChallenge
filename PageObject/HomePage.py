from selenium.webdriver.common.by import By
from PageObject.BasePage import BasePage


class HomePage(BasePage):
    main_region = (By.XPATH, '//*[@data-testid="main-region"]')

    def __init__(self, driver):
        super().__init__(driver)

    def get_home_page_title(self):
        return self.get_title(self.driver.title, self.main_region)



