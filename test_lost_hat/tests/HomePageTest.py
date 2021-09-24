import unittest

from selenium import webdriver

from config.test_settings import TestSettings
from test_lost_hat.page_object import HomePage, ClothesPage, AccessoriesPage, ArtPage


class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = TestSettings.page_url_lost_hat
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_page_title(self):
        self.assertTrue(self.driver.title == HomePage.page_title)

    def test_clothes_menu_option(self):
        HomePage.click_drop_down_menu_item(self.driver, 3)
        self.assertTrue(self.driver.current_url == ClothesPage.clothes_page_url)

    def test_accessories_menu_option(self):
        HomePage.click_drop_down_menu_item(self.driver, 6)
        self.assertTrue(self.driver.current_url == AccessoriesPage.accessories_page_url)

    def test_art_menu_option(self):
        HomePage.click_drop_down_menu_item(self.driver, 9)
        self.assertTrue(self.driver.current_url == ArtPage.art_page_url)

    def test_slider_size(self):
        self.assertTrue(HomePage.check_slider_element_size(self.driver, 3))