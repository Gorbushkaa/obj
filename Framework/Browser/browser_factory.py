from selenium import webdriver
import json


class BrowserFactory:

    def read_json(self):
        with open("conf.json") as f:
            data = json.load(f)
            return dict(data)

    def create_driver(self):
        browser = self.read_json()['browser']
        if browser == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("download.default_directory=D:/Python/Проекты/selenium2")
            driver = webdriver.Chrome()
            return driver
        elif browser == "firefox":
            driver = webdriver.Firefox()
            return driver

