from selenium.webdriver.common.by import By

class LoginPageLocators():

    EMAIL_FIELD = (By.XPATH, '//input[@placeholder="Email"]')

    PASSWORD_FIELD = (By.NAME, 'password')

    LOGIN_BUTTON = (By.XPATH, '//button[text()="Login"]')

    SIGN_UP_BTN = (By.XPATH, '//a[@href="https://www.phptravels.net/register"]')