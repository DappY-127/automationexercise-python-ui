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


    # Сюди додати потім реєстрацію/видалення акаунту бо воно майже в кожному тесткейсі буде 