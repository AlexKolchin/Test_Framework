from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def login_url(self):
        return self.browser.current_url

    def login_button(self):
        return self.browser.find_element(*LoginPageLocators.LOG_IN)

    def forgot_password_link(self):
        return self.browser.find_element(*LoginPageLocators.FORGOT_PASSWORD)
