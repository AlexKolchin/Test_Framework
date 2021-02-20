from pages.base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def login_link_selector(self):
        return self.browser.find_element(*MainPageLocators.LOGIN_LINK)

    def header_one_selector(self):
        return self.browser.find_element(*MainPageLocators.HELLO_WORLD)

    def header_one_selector_cn(self):
        return self.browser.find_element(*MainPageLocators.HELLO_WORLD_CN)

    def premium_content_open(self):
        premium_content_link = self.browser.find_element(*MainPageLocators.PREMIUM_CONTENT)
        premium_content_link.click()

    def premium_url(self):
        return self.browser.current_url

    def design_patterns_ebook_selector(self):
        return self.browser.find_element(*MainPageLocators.DESIGN_PATTERN_EBOOK)

    def refactoring_course_selector(self):
        return self.browser.find_element(*MainPageLocators.REFACTORING_COURSE)

    def refactoring_open(self):
        self.browser.find_element(*MainPageLocators.REFACTORING).click()

    def refactoring_url(self):
        return self.browser.current_url

    def what_is_refactoring_selector(self):
        return self.browser.find_element(*MainPageLocators.WHAT_IS_REFACTORING)

    def catalog_refactoring_selector(self):
        return self.browser.find_element(*MainPageLocators.CATALOG_REFACTORING)

    def code_smells_selector(self):
        return self.browser.find_element(*MainPageLocators.CODE_SMELLS)

    def refactorings_selector(self):
        return self.browser.find_element(*MainPageLocators.REFACTORINGS)

    def design_patterns_open(self):
        self.browser.find_element(*MainPageLocators.DESIGN_PATTERNS).click()

    def design_patterns_url(self):
        return self.browser.current_url

    def what_is_a_pattern_selector(self):
        return self.browser.find_element(*MainPageLocators.WHAT_IS_A_PATTERN)

    def catalog_design_patterns_selector(self):
        return self.browser.find_element(*MainPageLocators.CATALOG_DESIGN_PATTERNS)

    def creational_patterns_selector(self):
        return self.browser.find_element(*MainPageLocators.CREATIONAL_PATTERNS)

    def structural_patterns_selector(self):
        return self.browser.find_element(*MainPageLocators.STRUCTURAL_PATTERNS)

    def behavioral_patterns_selector(self):
        return self.browser.find_element(*MainPageLocators.BEHAVIORAL_PATTERNS)

    def code_examples_selector(self):
        return self.browser.find_element(*MainPageLocators.CODE_EXAMPLES)

