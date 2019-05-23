from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class HomePage(BasePage):

    def _verify_page(self):
        assert "PHPTRAVELS | Travel Technology Partner" in self.driver.title
        '''
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(HomePageLocators.MY_ACCOUNT_BTN)
        )
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(HomePageLocators.MY_ACCOUNT_BTN)
        )
        '''

    def click_my_account_btn(self):
        #el = self.driver.find_element(*HomePageLocators.MY_ACCOUNT_BTN)
        #el.click()
        self.driver.execute_script("""document.getElementsByTagName("a")[3].click();""")
        time.sleep(5)

    def click_login(self):
        el = self.driver.find_element(*HomePageLocators.LOGIN_BTN)
        el.click()

    def click_flights(self):
        self.driver.find_element(*HomePageLocators.FLIGHTS_BTN).click()

    def click_tours(self):
        self.driver.find_element(*HomePageLocators.TOURS_BTN).click()
        #WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, '//input[@class="hotelsearch locationlisttours"]')))
        self.driver.implicitly_wait(5)

    def enter_date(self, date):
        self.driver.find_element(*HomePageLocators.DATE_BTN).send_keys(date)

    def select_date(self):
        self.driver.find_element(*HomePageLocators.DATE_BTN).click()
        self.driver.find_element(*HomePageLocators.DATE_ARROW).click()
        self.driver.find_element(*HomePageLocators.JUNE_12).click()


    def select_adults_number(self):
        self.driver.find_element(*HomePageLocators.ADULTS).click()
        self.driver.find_element(*HomePageLocators.ADULTS_NUM).click()

    def select_tour_type(self):
        self.driver.find_element(*HomePageLocators.TOUR_TYPE).click()
        self.driver.find_element(*HomePageLocators.TYPE_FAMILY).click()


    def click_search(self):
        self.driver.find_element(*HomePageLocators.SEARCH_BTN).click()



