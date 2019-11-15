from Framework.Browser.browser_factory import BrowserFactory


class BrowserSingletone:
    _driver = None

    @classmethod
    def get_driver(self, browser):
        if self._driver is None:
            self._driver = BrowserFactory(browser)
        return self._driver

    @classmethod
    def quit_driver(cls):
        cls._driver.quit()
