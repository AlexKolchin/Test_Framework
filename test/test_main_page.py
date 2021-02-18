from pages.main_page import MainPage
from pages.consctants import *


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, MAIN_PAGE)
    page.open()
    page.go_to_login_page()


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, MAIN_PAGE)
    page.open()


def test_languages(browser):
    i = 0
    for lang in LANGUAGES:
        if lang == 'cn':
            page = MainPage(browser, MAIN_PAGE_CN)
            page.open()
            assert HELLO_WORLD_H1[i] == page.header_one_selector_cn().text, "Error"
            i += 1
        else:
            page = MainPage(browser, MAIN_PAGE + lang)
            page.open()
            assert HELLO_WORLD_H1[i] == page.header_one_selector().text, "Error"
            i += 1


def test_premium_content_side_bar_is_available(browser):
    page = MainPage(browser, MAIN_PAGE)
    page.open()
    page.premium_content_open()
    assert PREMIUM_CONTENT_URL == page.premium_url(), "Premium content url is not correct"
    assert page.design_patterns_ebook_selector().is_displayed(), "Design Patterns eBook button is not displayed"
    assert page.refactoring_course_selector().is_displayed(), "Refactoring Course button is not displayed"


def test_refactoring_side_bar_is_available(browser):
    page = MainPage(browser, MAIN_PAGE)
    page.open()
    page.refactoring_open()
    assert REFACTORING_URL == page.refactoring_url(), "Refactoring url is not correct"
    assert page.what_is_refactoring_selector().is_displayed(), "What is refactoring button is not displayed"
    assert page.catalog_refactoring_selector().is_displayed(), "Catalog button is not displayed"
    assert page.code_smells_selector().is_displayed(), "Code smells button is not displayed"
    assert page.refactorings_selector().is_displayed(), "Refactorings button is not displayed"


def test_design_patterns_side_bar_is_available(browser):
    page = MainPage(browser, MAIN_PAGE)
    page.open()
    page.design_patterns_open()
    assert DESIGN_PATTERNS_URL == page.design_patterns_url(), "Design Patterns url is not correct"
    assert page.what_is_a_pattern_selector().is_displayed(), "What is a Pattern button is not displayed"
    assert page.catalog_design_patterns_selector().is_displayed(), "Catalog button is not displayed"
    assert page.creational_patterns_selector().is_displayed(), "Creational Patterns button is not displayed"
    assert page.structural_patterns_selector().is_displayed(), "Structural Patterns button is not displayed"
    assert page.behavioral_patterns_selector().is_displayed(), "Behavioral Patterns button is not displayed"
    assert page.code_examples_selector().is_displayed(), "Code Examples button is not displayed"
