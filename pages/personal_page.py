import allure
from locators.personal_page_locators import PersonalLocators
from pages.base_page import BasePage
from src.config import Config

class PersonalPage(BasePage):

    @allure.step('Открываем главную страницу')
    def open_page(self, url):
        self.navigate(Config.URL)

    @allure.step('Нажимаем на кнопку "Личный кабинет" в шапке')
    def click_to_button_from_up(self):
        self.click_element(PersonalLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Вводим данные в поле "Email"')
    def set_email(self, email):
        self.enter_text(PersonalLocators.EMAIL_FIELD, email)

    @allure.step('Вводим данные в поле "Пароль"')
    def set_password(self, password):
        self.enter_text(PersonalLocators.PASSWORD_FIELD, password)

    @allure.step('Нажимаем на кнопку "Войти"')
    def click_sign_in_button(self):
        self.click_element(PersonalLocators.BUTTON)

    @allure.step('Вводим email, пароль в соответствующие поля')
    def login(self, email, password):
        self.set_email(email)
        self.set_password(password)
        self.click_sign_in_button()

    @allure.step('Ожидаем загрузки главной страницы')
    def wait_for_main_page(self):
        self.wait_for_element_visible(PersonalLocators.WAIT_MAIN_PAGE)

    @allure.step('Ожидаем загрузки страницы личного кабинета')
    def wait_for_account_page(self):
        self.wait_for_element_visible(PersonalLocators.WAIT_ACCOUNT_PAGE)

    @allure.step('Нажимаем на кнопку "история заказов"')
    def click_button_history(self):
        self.click_element(PersonalLocators.BUTTON_HISTORY)

    @allure.step('Ожидаем загрузки страницы "история заказов"')
    def wait_for_history_page(self):
        self.wait_for_element_visible(PersonalLocators.WAIT_HISTORY_PAGE)

    @allure.step('Нажимаем на кнопку "Выход"')
    def click_button_logout(self):
        self.click_element(PersonalLocators.BUTTON_LOGOUT)

    @allure.step('Ожидаем загрузки страницы входа')
    def wait_for_account_login(self):
        self.wait_for_element_visible(PersonalLocators.WAIT_ACCOUNT_LOGIN)