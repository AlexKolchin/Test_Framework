from pages.base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def login_link_selector(self):
        return self.browser.find_element(*MainPageLocators.LOGIN_LINK)

    def header_one_selector(self):
        return self.browser.find_element(*MainPageLocators.HELLO_WORLD)

    def header_one_selector_cn(self):
        return self.browser.find_element(*MainPageLocators.HELLO_WORLD_CN)
