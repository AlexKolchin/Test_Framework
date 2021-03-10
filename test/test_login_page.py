from pages.login_page import LoginPage
from pages.constants import LOGIN_PAGE
import time


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


def test_cant_login_with_unregistered_email(browser):
    """
    Test to varify unregistered user cant login
    :param browser: load webdriver
    :return:
    """
    page = LoginPage(browser, LOGIN_PAGE)
    page.open()
    page.enter_email()
    page.enter_password()
    page.click_login()
    assert page.alert_whoops().is_displayed(), "Alert is no displayed"
    assert 'These credentials do not match our records.' == page.wrong_credentials_text(), "Wrong credentials message is incorrect"


def test_wrong_email_popup(browser):
    """
    Test to verify that help pop-up apperas when incorrect email format is entered
    :param browser: load webdriver
    :return:
    """
    page = LoginPage(browser, LOGIN_PAGE)
    page.open()
    page.enter_email("dsadsada")
    page.click_login()
    print(page.alert_message())
    time.sleep(5)


def test_empty_login(browser):
    """
    Test to verify that user cant login with empty data
    :param browser: load browser
    :return:
    """
    page = LoginPage(browser, LOGIN_PAGE)
    page.open()
    page.click_login()
    assert page.alert_whoops().is_displayed(), "Alert is no displayed"
    assert 'The “Email” field is required.' == page.email_required_text(), "Email required message is incorrect"
    assert 'The “Password” field is required.' == page.password_required_text(), "Password required message is incorrect"
