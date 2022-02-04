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
        login_page = LoginPage(browser, link_login)
        login_page.open()
        login_page.register_new_user(email=str(time.time()) + "@fakemail.org", password='TbpJOkfSZ')
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_product_page()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_product_page()
        expected_product_name = page.get_product_name()
        expected_product_price = page.get_product_price()
        page.add_to_cart()
        page.basket_validation(expected_product_name, expected_product_price)


@pytest.mark.parametrize('promo', parametrize_short)
def test_guest_can_add_product_to_basket(browser, promo):
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
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
    page.add_to_cart()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
    page.should_not_be_success_message()


@pytest.mark.xfail()
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
    page.add_to_cart()
    page.should_disappear_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, link_main_page)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.is_basket_empty()
    basket_page.should_be_empty_basket_confirm_message()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.is_basket_empty()
    basket_page.should_be_empty_basket_confirm_message()


if __name__ == '__main__':
    pytest.main()
