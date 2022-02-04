from selenium.webdriver.common.by import By


class BasePageLocators():
    # ссылка на страницу логина
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    # неверный селектор ссылки на страницу логина
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    # значок зарегистрированного пользователя
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    # кнопка "перейти в корзину"
    GOTO_BASKET_BUTTON = (By.XPATH, '//span[@class="btn-group"]/a')


class BasketPageLocators():
    # фрейм с товарами в корзине, отсутствует когда корзина пуста
    BASKET_FRAME = (By.XPATH, '//div[@class="basket_items"]')
    # сообщение о пустой корзине
    BASKET_EMPTY_MESSAGE = (By.XPATH, '//div[@id="content_inner"]/p')


class MainPageLocators():
    # они тут были, но разъехались по другим классам
    pass


class LoginPageLocators():
    # форма ввода логина
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    # форма регистрации
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    # поле ввода мейла при регистрации
    REGISTER_EMAIL = (By.XPATH, '//input[@name="registration-email"]')
    # поле ввода пароля при регистрации
    REGISTER_PASS = (By.XPATH, '//input[@name="registration-password1"]')
    # поле подтверждения пароля
    REGISTER_PASS_CONFIRM = (By.XPATH, '//input[@name="registration-password2"]')
    # кнопка завершения регистрации
    REGISTER_BUTTON = (By.XPATH, '//button[@name="registration_submit"]')


class ProductPageLocators():
    # кнопка "добавить в корзину"
    ADD_TO_BASKET_BUTTON = (By.XPATH, '//button[@class="btn btn-lg btn-primary btn-add-to-basket"]')
    # уже забыл что это, поэтому комментарии лучше писать сразу
    ADD_TO_BASKET_FORM = (By.XPATH, '//form[@class="add-to-basket"]')
    # фрейм с данными о товаре
    PRODUCT_FORM = (By.XPATH, '//div[@class="col-sm-6 product_main"]')
    # название товара
    PRODUCT_NAME = (By.XPATH, '//div[@class="col-sm-6 product_main"]/h1')
    # цена товара
    PRODUCT_PRICE = (By.XPATH, '//div[@class="col-sm-6 product_main"]/p[1]')
    # название товара в корзине
    PRODUCT_IN_BASKET = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    # сообщение о добавлении в корзину
    ADD_TO_BASKET_CONFIRM = (By.XPATH, '//*[@id="messages"]/div[2]/div')
    # сумма товаров в корзине
    BASKET_VALUE = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')
