import pytest
import time

parametrize_full = [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9]
parametrize_short = [6, pytest.param(7, marks=pytest.mark.xfail)]
link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/hacking-exposed-wireless_208/'
link_main_page = 'http://selenium1py.pythonanywhere.com/'
link_login = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
