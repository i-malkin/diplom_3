
from ..data import urls
from ..locators import feed_locators
from .base_page import BasePage
import allure

class FeedPage(BasePage):
    page_link = urls.feed_url

    @allure.step('Возвращаем значения счетчиков')
    def check_counters(self):
        total_counter = int(self.wait_until_visibility(
            feed_locators.total_counter).text)
        day_counter = int(self.wait_until_visibility(
            feed_locators.day_counter).text)
        return (total_counter, day_counter)

    @allure.step('Клик по кнопке заказать')
    def click_order(self):
        self.click(feed_locators.first_order)

    @allure.step('Проверяем открытие Информация о заказе')
    def is_order_popup(self):
        popup = self.find_element(feed_locators.order_popup)
        popup.is_displayed()
        return popup


