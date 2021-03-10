import time

from selenium import webdriver
from selenium.webdriver import chrome, DesiredCapabilities
from configparser import ConfigParser

from selenium.webdriver.ie.options import Options

import constants

config = ConfigParser()
config.read("./input/Config.cfg")

def before_all(context):
    capability = {"brower": "path"}
    browser = constants.Browsers
    path = constants.WEBDRIVER_PATH
    if browser == "firefox":
        context.driver = webdriver.Firefox(path)
    elif browser == "chrome":
         context.driver = webdriver.Chrome(path)
    elif browser == "ie":
        context.driver = webdriver.Ie(path)
    else:
        raise ValueError("Unrecognized browser %s" % browser)
    print("this is excuted")
    context.driver.get("https://www.amazon.com")
    # context.driver.get(config.get("Environments1", "URL"))
    context.driver.maximize_window()
    context.driver.implicitly_wait(3)
    context.driver.find_element_by_xpath("//*[@id='nav-signin-tooltip']/a/span").click()
    context.driver.find_element_by_id("ap_email").send_keys(config.get("Logincredentials", "email"))
    time.sleep(5)
    context.driver.find_element_by_id("continue").click()
    time.sleep(5)
    context.driver.find_element_by_id("ap_password").send_keys(config.get("Logincredentials", "PASSWORD"))
    context.driver.find_element_by_id("signInSubmit").click()




def after_all(context):
    context.driver.quit()


# from behave import fixture
# def before_feature(context, feature):
#     print("Runs Before Each Feature")
#
# def after_feature(context, feature):
#     print("Run After Each Feature")
#
# def before_scenario(context, scenario):
#     print("Run Before Each Scenario")
#
# def after_scenario(context, scenario):
#     print("Run After Each Scenario")
