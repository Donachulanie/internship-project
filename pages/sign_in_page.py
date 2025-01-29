from time import sleep

from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class SignInPage(BasePage):
    EMAIL_FIELD_ID = (By.CSS_SELECTOR, "input[id='email-2']")
    PASSWORD_FIELD_ID = (By.CSS_SELECTOR, "input[id='field']")
    CONTINUE_BTN_IN_SIGN_IN_PAGE = (By.CSS_SELECTOR, "a[class='login-button w-button']")

    def input_valid_email_and_password(self, email, password):
        sleep(4)
        self.input_text(email, *self.EMAIL_FIELD_ID)
        self.input_text(password, *self.PASSWORD_FIELD_ID)


    def click_continue_button(self):
        sleep(2)
        self.click(*self.CONTINUE_BTN_IN_SIGN_IN_PAGE)


    def verify_user_logged_in(self):
        sleep(2)
        self.wait_for_element_invisible(*self.CONTINUE_BTN_IN_SIGN_IN_PAGE)




