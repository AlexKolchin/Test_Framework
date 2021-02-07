from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_forgot_password()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "login is absent in current url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOG_IN), "Log in link is not present"

    def should_be_forgot_password(self):
        assert self.is_element_present(*LoginPageLocators.FORGOT_PASSWORD), "Forgot password link is not present"
