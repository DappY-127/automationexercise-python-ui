import allure
from .base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):

    PAGE_URL= Links.HOME_PAGE

    SCROLL_UP_BTTN = ('css selector', '#scrollUp')
    ACTIVE_SLIDER_TEXT = ("xpath", "//div[@class = 'item active']//h2[contains(text(), 'Full-Fledged practice website for Automation Engineers')]")
    RECOMENDED_PRODUCTS_SLIDER = ("css selector", ".recommended_items")
    RECOMENDED_PRODUCTS_SLIDER_LEFT_ARROW = ("css selector", ".left.recommended-item-control")
    RECOMENDED_PRODUCTS_SLIDER_RIGHT_ARROW = ("css selector", ".right.recommended-item-control")
    RECOMENDED_PRODUCTS_CART_BTTNS = ("css selector", "#recommended-item-carousel .add-to-cart")
    ACTIVE_RECOMENDED_PRODUCTS_CART_BTTNS = ("css selector", "#recommended-item-carousel .active .add-to-cart")
    FIRST_ACTIVE_RECOMENDED_PRODUCTS_CART_BTTN = ("xpath", "(//*[@id='recommended-item-carousel']//*[contains(@class, 'active')]//*[contains(@class, 'add-to-cart')])[1]")
# this locators same as in products page, need to refactor later!!!
    PRODUCT_ADDED_MODAL = ("css selector", "#cartModal .modal-content")
    MODAL_VIEW_CART_BTTN = ("css selector", "#cartModal [href='/view_cart']")
    MODAL_CONTINUE_SHOPPING_BTTN = ("css selector", "#cartModal .btn")


    @allure.step("Click move upward arrow button")
    def click_move_upward_button(self):
        self.wait.until(EC.visibility_of_element_located(self.SCROLL_UP_BTTN))
        self.wait.until(EC.element_to_be_clickable(self.SCROLL_UP_BTTN)).click()

    @allure.step("Click add to cart first recomended product button")
    def click_first_recomended_product_add_to_cart_button(self):
        self.wait.until(EC.visibility_of_element_located(self.FIRST_ACTIVE_RECOMENDED_PRODUCTS_CART_BTTN))
        self.wait.until(EC.element_to_be_clickable(self.FIRST_ACTIVE_RECOMENDED_PRODUCTS_CART_BTTN)).click()

    @allure.step("'Full-Fledged practice website...' slider text label visible")
    def is_active_slider_text_visible(self):
        self.wait.until(EC.visibility_of_element_located(self.ACTIVE_SLIDER_TEXT))
        self.wait.until(EC.element_to_be_clickable(self.ACTIVE_SLIDER_TEXT))          

    @allure.step("Scroll down to 'Recomended Products' slider and its visible")
    def is_recomended_products_slider_visible(self):
        self.scroll_into_view(self.RECOMENDED_PRODUCTS_SLIDER) 
        self.wait.until(EC.visibility_of_element_located(self.RECOMENDED_PRODUCTS_SLIDER))
        self.make_screenshot("Recomended products")      

    @allure.step("Click on 'View product' product bttn by product id")
    def click_view_product_bttn_by_id(self, product_id):
        view_bttn_locator = ("xpath", f"//div[@class='choose']//a[@href='/product_details/{product_id}']")
        self.scroll_into_view(view_bttn_locator)
        self.wait.until(EC.element_to_be_clickable(view_bttn_locator)).click()         

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