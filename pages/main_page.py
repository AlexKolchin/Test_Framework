from .base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.XPATH, "/html/body/div/nav/div/ul/li[3]/a")
        login_link.click()

    def should_be_login_link(self):
        assert self.browser.find_element(By.XPATH, "/html/body/div/nav/div/ul/li[3]/a"), "Login link is not present"