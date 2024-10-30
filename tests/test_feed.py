import time
import allure
from selenium.webdriver.common.by import By

from locators.feed_page_locators import FeedLocators
from pages.feed_page import FeedPage
from src.config import Config

class TestFeed:
    @allure.title('Проверка открытия информации о заказе')
    @allure.description('Тест проверяет, что при нажатии на заказ всплывает дополнительное окно с информацией о заказе')
    def test_open_order(self, driver, create_order_auth_user):
        feed_page = FeedPage(driver)
        feed_page.open_page(Config.URL)
        user_data = create_order_auth_user['user_data']
        email = user_data['email']
        password = user_data['password']
        feed_page.click_to_personal_account()
        feed_page.login(email, password)
        feed_page.wait_load_main_page()
        feed_page.click_to_personal_account()
        feed_page.click_history_button()
        feed_page.wait_for_orders_list()
        feed_page.click_order_information()
        assert feed_page.displayed_order_information() == True

    @allure.title('Проверка отображения заказа как в истории, так и в ленте заказов')
    @allure.description('Тест проверяет, что созданный заказ отображается и в ленте заказов, и в истории заказов')
    def test_view_order(self, driver, create_order_auth_user):
        feed_page = FeedPage(driver)
        feed_page.open_page(Config.URL)
        user_data = create_order_auth_user['user_data']
        email = user_data['email']
        password = user_data['password']
        feed_page.click_to_personal_account()
        feed_page.login(email, password)
        feed_page.wait_load_main_page()
        feed_page.click_to_personal_account()
        feed_page.click_history_button()
        feed_page.wait_for_orders_list()
        number_order_from_history = driver.find_element(*FeedLocators.NUMBER_ORDER_FROM_HISTORY).text
        feed_page.click_to_feed()
        feed_page.wait_load_feed()
        number_order_from_feed = driver.find_element(*FeedLocators.NUMBER_ORDER_FROM_FEED).text
        assert number_order_from_history in number_order_from_feed, \
            f'Номер заказа из истории {number_order_from_history} и ленты {number_order_from_feed} совпадают'

    @allure.title('Проверка изменения счетчика заказов за всё время')
    @allure.description('Тест проверяет, что созданный заказ изменяет счетчик количества заказов за всё время')
    def test_count_orders_all_time(self, driver, create_user):
        feed_page = FeedPage(driver)
        feed_page.open_page(Config.URL)
        feed_page.click_to_feed()
        feed_page.wait_load_feed()
        before = driver.find_element(*FeedLocators.COUNTER).text
        feed_page.click_to_personal_account()
        user_data = create_user['user_data']
        email = user_data['email']
        password = user_data['password']
        feed_page.login(email, password)
        feed_page.wait_load_main_page()
        feed_page.drag_ingredient()
        feed_page.click_order()
        feed_page.wait_order_container()
        time.sleep(1)
        feed_page.click_close()
        feed_page.click_to_feed()
        feed_page.wait_load_feed()
        after = driver.find_element(*FeedLocators.COUNTER).text
        assert before != after, f'Начальное количество заказов: {before}, конечное количество: {after}'

    @allure.title('Проверка изменения счетчика заказов за день')
    @allure.description('Тест проверяет, что созданный заказ изменяет счетчик количества заказов за день')
    def test_count_orders_day(self, driver, create_user):
        feed_page = FeedPage(driver)
        feed_page.open_page(Config.URL)
        feed_page.click_to_feed()
        feed_page.wait_load_feed()
        before = driver.find_element(*FeedLocators.DAY_COUNTER).text
        feed_page.click_to_personal_account()
        user_data = create_user['user_data']
        email = user_data['email']
        password = user_data['password']
        feed_page.login(email, password)
        feed_page.wait_load_main_page()
        feed_page.drag_ingredient()
        feed_page.click_order()
        feed_page.wait_order_container()
        time.sleep(1)
        feed_page.click_close()
        feed_page.click_to_feed()
        feed_page.wait_load_feed()
        after = driver.find_element(*FeedLocators.DAY_COUNTER).text
        assert before != after, f'Начальное количество заказов: {before}, конечное количество: {after}'

    @allure.title('Проверка статуса оформленного заказа')
    @allure.description('Тест проверяет, что созданный заказ отображается в разделе "В работе"')
    def test_order_status(self, driver, create_order_auth_user):
        user_data = create_order_auth_user['user_data']
        email = user_data['email']
        password = user_data['password']
        feed_page = FeedPage(driver)
        feed_page.open_page(Config.URL)
        feed_page.click_to_personal_account()
        feed_page.login(email, password)
        feed_page.wait_load_main_page()
        feed_page.click_to_feed()
        feed_page.wait_load_feed()
        base_text = 'Все текущие заказы готовы!'
        actual_text = driver.find_element(*FeedLocators.STATUS).text
        assert actual_text != base_text, f' Номер {base_text} не совпадает с номером {actual_text}'
