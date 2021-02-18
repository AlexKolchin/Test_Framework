from pages.main_page import MainPage
from pages.consctants import *
import time


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, MAIN_PAGE)
    page.open()
    page.go_to_login_page()


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, MAIN_PAGE)
    page.open()
    assert "Log in" == page.login_link_selector().get_attribute("title"), "Login link is incorrect"


def test_languages(browser):
    i = 0
    url_list = ['', 'es', 'fr', 'pl', 'pt-br', 'cn', 'ru', 'uk']
    hello_list = ['Hello, world!', '¡Hola, mundo!', 'Hello, world!', 'Hello, world!',
                  'Olá mundo!', '你好， 世界！', 'Hello, world! Привет!', 'Hello, world! Привіт!']
    for lang in url_list:
        if lang == 'cn':
            page = MainPage(browser, MAIN_PAGE_CN)
            page.open()
            assert hello_list[i] == page.header_one_selector_cn().text, "Error"
            i += 1
        else:
            page = MainPage(browser, MAIN_PAGE+lang)
            page.open()
            assert hello_list[i] == page.header_one_selector().text, "Error"
            i += 1

