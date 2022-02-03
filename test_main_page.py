import pytest
import time
from .pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    time.sleep(10)
    page.go_to_login_page()


if __name__ == '__main__':
    pytest.main()
