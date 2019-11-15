from browser_factory import BrowserFactory


class BrowserSingletone:
    _browser = None

    @classmethod
    def get_browser(self, browser):
        if self._browser is None:
            self._browser = BrowserFactory(browser)
        return self._browser
