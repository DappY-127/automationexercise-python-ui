import allure
from .base_test import BaseTest


@allure.feature("Customer Support")
class TestContactUsFeature(BaseTest):

    @allure.title("Contact Us Form")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_scroll_up_arrow_bttn_with_scroll_down(self):
        self.home_page.open()
        self.home_page.is_header_visible()
        self.home_page.click_contact_us_button()
        self.contact_us_page.is_contact_us_form_visible()
        # self. ... fill form
        # confirm sending alert
        self.contact_us_page.make_screenshot("Success message")
        self.contact_us_page.click_home_bttn()
        self.home_page.is_header_visible()