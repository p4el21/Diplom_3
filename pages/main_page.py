import allure
from locators.main_page_locators import MainLocators
from pages.base_page import BasePage
from src.config import Config

class MainPage(BasePage):

    @allure.step('Открываем главную страницу')
    def open_page(self, url):
        self.navigate(Config.URL)

    @allure.step('Нажимаем на кнопку "Лента заказов" на главной странице')
    def click_to_orders_list(self):
        self.click_element(MainLocators.ORDERS_LIST_BUTTON)

    @allure.step('Нажимаем на кнопку "Конструктор" на главной странице')
    def click_to_constructor(self):
        self.click_element(MainLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Нажимаем на ингредиент "Булка" в разделе начинки')
    def click_to_ingredient(self):
        self.click_element(MainLocators.INGREDIENT_FIELD)

    @allure.step('Нажимаем на крестик в окне ингредиента')
    def click_to_x(self):
        self.click_element(MainLocators.X_BUTTON)

    @allure.step('Перетащить ингредиент в корзину')
    def drag_ingredient(self):
        self.drag_and_drop(MainLocators.INGREDIENT_FIELD, MainLocators.ORDER_BASKET)

    @allure.step('Нажимаем на кнопку "Оформить заказ"')
    def click_order(self):
        self.click_element(MainLocators.ORDER_BUTTON)

    @allure.step('Проверяем видимость элемента')
    def displayed_container(self):
        return self.is_displayed(MainLocators.CONTAINER)

    @allure.step('Ожидаем загрузки заказа')
    def wait_for_order(self):
        self.wait_for_element_visible(MainLocators.CONTAINER)

    @allure.step('Нажимаем на кнопку "закрыть"')
    def click_close_button(self):
        self.click_element(MainLocators.CLOSE_BUTTON)

    @allure.step('Проверяем видимость ингредиента')
    def displayed_ingredient(self):
        return self.is_displayed(MainLocators.INGREDIENT)








