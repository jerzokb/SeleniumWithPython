import time
CARD_BLOCK_HEADER = "SHOPPING CART"
cardBlock = "card-block"
buttonProceedToCheckout = "//*[@id=\"main\"]/div/div[2]/div[1]/div[2]/div/a"


def is_card_block_display(driver_instance):
    element = driver_instance.find_element_by_class_name(cardBlock)
    return element.is_displayed()


def get_card_block_text(driver_instance):
    element = driver_instance.find_element_by_class_name(cardBlock)
    return element.text.upper()


def click_proceed_to_checkout_button(driver_instance):
    driver_instance.find_element_by_xpath(buttonProceedToCheckout).click()