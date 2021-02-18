from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.XPATH, "/html/body/div/nav/div/ul/li[3]/a")
    HELLO_WORLD = (By.CSS_SELECTOR, ".page.text > h1")
    HELLO_WORLD_CN = (By.CSS_SELECTOR, ".page.text > h1 > span")


class LoginPageLocators():
    LOG_IN = (By.XPATH, "/html/body/div/div/div/div/div/div[1]/div[1]/form/div[2]/div[1]")
    FORGOT_PASSWORD = (By.XPATH, "/html/body/div/div/div/div/div/div[1]/div[1]/form/div[2]/div[2]/a")
