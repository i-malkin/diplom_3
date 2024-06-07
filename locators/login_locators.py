
from selenium.webdriver.common.by import By

email_field = (By.XPATH, ".//input[contains(@name,'name')]")
password_field = (By.XPATH, ".//input[contains(@name,'Пароль')]")
restore_password_button = (By.XPATH, ".//p/a[text()='Восстановить пароль']")
login_button = (By.XPATH, ".//button[text()='Войти']")
logout_button = (By.XPATH, ".//button[text()='Выход']")
profile_button = (By.XPATH, ".//p[text()='Личный Кабинет']")

