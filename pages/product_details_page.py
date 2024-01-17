import allure
from .base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class ProductDetailsPage(BasePage):
    
    PRODUCT_NAME = ("xpath", "//div[@class='product-information']/h2")
    PRODUCT_CATEGORY = ("xpath", "//div[@class='product-information']/p")
    PRODUCT_PRICE = ("xpath", "//div[@class='product-information']/span/span")
    PRODUCT_QUANTITY_INPUT = ("css selector", "#quantity")
    PRODUCT_AVAILABILITY = ("xpath", "(//div[@class='product-information']/p)[2]")
    PRODUCT_CONDITION = ("xpath", "(//div[@class='product-information']/p)[3]")
    PRODUCT_BRAND = ("xpath", "(//div[@class='product-information']/p)[4]")
    ADD_TO_CART_BTTN = ("css selector", "button.cart")
    REVIEW_NAME_FIELD = ("css selector", "#name")
    REVIEW_EMAIL_FIELD = ("css selector", "#email")
    REVIEW_FIELD = ("css selector", "#review")
    SUBMIT_REVIEW_BTTN = ("css selector", "#button-review")

    @allure.step("Click 'Add to cart' button")
    def click_add_to_cart_bttn(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_TO_CART_BTTN)).click()   

    @allure.step("Click 'Submit' review button")
    def click_submit_review_bttn(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_REVIEW_BTTN)).click()

    @allure.step("Product information visible")
    def is_product_details_visible(self):    
        self.wait.until(EC.visibility_of_element_located(self.PRODUCT_NAME))  
        self.wait.until(EC.visibility_of_element_located(self.PRODUCT_PRICE))  
        self.wait.until(EC.visibility_of_element_located(self.PRODUCT_CATEGORY))  
        self.wait.until(EC.visibility_of_element_located(self.PRODUCT_AVAILABILITY))  
        self.wait.until(EC.visibility_of_element_located(self.PRODUCT_CONDITION))  
        self.wait.until(EC.visibility_of_element_located(self.PRODUCT_BRAND))  