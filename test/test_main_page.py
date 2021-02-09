from pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    link = "https://refactoring.guru/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_should_see_login_link(browser):
    link = "https://refactoring.guru/"
    page = MainPage(browser, link)
    page.open()
    assert "Log in" == page.login_link_selector().get_attribute("title")
