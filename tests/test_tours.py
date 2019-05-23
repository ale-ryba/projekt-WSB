import unittest
from selenium import webdriver
from pages.home_page import HomePage
from pages.signup_page import SignupPage
from pages.login_page import LoginPage
from pages.tours_page import ToursPage
import time

class TravelTours(unittest.TestCase):
# Scenariusz: Wyszukanie wycieczki bez podania lokalizacji

    def setUp(self):

        # Warunki wstępne: Przeglądarka otwarta na stronie https://www.phptravels.net/

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.phptravels.net/")

    def tearDown(self):
        self.driver.quit()

    def test_tour(self):

        tours_page = HomePage(self.driver)

        # 1. Kliknij 'TOURS'
        tours_page.click_tours()

        # 2.Wpisz date
        #tours_page.enter_date('18/06/2019')
        tours_page.select_date()

        # 3. Wpisz liczbe osob
        tours_page.select_adults_number()

        # 4. Wybierz rodzaj wycieczki
        tours_page.select_tour_type()

        # 5. Kliknij 'SEARCH'
        tours_page.click_search()
        time.sleep(5)

        # Oczekiwany rezultat: Uzytkownik jest przenoszony na stronę z wynikami. Wyświetla się komunikat "No Results Found"
        tours_page = ToursPage(self.driver)
        time.sleep(3)

        assert "No Results Found" in self.driver.page_source