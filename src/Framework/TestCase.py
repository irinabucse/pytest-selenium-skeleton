import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from allure_commons.types import AttachmentType


class TestCase(unittest.TestCase):
    # driver = None

    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)

        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities={'browserName': 'chrome', 'javascriptEnabled': True})

    @allure.step("Launch site")
    def launch_site(self):
        self.driver.get("http://qaboy.com/")
        self.takeScreenshot("Launch_site")

    @allure.step("Verify Title loaded")
    def verify_site(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "site-title")))
        self.takeScreenshot("Title loaded")

    def takeScreenshot(self, title):
        allure.attach(self.driver.get_screenshot_as_png(), title, attachment_type=AttachmentType.PNG)

    def tearDown(self):
        self.driver.close()