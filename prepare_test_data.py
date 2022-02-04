import pytest
import time

# сюда вынесены тестовые данные: параметры, ссылки и т.д.

# полный набор параметров промоакции
parametrize_full = [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9]
# короткий набор параметров прмооакции
parametrize_short = [6, pytest.param(7, marks=pytest.mark.xfail)]
# ссылка на страницу товара
link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/hacking-exposed-wireless_208/'
# ссылка на главную страницу
link_main_page = 'http://selenium1py.pythonanywhere.com/'
# ссылка на страницу входа
link_login = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'


def fake_email():
    # возвращает сгенерированное фейкомыло
    return str(time.time()) + "@fakemail.org"


def fake_pass():
    # генератор пароля писать было лень
    return 'TbpJOkfSZ'

