from pages.base_page import BasePage
from locators.account_page_locators import AccoutPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


class AccountPage(BasePage):

    def _verify_page(self):
        assert "My Account" in self.driver.title

    def click_my_profile(self):
        self.driver.execute_script("""document.getElementsByTagName("a")[60].click();""")
        #//a[@href="#profile"]
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, 'password')))

    def enter_new_password(self, password):
        el = self.driver.find_element(*AccoutPageLocators.NEW_PASSWORD)
        el.click()
        el.send_keys(password)

    def confirm_new_password(self, confirmed_password):
        el = self.driver.find_element(*AccoutPageLocators.CONFIRM_NEW_PASSWORD)
        el.click()
        el.send_keys(confirmed_password)

    def click_submit(self):

        cookie_btn = self.driver.find_element(*AccoutPageLocators.COOKIE_BUTTON)
        cookie_btn.click()
        #time.sleep(3)
        el = self.driver.find_element(*AccoutPageLocators.SUBMIT_BUTTON)
        actions = ActionChains(self.driver)
        actions.move_to_element(el)
        actions.perform()
        el.click()
        #self.driver.implicitly_wait(3)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="alert alert-success"]')))