from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.XPATH, "/html/body/div/nav/div/ul/li[3]/a")
    HELLO_WORLD = (By.CSS_SELECTOR, ".page.text > h1")
    HELLO_WORLD_CN = (By.CSS_SELECTOR, ".page.text > h1 > span")
    PREMIUM_CONTENT = (By.CSS_SELECTOR, ".fa.fa-fw.fa-star")
    DESIGN_PATTERN_EBOOK = (By.CSS_SELECTOR, ".fa.fa-fw.fa-book")
    REFACTORING_COURSE = (By.CSS_SELECTOR, ".fa.fa-fw.fa-graduation-cap")
    REFACTORING = (By.CSS_SELECTOR, ".fa.fa-fw.fa-scissors")
    WHAT_IS_REFACTORING = (By.CSS_SELECTOR, ".animated.trail.active > ul > li:nth-child(1) > a")
    CATALOG_REFACTORING = (By.CSS_SELECTOR, ".animated.trail.active > ul > li:nth-child(2) > a")
    CODE_SMELLS = (By.CSS_SELECTOR, ".animated.trail.active > ul > li:nth-child(3) > a")
    REFACTORINGS = (By.CSS_SELECTOR, ".animated.trail.active > ul > li:nth-child(4) > a")
    DESIGN_PATTERNS = (By.CSS_SELECTOR, ".fa.fa-fw.fa-puzzle-piece")
    WHAT_IS_A_PATTERN = (By.CSS_SELECTOR, ".animated.trail.active > ul > li:nth-child(1) > a")
    CATALOG_DESIGN_PATTERNS = (By.CSS_SELECTOR, ".animated.trail.active > ul > li:nth-child(2) > a")
    CREATIONAL_PATTERNS = (By.CSS_SELECTOR, ".animated.trail.active > ul > li:nth-child(3) > a")
    STRUCTURAL_PATTERNS = (By.CSS_SELECTOR, ".animated.trail.active > ul > li:nth-child(4) > a")
    BEHAVIORAL_PATTERNS = (By.CSS_SELECTOR, ".animated.trail.active > ul > li:nth-child(5) > a")
    CODE_EXAMPLES = (By.CSS_SELECTOR, ".animated.trail.active > ul > li:nth-child(6) > a")


class LoginPageLocators():
    LOG_IN = (By.XPATH, "/html/body/div/div/div/div/div/div[1]/div[1]/form/div[2]/div[1]")
    FORGOT_PASSWORD = (By.XPATH, "/html/body/div/div/div/div/div/div[1]/div[1]/form/div[2]/div[2]/a")


class ContactUsPopupLocators():
    CONTACT_US_POPUP = (By.XPATH, '//*[@id="module_add_topic"]')
    CONTACT_US_FOOTER = (By.CSS_SELECTOR, ".footer-list.footer-list-horizontal > li:nth-child(6) > a")


class DesignPatternsLocators():
    LIST_OF_DESIGN_PATTERNS = (By.CSS_SELECTOR, ".dp4-p.dp-abs.dp-c.dp-p > span:nth-child(1)")
    CATALOG_INSIDE_OPEN = (By.CSS_SELECTOR, ".dp4-b.dp-abs.dp-c.dp-b > span > a")
    PATTERN_CARDS = (By.CSS_SELECTOR, ".pattern-card")
