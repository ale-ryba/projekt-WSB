from selenium.webdriver.common.by import By


class HomePageLocators():
    MY_ACCOUNT_BTN = (By.XPATH, '//a[@href="javascript:void(0);"]') #xpath nie działa

    LOGIN_BTN = (By.XPATH, '//a[@href="https://www.phptravels.net/login"]')

    FLIGHTS_BTN = (By.XPATH, '//span[text()="Flights   "]')

    TOURS_BTN = (By.XPATH, '//span[text()="Tours     "]')

    #CITY_BTN = (By.CLASS_NAME, 'select2-drop select2-display-none select2-with-searchbox select2-drop-active')

    DATE_BTN = (By.NAME, 'date')

    DATE_ARROW = (By.XPATH, '/html/body/div[12]/div[1]/table/thead/tr[1]/th[3]')

    JUNE_12 = (By.XPATH, '/html/body/div[12]/div[1]/table/tbody/tr[3]/td[4]')

    ADULTS = (By.XPATH, '//select[@name="adults"]')

    ADULTS_NUM = (By.XPATH, '//option[@value="3"]')

    TOUR_TYPE = (By.ID, 'tourtype')

    TYPE_FAMILY = (By.XPATH, '//option[@value="196"]')

    SEARCH_BTN = (By.XPATH, '//*[@id="tours"]/form/div[5]/button')

    #CITY_BTN = (By.XPATH, '//div[@class="select2-drop select2-display-none select2-with-searchbox select2-drop-active"]')
