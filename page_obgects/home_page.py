from page_obgects.checkout_page import CheckOutPage
from selenium.webdriver.common.by import By

class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href *= 'shop']")
    name_locator = (By.CSS_SELECTOR, "[name='name']")
    email_locator = (By.CSS_SELECTOR, ".form-group input[name='email']")
    pw_locator = (By.CSS_SELECTOR, ".form-group #exampleInputPassword1")
    check_me_out_locator = (By.CSS_SELECTOR, "[id='exampleCheck1']")
    gender_locator = (By.CSS_SELECTOR, ".form-group select[id='exampleFormControlSelect1']")
    employment_status_locator = (By.CSS_SELECTOR, ".form-group div input[id='inlineRadio1']")
    date_locator = (By.CSS_SELECTOR, ".form-group [name='bday']")
    submit_locator = (By.CSS_SELECTOR, ".btn-success[value='Submit']")


    def shop_items(self):
        self.driver.find_element(*HomePage.shop).click()
        checkout_page = CheckOutPage(self.driver)
        return checkout_page

    def get_name(self, name):
        fill_value = self.driver.find_element(*HomePage.name_locator)
        fill_value.send_keys(name)

    def get_email(self, email):
        self.driver.find_element(*HomePage.email_locator).send_keys(email)

    def get_pw(self, pw):
        self.driver.find_element(*HomePage.pw_locator).send_keys(pw)

    def checkbox(self):
        self.driver.find_element(*HomePage.check_me_out_locator).click()

    def select_gender(self):
        return self.driver.find_element(*HomePage.gender_locator)


    def get_status(self):
        self.driver.find_element(*HomePage.employment_status_locator).click()

    def get_date(self,date):
        self.driver.find_element(*HomePage.date_locator).send_keys(date)

    def submit_form(self):
        self.driver.find_element(*HomePage.submit_locator).click()


