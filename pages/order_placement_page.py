import allure
from .base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class OrderPlacementPage(BasePage):

    # PAGE_URL = Links.ORDER_PLACEMENT_PAGE

    CONTINUE_BTTN = ('css selector', '[data-qa="continue-button"]')
    DOWNLOAD_INVOICE_BTTN = ('css selector', '[href="/download_invoice/500"]')
    ORDER_PLACED_MSSG = ('css selector', '[data-qa="order-placed"]')

    @allure.step("Click continue button")
    def click_continue_button(self):
        self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BTTN)).click()
    
    @allure.step("Click 'Download Invoice' button")
    def click_download_invoice_button(self):
        self.wait.until(EC.element_to_be_clickable(self.DOWNLOAD_INVOICE_BTTN)).click()

    @allure.step("Order placement message visible")
    def is_order_placed_message_visible(self):
        self.wait.until(EC.visibility_of_element_located(self.ORDER_PLACED_MSSG))
        self.make_screenshot("Order Placed")