import allure
import pytest
import time
from .base_test import BaseTest


@allure.feature("Registration Functionality")
class TestRegistrationFeature(BaseTest):

    @allure.title("Register User")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("User registration")
    @allure.tag('TestCaseID: 1')
    def test_register_user_with_valid_data(self):
        self.home_page.open()
        self.home_page.is_opened()
        self.home_page.click_signup_login_button()
        self.signup_login_page.is_opened()
        self.signup_login_page.enter_signup_name()
        self.signup_login_page.enter_signup_email()
        self.signup_login_page.click_signup_button()
        self.signup_page.is_opened()
        self.signup_page.fill_account_info_section()
        self.signup_page.fill_address_info_section()
        self.signup_page.click_create_account_button()
        self.account_created_page.is_opened()
        self.account_created_page.is_account_created_message_visible()
        self.account_created_page.click_continue_button()
        self.home_page.is_opened()
        self.home_page.is_user_name_header_visible()
        self.home_page.is_user_status_correct()
        self.home_page.click_delete_account_button()
        self.account_deleted_page.is_opened()
        self.account_deleted_page.is_account_deleted_message_visible()
        self.account_deleted_page.click_continue_button()
        self.home_page.is_opened()

    @allure.title("Register User with existing email")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("User registration")
    @allure.tag('TestCaseID: 5')
    def test_register_user_with_existing_email(self):
        self.home_page.open()
        self.home_page.is_opened()
        self.home_page.click_signup_login_button()
        self.signup_login_page.is_opened()
        self.signup_login_page.enter_signup_name()
        self.signup_login_page.enter_existing_signup_email()
        self.signup_login_page.click_signup_button()
        self.signup_login_page.is_email_exist_error_visible()

    # @allure.title("Login User with correct email and password")
    # @allure.severity(allure.severity_level.CRITICAL)
    # @allure.story("User login")
    # @allure.tag('TestCaseID: 2')
    # def test_login_with_valid_data(self):
    #     self.home_page.open()
    #     self.home_page.click_signup_login_button()

    @allure.title("Login User with incorrect email and password")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("User login")
    @allure.tag('TestCaseID: 3')
    def test_login_with_invalid_data(self):
        self.home_page.open()
        self.home_page.is_opened()
        self.home_page.click_signup_login_button()
        self.signup_login_page.is_opened()
        self.signup_login_page.enter_incorrect_email_and_pass()
        self.signup_login_page.click_login_button()
        self.signup_login_page.is_invalid_email_or_password_error_visible()

#     @allure.title("Logout User")
#     @allure.severity(allure.severity_level.CRITICAL)
#     @allure.story("User logout")
#     @allure.tag('TestCaseID: 4')
#     def test_logout_user(self):
#         self.home_page.open()
#         self.home_page.click_signup_login_button()
