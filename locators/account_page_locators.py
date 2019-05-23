from selenium.webdriver.common.by import By

class AccoutPageLocators():

    MY_PROFILE = (By.PARTIAL_LINK_TEXT, 'My Profile')

    NEW_PASSWORD = (By.NAME, "password")

    CONFIRM_NEW_PASSWORD = (By.NAME, 'confirmpassword')

    SUBMIT_BUTTON = (By.XPATH, '//button[@class="btn btn-action btn-block updateprofile"]')

    COOKIE_BUTTON = (By.ID, 'cookyGotItBtn')

    '''
    aria - label = "dismiss cookie message"
    id="cookyGotItBtn"
    Got it!
    '''

