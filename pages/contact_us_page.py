import allure
import os
from .base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class ContactUsPage(BasePage):

    PAGE_URL= Links.CONTACT_US_PAGE

    NAME_FIELD = ('css selector', '[data-qa="name"]')
    EMAIL_FIELD = ('css selector', '[data-qa="email"]')
    SUBJECT_FIELD = ('css selector', '[data-qa="subject"]')
    MESSAGE_FIELD = ('css selector', '[data-qa="message"]')
    SUBMIT_BTTN = ('css selector', '[data-qa="submit-button"]')
    FILE_INPUT = ('css selector', '[name="upload_file"]')
    CONTACT_US_FORM = ('css selector', '#contact-us-form.contact-form')
    SUCCESS_MESSAGE = ('css selector', '.status.alert-success') # Success! Your details have been submitted successfully.
    HOME_SUCCESS_BTTN = ('css selector', '.btn-success')

    @allure.step("'Contact Us' send form visible")
    def is_contact_us_form_visible(self):
        self.wait.until(EC.visibility_of_element_located(self.NAME_FIELD))
        self.wait.until(EC.visibility_of_element_located(self.EMAIL_FIELD))
        self.wait.until(EC.visibility_of_element_located(self.SUBJECT_FIELD))
        self.wait.until(EC.visibility_of_element_located(self.MESSAGE_FIELD))
        self.wait.until(EC.visibility_of_element_located(self.FILE_INPUT))
        self.wait.until(EC.visibility_of_element_located(self.SUBMIT_BTTN))
        self.make_screenshot("Contact Us form")

    @allure.step("Click Home button")
    def click_home_bttn(self):
        self.wait.until(EC.visibility_of_element_located(self.HOME_SUCCESS_BTTN))
        self.wait.until(EC.visibility_of_element_located(self.SUCCESS_MESSAGE))
        self.wait.until(EC.element_to_be_clickable(self.HOME_SUCCESS_BTTN)).click()

    @allure.step("Upload file to Contact Us form")
    def upload_file_to_contact_us(self):
        file_input = self.wait.until(EC.visibility_of_element_located(self.FILE_INPUT))
        absolute_file_path = os.path.join(os.getcwd(), 'pages', 'resources', 'contactusfile.png')
        file_input.send_keys(absolute_file_path)
        self.make_screenshot('File uploaded')         
        # absolute_file_path = os.path.abspath(file_path)
        # file_input.send_keys(absolute_file_path)     

    @allure.step("Fill Contact Us form with random data")
    def fill_contact_us_form(self):
        self.fill_field(self.NAME_FIELD, self.fake.name())
        self.fill_field(self.EMAIL_FIELD, self.fake.email())
        self.fill_field(self.SUBJECT_FIELD, self.fake.sentence())
        self.fill_field(self.MESSAGE_FIELD, self.fake.paragraph()) 
        self.make_screenshot('Filled form')     

    @allure.step("Click submit button")
    def click_continue_button(self):
        self.wait.until(EC.visibility_of_element_located(self.SUBMIT_BTTN))       
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BTTN)).click()           

    @allure.step("Accept confirmation alert")
    def accept_alert(self):
        alert = self.wait.until(EC.alert_is_present())  
        self.browser.switch_to.alert  
        alert.accept()         