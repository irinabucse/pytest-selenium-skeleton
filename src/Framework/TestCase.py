import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class TestCase(unittest.TestCase):

    @allure.step("Launch site")
    def launch_site(self):
        self.driver = webdriver.Remote(
           command_executor='http://127.0.0.1:4444/wd/hub',
           desired_capabilities={'browserName': 'chrome', 'javascriptEnabled': True})
        self.driver.get("http://qaboy.com/")

    @allure.step("Verify Title loaded")
    def verify_site(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "site-title")))

