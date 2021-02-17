from pages.main_page import MainPage
from pages.consctants import *


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, MAIN_PAGE)
    page.open()
    page.go_to_login_page()


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, MAIN_PAGE)
    page.open()
    assert "Log in" == page.login_link_selector().get_attribute("title"), "Login link is incorrect"


