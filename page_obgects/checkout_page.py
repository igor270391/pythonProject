from selenium.webdriver.common.by import By

from page_obgects.confirm_page import ConfirmPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver


    card_title = (By.CSS_SELECTOR, "div .card-title a")
    card_footer = (By.CSS_SELECTOR, ".card-footer button")
    checkout_items_button = (By.XPATH, "//a[@class='nav-link btn btn-primary']")


    def get_title(self):
        return self.driver.find_elements(*CheckOutPage.card_title)

    def get_card_footer(self):
        return self.driver.find_elements(*CheckOutPage.card_footer)

    def checkout_items(self):
        self.driver.find_element(*CheckOutPage.checkout_items_button).click()
        confirm_page = ConfirmPage(self.driver)
        return confirm_page

