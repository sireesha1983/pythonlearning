
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import constants


class BestSeller:
    def click(self):
        self.driver.find_element_by_xpath(constants.Clickonbestseller).click()


class Newreases:
    def click(self):
        self.driver.find_element_by_xpath(constants.Clickonnewreases).click()


class Moversandshakers:
    def click(self):
        self.driver.find_element_by__xpath(constants.Clickonmoversandshakers).click()


class Mostwishedfor:
    def click(self):
        self.driver.find_element_by_xpath(constants.Clickonmostwishedfor).click()


class Giftideas:
    def click(self):
        self.driver.find_element_by_xpath(constants.Clickongiftideas).click()


class Firstimage:
    def click(self):
        self.driver.find_element_by_xpath(constants.Clickonfirstimage).click()


class Addingcart:
    def click(self):
        self.driver.find_element_by_id(constants.Clickonaddingcart).click()

class Proceedtocheckout:
    def click(self):
        self.driver.find_element_by_css_selector(constants.Clickonproceedtocheckout).click()





