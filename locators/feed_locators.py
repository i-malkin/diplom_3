
from selenium.webdriver.common.by import By

total_counter = (By.XPATH, './/div/p[text()="Выполнено за все время:"]/following-sibling::p')
day_counter = (By.XPATH, './/div/p[text()="Выполнено за сегодня:"]/following-sibling::p')
first_order = (By.XPATH, './/h2[contains(text(), "бургер")]')
order_popup = (By.XPATH, './/button[contains(@class,"Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK")]')


