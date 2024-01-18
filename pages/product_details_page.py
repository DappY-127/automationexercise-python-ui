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
# this locators same as in products page, need to refactor later!!!
    PRODUCT_ADDED_MODAL = ("css selector", "#cartModal .modal-content")
    MODAL_VIEW_CART_BTTN = ("css selector", "#cartModal [href='/view_cart']")
    MODAL_CONTINUE_SHOPPING_BTTN = ("css selector", "#cartModal .btn")

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

    @allure.step("Set product quantity")
    def set_product_quantity(self, quantity):
        self.fill_field(self.PRODUCT_QUANTITY_INPUT, f"{quantity}")

# this method same as in products page need to refactor it later to keep DRY 
    @allure.step("'Your product has been added to cart.' modal pop up visible")
    def is_added_modal_visible(self):
        self.wait.until(EC.visibility_of_element_located(self.PRODUCT_ADDED_MODAL))
        self.wait.until(EC.visibility_of_element_located(self.MODAL_VIEW_CART_BTTN))
        self.wait.until(EC.visibility_of_element_located(self.MODAL_CONTINUE_SHOPPING_BTTN))
        self.wait.until(EC.element_to_be_clickable(self.MODAL_VIEW_CART_BTTN))
        self.wait.until(EC.element_to_be_clickable(self.MODAL_CONTINUE_SHOPPING_BTTN))

# this method same as in products page need to refactor it later to keep DRY 
    @allure.step("Click 'Continue Shopping' button")
    def click_continue_shopping_bttn(self):
        self.is_added_modal_visible()
        self.wait.until(EC.element_to_be_clickable(self.MODAL_CONTINUE_SHOPPING_BTTN)).click()

# this method same as in products page need to refactor it later to keep DRY 
    @allure.step("Click 'View Cart' button")
    def click_view_cart_bttn(self):
        self.is_added_modal_visible()
        self.wait.until(EC.element_to_be_clickable(self.MODAL_VIEW_CART_BTTN)).click()     
