import pytest
from config.data import Data
from pages.account_created_page import AccountCreatedPage
from pages.account_deleted_page import AccountDeletedPage
from pages.home_page import HomePage
from pages.signup_login_page import SignupLoginPage
from pages.signup_page import SignupPage
from pages.testcases_page import TestCasesPage
from pages.contact_us_page import ContactUsPage
from pages.cart_page import CartPage
from pages.products_page import ProductsPage
from pages.product_details_page import ProductDetailsPage

class BaseTest:

    data: Data

    account_created_page: AccountCreatedPage
    account_deleted_page: AccountDeletedPage
    home_page: HomePage
    signup_login_page: SignupLoginPage
    signup_page: SignupPage
    test_cases_page: TestCasesPage
    contact_us_page: ContactUsPage
    cart_page: CartPage
    products_page: ProductsPage
    product_details_page: ProductDetailsPage

    @pytest.fixture(autouse=True)
    def setup(self, request, browser):
        request.cls.driver = browser
        request.cls.data = Data()

        request.cls.account_created_page = AccountCreatedPage(browser)
        request.cls.account_deleted_page = AccountDeletedPage(browser)
        request.cls.home_page = HomePage(browser)
        request.cls.signup_login_page = SignupLoginPage(browser)
        request.cls.signup_page = SignupPage(browser)
        request.cls.test_cases_page = TestCasesPage(browser)
        request.cls.contact_us_page = ContactUsPage(browser)
        request.cls.cart_page = CartPage(browser)
        request.cls.products_page = ProductsPage(browser)
        request.cls.product_details_page = ProductDetailsPage(browser)

    def account_register(self):
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

    def account_login(self):
        pass        

    def account_logout(self):
        pass        

    def account_deletion(self):
        self.home_page.click_delete_account_button()
        self.account_deleted_page.is_opened()
        self.account_deleted_page.is_account_deleted_message_visible()
        self.account_deleted_page.click_continue_button()
        self.home_page.is_opened()       

# from pages import (
#     AccountCreatedPage as CreatedPage,
#     AccountDeletedPage as DeletedPage,
#     HomePage,
#     SignupLoginPage,
#     SignupPage,
#     TestCasesPage,
#     ContactUsPage,
#     CartPage,
# )


    # Сюди додати потім реєстрацію/видалення акаунту бо воно майже в кожному тесткейсі буде 