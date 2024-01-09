import allure
from .base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class AccountDeletedPage(BasePage):

    # PAGE_URL= Links.

    ACCOUNT_DELETED_MSSG = ('css selector', '[data-qa="account-deleted"]')
    CONTINUE_BTTN = ('css selector', '[data-qa="continue-button"]')

    @allure.step("Click continue button")
    def click_continue_button(self):
        self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BTTN)).click()