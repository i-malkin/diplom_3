
from ..data import urls
from ..locators import forgot_password_locators
from .base_page import BasePage
import allure

class ForgotPasswordPage(BasePage):
    page_link = urls.forgot_password_url

    @allure.step('Заполняем поле Email')
    def input_email(self, email):
        email_field = self.find_element(forgot_password_locators.email_field)
        email_field.send_keys(email)

    @allure.step('Кликаем кнопку Восстановить пароль')
    def click_recover(self):
        self.click(forgot_password_locators.recover_button)

    @allure.step('Кликаем кнопку Показать пароль')
    def click_show_password(self):
        self.click(forgot_password_locators.show_password_button)

    @allure.step('Проверяем что поле пароля активно')
    def is_active_password_field(self):
        field_locator = forgot_password_locators.password_field
        field = self.driver.find_element(*field_locator)
        classes = field.get_attribute('class')
        return 'active' in classes

    @allure.step('Проверяем что адрес ссылки совпадает')
    def is_url_reset_password(self):
        expected_url_string = 'reset-password'
        self.wait_until_url_contains(expected_url_string)
        return expected_url_string in self.get_current_url()

