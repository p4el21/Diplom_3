import allure
from pages.recovery_page import RecoveryPage
from src.config import TestData, Config

class TestRecoveryPassword:
    @allure.title('Проверка перехода на страницу восстановления пароля')
    @allure.description('Тест проверяет, что можно успешно перейти на страницу восстановления пароля')
    def test_go_to_recovery(self, driver):
        recovery_page = RecoveryPage(driver)
        recovery_page.open_page(Config.URL)
        recovery_page.click_to_login_button()
        recovery_page.wait_for_login_page()
        recovery_page.click_recovery_button()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/forgot-password'

    @allure.title('Проверка ввода email и нажатия кнопки "Восстановить"')
    @allure.description('Тест проверяет, что можно ввести почту в поле и нажать кнопку восстановить')
    def test_click_to_recovery(self, driver):
        recovery_page = RecoveryPage(driver)
        recovery_page.open_page(Config.URL)
        recovery_page.click_to_login_button()
        recovery_page.wait_for_login_page()
        recovery_page.click_recovery_button()
        recovery_page.set_email(TestData.test_email)
        recovery_page.click_recovery()
        recovery_page.wait_for_reset_page()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/reset-password'

    @allure.title('Проверка активности поля "Пароль" при нажатии на кнопку "показать\скрыть пароль"')
    @allure.description('Тест проверяет, что нажатие на кнопку показать\скрыть пароль делает поле "Пароль" активным')
    def test_click_to_button(self, driver):
        recovery_page = RecoveryPage(driver)
        recovery_page.open_page(Config.URL)
        recovery_page.click_to_login_button()
        recovery_page.wait_for_login_page()
        recovery_page.click_recovery_button()
        recovery_page.set_email(TestData.test_email)
        recovery_page.click_recovery()
        recovery_page.wait_for_reset_page()
        recovery_page.click_hide_button()
        assert recovery_page.displayed_frame() == True