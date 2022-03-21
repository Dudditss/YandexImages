from BaseApp import BasePage
from selenium.webdriver.common.by import By
import time


class YandexSearchLocators:
    LOCATOR_YANDEX_NAVIGATION_BAR = (By.CLASS_NAME, "services-new__list-item")  # Локатор панели навигации
    LOCATOR_YANDEX_IMAGES = (By.CLASS_NAME, "PopularRequestList")  # Локатор панели навигации


class SearchHelper(BasePage):

    def check_navigation_bar(self):  # Функция получения элементов панели навигации
        all_list = self.find_elements(YandexSearchLocators.LOCATOR_YANDEX_NAVIGATION_BAR, time=5)
        nav_bar_menu = [x.text for x in all_list if len(x.text) > 0]
        all_list[3].click()
        time.sleep(3)
        return nav_bar_menu

    def images_bar(self):
        images_list = self.find_elements(YandexSearchLocators.LOCATOR_YANDEX_IMAGES, time=5)
        images = [x.text for x in images_list if len(x.text) > 0]
        images_list[0].click()
        time.sleep(3)
        return images
