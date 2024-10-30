import allure
from pages.base_page import BasePage
from locators.feed_page_locators import FeedLocators

class FeedPage(BasePage):
    @allure.step('Инициализация драйвера')
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Открываем главную страницу')
    def open_page(self, url):
        self.navigate(url)

    @allure.step('Нажимаем на кнопку "личный кабинет" на главной странице')
    def click_to_personal_account(self):
        self.click_element(FeedLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Вводим данные в поле "Email"')
    def set_email(self, email):
        self.enter_text(FeedLocators.EMAIL_FIELD, email)

    @allure.step('Вводим данные в поле "Пароль"')
    def set_password(self, password):
        self.enter_text(FeedLocators.PASSWORD_FIELD, password)

    @allure.step('Нажимаем на кнопку "Войти"')
    def click_sign_in_button(self):
        self.click_element(FeedLocators.SIGNIN_BUTTON)

    @allure.step('Вводим email, пароль в соответствующие поля')
    def login(self, email, password):
        self.set_email(email)
        self.set_password(password)
        self.click_sign_in_button()

    @allure.step('Ожидаем загрузки главной страницы')
    def wait_load_main_page(self):
        self.wait_for_element_visible(FeedLocators.WAIT_LOAD_MAIN_PAGE)

    @allure.step('Нажимаем на кнопку "история заказов"')
    def click_history_button(self):
        self.click_element(FeedLocators.HISTORY_BUTTON)

    @allure.step('Нажимаем на заказ в истории')
    def click_order_information(self):
        self.click_element(FeedLocators.ORDER_INFORMATION)

    @allure.step('Проверяем видимость окна ингредиента')
    def displayed_order_information(self):
        return self.is_displayed(FeedLocators.ORDER)

    @allure.step('Ожидаем загрузки заказов в истории заказов')
    def wait_for_orders_list(self):
        self.wait_for_element_visible(FeedLocators.ORDERS_LIST)

    @allure.step('Нажимаем на кнопку "Лента заказов"')
    def click_to_feed(self):
        self.click_element(FeedLocators.FEED_BUTTON)

    @allure.step('Ожидаем загрузки ленты заказов')
    def wait_load_feed(self):
        self.wait_for_element_visible(FeedLocators.FEED_ORDERS)

    @allure.step('Перетащить ингредиент в корзину')
    def drag_ingredient(self):
        self.drag_and_drop(FeedLocators.INGREDIENT_FIELD, FeedLocators.ORDER_BASKET)

    @allure.step('Нажимаем на кнопку "Оформить заказ"')
    def click_order(self):
        self.click_element(FeedLocators.ORDER_BUTTON)

    @allure.step('Ожидаем загрузки окна с заказом')
    def wait_order_container(self):
        self.wait_for_element_visible(FeedLocators.ORDER_CONTAINER)

    @allure.step('Закрываем окно с заказом на крестик')
    def click_close(self):
        self.click_element(FeedLocators.CLOSE_BUTTON)