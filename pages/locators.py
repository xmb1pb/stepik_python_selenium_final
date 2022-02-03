from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.XPATH, '//button[@class="btn btn-lg btn-primary btn-add-to-basket"]')
    ADD_TO_BASKET_FORM = (By.XPATH, '//form[@class="add-to-basket"]')
    PRODUCT_FORM = (By.XPATH, '//div[@class="col-sm-6 product_main"]')
    PRODUCT_NAME = (By.XPATH, '//div[@class="col-sm-6 product_main"]/h1')
    PRODUCT_PRICE = (By.XPATH, '//div[@class="col-sm-6 product_main"]/p[1]')
    PRODUCT_IN_BASKET = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    ADD_TO_BASKET_CONFIRM = (By.XPATH, '//*[@id="messages"]/div[2]/div')
    BASKET_VALUE = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')

