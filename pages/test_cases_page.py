import allure
from .base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class TestCasesPage(BasePage):
    
    PAGE_URL= Links.TEST_CASES_PAGE

    TEST_CASES = ("css selector", ".panel-group h4")

    @allure.step("Test cases panels visible")
    def is_testcases_visible(self):
        self.wait.until(EC.visibility_of_all_elements_located(self.TEST_CASES))
