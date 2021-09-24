from selenium.webdriver.common.by import By

productItem = "thumbnail"
buttonAddToCart = "//*[@id=\"add-to-cart-or-refresh\"]/div[2]/div/div[2]/button"
productTitle = "product-title"
selectedProductName = "//*[@id=\"main\"]/div[1]/div[2]/h1"
productPrice = "price"
selectedProductPrice = "//*[@id=\"main\"]/div[1]/div[2]/div[1]/div[2]/div/span[1]"


def click_on_product_item(driver_instance, index):
    elements = driver_instance.find_elements_by_class_name(productItem)
    if index >= len(elements):
        print("Item not found")
    else:
        elements[index].click()


def get_add_to_cart_button(driver_instance):
    element = driver_instance.find_element_by_xpath(buttonAddToCart)
    return element.is_displayed()


def get_product_title(driver_instance, index):
    elements = driver_instance.find_elements_by_class_name(productTitle)
    return elements[index].text


def get_product_price(driver_instance, index):
    elements = driver_instance.find_elements_by_class_name(productPrice)
    return elements[index].text


def get_selected_product_name(driver_instance):
    return driver_instance.find_element_by_xpath(selectedProductName).text


def get_selected_product_price(driver_instance):
    return driver_instance.find_element_by_xpath(selectedProductPrice).text

def click_add_to_cart_button(driver_instance):
    driver_instance.find_element_by_xpath(buttonAddToCart).click()

def add_product_to_cart(driver_instance, index):
    click_on_product_item(driver_instance, index)
    click_add_to_cart_button(driver_instance)