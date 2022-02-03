import time
import pytest
from .pages.product_page import ProductPage

expected_product_name = 'The shellcoder\'s handbook'
expected_product_price = '9,99 £'
expected_confirmation = 'Ваша корзина удовлетворяет условиям предложения Deferred benefit offer.'


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.basket_validation(expected_product_name, expected_confirmation, expected_product_price)





if __name__ == '__main__':
    pytest.main()

'''
to be implemented:

 done   Добавить новый файл для тест-кейсов, связанных со страницей товара. Назовите файл с тестами test_product_page.py.
    Создать класс Page Object для страницы товара. Опишите его в файле product_page.py в папке pages.
    Описать в нем метод для добавления в корзину.
    Дописать методы-проверки.
    Описать необходимые локаторы к элементам страницы.
    Написать сам тест-кейс, используя все вышеописанное. Назовите тест test_guest_can_add_product_to_basket.

'''