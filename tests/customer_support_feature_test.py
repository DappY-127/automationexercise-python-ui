import allure
from .base_test import BaseTest


@allure.feature("Customer Support")
class TestContactUsFeature(BaseTest):

    @allure.title("Contact Us Form")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag('TestCaseID: 6')
    def test_contact_us_form(self):
        self.home_page.open()
        self.home_page.is_header_visible()
        self.home_page.click_contact_us_button()
        self.contact_us_page.is_contact_us_form_visible()
        self.contact_us_page.fill_contact_us_form()
        self.contact_us_page.upload_file_to_contact_us()
        self.contact_us_page.click_continue_button()
        self.contact_us_page.accept_alert()
        self.contact_us_page.make_screenshot("Success message")
        self.contact_us_page.click_home_bttn()
        self.home_page.is_header_visible()