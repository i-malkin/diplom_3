
from ..locators import login_locators
from .base_page import BasePage
from ..data import data, urls
import allure


class LoginPage(BasePage):
    page_link = urls.login_url

    @allure.step('Кликаем по кнопке Личный кабинет')
    def click_profile(self):
        self.wait_until_url_matches(urls.base_url)
        self.click(login_locators.profile_button).click()

    @allure.step('Кликаем кнопку восстановить пароль')
    def click_recover(self):
        self.click(login_locators.restore_password_button)

    @allure.step('Выполняем авторизацию')
    def login(self, email, password):
        email_field = self.wait_until_visibility(login_locators.email_field)
        password_field = self.wait_until_visibility(
            login_locators.password_field)
        email_field.send_keys(email)
        password_field.send_keys(password)
        self.click(login_locators.login_button)

    @allure.step('Авторизация тестового-пользователя')
    def login_test_user(self):
        email = data.TEST_USER['email']
        password = data.TEST_USER['password']
        self.login(email, password)

    @allure.step('Проверяем авторизацию')
    def is_logged_in(self):
        log_out_button = self.wait_until_visibility(
            login_locators.logout_button)
        return log_out_button.is_displayed()

