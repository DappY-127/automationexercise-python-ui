import allure
from .base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class HomePage(BasePage):

    PAGE_URL= Links.HOME_PAGE

    USERNAME_FIELD = ("xpath", "//input[@name='username']")
    HOME_PAGE_LOGO_BTTN = ('css selector', '.logo img')
    HEADER_HOME_BTTN = ('xpath', '//a[contains(text(), "Home")]')
    HEADER_PRODUCTS_BTTN = ('xpath', '//a[contains(text(), "Products")]')
    HEADER_CART_BTTN = ('xpath', '//a[contains(text(), "Cart")]')
    HEADER_SIGNUP_LOGIN_BTTN = ('xpath', '//a[contains(text(), " Signup / Login")]') 
    HEADER_CONTACT_US_BTTN = ('xpath', '//a[contains(text(), "Contact us")]')
    HEADER_LOGOUT_BTTN = ('xpath', '//a[contains(text(), " Logout")]')
    HEADER_DELETE_ACC_BTTN = ('xpath', '//a[contains(text(), " Delete Account")]')
    HEADER_TEST_CASE_BTTN = ('xpath', '//a[contains(text(), " Test Cases")]')
    SUBSCRIPTION_EMAIL_FIELD = ('css selector', '#susbscribe_email')
    SUBSCRIPTION_BTTN = ('css selector', '#subscribe')
    SUBSCRIPTION_TEXT = ('css selector', '.single-widget h2')
    USER_STATUS = ('xpath', '//a[contains(text(), "Logged in as")]')
    SCROLL_UP_BTTN = ('css selector', '#scrollUp')
    ACTIVE_SLIDER_TEXT = ("xpath", "//div[@class = 'item active']//h2[contains(text(), 'Full-Fledged practice website for Automation Engineers')]")
    HEADER = ("css selector", ".nav.navbar-nav")

    @allure.step("Click Signup/Login header button")
    def click_signup_login_button(self):
        self.wait.until(EC.element_to_be_clickable(self.HEADER_SIGNUP_LOGIN_BTTN)).click()

    @allure.step("Click delete account header button")
    def click_delete_account_button(self):
        self.wait.until(EC.element_to_be_clickable(self.HEADER_DELETE_ACC_BTTN)).click()

    @allure.step("Click 'Test Cases' header button")
    def click_testcases_button(self):
        self.wait.until(EC.element_to_be_clickable(self.HEADER_TEST_CASE_BTTN)).click()

    @allure.step("Click 'Contact Us' header button")
    def click_contact_us_button(self):
        self.wait.until(EC.element_to_be_clickable(self.HEADER_CONTACT_US_BTTN)).click()

    @allure.step("Click move upward arrow button")
    def click_move_upward_button(self):
        self.wait.until(EC.visibility_of_element_located(self.SCROLL_UP_BTTN))
        self.wait.until(EC.element_to_be_clickable(self.SCROLL_UP_BTTN)).click()

    @allure.step("Scroll down page to bottom")
    def page_scroll_down(self):
        actions = ActionChains(self.browser)
        actions.send_keys(Keys.END).perform()

    @allure.step("Scroll up")
    def page_scroll_up(self):
        actions = ActionChains(self.browser)
        actions.send_keys(Keys.HOME).perform()

    @allure.step("'SUBSCRIPTION' footer block visible")
    def is_subscription_label_visible(self):
        self.wait.until(EC.visibility_of_element_located(self.SUBSCRIPTION_TEXT))
        self.wait.until(EC.visibility_of_element_located(self.SUBSCRIPTION_BTTN))
        self.wait.until(EC.visibility_of_element_located(self.SUBSCRIPTION_EMAIL_FIELD))
       

    @allure.step("Site header visible")
    def is_header_visible(self):
        self.wait.until(EC.visibility_of_element_located(self.HEADER))

    @allure.step("'Full-Fledged practice website...' slider text label visible")
    def is_active_slider_text_visible(self):
        self.wait.until(EC.visibility_of_element_located(self.ACTIVE_SLIDER_TEXT))
        self.wait.until(EC.element_to_be_clickable(self.ACTIVE_SLIDER_TEXT))          