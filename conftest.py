import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart driver for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit driver..")
    browser.quit()
