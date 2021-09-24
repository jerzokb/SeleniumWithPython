import random
import time

CURRENT_URL = "https://autodemo.testoneo.com/en/order"
FIRST_STEP_TITLE = "Personal Information"
SECOND_STEP_TITLE = "Addresses"
THIRD_STEP_TITLE = "Shipping Method"
FOURTH_STEP_TITLE = "Payment"
CARD_TITLE = "Your order is confirmed"
POST_CODE = "12-345"
PHONE_NUMBER = "123-456-789"

SIGN_IN_ADDRESS = "beatapalka@wp.pl"
SIGN_IN_PASSWORD = "beatapalka"

stepTitles = "step-title"
firstName = "firstname"
lastname = "lastname"
email = "email"
buttonContinue = "continue"
company = "company"
address1 = "address1"
postCode = "postcode"
city = "city"
phone = "phone"
buttonConfirmAddresses = "confirm-addresses"
formDeliveryOptions = "delivery-options"
buttonConfirmDelivery = "confirmDeliveryOption"
paymentOption1 = "payment-option-1"
paymentOption2 = "payment-option-2"
approveConditions = "conditions_to_approve[terms-and-conditions]"
buttonConfirmPayment = "//*[@id=\"payment-confirmation\"]/div[1]/button"
cardTitle = "card-title"
confirmationText = "//*[@id=\"content-hook_order_confirmation\"]/div/div/div/p"

def get_step_title_text(driver_instance, index):
    elements = driver_instance.find_elements_by_class_name(stepTitles)
    return elements[index].text.upper()


def input_first_name(driver_instance, first_name):
    element = driver_instance.find_element_by_name(firstName)
    element.clear()
    element.send_keys(first_name)


def input_last_name(driver_instance, last_name):
    element = driver_instance.find_element_by_name(lastname)
    element.clear()
    element.send_keys(last_name)


def input_email(driver_instance, email_text):
    element = driver_instance.find_element_by_name(email)
    element.clear()
    element.send_keys(email_text)


def click_continue_button(driver_instance):
    element = driver_instance.find_element_by_class_name(buttonContinue)
    element.click()


def fill_in_first_step_data(driver_instance, first_name, last_name, email_text):
    input_first_name(driver_instance, first_name)
    input_last_name(driver_instance, last_name)
    input_email(driver_instance, email_text)
    click_continue_button(driver_instance)


def get_first_name_value(driver_instance):
    element = driver_instance.find_element_by_name(firstName)
    return element.get_attribute('value')


def get_last_name_value(driver_instance):
    element = driver_instance.find_element_by_name(lastname)
    return element.get_attribute('value')


def input_company_name(driver_instance, company_name):
    element = driver_instance.find_element_by_name(company)
    element.clear()
    element.send_keys(company_name)


def input_address(driver_instance, address_text):
    element = driver_instance.find_element_by_name(address1)
    element.clear()
    element.send_keys(address_text)


def input_postal_code(driver_instance, postal_code_text):
    element = driver_instance.find_element_by_name(postCode)
    element.clear()
    element.send_keys(postal_code_text)


def input_city(driver_instance, city_name):
    element = driver_instance.find_element_by_name(city)
    element.clear()
    element.send_keys(city_name)


def input_phone(driver_instance, phone_number):
    element = driver_instance.find_element_by_name(phone)
    element.clear()
    element.send_keys(phone_number)


def click_confirmation_addresses_button(driver_instance):
    element = driver_instance.find_element_by_name(buttonConfirmAddresses)
    element.click()


def fill_in_second_step_data(driver_instance, company_name, address_text, postal_code_text, city_name, phone_number):
    input_company_name(driver_instance, company_name)
    input_address(driver_instance, address_text)
    input_postal_code(driver_instance, postal_code_text)
    input_city(driver_instance, city_name)
    input_phone(driver_instance, phone_number)
    click_confirmation_addresses_button(driver_instance)


def is_delivery_option_displayed(driver_instance):
    element = driver_instance.find_element_by_class_name(formDeliveryOptions)
    return element.is_displayed()


def click_confirmation_delivery_button(driver_instance):
    element = driver_instance.find_element_by_name(buttonConfirmDelivery)
    element.click()


def click_payment_option(driver_instance):
    option = random.randint(0, 1)
    if option == 0:
        element = driver_instance.find_element_by_id(paymentOption1)
        element.click()
    else:
        element = driver_instance.find_element_by_id(paymentOption2)
        element.click()

def approve_conditions(driver_instance):
    element = driver_instance.find_element_by_id(approveConditions)
    element.click()


def click_confirm_payment_button(driver_instance):
    element = driver_instance.find_element_by_xpath(buttonConfirmPayment)
    element.click()


def confirm_order(driver_instance):
    click_confirmation_delivery_button(driver_instance)
    click_payment_option(driver_instance)
    approve_conditions(driver_instance)
    click_confirm_payment_button(driver_instance)


def get_card_title_text(driver_instance):
    element = driver_instance.find_element_by_class_name(cardTitle)
    return element.text


def get_confirmations_text(driver_instance):
    element = driver_instance.find_element_by_xpath(confirmationText)
    return element.text