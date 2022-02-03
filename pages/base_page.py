from selenium.common.exceptions import NoSuchElementException

class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, by_method, elem_locator):
        try:
            self.browser.find_element(by_method, elem_locator)
        except NoSuchElementException:
            return False
        return True
