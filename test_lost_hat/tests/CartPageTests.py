import time
import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager

from config.test_settings import TestSettings
from test_lost_hat.page_object import HomePage, ClothesPage, AccessoriesPage, ArtPage, ProductsPage, \
    ProductAddedToCartPage, CartPage, OrderPage


class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        # driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        # driver = webdriver.Opera(executable_path=OperaDriverManager().install())
        self.url = TestSettings.page_url_lost_hat
        self.driver.get(self.url)
        self.driver.maximize_window()

        ProductsPage.add_product_to_cart(self.driver, 1)
        ProductAddedToCartPage.click_proceed_to_checkout_button(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_cart_block_text(self):
        self.assertEqual(CartPage.get_card_block_text(self.driver), CartPage.CARD_BLOCK_HEADER)

    def test_proceed_to_checkout_button(self):
        CartPage.click_proceed_to_checkout_button(self.driver)
        self.assertEqual(self.driver.current_url, OrderPage.CURRENT_URL)