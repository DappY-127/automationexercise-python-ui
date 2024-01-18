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

    @allure.step("Click on 'View product' product bttn by product id")
    def click_view_product_bttn_by_id(self, product_id):
        view_bttn_locator = ("xpath", f"//div[@class='choose']//a[@href='/product_details/{product_id}']")
        self.scroll_into_view(view_bttn_locator)
        self.wait.until(EC.element_to_be_clickable(view_bttn_locator)).click()         