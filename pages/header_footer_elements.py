import allure
from selenium.webdriver.support import expected_conditions as EC


class HeaderFooterElements():
    
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
    SUCCESS_SUBSCRIBE_MSSG = ('css selector', '#success-subscribe')
    HEADER = ("css selector", ".nav.navbar-nav")
    USERNAME_FIELD = ("xpath", "//input[@name='username']")
    USER_STATUS = ('xpath', '//a[contains(text(), "Logged in as")]')

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

    @allure.step("Click subscribe footer button")
    def click_subscribe_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBSCRIPTION_BTTN)).click()

    @allure.step("Click cart header button")
    def click_cart_button(self):
        self.wait.until(EC.element_to_be_clickable(self.HEADER_CART_BTTN)).click()

    @allure.step("Click products header button")
    def click_products_button(self):
        self.wait.until(EC.element_to_be_clickable(self.HEADER_PRODUCTS_BTTN)).click()

    @allure.step("Click delete account header button")
    def click_delete_account_button(self):
        self.wait.until(EC.visibility_of_element_located(self.HEADER_DELETE_ACC_BTTN))  
        self.wait.until(EC.element_to_be_clickable(self.HEADER_DELETE_ACC_BTTN)).click()

    @allure.step("'SUBSCRIPTION' footer block visible")
    def is_subscription_label_visible(self):
        self.wait.until(EC.visibility_of_element_located(self.SUBSCRIPTION_TEXT))
        self.wait.until(EC.visibility_of_element_located(self.SUBSCRIPTION_BTTN))
        self.wait.until(EC.visibility_of_element_located(self.SUBSCRIPTION_EMAIL_FIELD))
       
    @allure.step("Site header visible")
    def is_header_visible(self):
        self.wait.until(EC.visibility_of_element_located(self.HEADER))      

    @allure.step("User name header visible")
    def is_user_name_header_visible(self):
        self.wait.until(EC.visibility_of_element_located(self.HEADER_LOGOUT_BTTN))      
        self.wait.until(EC.visibility_of_element_located(self.HEADER_DELETE_ACC_BTTN))      
        # self.wait.until(EC.visibility_of_element_located(self.USERNAME_FIELD))      
        # self.wait.until(EC.visibility_of_element_located(self.USER_STATUS))      

    # def is_user_status_correct(self):
    #     user_name = self.USER_STATUS.text
    #     expected_user_status = f' Logged in as {user_name}'

    #     if user_status_text == expected_user_status:
    #         return True
    #     else:
    #         raise ValueError(f'User status incorrect. Expected: {expected_user_status}. Actual: {user_status_text}')

    @allure.step("Fill email in subscription field")
    def fill_subscription_email(self):
        self.fill_field(self.SUBSCRIPTION_EMAIL_FIELD, self.fake.email())          

    @allure.step("Succes subscription footer message visible")
    def is_succes_subscription_mssg_visible(self):
        self.wait.until(EC.visibility_of_element_located(self.SUCCESS_SUBSCRIBE_MSSG))   
        self.make_screenshot("Success message")
