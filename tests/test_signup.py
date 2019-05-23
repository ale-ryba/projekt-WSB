import unittest
from selenium import webdriver
import time
from pages.home_page import HomePage
from pages.signup_page import SignupPage
from pages.login_page import LoginPage
from locators.signup_page_locators import SignupPageLocators
from selenium.webdriver.common.keys import Keys
from ddt import ddt, data, unpack
import csv

@ddt
class TravelSignUp(unittest.TestCase):

    # Scenariusz: Rejestracja nowego użytkownika z użyciem niepoprawnego adresu email

    def setUp(self):

        # Warunki wstępne: Przeglądarka otwarta na stronie https://www.phptravels.net/

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.phptravels.net/")

    def tearDown(self):
        self.driver.quit()

    def get_data(file_name):
        rows = []
        data_file = open(file_name, 'rt')
        reader = csv.reader(data_file)
        next(reader, None)
        for row in reader:
            rows.append(row)
        return rows


    @data(*get_data("wrong_email.csv"))
    @unpack
    def test_signup_invalid_email(self, first_name, last_name, mobile_num, wrong_email, password, password_confirmed):

        # 1 & 2 Kliknij "MY ACCOUNT" i "Login"

        home_page = HomePage(self.driver)
        home_page.click_my_account_btn()

        # 3. Kliknij przycisk ‘SIGN UP’
        login_page = LoginPage(self.driver)
        login_page.click_sign_up_btn()

        signup_page = SignupPage(self.driver)

        # 4. Wprowadź imię
        signup_page.submit_first_name(first_name)

        # 5. Wprowadź nazwisko
        signup_page.submit_last_name(last_name)

        # 6. Wprowadź numer komórkowy
        signup_page.submit_mobile_number(mobile_num)

        # 7. Wprowadź niepoprawny adres email
        signup_page.submit_email(wrong_email)

        # 8. Wprowadz hasło
        signup_page.submit_password(password)

        # 9. Wprowadź powtórnie hasło
        signup_page.confirm_password(password_confirmed)

        # 10. Potwierdz rejestrację klikając 'SIGN UP'
        signup_page.confirm_signup()

        # Oczekiwany rezultat: Konto nie zostaje utworzone. Wyświetlany jest komunikat: “The Email field must contain a valid email address. ”

        error_notices = self.driver.find_elements_by_xpath('//div[@class="alert alert-danger"]')
        visible_error_notices = []
        for error in error_notices:
            if error.is_displayed():
                visible_error_notices.append(error)
        self.assertEqual(len(visible_error_notices), 1)
        self.assertEqual(visible_error_notices[0].text, "The Email field must contain a valid email address.")


if __name__ ==  '__main__':
    unittest.main(verbosity=2)

