from selenium.webdriver.common.by import By

class MainLocators:
    ORDERS_LIST_BUTTON = By.XPATH, '//a[@href="/feed"]'
    CONSTRUCTOR_BUTTON = By.XPATH, '//a[@href="/"]'
    INGREDIENT_FIELD = By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]'
    X_BUTTON = By.XPATH, '//button[@type="button"]'
    ORDER_BASKET = By.XPATH, '//*[@id="root"]/div/main/section[2]/ul'
    ORDER_BUTTON = By.XPATH, './/button[contains(text(), "Оформить заказ")]'
    CONTAINER = By.XPATH, './/div[contains(@class, "Modal_modal__container")]'
    CLOSE_BUTTON = By.XPATH, '//*[@id="root"]/div/section/div[1]/button/svg'
    INGREDIENT = By.XPATH, './/div[contains(@class, "Modal_modal__contentBox")]'
    COUNTER = By.XPATH, './/a[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]//div[contains(@class, "counter_counter")]'