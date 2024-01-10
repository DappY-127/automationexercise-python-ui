import allure
from .base_test import BaseTest
import time


@allure.feature("Shopping & Checkout")
class TestShoppingCheckoutFeature(BaseTest):
    
    @allure.title("Verify Subscription in home page")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Subscription Handling")
    @allure.tag('TestCaseID: 10')
    def test_verify_subscription_at_home_page(self):
        self.home_page.open()
        self.home_page.page_scroll_down()
        self.home_page.is_subscription_label_visible()
        time.sleep(3)
        self.home_page.fill_subscription_email()
        time.sleep(3)
        self.home_page.click_subscribe_button()     
        self.home_page.is_succes_subscription_mssg_visible()   

    @allure.title("Verify Subscription in cart page")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Subscription Handling")
    @allure.tag('TestCaseID: 11')
    def test_verify_subscription_at_cart_page(self):
        self.home_page.open()
        self.home_page.click_cart_button()
        self.cart_page.is_header_visible()
        self.cart_page.page_scroll_down()
        self.cart_page.is_subscription_label_visible()
        time.sleep(3)
        self.cart_page.fill_subscription_email()
        time.sleep(3)
        self.cart_page.click_subscribe_button()     
        self.cart_page.is_succes_subscription_mssg_visible() 

