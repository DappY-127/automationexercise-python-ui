import allure
import pytest
from .base_test import BaseTest
import random


@allure.feature("Product Management")
class TestProductManagementFeature(BaseTest):
    
    @allure.title("Verify All Products and Product Detail Page")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("Product Display & Information")
    @allure.tag('TestCaseID: 8')
    def test_product_detail_presence(self):
        self.home_page.open()
        self.home_page.is_opened()
        self.home_page.click_products_button()
        self.products_page.is_header_visible()
        self.products_page.is_opened()
        self.products_page.is_products_visible()
        self.products_page.click_view_product_bttn_by_id(2)
        self.product_details_page.is_header_visible()
        self.product_details_page.is_product_details_visible()

    valid_categories = ["Women", "Men", "Kids"]
    valid_subcategories = {
        "Women": ["Dress", "Tops", "Saree"],
        "Men": ["Tshirts", "Jeans"],
        "Kids": ["Dress", "Tops & Shirts"]
    }

    category = random.choice(valid_categories)
    subcategory = random.choice(valid_subcategories[category])

    @allure.title("View Category Products")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("Product Display & Information")
    @allure.tag('TestCaseID: 18')
    # @pytest.mark.parametrize("category, subcategory", [("Women", "Dress"), ("Women", "Tops"), ("Women", "Saree"),
    #                                                 ("Men", "Tshirts"), ("Men", "Jeans"),
    #                                                 ("Kids", "Dress"), ("Kids", "Tops & Shirts")])
    def test_category_products_presence(self):
        self.home_page.open()
        self.home_page.is_opened()
        self.home_page.click_products_button()
        self.products_page.is_header_visible()
        self.products_page.is_opened()
        self.products_page.is_products_visible()
        self.products_page.click_category_and_subcategory(self.category, self.subcategory)
        self.products_page.is_header_visible()
        self.products_page.is_products_visible()
        self.products_page.verify_category_and_subcategory_products(self.category, self.subcategory)

    valid_brands = ["Polo", "H&M", "Madame", "Mast & Harbour", "Babyhug", "Allen Solly Junior", "Kookie Kids", "Biba"]

    brand = random.choice(valid_brands)

    @allure.title("View & Cart Brand Products")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("Product Display & Information")
    @allure.tag('TestCaseID: 19')
    # @pytest.mark.parametrize("brand", valid_brands)
    def test_brand_products_presence(self):
        self.home_page.open()
        self.home_page.is_opened()
        self.home_page.click_products_button()
        self.products_page.is_header_visible()
        self.products_page.is_opened()
        self.products_page.is_products_visible()
        self.products_page.click_product_sidebar_category(self.brand)
        self.products_page.is_header_visible()
        self.products_page.verify_brand_page_and_brand_products(self.brand)        

    @allure.title("Search Product")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("Product Display & Information")
    @allure.tag('TestCaseID: 9')
    def test_product_search(self):
        self.home_page.open()
        self.home_page.is_opened()
        self.home_page.click_products_button()
        self.products_page.is_opened()
        self.products_page.is_header_visible()
        self.products_page.is_products_visible()
        self.products_page.fill_product_search_and_click_search_bttn("Dress")
        self.products_page.is_searched_products_visible()

    @allure.title("Add Products in Cart")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Cart & Wishlist")
    @allure.tag('TestCaseID: 12')
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

    @allure.title("Verify Product Quantity in Cart")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Cart & Wishlist")
    @allure.tag('TestCaseID: 13')
    def test_product_cart_quantity(self):
        self.home_page.open()
        self.home_page.is_opened()
        self.home_page.click_view_product_bttn_by_id(6)
        self.product_details_page.is_product_details_visible()
        self.product_details_page.set_product_quantity(4)
        self.product_details_page.click_add_to_cart_bttn()
        self.product_details_page.click_view_cart_bttn()
        self.cart_page.is_opened()
        self.cart_page.check_cart_first_product_quantity(4)

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

    @allure.title("Add Review on Product")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Cart & Wishlist")
    @allure.tag('TestCaseID: 21')
    def test_add_product_review(self):
        self.home_page.open()
        self.home_page.is_opened()
        self.home_page.click_view_product_bttn_by_id(5)
        self.product_details_page.is_product_details_visible()
        self.product_details_page.add_product_review()
        self.product_details_page.is_success_mssg_visible()
        

    @allure.title("Add to cart from Recommended items")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Cart & Wishlist")
    @allure.tag('TestCaseID: 22')
    def test_add_to_cart_from_recomended_items(self):
        self.home_page.open()
        self.home_page.is_opened()
        self.home_page.is_recomended_products_slider_visible()
        self.home_page.click_first_recomended_product_add_to_cart_button()
        self.home_page.click_view_cart_bttn()
        self.cart_page.is_opened()
        self.cart_page.is_cart_not_empty()
