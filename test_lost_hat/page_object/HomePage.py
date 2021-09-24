from selenium.webdriver.common.by import By

page_title = "Lost Hat"

topMenuDropDownItemClothes = "category-3"
topMenuDropDownItemAccessories = "category-6"
topMenuDropDownItemArt = "category-9"
sliderElement = '//*[@id="carousel"]/ul/li'
#isSizeCorrect = True

def click_drop_down_menu_item(driver_instance, index):
    if index == 3:
        driver_instance.find_element_by_id(topMenuDropDownItemClothes).click()
    elif index == 6:
        driver_instance.find_element_by_id(topMenuDropDownItemAccessories).click()
    elif index == 9:
        driver_instance.find_element_by_id(topMenuDropDownItemArt).click()

def check_slider_element_size(driver_instance, expected_size):
    slider = driver_instance.find_elements_by_xpath(sliderElement)
    if len(slider) == expected_size:
        isSizeCorrect = True
    else:
        isSizeCorrect = False
    return isSizeCorrect