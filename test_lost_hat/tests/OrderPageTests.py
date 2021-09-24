import time
import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager
from faker import Faker

from config.test_settings import TestSettings
from test_lost_hat.page_object import HomePage, ClothesPage, AccessoriesPage, ArtPage, ProductsPage, \
    ProductAddedToCartPage, CartPage, OrderPage

faker = Faker()
fake_first_name = faker.first_name()
fake_last_name = faker.last_name()
fake_email = faker.email()
fake_company = faker.company()
fake_address = faker.address()
fake_postal_code = "12-345"
fake_city = faker.city()
fake_phone = "123-456-789"


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

        CartPage.click_proceed_to_checkout_button(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_first_step_title(self):
        self.assertIn(OrderPage.FIRST_STEP_TITLE.upper(), OrderPage.get_step_title_text(self.driver, 0))

    def test_second_step_title(self):
        self.assertIn(OrderPage.SECOND_STEP_TITLE.upper(), OrderPage.get_step_title_text(self.driver, 1))

    def test_third_step_title(self):
        self.assertIn(OrderPage.THIRD_STEP_TITLE.upper(), OrderPage.get_step_title_text(self.driver, 2))

    def test_fourth_step_title(self):
        self.assertIn(OrderPage.FOURTH_STEP_TITLE.upper(), OrderPage.get_step_title_text(self.driver, 3))

    def test_first_step(self):
        OrderPage.fill_in_first_step_data(self.driver, fake_first_name, fake_last_name, fake_email)
        self.assertEqual(OrderPage.get_first_name_value(self.driver), fake_first_name)
        self.assertEqual(OrderPage.get_last_name_value(self.driver), fake_last_name)

    def test_second_step(self):
        OrderPage.fill_in_first_step_data(self.driver, fake_first_name, fake_last_name, fake_email)
        OrderPage.fill_in_second_step_data(self.driver, fake_company, fake_address, fake_postal_code, fake_city, fake_phone)
        self.assertTrue(OrderPage.is_delivery_option_displayed(self.driver))

    def test_confirm_order(self):
        OrderPage.fill_in_first_step_data(self.driver, fake_first_name, fake_last_name, fake_email)
        OrderPage.fill_in_second_step_data(self.driver, fake_company, fake_address, fake_postal_code, fake_city,
                                           fake_phone)
        OrderPage.confirm_order(self.driver)
        self.assertIn(OrderPage.CARD_TITLE.upper(), OrderPage.get_card_title_text(self.driver).upper())
        self.assertIn(fake_email, OrderPage.get_confirmations_text(self.driver))