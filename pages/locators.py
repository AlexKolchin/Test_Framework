from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.XPATH, "/html/body/div/nav/div/ul/li[3]/a")


class LoginPageLocators():
    LOG_IN = (By.XPATH, "/html/body/div/div/div/div/div/div[1]/div[1]/form/div[2]/div[1]")
    FORGOT_PASSWORD = (By.XPATH, "/html/body/div/div/div/div/div/div[1]/div[1]/form/div[2]/div[2]")
