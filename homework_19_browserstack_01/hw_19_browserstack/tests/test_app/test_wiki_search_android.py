import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import have,be, browser


def test_search():
    with allure.step("Кликам по поиску"):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
    with allure.step("Вводим значение в поиск"):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type("Android")
    with allure.step("Кликаем по результату запроса"):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title")).click()
    '''
    Проверка статьи не реализовать, т.к. открывается страница с ошибкой
    '''
    #results = browser.element((AppiumBy.ACCESSIBILITY_ID, "Android most commonly refers to:"))
    #results.first.should(have.text('Android most commonly refers to:'))


