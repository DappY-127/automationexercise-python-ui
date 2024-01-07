import allure
from .base_test import BaseTest


@allure.feature("Registration Functionality")
class TestScrollingFeature(BaseTest):

    @allure.title("Scroll Up using 'Arrow' button and Scroll Down functionality")
    @allure.severity("Normal")
    def test_scroll_up_arrow_bttn_with_scroll_down(self):
        self.home_page.open()
        self.home_page.page_scroll_down()
        self.home_page.is_subscription_label_visible()
        self.home_page.make_screenshot("site scrolled down")
        self.home_page.click_move_upward_button()
        self.home_page.is_header_visible()  
        self.home_page.is_active_slider_text_visible()  
        self.home_page.make_screenshot("site scrolled up")

    @allure.title("Scroll Up without 'Arrow' button and Scroll Down functionality")
    @allure.severity("Normal")
    def test_test_scroll_up_scroll_down(self):
        self.home_page.open()
        self.home_page.page_scroll_down()
        self.home_page.is_subscription_label_visible()
        self.home_page.make_screenshot("site scrolled down")
        self.home_page.page_scroll_up()        
        self.home_page.is_header_visible()        
        self.home_page.is_active_slider_text_visible()        
        self.home_page.make_screenshot("site scrolled up")



