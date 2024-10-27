import allure
from pages.personal_page import PersonalPage
from src.config import Config

class TestPersonalAccount:
    @allure.title('Проверка перехода в личный кабинет в шапке профиля')
    @allure.description('Тест проверяет, что можно успешно перейти в личный кабинет, нажав на соответствующую кнопку в шапке профиля')
    def test_click_to_personal_account(self, driver):
        personal_page = PersonalPage(driver)
        personal_page.open_page(Config.URL)
        personal_page.click_to_button_from_up()
        personal_page.wait_for_account_login()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    @allure.title('Проверка перехода в историю заказов в личном кабинете')
    @allure.description('Тест проверяет, что можно успешно перейти в историю заказов, находясь в личном кабинете')
    def test_click_to_history(self, driver, create_user):
        personal_page = PersonalPage(driver)
        personal_page.open_page(Config.URL)
        user_data = create_user['user_data']
        email = user_data['email']
        password = user_data['password']
        personal_page.click_to_button_from_up()
        personal_page.login(email, password)
        personal_page.wait_for_main_page()
        personal_page.click_to_button_from_up()
        personal_page.wait_for_account_page()
        personal_page.click_button_history()
        personal_page.wait_for_history_page()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/order-history'

    @allure.title('Проверка выхода из аккаунта в личном кабинете')
    @allure.description('Тест проверяет, что можно успешно выйти из аккаунта, находясь в личном кабинете')
    def test_click_to_logout_account(self, driver, create_user):
        personal_page = PersonalPage(driver)
        personal_page.open_page(Config.URL)
        user_data = create_user['user_data']
        email = user_data['email']
        password = user_data['password']
        personal_page.click_to_button_from_up()
        personal_page.login(email, password)
        personal_page.wait_for_main_page()
        personal_page.click_to_button_from_up()
        personal_page.wait_for_account_page()
        personal_page.click_button_logout()
        personal_page.wait_for_account_login()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
