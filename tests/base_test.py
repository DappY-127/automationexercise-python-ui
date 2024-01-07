import pytest
from config.data import Data
from pages.account_created_page import AccountCreatedPage
from pages.account_deleted_page import AccountDeletedPage
from pages.home_page import HomePage
from pages.signup_login_page import SignupLoginPage
from pages.signup_page import SignupPage

class BaseTest:

    data: Data

    account_created_page: AccountCreatedPage
    account_deleted_page: AccountDeletedPage
    home_page: HomePage
    signup_login_page: SignupLoginPage
    signup_page: SignupPage

    @pytest.fixture(autouse=True)
    def setup(self, request, browser):
        request.cls.driver = browser
        request.cls.data = Data()

        request.cls.account_created_page = AccountCreatedPage(browser)
        request.cls.account_deleted_page = AccountDeletedPage(browser)
        request.cls.home_page = HomePage(browser)
        request.cls.signup_login_page = SignupLoginPage(browser)
        request.cls.signup_page = SignupPage(browser)


    # Сюди додати потім реєстрацію/видалення акаунту бо воно майже в кожному тесткейсі буде 