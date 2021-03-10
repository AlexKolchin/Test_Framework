from pages.contact_us_popup import ContactUsPopup
from pages.constants import MAIN_PAGE


def test_contact_us_popup_is_available(browser):
    """
    Test to verify guest can open "Contact Us" link
    :param browser: load webdriver
    :return: TRUE if popup is opened
    """
    page = ContactUsPopup(browser, MAIN_PAGE)
    page.open()
    page.contact_us_footer_open()
    page.wait(5)
    page.switch_to_contact_us_popup()
    assert page.contact_us_popup_selector().is_displayed(), "Contact us pop up is not displayed"