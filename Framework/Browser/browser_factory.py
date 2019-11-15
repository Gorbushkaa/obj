from selenium import webdriver


class BrowserFactory:
    def __init__(self, browser):
        self.browser = browser

    def create_driver(self):
        if self.browser == "chrome":
            driver = webdriver.Chrome()
            return driver
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
            return driver

