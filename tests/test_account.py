import unittest
from selenium import webdriver
import time
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.account_page import AccountPage

class TravelAccount(unittest.TestCase):

    def setUp(self):

        # Warunki wstępne: Przeglądarka otwarta na stronie https://www.phptravels.net/account

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.phptravels.net")

    def tearDown(self):
        self.driver.quit()

    def test_password_change(self):

        # 1. Logowanie
        home_page = HomePage(self.driver)
        home_page.click_my_account_btn()

        # 2. Wprowadź poprawny adres email
        login_page = LoginPage(self.driver)
        login_page.submit_email('user@phptravels.com')

        # 3. Wprowadź poprawne hasło
        login_page.submit_password('demouser')

        # 4. Kliknij 'LOGIN'
        login_page.click_login_btn()

        account_page = AccountPage(self.driver)

        # 5. Kliknij 'My Profile'
        account_page.click_my_profile()

        # 6. Wprowadz nowe haslo
        account_page.enter_new_password('demouser123')

        # 7. Wprowadz powtornie nowe haslo
        account_page.confirm_new_password('demouser123')

        # 8. Kliknij SUBMIT
        account_page.click_submit()

        # Oczekiwany rezultat: Wyświetla się komunikat "Profile Updated Successfully"
        success_notices = self.driver.find_elements_by_xpath('//div[@class="alert alert-success"]')
        visible_success_notices = []
        for success in success_notices:
            if success.is_displayed():
                visible_success_notices.append(success)
        self.assertEqual(len(visible_success_notices), 1)
        self.assertEqual(visible_success_notices[0].text, "Profile Updated Successfully.")


