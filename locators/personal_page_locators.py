from selenium.webdriver.common.by import By

class PersonalLocators:
    PERSONAL_ACCOUNT_BUTTON = By.XPATH, '//a[contains(@class, "AppHeader_header") and @href="/account"]'
    EMAIL_FIELD = By.XPATH, '//input[@name="name"]'
    PASSWORD_FIELD = By.XPATH, '//input[@name="Пароль"]'
    BUTTON = By.XPATH, '//button[contains(text(), "Войти")]'
    WAIT_MAIN_PAGE = By.XPATH, '//button[contains(text(), "Оформить заказ")]'
    BUTTON_HISTORY = By.XPATH, '//a[@href="/account/order-history"]'
    WAIT_ACCOUNT_PAGE = By.XPATH, '//button[contains(text(), "Сохранить")]'
    WAIT_HISTORY_PAGE = By.XPATH, '//a[@aria-current="page"]'
    BUTTON_LOGOUT = By.XPATH, '//button[contains(text(), "Выход")]'
    WAIT_ACCOUNT_LOGIN = By.XPATH, '//button[contains(text(), "Войти")]'