
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import allure

class BasePage():

    page_link = None

    @allure.step('Инициализация BasePage с драйвером')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Загрузка страницы с ссылкой')
    def load(self):
        self.driver.get(self.page_link)

    @allure.step('Ожидание, секунд')
    def wait(self, time):
        wait = WebDriverWait(self.driver, time)
        return wait

    @allure.step('Ожидание видимости элемента, локатор')
    def wait_until_visibility(self, locator):
        return self.wait(5).until(
            EC.visibility_of_element_located(locator))

    @allure.step('Ожидание, пока URL содержит: {string}')
    def wait_until_url_contains(self, string):
        return self.wait(5).until(EC.url_contains(string))

    @allure.step('Ожидание, пока URL совпадает с: {string}')
    def wait_until_url_matches(self, string):
        return self.wait(5).until(EC.url_matches(string))

    @allure.step('Ожидание, пока элемент станет кликабельным')
    def wait_until_element_is_clickable(self, element):
        element = self.wait(5).until(
            EC.element_to_be_clickable(element))
        return element

    @allure.step('Клик по элементу с локатором')
    def click(self, locator):
        button = self.wait(5).until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].click();", button)

        return button

    @allure.step('Клик по элементу с локатором, с ожиданием')
    def click_wait(self, locator):
        button = self.wait(5).until(EC.element_to_be_clickable(locator))
        action = ActionChains(self.driver)
        action.move_to_element(button)
        action.pause(1)
        action.click()
        action.perform()

        return button

    @allure.step('Поиск элемента с локатором')
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Получение текущего URL')
    def get_current_url(self):
        url = self.driver.current_url
        return url

    @allure.step('Проверка, загружена ли страница')
    def is_loaded(self):
        return self.get_current_url() == self.page_link

    @allure.step('Ожидаем пока элемент станет невидимым')
    def invisility_of_elememnt_located(self, locator):
        return self.wait(5).until(EC.invisibility_of_element_located(locator))

    @allure.step('Перетаскивание элемента')
    def drag_and_drop(self, drag, drop):
        action = ActionChains(self.driver)
        action.move_to_element(drag)
        action.pause(1)
        action.click_and_hold(drag)
        action.release(drop)
        action.pause(1)
        action.perform()

