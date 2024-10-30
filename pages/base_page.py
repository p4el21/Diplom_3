import allure
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    @allure.step('Инициализация драйвера')
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def navigate(self, url):
        self.driver.get(url)

    def find_element(self, locator, timeout = 20):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            print(f'Element with locator {locator} not found within {timeout} seconds.')
            return None

    def click_element(self, locator, timeout = 30):
        element = self.find_element(locator, timeout)
        if element:
            element.click()
        else:
            print(f'Failed to click on element with {locator}.')

    def enter_text(self, locator, text, timeout = 20):
        element = self.find_element(locator, timeout)
        if element:
            element.clear()
            element.send_keys(text)
        else:
            print(f'Failed to enter text in element with {locator}.')

    def wait_for_element_visible(self, locator, timeout = 40):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            print(f'Element with locator {locator} not visible after {timeout} seconds.')
            return None

    def is_displayed(self, locator, timeout = 20):
        try:
            element = self.find_element(locator)
            return element.is_displayed()
        except TimeoutException:
            print(f'Element with locator {locator} not visible after {timeout} seconds.')
            return False

    def drag_and_drop(self, locator_1, locator_2, timeout=20):
        actions = ActionChains(self.driver)
        element_1 = self.find_element(locator_1, timeout)
        element_2 = self.find_element(locator_2, timeout)
        actions.drag_and_drop(element_1, element_2).perform()


