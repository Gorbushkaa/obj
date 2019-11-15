import pytest
from Framework.Browser.browser_sigletone import BrowserSingletone
import json


def pytest_addoption(parser):
    conf = json.dump("conf.json")
    parser.addoption('--browser', action='store', default=conf["browser"])


@pytest.fixture(scope="session")
def browser(request):
    browser = request.config.getoption('--browser')
    bs = BrowserSingletone()
    driver = bs.get_driver(browser)
    yield driver
    bs.quit_driver()
