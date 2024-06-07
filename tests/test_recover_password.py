
from ..pages.forgot_password_page import ForgotPasswordPage
from ..pages.login_page import LoginPage
from ..data.data import TEST_EMAIL
import allure

class TestRecoverPassword:
    @allure.title('Тест перехода на страницу восстановления пароля')
    def test_link_to_recover_password(self, driver):
        login_page = LoginPage(driver)
        forgot_page = ForgotPasswordPage(driver)
        login_page.load()
        login_page.click_recover()
        assert forgot_page.is_loaded()


    @allure.title('Тест перехода на страницу восстановления пароля')
    def test_enter_email_recovery(self, driver):
        forgot_page = ForgotPasswordPage(driver)
        forgot_page.input_email(TEST_EMAIL)
        forgot_page.click_recover()
        assert forgot_page.is_url_reset_password()


    @allure.title('Тест на работу кнопки "Показать пароль"')
    def test_show_password(self, driver):
        forgot_page = ForgotPasswordPage(driver)
        forgot_page.click_show_password()
        assert forgot_page.is_active_password_field()

