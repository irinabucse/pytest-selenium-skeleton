import unittest

from framework.page_factory import PageFactory
from framework.test_case import TestCase


class TestHomepage(TestCase):
    url = "http://qaboy.com/"

    def test_page_load_test(self):
        homepage = PageFactory.get_page_object(self.driver, 'homepage', self.url)
        homepage.load()
        self.takeScreenshot("Launch_site: " + self.url)
        self.verify_page_loaded(homepage)

