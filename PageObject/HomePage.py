from selenium.webdriver.common.by import By
from PageObject.BasePage import BasePage


class HomePage(BasePage):
    filter_btn = (By.XPATH, '//*[contains(@class,"module_grid__btn_filter")]')
    request_status_cbo = (By.XPATH, '//*[@id="formControlsSelect"]')
    select_inactive_btn = (By.XPATH, '//*[@id="formControlsSelect"]/*[@value="inactive"]')
    apply_filter_btn = (By.XPATH, '//*[@class="btn-filter btn btn-default"]')
    request_status_column = '//tbody/tr/td[2]'
    first_name_column = (By.XPATH, '//tbody/tr/td[6]')
    sort_arrow_xpath = (By.XPATH, '//*[@data-field="firstName"]//*[@class="dropup table-sorting-dropup-icon"]')
    sort_caret_xpath = (By.XPATH, '//*[@class="caret table-sorting-clean-caret"]')

    def __init__(self, driver):
        super().__init__(driver)

    def click_filter_btn(self):
        self.click_action(self.filter_btn, 10)

    def select_filter_status(self, status):
        self.click_action(self.request_status_cbo)
        if status == 'Inactive':
            self.click_action(self.select_inactive_btn)

    def apply_filter(self):
        self.click_action(self.apply_filter_btn, 10)

    def verify_filter_status(self):
        status_list = []
        count_status = len(self.driver.find_elements_by_xpath(self.request_status_column))
        for index in range(1, count_status + 1):
            status = self.get_element_text((By.XPATH, '//tbody/tr['+str(index)+']/td[2]/div/p'))
            status_list.append(status)
        # print(status_list)
        return status_list

    def sort_descending(self):
        self.click_action(self.sort_arrow_xpath, 10)

    def sort_ascending(self):
        self.click_action(self.sort_arrow_xpath, 10)
        self.click_action(self.sort_caret_xpath, 10)

    def get_first_name_list(self):
        first_name_list = []
        count_name = self.count_element_action(self.first_name_column)
        for index in range(1, count_name + 1):
            first_name = self.get_element_text((By.XPATH, '//tbody/tr['+str(index)+']/td[6]'))
            first_name_list.append(first_name)
        return first_name_list

    def verify_sorting_first_name(self, sort_type):
        if sort_type == 'Ascending':
            self.sort_ascending()
            first_name_sort_asc = self.get_first_name_list()
            return first_name_sort_asc
        if sort_type == "Descending":
            self.sort_descending()
            first_name_sort_desc = self.get_first_name_list()
            return first_name_sort_desc


