from Framework.Browser.browser_factory import BrowserFactory
import json


class BrowserSingletone:
    _driver = None

    @classmethod
    def get_driver(cls):
        if cls._driver is None:
            cls._driver = BrowserFactory().create_driver()
        return cls._driver

    @classmethod
    def quit_driver(cls):
        cls._driver.quit()

    @classmethod
    def read_json(cls):
        with open("conf.json") as f:
            data = json.load(f)
            return(data)