from .pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    link = "https://refactoring.guru/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_should_see_login_link(browser):
    link = "https://refactoring.guru/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_link()
