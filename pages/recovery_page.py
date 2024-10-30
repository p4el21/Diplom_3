import allure
from locators.recovery_page_locators import RecoveryLocators
from pages.base_page import BasePage

class RecoveryPage(BasePage):

    @allure.step('Открываем главную страницу')
    def open_page(self, url):
        self.navigate(url)

    @allure.step('Нажимаем на кнопку "Войти в аккаунт" на главной странице')
    def click_to_login_button(self):
        self.click_element(RecoveryLocators.LOGIN_BUTTON)

    @allure.step('Ожидаем загрузки страницы входа')
    def wait_for_login_page(self):
        self.wait_for_element_visible(RecoveryLocators.WAIT_ACCOUNT_LOGIN)

    @allure.step('Нажимаем на кнопку "Восстановить пароль"')
    def click_recovery_button(self):
        self.click_element(RecoveryLocators.RECOVERY_BUTTON_1)

    @allure.step('Вводим данные в поле "Email"')
    def set_email(self, email):
        self.enter_text(RecoveryLocators.EMAIL_FIELD, email)

    @allure.step('Нажимаем на кнопку "Восстановить"')
    def click_recovery(self):
        self.click_element(RecoveryLocators.RECOVERY_BUTTON_2)

    @allure.step('Ожидаем загрузки страницы сброса пароля')
    def wait_for_reset_page(self):
        self.wait_for_element_visible(RecoveryLocators.WAIT_RESET_PAGE)

    @allure.step('Нажимаем на кнопку "Показать\скрыть" пароль')
    def click_hide_button(self):
        self.click_element(RecoveryLocators.HIDE_BUTTON)

    @allure.step('Проверяем видимость элемента')
    def displayed_frame(self):
        return self.is_displayed(RecoveryLocators.ACTIVE_FIELD)