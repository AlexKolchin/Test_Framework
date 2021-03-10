from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def login_button(self):
        return self.browser.find_element(*LoginPageLocators.LOG_IN)

    def forgot_password_link(self):
        return self.browser.find_element(*LoginPageLocators.FORGOT_PASSWORD)

    def click_login(self):
        self.browser.find_element(*LoginPageLocators.LOG_IN).click()

    def alert_whoops(self):
        return self.browser.find_element(*LoginPageLocators.ALERT_WHOOPS)

    def email_required_text(self):
        return self.browser.find_element(*LoginPageLocators.EMAIL_IS_REQUIRED).text

    def password_required_text(self):
        return self.browser.find_element(*LoginPageLocators.PASSWORD_IS_REQUIRED).text

    def wrong_credentials_text(self):
        return self.browser.find_element(*LoginPageLocators.WRONG_CREDENTIALS).text

    def enter_email(self, email="test@gmail.com"):
        self.browser.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(email)

    def enter_password(self, password="1234"):
        self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(password)

    def alert_message(self):
        return self.browser.switch_to.alert().getText()

