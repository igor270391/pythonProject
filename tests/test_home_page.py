import pytest

from page_obgects.home_page import HomePage
from test_data.home_page_data import HomePageData
from utilities.baseclass import BaseClass
from selenium.webdriver.common.by import By

class TestHomePage(BaseClass):

    def test_form_submition(self, get_data):
        home_pg = HomePage(self.driver)
        home_pg.get_name(get_data["gender"])

        home_pg.get_email(get_data["email"])
        home_pg.get_pw("!£$%&&12d")
        home_pg.checkbox()
        self.select_option_by_text(home_pg.select_gender(), get_data["gender"])
        home_pg.get_status()
        home_pg.get_date("31/12/2024")
        home_pg.submit_form()
        success_status = self.driver.find_element(By.CSS_SELECTOR, "[class*='alert-success']").text
        assert ("Success" in success_status)

    @pytest.fixture(params= HomePageData.test_home_page_data)
    def get_data(self, request):
        return request.param