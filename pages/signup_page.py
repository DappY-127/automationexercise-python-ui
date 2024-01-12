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

    @allure.step("Fill 'Enter Account Information' section")
    def fill_account_info_section(self):
        self.select_radio_button(self.MR_RADIO_BTTN)
        self.select_option(self.BIRTH_DAY_SELECT, str(self.fake.random_int(min=1, max=31)))
        self.select_option(self.BIRTH_MONTH_SELECT, str(self.fake.month_name()))
        self.select_option(self.BIRTH_YEAR_SELECT, str(self.fake.random_int(min=1900, max=2021)))
        self.select_checkbox(self.NEWSLETTER_CHECKBOX)
        self.select_checkbox(self.SPECIAL_OFFERS_CHECKBOX)

    @allure.step("Fill 'Address Information' section")
    def fill_address_info_section(self):
        self.fill_field(self.FIRST_NAME_FIELD, self.fake.first_name())
        self.fill_field(self.LAST_NAME_FIELD, self.fake.last_name())
        self.fill_field(self.COMPANY_FIELD, self.fake.company())
        self.fill_field(self.ADDRESS_FIELD, self.fake.street_address()) 
        self.fill_field(self.ADDRESS2_FIELD, self.fake.secondary_address()) 
        self.select_option(self.COUNTRY_SELECT, "Canada")
        self.fill_field(self.STATE_FIELD, self.fake.state()) 
        self.fill_field(self.CITY_FIELD, self.fake.city()) 
        self.fill_field(self.ZIP_FIELD, self.fake.zipcode()) 
        self.fill_field(self.MOBILE_NUMBER_FIELD, self.fake.phone_number()) 
        self.make_screenshot('Filled form')
  