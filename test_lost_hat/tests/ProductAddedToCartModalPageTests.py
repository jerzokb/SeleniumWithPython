import time
import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager

from config.test_settings import TestSettings
from test_lost_hat.page_object import HomePage, ClothesPage, AccessoriesPage, ArtPage, ProductsPage, \
    ProductAddedToCartPage, CartPage


class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        # driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        # driver = webdriver.Opera(executable_path=OperaDriverManager().install())
        self.url = TestSettings.page_url_lost_hat
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_modal_screen_is_displayed(self):
        ProductsPage.add_product_to_cart(self.driver, 1)
        self.assertTrue(ProductAddedToCartPage.is_moda_dialog_displayed(self.driver))

    def test_modal_screen_title_text(self):
        ProductsPage.add_product_to_cart(self.driver, 1)
        self.assertEqual(ProductAddedToCartPage.get_modal_screen_title_text(self.driver),
                         ProductAddedToCartPage.modalScreenTitle)

    def test_modal_screen_product_name(self):
        product_name = ProductsPage.get_product_title(self.driver, 1)
        ProductsPage.add_product_to_cart(self.driver, 1)
        self.assertEqual(ProductAddedToCartPage.get_modal_screen_product_name(self.driver).upper(),
                         product_name.upper())

    def test_modal_screen_product_price(self):
        product_price = ProductsPage.get_product_price(self.driver, 1)
        ProductsPage.add_product_to_cart(self.driver, 1)
        self.assertEqual(ProductAddedToCartPage.get_modal_screen_product_price(self.driver), product_price)

    def test_continue_shopping(self):
        ProductsPage.add_product_to_cart(self.driver, 1)
        ProductAddedToCartPage.click_continue_shopping_button(self.driver)
        self.assertTrue(ProductsPage.get_add_to_cart_button(self.driver))

    def test_proceed_to_checkout(self):
        ProductsPage.add_product_to_cart(self.driver, 1)
        ProductAddedToCartPage.click_proceed_to_checkout_button(self.driver)
        self.assertTrue(CartPage.is_card_block_display(self.driver))
