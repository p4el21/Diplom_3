from selenium.webdriver.common.by import By

class RecoveryLocators:
    LOGIN_BUTTON = By.XPATH, '//button[contains(text(), "Войти в аккаунт")]'
    WAIT_ACCOUNT_LOGIN = By.XPATH, '//button[contains(text(), "Войти")]'
    RECOVERY_BUTTON_1 = By.XPATH, "//a[@href='/forgot-password']"
    EMAIL_FIELD = By.XPATH, '//input[@name="name"]'
    RECOVERY_BUTTON_2 = By.XPATH, '//button[contains(text(), "Восстановить")]'
    WAIT_RESET_PAGE = By.XPATH, '//button[contains(text(), "Сохранить")]'
    HIDE_BUTTON = By.XPATH, ".//div[contains(@class, 'input__icon')]"
    ACTIVE_FIELD = By.XPATH, ".//div[contains(@class, 'input_status_active')]"