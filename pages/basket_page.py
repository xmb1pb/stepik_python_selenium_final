from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_empty_basket_confirm_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), \
            "No empty basket message present, but it should"

    def should_not_be_empty_basket_confirm_message(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), \
            "Empty basket message present, but it should"

    def is_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_FRAME), \
            "Basket frame present, not empty"
