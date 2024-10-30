import allure
from locators.main_page_locators import MainLocators
from pages.main_page import MainPage
from src.config import Config

class TestMain:
    @allure.title('Проверка перехода на ленту заказов')
    @allure.description('Тест проверяет, что можно успешно перейти на страницу с лентой заказов')
    def test_go_to_orders_list(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Config.URL)
        main_page.click_to_orders_list()
        assert driver.current_url == Config.URL_FEED

    @allure.title('Проверка перехода на конструктор')
    @allure.description('Тест проверяет, что можно успешно перейти на страницу с конструктором')
    def test_go_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Config.URL)
        main_page.click_to_orders_list()
        main_page.click_to_constructor()
        assert driver.current_url == Config.URL

    @allure.title('Проверка клика на ингредиент')
    @allure.description('Тест проверяет, что при нажатии на ингредиент всплывает окно с деталями')
    def test_open_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Config.URL)
        main_page.click_to_ingredient()
        assert main_page.displayed_ingredient() == True

    @allure.title('Проверка закрытия ингредиента по крестику')
    @allure.description('Тест проверяет, что при нажатии на крестик ингредиент закрывается')
    def test_close_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Config.URL)
        main_page.click_to_ingredient()
        main_page.click_to_x()

    @allure.title('Проверка изменения каунтера')
    @allure.description('Тест проверяет, что при добавления ингредиента в заказ, каунтер над ним изменяется')
    def test_add_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Config.URL)
        base_value = int(driver.find_element(*MainLocators.COUNTER).text)
        main_page.drag_ingredient()
        new_value = int(driver.find_element(*MainLocators.COUNTER).text)
        assert new_value == base_value + 2

    @allure.title('Проверка оформления заказ')
    @allure.description('Тест проверяет, что залогиненный пользователь может оформить заказ')
    def test_create_order(self, driver, login_user):
        main_page = MainPage(driver)
        main_page.open_page(Config.URL)
        main_page.drag_ingredient()
        main_page.click_order()
        main_page.wait_for_order()
        assert main_page.displayed_container() == True

