import allure
from .base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class PaymentPage(BasePage):

    PAYMENT_LABEL = ("css selector", ".payment-information")
    # PAYMENT_LABEL = ("css selector", ".payment-information")
    CARD_NAME_FIELD = ("css selector", "[data-qa='name-on-card']")
    CARD_NUMBER_FIELD = ("css selector", "[data-qa='card-number']")
    CARD_CVC_FIELD = ("css selector", "[data-qa='cvc']")
    CARD_EXPIRATION_MONTH_FIELD = ("css selector", "[data-qa='expiry-month']")
    CARD_EXPIRATION_YEAR_FIELD = ("css selector", "[data-qa='expiry-year']")
    PAY_AND_CONFIRM_ORDER_BTTN = ("css selector", "#submit[data-qa='pay-button']")

    @allure.step("Click confirm order button")
    def click_confirm_order_button(self):
        self.wait.until(EC.element_to_be_clickable(self.PAY_AND_CONFIRM_ORDER_BTTN)).click()

    @allure.step("Fill 'Enter payment details' section")
    def fill_payment_details_section(self):
        self.fill_field(self.CARD_NAME_FIELD, self.data.credit_card_name)
        self.fill_field(self.CARD_NUMBER_FIELD, self.data.credit_card_number)
        self.fill_field(self.CARD_CVC_FIELD, self.data.card_cvc)
        self.fill_field(self.CARD_EXPIRATION_MONTH_FIELD, self.data.expiration_month)
        self.fill_field(self.CARD_EXPIRATION_YEAR_FIELD, self.data.expiration_year)
        self.make_screenshot('Filled card information section form')

    @allure.step("Payment page label visible")
    def is_products_visible(self):
        self.wait.until(EC.visibility_of_element_located(self.PAYMENT_LABEL))
        self.make_screenshot("Payment Label")    


# validate succes message


