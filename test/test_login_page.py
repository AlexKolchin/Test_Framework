from pages.login_page import LoginPage
from pages.consctants import *


def test_login_page_is_present(browser):
    page = LoginPage(browser, LOGIN_PAGE)
    page.open()
    assert "login" in page.login_url(), "Login url is not correct"
    assert page.login_button().is_enabled(), "Login button is not enabled"
    assert "forgot" == page.forgot_password_link().get_attribute("class"), "Forgot Password link is not correct"

