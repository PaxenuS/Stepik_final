from .base_page import BasePage
from .locators import LoginPageLocators, MainPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "Ссылка не содержит 'login'"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Форма логина не найдена"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Форма регистрации не найдена"

    def register_new_user(self, email, password):
        field_email = self.browser.find_element(*LoginPageLocators.EMAIL)
        field_email.send_keys(email)
        field_password = self.browser.find_element(*LoginPageLocators.PASSWORD)
        field_password.send_keys(password)
        field_password_r = self.browser.find_element(*LoginPageLocators.PASSWORD_R)
        field_password_r.send_keys(password)
        botton = self.browser.find_element(*LoginPageLocators.BOTTON)
        botton.click()
