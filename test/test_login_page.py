from pages.login_page import LoginPage


def test_login_page_is_present(browser):
    link = "https://refactoring.guru/login"
    page = LoginPage(browser, link)
    page.open()
    assert "login" in page.login_url(), "Login url is not correct"
    assert page.login_button().is_enabled(), "Login button is not enabled"
    assert "forgot" == page.forgot_password_link().get_attribute("class"), "Forgot Password link is not correct"
