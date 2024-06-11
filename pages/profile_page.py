
from ..locators import profile_locators
from ..pages.base_page import BasePage
from ..data import urls
import allure

class ProfilePage(BasePage):
    page_link = urls.profile_url

    @allure.step('Кликаем по кнопке История заказов')
    def click_order_history(self):
        self.click(profile_locators.order_history_button)

    @allure.step('Проверка что адрес страницы является адресом Истории заказов')
    def is_url_order_history(self):
        expected_string = 'order-history'
        self.wait_until_url_contains(expected_string)
        return expected_string in self.get_current_url()

    @allure.step('Кликаем по кнопке Выйти')
    def click_log_out(self):
        self.click(profile_locators.logout_button)

    @allure.step('Проверка что адрес страницы является адресом страницы авторизации')
    def is_url_login(self):
        expected_string = 'login'
        self.wait_until_url_contains(expected_string)
        return expected_string in self.get_current_url()

