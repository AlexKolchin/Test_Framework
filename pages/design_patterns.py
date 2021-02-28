from pages.base_page import BasePage
from pages.locators import DesignPatternsLocators
import re


class DesignPatternsPage(BasePage):
    def get_number_of_patterns(self):
        text = self.browser.find_element(*DesignPatternsLocators.LIST_OF_DESIGN_PATTERNS).text
        return int(re.search(r'\d+', text).group())

    def open_catalog(self):
        self.browser.find_element(*DesignPatternsLocators.CATALOG_INSIDE_OPEN).click()

    def get_number_of_cards(self):
        cards_list = self.browser.find_elements(*DesignPatternsLocators.PATTERN_CARDS)
        return len(cards_list)

