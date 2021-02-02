def test_guest_can_go_to_login_page(browser):
    link = "https://refactoring.guru/"
    browser.get(link)
    login_link = browser.find_element_by_xpath("/html/body/div/nav/div/ul/li[3]/a")
    login_link.click()