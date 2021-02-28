from pages.login_page import LoginPage
from pages.constants import *


def test_login_page_is_present(browser):
    """
    Test to verify login page is working
    :param browser: load webdriver
    :return: TRUE if url contains "login", login button is enabled, forgot password link is correct
    """
    page = LoginPage(browser, LOGIN_PAGE)
    page.open()
    assert "login" in page.get_url(), "Login url is not correct"
    assert page.login_button().is_enabled(), "Login button is not enabled"
    assert "forgot" == page.forgot_password_link().get_attribute("class"), "Forgot Password link is not correct"

