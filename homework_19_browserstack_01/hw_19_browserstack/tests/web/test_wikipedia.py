import allure
from selene import have, browser


def test_search():
    browser.open('/')

    with allure.step('Type search'):
        browser.element('#searchInput').type('Appium')

    with allure.step('Verify content found'):
        results = browser.all('.suggestion-link')
        results.should(have.size_greater_than(0))
        #results.first.should(have.text('Appius'))
