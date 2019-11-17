from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Framework.Browser.browser_sigletone import BrowserSingletone as BS
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self):
        self.driver = BS.get_driver()
        self.url = BS.read_json()['url']

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message="Невозможно найти объект с локатором{}".format(locator))

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message="Невозможно найти объект с локатором{}".format(locator))

    def go_to_site(self):
        return self.driver.get(self.url)

    def click_button(self, locator):
        self.find_element(locator).click()

