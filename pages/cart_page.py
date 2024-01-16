import allure
from .base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class CartPage(BasePage):
    
    PAGE_URL= Links.CART_PAGE

    EMPTY_CART = ("css selector", "#empty_cart")
    PROCEED_TO_CHECKOUT_BTTN = ("css selector", "a[class='btn btn-default check_out']")
    CART_PRODUCT_NAMES = ("xpath", "//td[contains(@class, 'cart_description')]//a")
    CART_PRODUCT_PRICES = ("xpath", "//td[contains(@class, 'cart_price')]/p")
    CART_PRODUCT_QUANTITY = ("xpath", "//td[contains(@class, 'cart_quantity')]/button")
    CART_TOTAL_PRODUCT_PRICES = ("xpath", "//p[contains(@class, 'cart_total_price')]")
    DELETE_FROM_CART_BTTNS = ("xpath", "a[class='cart_quantity_delete']")
    
    @allure.step("Get list of product names in the cart")
    def get_cart_product_names(self):
        product_names = self.get_elements_text(self.CART_PRODUCT_NAMES)
        allure.attach(f"Product Names: {', '.join(product_names)}", name="Cart Products")
        return product_names

    @allure.step("Get list of product prices in the cart")
    def get_cart_product_prices(self):
        product_prices = self.get_elements_text(self.CART_PRODUCT_PRICES)
        allure.attach(f"Product Prices: {', '.join(product_prices)}", name="Cart Product Prices")
        return product_prices

    @allure.step("Get list of product quantities in the cart")
    def get_cart_product_quantities(self):
        product_quantities = self.get_elements_text(self.CART_PRODUCT_QUANTITY)
        allure.attach(f"Product Quantities: {', '.join(product_quantities)}", name="Cart Product Quantities")
        return product_quantities

    @allure.step("Get total price of products in the cart")
    def get_cart_total_price(self):
        total_price = self.get_element_text(self.CART_TOTAL_PRODUCT_PRICES)
        allure.attach(f"Total Price: {total_price}", name="Cart Total Price")
        return total_price

    @allure.step("Check if the cart is not empty")
    def is_cart_not_empty(self):
        is_empty = self.wait.until(EC.invisibility_of_element_located(self.EMPTY_CART))
        allure.attach(f"Is Cart Empty: {not is_empty}", name="Cart Empty Check")
        return not is_empty

    @allure.step("Products at cart presence")
    def is_cart_products_present(self):
        self.wait.until(EC.presence_of_all_elements_located(self.CART_PRODUCT_NAMES))
        self.wait.until(EC.presence_of_all_elements_located(self.CART_PRODUCT_QUANTITY))
        self.wait.until(EC.presence_of_all_elements_located(self.CART_PRODUCT_PRICES))
        self.wait.until(EC.presence_of_all_elements_located(self.CART_TOTAL_PRODUCT_PRICES))

    # Helper methods
    def get_elements_text(self, locator):
        elements = self.wait.until(EC.presence_of_all_elements_located(locator))
        return [element.text for element in elements]

    def get_element_text(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        return element.text