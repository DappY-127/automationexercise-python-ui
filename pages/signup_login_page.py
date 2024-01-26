import allure
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

    @allure.step("Enter name for signup")
    def enter_signup_name(self):
        self.fill_field(self.SIGNUP_NAME_FIELD, self.data.login_name)

    @allure.step("Enter email for signup")
    def enter_signup_email(self):
        self.fill_field(self.SIGNUP_EMAIL_ADDRESS_FIELD, self.data.email)

    @allure.step("Enter existing email for signup")
    def enter_existing_signup_email(self):
        self.fill_field(self.SIGNUP_EMAIL_ADDRESS_FIELD, "example.test@mail.com")

    @allure.step("Enter incorrect email address and password")
    def enter_incorrect_email_and_pass(self):
        self.fill_field(self.LOGIN_EMAIL_ADDRESS_FIELD, "example.test@mail.com")
        self.fill_field(self.LOGIN_PASSWORD_FIELD, "realyincorrectpassword")

    @allure.step("Click signup button")
    def click_signup_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SIGNUP_BTTN)).click()
        self.check_and_close_ad_if_present()
        
    @allure.step("Enter login email")
    def enter_login(self):
        self.fill_field(self.LOGIN_EMAIL_ADDRESS_FIELD, self.data.email)
        
    @allure.step("Enter password")
    def enter_password(self):
        self.fill_field(self.LOGIN_PASSWORD_FIELD, self.data.password)

    @allure.step("Click login button")
    def click_login_button(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BTTN)).click()
        self.check_and_close_ad_if_present()

    @allure.step("'Email Address already exist!' error message visible")
    def is_email_exist_error_visible(self):       
        error_msg_text = self.wait.until(EC.visibility_of_element_located(self.EMAIL_EXIST_ERR_MSG)).text
        expected_error_msg = "Email Address already exist!"

        with allure.step(f"Verify error message text is correct"):
            assert expected_error_msg == error_msg_text, f"Expected: {expected_error_msg}, Actual: {error_msg_text}"
        self.make_screenshot("'Email Address already exist!' error")

    @allure.step("'Your email or password is incorrect!' error message visible")
    def is_invalid_email_or_password_error_visible(self):       
        error_msg_text = self.wait.until(EC.visibility_of_element_located(self.INVALID_MAIL_PASSWORD_MSG)).text
        expected_error_msg = "Your email or password is incorrect!"

        with allure.step(f"Verify error message text is correct"):
            assert expected_error_msg == error_msg_text, f"Expected: {expected_error_msg}, Actual: {error_msg_text}"
        self.make_screenshot("'Your email or password is incorrect!' error")