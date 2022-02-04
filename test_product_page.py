import pytest
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from .prepare_test_data import *


@pytest.mark.login_user()
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        # фикстура регистрирует нового пользователя перед тестом
        login_page = LoginPage(browser, link_login)
        login_page.open()
        login_page.register_new_user(email=fake_email(), password=fake_pass())
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        # зарегистрированный пользователь не видит сообщения об
        # успешном добавлении товара в корзину на странице товара
        page = ProductPage(browser, link)
        page.open()
        page.should_be_product_page()
        page.should_not_be_success_message()

    @pytest.mark.need_review()
    def test_user_can_add_product_to_basket(self, browser):
        # зарегистрированный пользователь может добавить товар в корзину
        page = ProductPage(browser, link)
        page.open()
        page.should_be_product_page()
        expected_product_name = page.get_product_name()
        expected_product_price = page.get_product_price()
        page.add_to_cart()
        page.basket_validation(expected_product_name, expected_product_price)


@pytest.mark.need_review()
@pytest.mark.parametrize('promo', parametrize_short)
def test_guest_can_add_product_to_basket(browser, promo):
    # гость может добавить товар в корзину с учетов промо-акции
    # короткий набор данный использует только два параметра 6 и 7, при этом 7 ожидаемо падает
    # для прогона с полным набором данных нужно передать parametrize_full
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo}"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
    expected_product_name = page.get_product_name()
    expected_product_price = page.get_product_price()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.basket_validation(expected_product_name, expected_product_price)


@pytest.mark.xfail()
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    # гость не видит сообщение о добавлении товара в корзину после добавления товара в корзину
    # ехал корзина через корзина
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
    page.add_to_cart()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    # гость не видит сообщения о добавлении товара в корзину на странице товара
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
    page.should_not_be_success_message()


@pytest.mark.xfail()
def test_message_disappeared_after_adding_product_to_basket(browser):
    # сообщение о добавлении товара в корзину исчезает после добавления товара в корзину
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
    page.add_to_cart()
    page.should_disappear_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    # гость видит ссылку "войти\регистрация" на странице товара
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review()
def test_guest_can_go_to_login_page_from_product_page(browser):
    # гость может перейти на страницу входа со страницы товара
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    # гость не видит товаров в корзине, переходя в корзину со главноей страницы
    page = MainPage(browser, link_main_page)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.is_basket_empty()
    basket_page.should_be_empty_basket_confirm_message()

@pytest.mark.need_review()
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    # гость не видит товаров в корзине, переходя в корзину со страницы товара
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.is_basket_empty()
    basket_page.should_be_empty_basket_confirm_message()


if __name__ == '__main__':
    pytest.main()
