import allure
from allure_commons.types import AttachmentType
from faker import Faker
from .header_footer_elements import HeaderFooterElements
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class BasePage(HeaderFooterElements):

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10, poll_frequency=1)
        self.fake = Faker()

    def open(self):
        with allure.step(f"Open {self.PAGE_URL} page"):
            self.browser.get(self.PAGE_URL)         

    def is_opened(self):
        with allure.step(f"Page {self.PAGE_URL} is opened"):
            self.wait.until(EC.url_to_be(self.PAGE_URL))

    def make_screenshot(self, screenshot_name):
        allure.attach(
            body=self.browser.get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=AttachmentType.PNG
        )

    def fill_field(self, locator, value):
        # field = self.wait.until(EC.element_to_be_clickable(locator))
        field = self.wait.until(EC.visibility_of_element_located(locator))
        field.clear()
        field.send_keys(value)       

    @allure.step("Scroll down page to bottom")
    def page_scroll_down(self):
        actions = ActionChains(self.browser)
        actions.send_keys(Keys.END).perform()

    @allure.step("Scroll up")
    def page_scroll_up(self):
        actions = ActionChains(self.browser)
        actions.send_keys(Keys.HOME).perform()
