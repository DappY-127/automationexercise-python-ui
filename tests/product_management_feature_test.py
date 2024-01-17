import allure
import pytest
from .base_test import BaseTest
import time


@allure.feature("Product Management")
class TestProductManagementFeature(BaseTest):
    
    @allure.title("Verify All Products and Product Detail Page")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("Product Display & Information")
    @allure.tag('TestCaseID: 8')
    def test_(self):
        self.home_page.open()
        self.home_page.is_opened()
        self.home_page.click_products_button()
        self.products_page.is_header_visible()
        self.products_page.is_opened()
        self.products_page.is_products_visible()
        self.products_page.click_view_product_bttn_by_id(2)
        self.product_details_page.is_product_details_visible()

    # @allure.title("View Category Products")
    # @allure.severity(allure.severity_level.NORMAL)
    # @allure.story("Product Display & Information")
    # @allure.tag('TestCaseID: 18')
    # def test_(self):
    #     # self.home_page.open()
    #     pass

    # @allure.title("View & Cart Brand Products")
    # @allure.severity(allure.severity_level.NORMAL)
    # @allure.story("Product Display & Information")
    # @allure.tag('TestCaseID: 19')
    # def test_(self):
    #     # self.home_page.open()
    #     pass

    # @allure.title("Search Product")
    # @allure.severity(allure.severity_level.NORMAL)
    # @allure.story("Product Display & Information")
    # @allure.tag('TestCaseID: 9')
    # def test_(self):
    #     self.home_page.open()
    #     self.home_page.click_products_button()
    #     self.products_page.is_opened()
    #     self.products_page.is_header_visible()
    #     self.products_page.is_products_visible()
    #     self.products_page.fill_product_search_and_click_search_bttn()
    #     self.products_page.is_searched_products_visible()

    @allure.title("Add Products in Cart")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Cart & Wishlist")
    @allure.tag('TestCaseID: 12')
    # @pytest.mark.skip()
    def test_add_product_to_cart(self):
        self.home_page.open()
        self.home_page.is_opened()
        self.home_page.click_products_button()
        self.products_page.is_opened()
        self.products_page.add_product_to_cart_by_name('Sleeveless Dress')
        self.products_page.click_continue_shopping_bttn()
        self.products_page.add_product_to_cart_by_name('Winter Top')
        self.products_page.click_view_cart_bttn()
        self.cart_page.is_opened()
        self.cart_page.is_cart_products_present('Sleeveless Dress', 'Winter Top')

    # @allure.title("Verify Product Quantity in Cart")
    # @allure.severity(allure.severity_level.CRITICAL)
    # @allure.story("Cart & Wishlist")
    # @allure.tag('TestCaseID: 13')
    # def test_product_cart_quantity(self):
    #     # self.home_page.open()
    #     pass

    @allure.title("Remove Products From Cart")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Cart & Wishlist")
    @allure.tag('TestCaseID: 17')
    def test_remove_product_from_cart(self):
        self.home_page.open()
        self.home_page.is_opened()
        self.home_page.click_products_button()
        self.products_page.is_opened()
        self.products_page.add_product_to_cart_by_name('Madame Top For Women')
        self.products_page.click_continue_shopping_bttn()
        self.products_page.add_product_to_cart_by_name('Winter Top')
        self.products_page.click_continue_shopping_bttn()
        self.products_page.add_product_to_cart_by_name('Lace Top For Women')
        self.products_page.click_view_cart_bttn()
        self.cart_page.is_opened()
        self.cart_page.is_cart_products_present('Madame Top For Women', 'Winter Top', 'Lace Top For Women')   
        self.cart_page.delete_first_cart_product()
        self.cart_page.is_cart_products_present('Winter Top', 'Lace Top For Women') 

    @allure.title("Remove All Products From Cart")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Cart & Wishlist")
    @allure.tag('TestCaseID: ~')
    def test_remove_product_from_cart_until_products_present(self):
        self.home_page.open()
        self.home_page.is_opened()
        self.home_page.click_products_button()
        self.products_page.is_opened()
        self.products_page.add_product_to_cart_by_name('Lace Top For Women')
        self.products_page.click_view_cart_bttn()
        self.cart_page.is_opened()
        self.cart_page.is_cart_products_present('Lace Top For Women')   
        self.cart_page.delete_first_cart_product()
        self.cart_page.is_cart_empty()    
