import unittest

from selenium import webdriver

from config.test_settings import TestSettings
from test_lost_hat.page_object import HomePage, ClothesPage, AccessoriesPage, ArtPage, ProductsPage


class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = TestSettings.page_url_lost_hat
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_select_product_item(self):
        ProductsPage.click_on_product_item(self.driver, 1)
        self.assertTrue(ProductsPage.get_add_to_cart_button(self.driver))

    def test_selected_product_name(self):
        product_name = ProductsPage.get_product_title(self.driver, 1)
        ProductsPage.click_on_product_item(self.driver, 1)
        selected_product_name = ProductsPage.get_selected_product_name(self.driver)
        self.assertEqual(product_name.upper(), selected_product_name.upper())

    def test_selected_product_price(self):
        product_price = ProductsPage.get_product_price(self.driver, 1)
        ProductsPage.click_on_product_item(self.driver, 1)
        selected_product_price = ProductsPage.get_selected_product_price(self.driver)
        self.assertEqual(product_price.upper(), selected_product_price.upper())

