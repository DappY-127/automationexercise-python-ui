import allure
from .base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage(BasePage):

    PAGE_URL = Links.CHECKOUT_PAGE

    PLACE_ORDER_BTTN = ("css selector", "[href='/payment']")
    ORDER_MSSG_FIELD = ("css selector", "#ordermsg [name='message']")
    YOUR_DELIVERY_ADDRESS_LABEL = ("css selector", "#address_delivery")
    YOUR_BILLING_ADDRESS_LABEL = ("css selector", "#address_invoice")
    # info = ("", ".address_firstname.address_lastname")
    DA_FIRST_SECOND_NAME = ('css selector', '#address_delivery .address_firstname.address_lastname')
    BA_FIRST_SECOND_NAME = ('css selector', '#address_invoice .address_firstname.address_lastname')
    DA_ADDRESS_1 = ("xpath", "(//*[@id='address_delivery']//*[contains(@class, 'address_address1') and contains(@class, 'address_address2')])[2]")
    BA_ADDRESS_1 = ("xpath", "(//*[@id='address_invoice']//*[contains(@class, 'address_address1') and contains(@class, 'address_address2')])[2]")
    DA_ADDRESS_2 = ("xpath", "(//*[@id='address_delivery']//*[contains(@class, 'address_address1') and contains(@class, 'address_address2')])[3]")
    BA_ADDRESS_2 = ("xpath", "(//*[@id='address_invoice']//*[contains(@class, 'address_address1') and contains(@class, 'address_address2')])[3]")
    DA_ADDRESS = ('css selector', '#address_delivery .address_city.address_state_name.address_postcode') # State + City + Zip format
    BA_ADDRESS= ('css selector', '#address_invoice .address_city.address_state_name.address_postcode')
    DA_COUNTRY = ('css selector', '#address_delivery .address_country_name')
    BA_COUNTRY = ('css selector', '#address_invoice .address_country_name')
    DA_PHONE_NUMBER = ('css selector', '#address_delivery .address_phone')
    BA_PHONE_NUMBER = ('css selector', '#address_invoice .address_phone')

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
        self.scroll_into_view(self.PLACE_ORDER_BTTN)
        self.wait.until(EC.element_to_be_clickable(self.PLACE_ORDER_BTTN)).click()
        self.check_and_close_ad_if_present()
    
    @allure.step("Fill order comment")
    def fill_order_commnets(self):
        self.scroll_into_view(self.ORDER_MSSG_FIELD)
        self.fill_field(self.ORDER_MSSG_FIELD, self.fake.paragraph())
        self.make_screenshot('Order comments')

    @allure.step("Verify address information")
    def verify_address_info(self):
        self.verify_delivery_address_info()
        self.verify_billing_address_info()
        self.make_screenshot("Address information")

    @allure.step("Verify delifery address information")
    def verify_delivery_address_info(self):
        name_text = self.get_element_text(self.DA_FIRST_SECOND_NAME)
        address1_text = self.get_element_text(self.DA_ADDRESS_1)
        address2_text = self.get_element_text(self.DA_ADDRESS_2)
        address_text = self.get_element_text(self.DA_ADDRESS)
        country_text = self.get_element_text(self.DA_COUNTRY)
        phone_text = self.get_element_text(self.DA_PHONE_NUMBER)

        with allure.step("Verify name information"):
            assert self.data.first_name in name_text, f"Expected: {self.data.first_name} in {name_text}"
            assert self.data.last_name in name_text, f"Expected: {self.data.last_name} in {name_text}"

        with allure.step("Verify address information"):
            assert self.data.street_address in address1_text, f"Expected: {self.data.street_address} in {address1_text}"
            assert self.data.secondary_address in address2_text, f"Expected: {self.data.secondary_address} in {address2_text}"
            assert self.data.city in address_text, f"Expected: {self.data.city} in {address_text}"
            assert self.data.state in address_text, f"Expected: {self.data.state} in {address_text}"
            assert self.data.zipcode in address_text, f"Expected: {self.data.zipcode} in {address_text}"

        with allure.step("Verify country and phone information"):
            assert self.data.country in country_text, f"Expected: {self.data.country} in {country_text}"
            assert self.data.phone_number in phone_text, f"Expected: {self.data.phone_number} in {phone_text}"

    @allure.step("Verify billing address information")
    def verify_billing_address_info(self):
        name_text = self.get_element_text(self.BA_FIRST_SECOND_NAME)
        address1_text = self.get_element_text(self.BA_ADDRESS_1)
        address2_text = self.get_element_text(self.BA_ADDRESS_2)
        address_text = self.get_element_text(self.BA_ADDRESS)
        country_text = self.get_element_text(self.BA_COUNTRY)
        phone_text = self.get_element_text(self.BA_PHONE_NUMBER)

        with allure.step("Verify name information"):
            assert self.data.first_name in name_text, f"Expected: {self.data.first_name} in {name_text}"
            assert self.data.last_name in name_text, f"Expected: {self.data.last_name} in {name_text}"

        with allure.step("Verify address information"):
            assert self.data.street_address in address1_text, f"Expected: {self.data.street_address} in {address1_text}"
            assert self.data.secondary_address in address2_text, f"Expected: {self.data.secondary_address} in {address2_text}"
            assert self.data.city in address_text, f"Expected: {self.data.city} in {address_text}"
            assert self.data.state in address_text, f"Expected: {self.data.state} in {address_text}"
            assert self.data.zipcode in address_text, f"Expected: {self.data.zipcode} in {address_text}"

        with allure.step("Verify country and phone information"):
            assert self.data.country in country_text, f"Expected: {self.data.country} in {country_text}"
            assert self.data.phone_number in phone_text, f"Expected: {self.data.phone_number} in {phone_text}"            
        