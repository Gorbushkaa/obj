from selenium import webdriver


class BrowserFactory:
    def __init__(self, browser):
        self.browser = browser

    def create_driver(self):
        if self.browser == "chrome":
            driver = webdriver.Chrome()
            yield driver
            driver.quit()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
            yield driver
            driver.quit()

