import pytest
from pages.main_page import MainPage
from pages.constants import MAIN_PAGE, MAIN_PAGE_CN, LANGUAGES, HELLO_WORLD_H1


def test_guest_can_go_to_login_page(browser):
    """
    Test to verify guest can open login page
    :param browser: load webdriver
    :return:TRUE if link is opened
    """
    page = MainPage(browser, MAIN_PAGE)
    page.open()
    page.go_to_login_page()


def test_guest_should_see_login_link(browser):
    """
    Test to verify guest can see the login link
    :param browser: load webdriver
    :return: TRUE if login link contain "Log in"
    """
    page = MainPage(browser, MAIN_PAGE)
    page.open()
    assert "Log in" == page.login_link_selector().get_attribute("title"), "Login link is incorrect"


def test_premium_content_side_bar_is_available(browser):
    """
    Test to verify that Premium Content side bar is available
    :param browser: load webdriver
    :return: TRUE if url is correct, side bar menu buttons are available
    """
    page = MainPage(browser, MAIN_PAGE)
    page.open()
    page.premium_content_open()
    assert PREMIUM_CONTENT_PAGE == page.get_url(), "Premium content url is not correct"
    assert page.design_patterns_ebook_selector().is_displayed(), "Design Patterns eBook button is not displayed"
    assert page.refactoring_course_selector().is_displayed(), "Refactoring Course button is not displayed"


def test_refactoring_side_bar_is_available(browser):
    """
    Test to verify that Refactoring side bar is available
    :param browser: load webdriver
    :return: TRUE if url is correct, side bar menu buttons are available
    """
    page = MainPage(browser, MAIN_PAGE)
    page.open()
    page.refactoring_open()
    assert REFACTORING_PAGE == page.get_url(), "Refactoring url is not correct"
    assert page.what_is_refactoring_selector().is_displayed(), "What is refactoring button is not displayed"
    assert page.catalog_refactoring_selector().is_displayed(), "Catalog button is not displayed"
    assert page.code_smells_selector().is_displayed(), "Code smells button is not displayed"
    assert page.refactorings_selector().is_displayed(), "Refactorings button is not displayed"


def test_design_patterns_side_bar_is_available(browser):
    """
    Test to verify that Design Patterns side bar is available
    :param browser: load webdriver
    :return: TRUE if url is correct, side bar menu buttons are available
    """
    page = MainPage(browser, MAIN_PAGE)
    page.open()
    page.design_patterns_open()
    assert DESIGN_PATTERNS_PAGE == page.get_url(), "Design Patterns url is not correct"
    assert page.what_is_a_pattern_selector().is_displayed(), "What is a Pattern button is not displayed"
    assert page.catalog_design_patterns_selector().is_displayed(), "Catalog button is not displayed"
    assert page.creational_patterns_selector().is_displayed(), "Creational Patterns button is not displayed"
    assert page.structural_patterns_selector().is_displayed(), "Structural Patterns button is not displayed"
    assert page.behavioral_patterns_selector().is_displayed(), "Behavioral Patterns button is not displayed"
    assert page.code_examples_selector().is_displayed(), "Code Examples button is not displayed"


def test_language_chinese(browser):
    """
    Test to verify chinese page contains chinese Hello
    :param browser: load webdriver
    :return: TRUE if chinese hello equals the one in the list
    """
    page = MainPage(browser, MAIN_PAGE_CN)
    page.open()
    assert '你好， 世界！' == page.header_one_selector_cn().text, "Language error"


@pytest.mark.parametrize('language, hello', [(LANGUAGES[i], HELLO_WORLD_H1[i]) for i in range(len(LANGUAGES))])
def test_language_parameters(browser, language, hello):
    """
    Test to verify main page on different languages contains different hello`s
    :param browser: load browser
    :param language: LANGUAGES = ['', 'es', 'fr', 'pl', 'pt-br', 'ru', 'uk']
    :param hello: HELLO_WORLD_H1 = ['Hello, world!', '¡Hola, mundo!', 'Hello, world!', 'Hello, world!',
                  'Olá mundo!', 'Hello, world! Привет!', 'Hello, world! Привіт!']
    :return: TRUE if different hellos equals the one in the list
    """
    page = MainPage(browser, MAIN_PAGE + language)
    page.open()
    assert hello == page.header_one_selector().text, "Language error"
