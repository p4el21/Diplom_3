from selenium.webdriver.common.by import By

class FeedLocators:
    PERSONAL_ACCOUNT_BUTTON = By.XPATH, '//a[contains(@class, "AppHeader_header") and @href="/account"]'
    EMAIL_FIELD = By.XPATH, '//input[@name="name"]'
    PASSWORD_FIELD = By.XPATH, '//input[@name="Пароль"]'
    SIGNIN_BUTTON = By.XPATH, '//button[contains(text(), "Войти")]'
    WAIT_LOAD_MAIN_PAGE = By.XPATH, '//button[contains(text(), "Оформить заказ")]'
    HISTORY_BUTTON = By.XPATH, '//a[@href="/account/order-history"]'
    ORDER_INFORMATION = By.XPATH, './/li[contains(@class, "OrderHistory_listItem")]'
    ORDER = By.XPATH, ".//div[contains(@class, 'Modal_orderBox')]"
    ORDERS_LIST = By.XPATH, ".//div[contains(@class, 'OrderHistory_textBox')]"
    FEED_BUTTON = By.XPATH, '//a[@href="/feed"]'
    FEED_ORDERS = By.XPATH,  './/div[contains(@class, "OrderFeed_contentBox")]'
    INGREDIENT_FIELD = By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]'
    ORDER_BASKET = By.XPATH, './/ul[contains(@class, "BurgerConstructor_basket")]'
    ORDER_BUTTON = By.XPATH, './/button[contains(text(), "Оформить заказ")]'
    ORDER_CONTAINER = By.XPATH, './/div[contains(@class, "Modal_modal__container")]'
    CLOSE_BUTTON = By.XPATH, '//*[@id="root"]/div/section/div[1]/button'
