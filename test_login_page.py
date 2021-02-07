from .pages.login_page import LoginPage


def test_login_page_is_present(browser):
    link = "https://refactoring.guru/login"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
