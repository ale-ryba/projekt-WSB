from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):

    def _verify_page(self):
        assert "Login" in self.driver.title

    def submit_email(self, email):
        el = self.driver.find_element(*LoginPageLocators.EMAIL_FIELD)
        el.click()
        el.send_keys(email)

    def submit_password(self, password):
        el = self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD)
        el.send_keys(password)

    def click_login_btn(self):
        self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        time.sleep(5)

        """
        WebDriverWait(self.driver, 15).until(EC.title_is('My Account'))
        nie można użyć explicitly wait, bo test_login_wrong_password będzie failował
        """

    def click_sign_up_btn(self):
        self.driver.execute_script("""document.getElementsByTagName("a")[61].click();""")
        WebDriverWait(self.driver, 15).until(EC.title_is('Register'))