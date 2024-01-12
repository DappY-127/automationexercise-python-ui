import allure
import random
from .base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class SignupLoginPage(BasePage):

    PAGE_URL= Links.SIGNUP_LOGIN_PAGE

    LOGIN_EMAIL_ADDRESS_FIELD = ('css selector', '[data-qa="login-email"]')
    LOGIN_PASSWORD_FIELD = ('css selector', '[data-qa="login-password"]')
    LOGIN_BTTN = ('css selector', '[data-qa="login-button"]')
    LOGIN_INFO_LABEL = ('css selector', '.login-form h2')
    SIGNUP_NAME_FIELD = ('css selector', '[data-qa="signup-name"]')
    SIGNUP_EMAIL_ADDRESS_FIELD = ('css selector', '[data-qa="signup-email"]')
    SIGNUP_BTTN = ('css selector', '[data-qa="signup-button"]')
    SIGNUP_INFO_LABEL = ('css selector', '.signup-form h2')
    INVALID_MAIL_PASSWORD_MSG = ('xpath', '//*[text()="Your email or password is incorrect!"]')
    EMAIL_EXIST_ERR_MSG = ('xpath', '//*[text()="Email Address already exist!"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.LOGIN_EMAIL = self.generate_random_email()
        self.LOGIN_NAME = self.fake.name()

    @staticmethod
    def generate_random_email():
        random_number = random.randint(0, 9999)  # Generates a random 4-digit number
        return f"testmail{random_number}@mail.com"

    @allure.step("Enter name for signup")
    def enter_signup_name(self):
        self.fill_field(self.SIGNUP_NAME_FIELD, self.LOGIN_NAME)
        # self.wait.until(EC.element_to_be_clickable(self.SIGNUP_NAME_FIELD)).send_keys(self.LOGIN_NAME)
        print(self.LOGIN_NAME)

    @allure.step("Enter email for signup")
    def enter_signup_email(self):
        self.fill_field(self.SIGNUP_EMAIL_ADDRESS_FIELD, self.LOGIN_EMAIL)
        # self.wait.until(EC.element_to_be_clickable(self.SIGNUP_EMAIL_ADDRESS_FIELD)).send_keys(self.LOGIN_EMAIL)
        print(self.LOGIN_EMAIL)

    @allure.step("Click signup button")
    def click_signup_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SIGNUP_BTTN)).click()
        
    @allure.step("Enter login email")
    def enter_login(self, login):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_EMAIL_ADDRESS_FIELD)).send_keys(login)
        
    @allure.step("Enter password")
    def enter_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_PASSWORD_FIELD)).send_keys(password)

    @allure.step("Click login button")
    def click_login_button(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BTTN)).click()
