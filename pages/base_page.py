import allure
from allure_commons.types import AttachmentType
from faker import Faker
from .header_footer_elements import HeaderFooterElements
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from config.data import Data


class BasePage(HeaderFooterElements):

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 15, poll_frequency=1)
        self.fake = Faker()
        self.data = Data()

    def open(self):
        with allure.step(f"Open {self.PAGE_URL} page"):
            self.browser.get(self.PAGE_URL)         

    def is_opened(self):
        # with allure.step(f"Page {self.PAGE_URL} is opened"):
        #     self.wait.until(EC.url_to_be(self.PAGE_URL))
        
        self.check_and_close_ad_if_present()
        try:
            with allure.step(f"Page {self.PAGE_URL} is opened"):
                self.check_and_close_ad_if_present()
                self.wait.until_not(EC.url_contains("#google_vignette"))
                self.wait.until(EC.url_to_be(self.PAGE_URL))
        except Exception as e:
            current_url = self.browser.current_url
            self.make_screenshot("Opened page")
            allure.attach(f"Test failed. Exception: {str(e)}. Current URL: {current_url}", name="Test Failure Details", attachment_type=allure.attachment_type.TEXT)
            raise

    def make_screenshot(self, screenshot_name):
        allure.attach(
            body=self.browser.get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=AttachmentType.PNG
        )

    @allure.step("Fill field with value: {value}")
    def fill_field(self, locator, value):
        # field = self.wait.until(EC.element_to_be_clickable(locator))
        field = self.wait.until(EC.visibility_of_element_located(locator))
        field.clear()
        field.send_keys(value)

    @allure.step("Select option with value: {option_text}")
    def select_option(self, select_locator, option_text):
        select_element = self.wait.until(EC.visibility_of_element_located(select_locator))
        select = Select(select_element)
        try:
            select.select_by_visible_text(option_text)
        except NoSuchElementException:
            # If not found by visible text, try selecting by value
            select.select_by_value(option_text)

    def select_radio_button(self, radio_locator):
        radio_button = self.wait.until(EC.element_to_be_clickable(radio_locator))
        radio_button.click()

    def select_checkbox(self, checkbox_locator):
        checkbox = self.wait.until(EC.element_to_be_clickable(checkbox_locator))
        if not checkbox.is_selected():
            checkbox.click()

    def unselect_checkbox(self, checkbox_locator):
        checkbox = self.wait.until(EC.element_to_be_clickable(checkbox_locator))
        if checkbox.is_selected():
            checkbox.click()

    @allure.step("Scroll down page to bottom")
    def page_scroll_down(self):
        actions = ActionChains(self.browser)
        actions.send_keys(Keys.END).perform()

    @allure.step("Scroll up")
    def page_scroll_up(self):
        actions = ActionChains(self.browser)
        actions.send_keys(Keys.HOME).perform()

    @allure.step("Verify user status text")
    def is_user_status_correct(self):
        user_name = self.data.login_name
        user_status_element = self.wait.until(EC.visibility_of_element_located(self.USER_STATUS))
        user_status_text = user_status_element.text
        expected_user_status = f'Logged in as {user_name}'

        with allure.step(f"Verify user status text is correct for user {user_name}"):
            assert user_status_text == expected_user_status, f"Expected: {expected_user_status}, Actual: {user_status_text}"

    @allure.step("Scroll element into view")
    def scroll_into_view(self, element_locator):
        element = self.wait.until(EC.presence_of_element_located(element_locator))
        self.browser.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Hover mouse over element")
    def hover_over_element(self, element_locator):
        element = self.wait.until(EC.presence_of_element_located(element_locator))
        actions = ActionChains(self.browser)
        actions.move_to_element(element).perform() 

    # Helper methods
    def get_elements_text(self, locator):
        elements = self.wait.until(EC.presence_of_all_elements_located(locator))
        return [element.text for element in elements]

    def get_element_text(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        return element.text                   
