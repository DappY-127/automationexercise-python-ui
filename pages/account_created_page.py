import allure
from .base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class AccountCreatedPage(BasePage):

    # PAGE_URL= Links.

    ACCOUNT_CREATED_MSSG = ('css selector', '[data-qa="account-created"]')
    CONTINUE_BTTN = ('css selector', '[data-qa="continue-button"]')

    @allure.step("Click continue button")
    def click_continue_button(self):
        self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BTTN)).click()






