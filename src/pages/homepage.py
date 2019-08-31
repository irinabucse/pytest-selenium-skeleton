import allure

from framework.base_page import BasePage


class Homepage:

    def __init__(self, driver, base_url, trailing_slash_flag):
        self.driver = driver
        self.trailing_slash_flag = trailing_slash_flag
        self.base_url = base_url
        # super().__init__(base_url, trailing_slash_flag)

    @allure.step("Launch site")
    def load(self):
        self.driver.get(self.base_url)
