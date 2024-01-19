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

    @allure.step("Check if the cart is empty")
    def is_cart_empty(self):
        is_visible = self.wait.until(EC.visibility_of_element_located(self.EMPTY_CART))
        allure.attach(f"Is Cart Empty: {is_visible}", name="Cart Empty Check")
        self.make_screenshot("Empty Cart")

    @allure.step("Check firs cart product quantity")
    def check_cart_first_product_quantity(self, quantity):
        actual_quantity = self.get_cart_product_quantities()
        actual_quantity = int(actual_quantity[0])
        with allure.step(f"Verify quantity is correct for first cart product"):
            assert actual_quantity == quantity, f"Expected: {quantity}, Actual: {actual_quantity}"
        self.make_screenshot("Product quantity")
        
    @allure.step("Products at cart presence")
    def is_cart_products_present(self, *product_names_to_check):
        self.is_cart_not_empty()
        cart_product_names = self.get_cart_product_names()

        for product_name in product_names_to_check:
            assert product_name in cart_product_names, f"Product '{product_name}' not found in the cart"

        allure.attach(f"Products Checked: {', '.join(product_names_to_check)}", name="Products Presence Check")
        # Additional checks for other cart elements
        self.wait.until(EC.presence_of_all_elements_located(self.CART_PRODUCT_QUANTITY))
        self.wait.until(EC.presence_of_all_elements_located(self.CART_PRODUCT_PRICES))
        self.wait.until(EC.presence_of_all_elements_located(self.CART_TOTAL_PRODUCT_PRICES))
        self.make_screenshot("Cart products")

    @allure.step("Delete first product from cart")
    def delete_first_cart_product(self):
        self.is_cart_not_empty()
        delete_button_locator = ("xpath", "//a[@class='cart_quantity_delete'][1]")
        delete_button = self.wait.until(EC.element_to_be_clickable(delete_button_locator))
        delete_button.click()

        product_name = self.get_cart_product_names()[0]
        delete_button.click()
        allure.attach(f"Deleted Product: {product_name}", name="Deleted Product")
