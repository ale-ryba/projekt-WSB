from pages.base_page import BasePage
import time
from locators.signup_page_locators import SignupPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class SignupPage(BasePage):

    def _verify_page(self):
        assert "Register" in self.driver.title

    def submit_first_name(self, first_name):
        el = self.driver.find_element(*SignupPageLocators.FIRST_NAME_FIELD)
        el.click()
        el.send_keys(first_name)

    def submit_last_name(self, last_name):
        el = self.driver.find_element(*SignupPageLocators.LAST_NAME_FIELD)
        el.click()
        el.send_keys(last_name)

    def submit_mobile_number(self, mobile_number):
        el = self.driver.find_element(*SignupPageLocators.MOBILE_NUMBER_FIELD)
        el.click()
        el.send_keys(mobile_number)

    def submit_email(self, email):
        el = self.driver.find_element(*SignupPageLocators.EMAIL_FIELD)
        el.click()
        el.send_keys(email)

    def submit_password(self, password):
        el = self.driver.find_element(*SignupPageLocators.PASSWORD_FIELD)
        el.click
        el.send_keys(password)

    def confirm_password(self, password_confirmed):
        el = self.driver.find_element(*SignupPageLocators.CONFIRM_PASSWORD_FIELD)
        el.send_keys(password_confirmed)

    def confirm_signup(self):
        self.driver.find_element(*SignupPageLocators.SIGNUP_BUTTON).click()
        #WebDriverWait(self.driver, 15).until(EC.visibility_of('//div[@class="alert alert-danger"]'))
        self.driver.implicitly_wait(5)

