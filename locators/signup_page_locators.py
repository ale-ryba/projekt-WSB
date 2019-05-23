from selenium.webdriver.common.by import By

class SignupPageLocators():

    FIRST_NAME_FIELD = (By.NAME, 'firstname')
    #//input[@name="firstname"]

    LAST_NAME_FIELD = (By.NAME, 'lastname')

    MOBILE_NUMBER_FIELD = (By.XPATH, '//input[@placeholder="Mobile Number"]')

    EMAIL_FIELD = (By.XPATH, '//input[@placeholder="Email"]')

    PASSWORD_FIELD = (By.XPATH, '//input[@placeholder="Password"]')

    CONFIRM_PASSWORD_FIELD = (By.XPATH, '//input[@name="confirmpassword"]')

    SIGNUP_BUTTON = (By.XPATH, '//button[text()=" Sign Up"]')
