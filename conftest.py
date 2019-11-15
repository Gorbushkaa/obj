from selenium import webdriver
import pytest
from browser_sigletone import BrowserSingletone
import json


def pytest_addoption(parser):
    conf = json.dump("conf.json")
    parser.addoption('--browser', action='store', default=conf["browser"])


@pytest.fixture(scope="session")
def browser(request):
    browser = request.config.getoption('--browser')
    bs = BrowserSingletone()
    bs.get_browser(browser)
