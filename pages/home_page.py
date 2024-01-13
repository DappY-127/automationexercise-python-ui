import allure
from .base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):

    PAGE_URL= Links.HOME_PAGE

    SCROLL_UP_BTTN = ('css selector', '#scrollUp')
    ACTIVE_SLIDER_TEXT = ("xpath", "//div[@class = 'item active']//h2[contains(text(), 'Full-Fledged practice website for Automation Engineers')]")

    @allure.step("Click move upward arrow button")
    def click_move_upward_button(self):
        self.wait.until(EC.visibility_of_element_located(self.SCROLL_UP_BTTN))
        self.wait.until(EC.element_to_be_clickable(self.SCROLL_UP_BTTN)).click()

    @allure.step("'Full-Fledged practice website...' slider text label visible")
    def is_active_slider_text_visible(self):
        self.wait.until(EC.visibility_of_element_located(self.ACTIVE_SLIDER_TEXT))
        self.wait.until(EC.element_to_be_clickable(self.ACTIVE_SLIDER_TEXT))          