import time

from selenium.webdriver.common.by import By



from page_obgects.checkout_page import CheckOutPage
from page_obgects.home_page import HomePage
from utilities.baseclass import BaseClass

# we use BaseClass to use web_driver-*
class TestOne(BaseClass):

    def test_e2e(self):

        log = self.get_logger()

        home_page = HomePage(self.driver)
        checkout_page = home_page.shop_items()

        log.info("Getting all the card titles")

        cards = checkout_page.get_title()
        i = -1
        for card in cards:
            i= i + 1
            card_text = card.text
            log.info(card_text)
            if card_text == "Blackberry":
                checkout_page.get_card_footer()[i].click()


        confirm_page = checkout_page.checkout_items()
        confirm_page.apply_checkout().click()

        log.info("Entering country name as ital")
        confirm_page.input_country().send_keys("ital")
        self.verify_link_presence("Italy")


        confirm_page.select_country_name().click()
        confirm_page.purchase_items().click()

        success_message = confirm_page.purchase_status().text
        assert ("Thank you!" in success_message)
        log.info("Text received from app is:" + success_message)