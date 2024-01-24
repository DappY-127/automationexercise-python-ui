import allure
from .base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage(BasePage):

    PAGE_URL = Links.CHECKOUT_PAGE

    PLACE_ORDER_BTTN = ("css selector", "[href='/payment']")
    ORDER_MSSG_FIELD = ("css selector", "#ordermsg")
    YOUR_DELIVERY_ADDRESS_LABEL = ("css selector", "#address_delivery")
    YOUR_BILLING_ADDRESS_LABEL = ("css selector", "#address_invoice")
    # info = ("", ".address_firstname.address_lastname")

    CHECKOUT_PRODUCT_NAMES = ("xpath", "//td[contains(@class, 'cart_description')]//a")
    CHECKOUT_PRODUCT_PRICES = ("xpath", "//td[contains(@class, 'cart_price')]/p")
    CHECKOUT_PRODUCT_QUANTITY = ("xpath", "//td[contains(@class, 'cart_quantity')]/button")
    CHECKOUT_TOTAL_PRODUCT_PRICES = ("xpath", "//p[contains(@class, 'cart_total_price')]")# need attention

    @allure.step("'YOUR DELIVERY ADDRESS' information block visible")
    def is_delivery_address_visible(self):
        self.wait.until(EC.visibility_of_element_located(self.YOUR_DELIVERY_ADDRESS_LABEL))
        self.make_screenshot("Delivery Address")

    @allure.step("'YOUR BILLING ADDRESS' information block visible")
    def is_billing_address_visible(self):
        self.wait.until(EC.visibility_of_element_located(self.YOUR_BILLING_ADDRESS_LABEL))
        self.make_screenshot("Billing Address")

    @allure.step("Click 'Place Order' button")
    def click_place_order_button(self):
        self.wait.until(EC.element_to_be_clickable(self.PLACE_ORDER_BTTN)).click()
    