from pages.base_page import BasePage
from pages.locators import ContactUsPopupLocators


class ContactUsPopup(BasePage):
    def switch_to_contact_us_popup(self):
        self.browser.switch_to.frame(self.browser.find_element_by_tag_name('iframe'))

    def contact_us_popup_selector(self):
        return self.browser.find_element(*ContactUsPopupLocators.CONTACT_US_POPUP)

    def contact_us_footer_open(self):
        self.browser.find_element(*ContactUsPopupLocators.CONTACT_US_FOOTER).click()