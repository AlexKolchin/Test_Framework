from pages.design_patterns import DesignPatternsPage
from pages.constants import *


def test_number_of_design_patterns(browser):
    """
    Test to verify that number of patterns on main page equals the real number of patterns
    :param browser: load webdriver
    :return:
    """
    page = DesignPatternsPage(browser, DESIGN_PATTERNS_PAGE)
    page.open()
    number_of_patterns = page.get_number_of_patterns()
    page.open_catalog()
    assert number_of_patterns == page.get_number_of_cards(), 'Error'

