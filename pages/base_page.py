import math
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from .locators import BasePageLocators


class BasePage:
    # конструктор
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self) -> None:
        # открывает ссылку в браузере
        self.browser.get(self.url)

    def is_element_present(self, by_method, elem_locator) -> bool:
        # проверяет наличие элемента
        try:
            self.browser.find_element(by_method, elem_locator)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, by_method, elem_locator, timeout=4) -> bool:
        # проверяет отсутствие элемента
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((by_method, elem_locator)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, by_method, elem_locator, timeout=4) -> bool:
        # проверяет что элемент исчезает когда надо
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((by_method, elem_locator)))
        except TimeoutException:
            return False
        return True

    def should_be_login_link(self):
        # проверяет наличие ссылки на страницу входа
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), \
            "Login link is not presented"

    def go_to_basket(self):
        # кликает на кнопку "перейти в корзину"
        # не проверял, что будет, если вызвать его на BasketPage
        basket_button = self.browser.find_element(*BasePageLocators.GOTO_BASKET_BUTTON)
        basket_button.click()

    def go_to_login_page(self):
        # кликает на ссылку на страницу входа
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_authorized_user(self):
        # проверяет что пользователь авторизован
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                         " probably unauthorised user"

    def solve_quiz_and_get_code(self):
        # судя по всему, решает главный вопрос жизни, вселенной и всего такого
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
