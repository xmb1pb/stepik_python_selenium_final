from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        enter_email = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL).send_keys(email)
        enter_password = self.browser.find_element(*LoginPageLocators.REGISTER_PASS).send_keys(password)
        re_enter_password = self.browser.find_element(*LoginPageLocators.REGISTER_PASS_CONFIRM).send_keys(password)
        reg_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'Seems that URL is not login URL'

    def should_be_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM), 'Seems that login form is missing from login page'

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM), 'Seems that registration form is missing from login page'
