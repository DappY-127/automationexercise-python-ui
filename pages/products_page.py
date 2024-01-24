import allure
from .base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage(BasePage):
    
    PAGE_URL= Links.PRODUCT_PAGE

    LEFT_SIDEBAR = ("css selector", ".left-sidebar")
    CATEGORY_SIDEBAR = ("css selector", ".left-sidebar #accordian")
    BRANDS_SIDEBAR = ("css selector", ".left-sidebar .brands-name")
    BRANDS_SIDEBAR_CATEGORIES = ("css selector", ".left-sidebar .brands-name li")
    PRODUCTS_TEXT = ("css selector", ".features_items h2.text-center")
    ALL_PRODUCTS = ("css selector", ".features_items")
    ALL_PRODUCT_CARDS = ("xpath", "//div[@class='single-products']")
    PRODUCTS_SEARCH_FIELD = ("css selector", "#search_product")
    SUBMIT_SEARCH_BTTN = ("css selector", "#submit_search")
    PRODUCT_ADDED_MODAL = ("css selector", "#cartModal .modal-content")
    MODAL_VIEW_CART_BTTN = ("css selector", "#cartModal [href='/view_cart']")
    MODAL_CONTINUE_SHOPPING_BTTN = ("css selector", "#cartModal .btn")
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

    @allure.step("'Your product has been added to cart.' modal pop up visible")
    def is_added_modal_visible(self):
        self.wait.until(EC.visibility_of_element_located(self.PRODUCT_ADDED_MODAL))
        self.wait.until(EC.visibility_of_element_located(self.MODAL_VIEW_CART_BTTN))
        self.wait.until(EC.visibility_of_element_located(self.MODAL_CONTINUE_SHOPPING_BTTN))
        self.wait.until(EC.element_to_be_clickable(self.MODAL_VIEW_CART_BTTN))
        self.wait.until(EC.element_to_be_clickable(self.MODAL_CONTINUE_SHOPPING_BTTN))

    @allure.step("Click 'Continue Shopping' button")
    def click_continue_shopping_bttn(self):
        self.is_added_modal_visible()
        self.wait.until(EC.element_to_be_clickable(self.MODAL_CONTINUE_SHOPPING_BTTN)).click()    

    @allure.step("Click 'View Cart' button")
    def click_view_cart_bttn(self):
        self.is_added_modal_visible()
        self.wait.until(EC.element_to_be_clickable(self.MODAL_VIEW_CART_BTTN)).click()    

    @allure.step("Enter {search_data} in search input and click search button")
    def fill_product_search_and_click_search_bttn(self, search_data):
        self.fill_field(self.PRODUCTS_SEARCH_FIELD, search_data)
        self.wait.until(EC.visibility_of_element_located(self.SUBMIT_SEARCH_BTTN))       
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_SEARCH_BTTN)).click()  
        self.make_screenshot("Search result")

    @allure.step("Add product: {product_name} to cart")
    def add_product_to_cart_by_name(self, product_name):  
        # product_locator = ("xpath", "f'//div[@class='product-overlay']//p[text()='{product_name}']'")
        # product_locator = ("xpath", "f'//div[@class='single-products']//p[text()='{product_name}']'")
        product_name_locator = ("xpath", f"(//p[text()='{product_name}'])[1]")
        product_price_locator = ("xpath", f"//p[text()='{product_name}']/preceding-sibling::h2")
        add_to_cart_locator = ("xpath", f"(//p[text()='{product_name}']/following-sibling::a[@class='btn btn-default add-to-cart'])[2]")
        self.wait.until(EC.visibility_of_element_located(product_name_locator))       
        self.wait.until(EC.visibility_of_element_located(product_price_locator))  
        self.scroll_into_view(product_name_locator)
        self.hover_over_element(product_name_locator)     
        self.wait.until(EC.element_to_be_clickable(add_to_cart_locator)).click()  

    @allure.step("Click View product with id: {product_id}")
    def click_view_product_bttn_by_id(self, product_id):
        view_bttn_locator = ("xpath", f"//div[@class='choose']//a[@href='/product_details/{product_id}']")
        self.scroll_into_view(view_bttn_locator)
        self.wait.until(EC.element_to_be_clickable(view_bttn_locator)).click()

    @allure.step("Click '{product_brand}' product brand")
    def click_product_sidebar_category(self, product_brand):
        """
        Clicks on the specified product brand in the left sidebar category.
        Valid Brands:
        - Polo
        - H&M
        - Madame
        - Mast & Harbour
        - Babyhug
        - Allen Solly Junior
        - Kookie Kids
        - Biba
        """
        valid_brands = ["Polo", "H&M", "Madame", "Mast & Harbour", "Babyhug", "Allen Solly Junior", "Kookie Kids", "Biba"]

        if product_brand not in valid_brands:
            raise ValueError(f"Invalid product brand. Valid brands are: {', '.join(valid_brands)}")

        product_category = ('css selector', f'.left-sidebar .brands-name a[href="/brand_products/{product_brand}"]')
        self.scroll_into_view(product_category)
        self.wait.until(EC.element_to_be_clickable(product_category)).click()

    @allure.step("Verify '{product_brand}' product brand category is opened")
    def verify_brand_page_and_brand_products(self, product_brand):
        expected_text = f"Brand - {product_brand} Products"

        # Verify the presence of the brand text in the PRODUCTS_TEXT selector
        products_text = self.wait.until(EC.visibility_of_element_located(self.PRODUCTS_TEXT))
        products_text = products_text.text
        expected_text_uppercase = expected_text.upper()
        actual_text_uppercase = products_text.upper()
        # products_text = self.get_element_text(self.PRODUCTS_TEXT)
        assert expected_text_uppercase  in actual_text_uppercase, f"Expected '{expected_text}' in PRODUCTS_TEXT, but found '{products_text}'"
        self.make_screenshot("Category products")

    @allure.step("Click '{category} -> {subcategory}' category and subcategory")
    def click_category_and_subcategory(self, category, subcategory):
        category_locator = ('css selector', f'a[href="#{category}"]')
        subcategory_locator = ('xpath', f'//div[@id="{category}"]//a[contains(text(), "{subcategory}")]')

        self.wait.until(EC.element_to_be_clickable(category_locator)).click()
        self.wait.until(EC.element_to_be_clickable(subcategory_locator)).click()

    @allure.step("Verify '{category} -> {subcategory}' category and subcategory are opened")
    def verify_category_and_subcategory_products(self, category, subcategory):
        expected_text = f"{category} - {subcategory} Products"

        # Verify the presence of the category and subcategory text in the PRODUCTS_TEXT selector
        products_text = self.wait.until(EC.visibility_of_element_located(self.PRODUCTS_TEXT))
        products_text = products_text.text
        expected_text_uppercase = expected_text.upper()
        actual_text_uppercase = products_text.upper()
        assert expected_text_uppercase in actual_text_uppercase, f"Expected '{expected_text}' in PRODUCTS_TEXT, but found '{products_text}'"
        self.make_screenshot("Category and subcategory products")        

              