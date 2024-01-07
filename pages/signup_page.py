import allure
from .base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class SignupPage(BasePage):

    PAGE_URL= Links.SIGNUP_PAGE

    CREATE_ACC_BTTN = ('xpath', '[data-qa="create-account"]')
    MR_RADIO_BTTN = ('css selector', '#id_gender1')
    MRS_RADIO_BTTN = ('css selector', '#id_gender2')
    NAME_FIELD = ('css selector', '#name')
    EMAIL_FIELD = ('css selector', '#email')
    PASSWORD_FIELD = ('css selector', '#password')
    BIRTH_DAY_SELECT = ('css selector', '#days')
    BIRTH_MONTH_SELECT = ('css selector', '#months')
    BIRTH_YEAR_SELECT = ('css selector', '#years')
    NEWSLETTER_CHECKBOX = ('css selector', '#newsletter')
    SPECIAL_OFFERS_CHECKBOX = ('css selector', '#optin')
    FIRST_NAME_FIELD = ('css selector', '#first_name')
    LAST_NAME_FIELD = ('css selector', '#last_name')
    COMPANY_FIELD = ('css selector', '#company')
    ADDRESS_FIELD = ('css selector', '#address1')
    ADDRESS2_FIELD = ('css selector', '#address2')
    COUNTRY_SELECT = ('css selector', '#country')
    STATE_FIELD = ('css selector', '#state')
    CITY_FIELD = ('css selector', '#city')
    ZIP_FIELD = ('css selector', '#zipcode')
    MOBILE_NUMBER_FIELD = ('css selector', '#mobile_number')

    @allure.step("Click create account button")
    def click_create_account_button(self):
        self.wait.until(EC.element_to_be_clickable(self.CREATE_ACC_BTTN)).click()

    # @allure.step("Fill 'Enter Account Information' section")
    # def fill_account_info_section(self):
    #     pass

    # @allure.step("Fill 'Address Information' section")
    # def fill_address_info_section(self):
    #     pass

    # @allure.step("Fill First name")
    # def fill_(self):
    #     pass

