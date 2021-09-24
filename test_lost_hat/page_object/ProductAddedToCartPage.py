import time

modalHeader = "modal-header"
modalTitle = "myModalLabel"
modalScreenTitle = "\ue876Product successfully added to your shopping cart"
modalProductName = "product-name"
modalProductPrice = "//*[@id=\"blockcart-modal\"]/div/div/div[2]/div/div[1]/div/div[2]/p[1]"
buttonContinueShopping = "//*[@id=\"blockcart-modal\"]/div/div/div[2]/div/div[2]/div/div/button"
buttonProceedToCheckout = "//*[@id=\"blockcart-modal\"]/div/div/div[2]/div/div[2]/div/div/a"


def is_moda_dialog_displayed(driver_instance):
    time.sleep(5)
    element = driver_instance.find_element_by_class_name(modalHeader)
    return element.is_displayed()


def get_modal_screen_title_text(driver_instance):
    time.sleep(5)
    element = driver_instance.find_element_by_id(modalTitle)
    return element.text


def get_modal_screen_product_name(driver_instance):
    time.sleep(5)
    element = driver_instance.find_element_by_class_name(modalProductName)
    return element.text


def get_modal_screen_product_price(driver_instance):
    time.sleep(5)
    element = driver_instance.find_element_by_xpath(modalProductPrice)
    return element.text


def click_continue_shopping_button(driver_instance):
    time.sleep(5)
    driver_instance.find_element_by_xpath(buttonContinueShopping).click()


def click_proceed_to_checkout_button(driver_instance):
    time.sleep(5)
    driver_instance.find_element_by_xpath(buttonProceedToCheckout).click()