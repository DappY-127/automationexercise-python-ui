import allure
from .base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage(BasePage):
    
    PAGE_URL= Links.PRODUCT_PAGE

    LEFT_SIDEBAR = ("css selector", ".left-sidebar")
    CATEGORY_SIDEBAR = ("css selector", ".left-sidebar #accordian")
    BRANDS_SIDEBAR = ("css selector", ".left-sidebar .brands-name")
    ALL_PRODUCTS = ("css selector", ".features_items")
    PRODUCTS_SEARCH_FIELD = ("css selector", "#search_product")
    SUBMIT_SEARCH_BTTN = ("css selector", "#submit_search")
    # FIRST_PRODUCT_CARD = ()
    FIRST_PRODUCT_CARD_VIEW_PRODUCT_BTTN = ("css selector", ".choose [href='/product_details/1']")

    @allure.step("'ALL PRODUCTS' page visible")
    def is_products_visible(self):
        self.wait.until(EC.visibility_of_element_located(self.LEFT_SIDEBAR))
        self.wait.until(EC.visibility_of_element_located(self.ALL_PRODUCTS))
        self.make_screenshot("Products page")

    @allure.step("'SEARCH PRODUCTS' page visible")
    def is_searched_products_visible(self):
        self.wait.until(EC.visibility_of_element_located(self.LEFT_SIDEBAR))
        self.wait.until(EC.visibility_of_element_located(self.ALL_PRODUCTS))
        self.make_screenshot("Searched products page")

    @allure.step("Enter product name in search input and click search button")
    def fill_product_search_and_click_search_bttn(self):
        self.fill_field(self.PRODUCTS_SEARCH_FIELD, "Dress")
        self.wait.until(EC.visibility_of_element_located(self.SUBMIT_SEARCH_BTTN))       
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_SEARCH_BTTN)).click()  
        self.make_screenshot("Search result")
              