from selenium.webdriver.common.by import By



class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    final_checkout_button = (By.XPATH, "//button[@class='btn btn-success']")
    location_input = (By.CSS_SELECTOR, "input#country")
    country_link_name = (By.LINK_TEXT, "Italy")
    purchase_button = (By.CSS_SELECTOR, "input.btn-success")
    purchase_text_status = (By.CSS_SELECTOR, "[class*='alert-success']")

    def apply_checkout(self):
        return self.driver.find_element(*ConfirmPage.final_checkout_button)

    def input_country(self):
        return self.driver.find_element(*ConfirmPage.location_input)

    def select_country_name(self):
        return self.driver.find_element(*ConfirmPage.country_link_name)

    def purchase_items(self):
        return self.driver.find_element(*ConfirmPage.purchase_button)

    def purchase_status(self):
        return self.driver.find_element(*ConfirmPage.purchase_text_status)