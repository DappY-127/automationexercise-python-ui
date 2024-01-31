import allure
from .base_test import BaseTest


@allure.feature("Shopping & Checkout")
class TestShoppingCheckoutFeature(BaseTest):
    
    @allure.title("Verify Subscription in home page")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Subscription Handling")
    @allure.tag('TestCaseID: 10')
    def test_verify_subscription_at_home_page(self):
        self.home_page.open()
        self.home_page.is_opened()
        self.home_page.page_scroll_down()
        self.home_page.is_subscription_label_visible()
        self.home_page.fill_subscription_email()
        self.home_page.click_subscribe_button()     
        self.home_page.is_succes_subscription_mssg_visible()   

    @allure.title("Verify Subscription in cart page")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Subscription Handling")
    @allure.tag('TestCaseID: 11')
    def test_verify_subscription_at_cart_page(self):
        self.home_page.open()
        self.home_page.is_opened()
        self.home_page.click_cart_button()
        self.cart_page.is_opened()
        self.cart_page.is_header_visible()
        self.cart_page.page_scroll_down()
        self.cart_page.is_subscription_label_visible()
        self.cart_page.fill_subscription_email()
        self.cart_page.click_subscribe_button()     
        self.cart_page.is_succes_subscription_mssg_visible()

    @allure.title("Place Order: Register while Checkout")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Checkout Process")
    @allure.tag('TestCaseID: 14')
    def test_order_placement_register_while_checkout(self):
        self.home_page.open()
        self.home_page.is_opened()
        self.home_page.click_products_button()
        self.products_page.is_opened()
        self.products_page.add_product_to_cart_by_name('Lace Top For Women')
        self.products_page.click_view_cart_bttn()
        self.cart_page.is_opened()
        self.cart_page.is_cart_products_present('Lace Top For Women') 
        self.cart_page.click_proceed_to_checkout_bttn()
        self.cart_page.click_login_register_bttn()
        self.signup_login_page.is_opened()
        self.signup_login_page.enter_signup_name()
        self.signup_login_page.enter_signup_email()
        self.signup_login_page.click_signup_button()
        self.signup_page.is_opened()
        self.signup_page.fill_account_info_section()
        self.signup_page.fill_address_info_section()
        self.signup_page.click_create_account_button()
        self.account_created_page.is_opened()
        self.account_created_page.is_account_created_message_visible()
        self.account_created_page.click_continue_button()
        self.home_page.is_opened()
        self.home_page.is_user_name_header_visible()
        self.home_page.is_user_status_correct()
        self.home_page.click_cart_button()
        self.cart_page.is_opened()
        self.cart_page.is_cart_products_present('Lace Top For Women') 
        self.cart_page.click_proceed_to_checkout_bttn()
        self.checkout_page.is_opened()
        self.checkout_page.is_delivery_address_visible()
        self.checkout_page.is_billing_address_visible()
        self.checkout_page.verify_delivery_address_info()
        self.checkout_page.verify_billing_address_info()
        self.checkout_page.fill_order_commnets()
        self.checkout_page.click_place_order_button()       
        self.payment_page.is_payments_label_visible()  
        self.payment_page.fill_payment_details_section()  
        self.payment_page.click_confirm_order_button()
        self.order_placement_page.is_order_placed_message_visible()
        self.order_placement_page.click_continue_button()
        self.home_page.is_opened()

        self.account_deletion()

    @allure.title("Place Order: Register before Checkout")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Checkout Process")
    @allure.tag('TestCaseID: 15')
    def test_order_placement_register_before_checkout(self):
        self.account_register()

        self.home_page.click_products_button()
        self.products_page.is_opened()
        self.products_page.add_product_to_cart_by_name('Rose Pink Embroidered Maxi Dress')
        self.products_page.click_view_cart_bttn()
        self.cart_page.is_opened()
        self.cart_page.is_cart_products_present('Rose Pink Embroidered Maxi Dress') 
        self.cart_page.click_proceed_to_checkout_bttn()
        self.checkout_page.is_opened()
        self.checkout_page.is_delivery_address_visible()
        self.checkout_page.is_billing_address_visible()
        self.checkout_page.verify_delivery_address_info()
        self.checkout_page.verify_billing_address_info()
        self.checkout_page.fill_order_commnets()
        self.checkout_page.click_place_order_button()       
        self.payment_page.is_payments_label_visible()  
        self.payment_page.fill_payment_details_section()  
        self.payment_page.click_confirm_order_button()
        self.order_placement_page.is_order_placed_message_visible()
        self.order_placement_page.click_continue_button()
        self.home_page.is_opened()

        self.account_deletion()  

    @allure.title("Place Order: Login before Checkout")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Checkout Process")
    @allure.tag('TestCaseID: 16')
    def test_order_placement_login_before_checkout(self):
        self.account_register()
        self.account_logout()
        self.account_login()

        self.home_page.click_products_button()
        self.products_page.is_opened()
        self.products_page.add_product_to_cart_by_name('Little Girls Mr. Panda Shirt')
        self.products_page.click_view_cart_bttn()
        self.cart_page.is_opened()
        self.cart_page.is_cart_products_present('Little Girls Mr. Panda Shirt') 
        self.cart_page.click_proceed_to_checkout_bttn()
        self.checkout_page.is_opened()
        self.checkout_page.is_delivery_address_visible()
        self.checkout_page.is_billing_address_visible()
        self.checkout_page.verify_delivery_address_info()
        self.checkout_page.verify_billing_address_info()
        self.checkout_page.fill_order_commnets()
        self.checkout_page.click_place_order_button()       
        self.payment_page.is_payments_label_visible()  
        self.payment_page.fill_payment_details_section()  
        self.payment_page.click_confirm_order_button()
        self.order_placement_page.is_order_placed_message_visible()
        self.order_placement_page.click_continue_button()
        self.home_page.is_opened()

        self.account_deletion()          

    @allure.title("Search Products and Verify Cart After Login")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Checkout Process")
    @allure.tag('TestCaseID: 20')
    def test_products_presence_at_cart_after_login(self):
        self.account_register()
        self.account_logout()

        self.home_page.open()
        self.home_page.is_opened()
        self.home_page.click_products_button()
        self.products_page.is_opened()
        self.products_page.is_header_visible()
        self.products_page.is_products_visible()
        self.products_page.fill_product_search_and_click_search_bttn("Jeans")
        self.products_page.is_searched_products_visible()
        self.products_page.add_product_to_cart_by_name('Soft Stretch Jeans')
        self.products_page.click_continue_shopping_bttn()
        self.products_page.add_product_to_cart_by_name('Regular Fit Straight Jeans')
        self.products_page.click_continue_shopping_bttn()
        self.products_page.add_product_to_cart_by_name('Grunt Blue Slim Fit Jeans')
        self.products_page.click_view_cart_bttn()
        self.cart_page.is_opened()
        self.cart_page.is_cart_products_present('Soft Stretch Jeans', 'Regular Fit Straight Jeans', 'Grunt Blue Slim Fit Jeans')
        self.cart_page.click_signup_login_button()

        self.account_login()

        self.home_page.click_cart_button()
        self.cart_page.is_opened()
        self.cart_page.is_cart_products_present('Soft Stretch Jeans', 'Regular Fit Straight Jeans', 'Grunt Blue Slim Fit Jeans')

        self.cart_page.click_home_button()
        self.account_deletion() 

    @allure.title("Verify address details in checkout page")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Checkout Process")
    @allure.tag('TestCaseID: 23')
    def test_address_details_in_checkout_page(self):
        self.account_register()

        self.home_page.click_products_button()
        self.products_page.is_opened()
        self.products_page.is_header_visible()
        self.products_page.is_products_visible()
        self.products_page.add_product_to_cart_by_name('Sleeves Printed Top - White')
        self.products_page.click_view_cart_bttn()
        self.cart_page.is_opened()
        self.cart_page.is_cart_products_present('Sleeves Printed Top - White')
        self.cart_page.click_proceed_to_checkout_bttn()
        self.checkout_page.is_opened()
        self.checkout_page.is_delivery_address_visible()
        self.checkout_page.is_billing_address_visible()
        self.checkout_page.verify_delivery_address_info()
        self.checkout_page.verify_billing_address_info()

        self.checkout_page.click_home_button()
        self.account_deletion()

    # @allure.title("Download Invoice after purchase order")
    # @allure.severity(allure.severity_level.CRITICAL)
    # @allure.story("Checkout Process")
    # @allure.tag('TestCaseID: 24')
    # def test_invoice_download_after_order_purchase(self): 
    #     self.account_register()

    #     self.home_page.click_products_button()
    #     self.products_page.is_opened()
    #     self.products_page.add_product_to_cart_by_name('Green Side Placket Detail T-Shirt')
    #     self.products_page.click_view_cart_bttn()
    #     self.cart_page.is_opened()
    #     self.cart_page.is_cart_products_present('Green Side Placket Detail T-Shirt') 
    #     self.cart_page.click_proceed_to_checkout_bttn()
    #     self.checkout_page.is_opened()
    #     self.checkout_page.is_delivery_address_visible()
    #     self.checkout_page.is_billing_address_visible()
    #     self.checkout_page.verify_delivery_address_info()
    #     self.checkout_page.verify_billing_address_info()
    #     self.checkout_page.fill_order_commnets()
    #     self.checkout_page.click_place_order_button()       
    #     self.payment_page.is_payments_label_visible()  
    #     self.payment_page.fill_payment_details_section()  
    #     self.payment_page.click_confirm_order_button()
    #     self.order_placement_page.is_order_placed_message_visible()
    #     self.order_placement_page.click_download_invoice_button()
    #     self.order_placement_page.click_continue_button()
    #     self.home_page.is_opened()

    #     self.account_deletion()         