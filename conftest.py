import pytest
from Framework.Browser.browser_sigletone import BrowserSingletone
import json


def pytest_addoption(parser):
    data = read_json()
    parser.addoption('--browser', action='store', default=data["browser"])


def read_json():
    with open("conf.json", "r") as f:
        data = json.load(f)
    return data


def switch_browser(browser):
    with open("conf.json") as f:
        data = json.load(f)
        print(data)
        if data["browser"] != browser:
            data["browser"] = browser
            f.seek(0)
            f.write(data)


@pytest.fixture(scope="session")
def browser(request):
    browser = request.config.getoption('--browser')
    switch_browser(browser)
    bs = BrowserSingletone()
    driver = bs.get_driver()
    yield driver
    bs.quit_driver()
