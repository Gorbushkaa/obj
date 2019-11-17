from base_app import BasePage
from selenium.webdriver.common.by import By


class SteamLocators:
    LOCATOR_STEAM_BUTTON_WELCOME_STEAM = (By.XPATH, "//a[@class='header_installsteam_btn_content']")
    LOCATOR_STEAM_BUTTON_DOWNLOAD = (By.XPATH, "//a[@class='about_install_steam_link']")


class Steam(BasePage):

    def click_welcome(self):
        self.click_button(SteamLocators.LOCATOR_STEAM_BUTTON_WELCOME_STEAM)

    def click_download(self):
        self.click_button(SteamLocators.LOCATOR_STEAM_BUTTON_DOWNLOAD)



