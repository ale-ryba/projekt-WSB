import unittest
from selenium import webdriver
import time
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.account_page import AccountPage


class TravelLogin(unittest.TestCase):

    def setUp(self):

        # Warunki wstępne: Przeglądarka otwarta na stronie https://www.phptravels.net/

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.phptravels.net/")

    def tearDown(self):
        self.driver.quit()

    def test_login_correct_credents(self):

        # Scenariusz: Logowanie zarejestrowanego użytkownika poprawnymi danymi do logowania

        # 1. Kliknij "MY ACCOUNT"
        # ta metoda klika My Account i Login za jednym razem
        home_page = HomePage(self.driver)
        home_page.click_my_account_btn()

        '''
        # 2. Kliknij "Login"
        main_page.click_login()
        time.sleep(3)
        '''
        # 3. Wprowadź poprawny adres email
        login_page = LoginPage(self.driver)
        login_page.submit_email('user@phptravels.com')

        # 4. Wprowadź poprawne hasło
        login_page.submit_password('demouser')

        # 5. Kliknij 'LOGIN'
        login_page.click_login_btn()

        #Oczekiwany rezulat: Użytkownik jest poprawnie zalogowany. Następuje automatyczne przeniesienie na stronę https://www.phptravels.net/account/

        account_page = AccountPage(self.driver)

    def test_login_wrong_password(self):
        # Scenariusz: Logowanie zarejestrowanego użytkownika z użyciem niepoprawnego hasła

        # 1 & 2. Kliknij "MY ACCOUNT"
        main_page = HomePage(self.driver)
        main_page.click_my_account_btn()

        # 3. Wprowadź poprawny adres email
        login_page = LoginPage(self.driver)
        login_page.submit_email('user@phptravels.com')

        # 4. Wprowadź niepoprawne hasło
        login_page.submit_password('zlehaslo123')

        # 5. Kliknij 'LOGIN'
        login_page.click_login_btn()


        # Oczekiwany rezultat: Wyświetla się komunikat "Invalid Email or Password"

        error_notices = self.driver.find_elements_by_xpath('//div[@class="alert alert-danger"]')
        visible_error_notices = []
        for error in error_notices:
            if error.is_displayed():
                visible_error_notices.append(error)
        self.assertEqual(len(visible_error_notices), 1)
        self.assertEqual(visible_error_notices[0].text, "Invalid Email or Password")

if __name__ ==  '__main__':
    unittest.main(verbosity=2)
