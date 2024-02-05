import allure
import os
import time
from .base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class OrderPlacementPage(BasePage):

    # PAGE_URL = Links.ORDER_PLACEMENT_PAGE

    CONTINUE_BTTN = ('css selector', '[data-qa="continue-button"]')
    DOWNLOAD_INVOICE_BTTN = ('css selector', '.btn.check_out')
    ORDER_PLACED_MSSG = ('css selector', '[data-qa="order-placed"]')

    @allure.step("Click continue button")
    def click_continue_button(self):
        self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BTTN)).click()
        self.check_and_close_ad_if_present()
    
    @allure.step("Click 'Download Invoice' button")
    def click_download_invoice_button(self):
        self.wait.until(EC.element_to_be_clickable(self.DOWNLOAD_INVOICE_BTTN)).click()
        time.sleep(2)
        downloaded_file_path = os.path.join(os.getcwd(), 'pages', 'resources', 'invoice.txt')
        self.is_file_present(downloaded_file_path)

    @allure.step("Order placement message visible")
    def is_order_placed_message_visible(self):
        self.wait.until(EC.visibility_of_element_located(self.ORDER_PLACED_MSSG))
        self.make_screenshot("Order Placed")

    @allure.step("Invoice downloaded")
    def is_file_present(self, file_path):
        with allure.step(f"Verify the presence of the file at {file_path}"):
            if not os.path.exists(file_path) or not os.path.isfile(file_path):
                allure.attach(f"Test failed. File is missing. Current file path : {file_path}", name="Test Failure Details", attachment_type=allure.attachment_type.TEXT)
                raise FileNotFoundError(f"File {file_path} not found")

        allure.attach.file(f"File downloaded. File path : {file_path}", name="File path", attachment_type=allure.attachment_type.TEXT)
        return True
    