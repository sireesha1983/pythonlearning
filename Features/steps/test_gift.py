import time

from behave import when, then

import constants


@when(u'i click on find a gift')
def click_on_find_a_gigt(context):
    context.driver.find_element_by_xpath(constants.Findagift).click()


@when(u'i click on mothers day')
def click_on_mothers_day(context):
    context.driver.find_element_by_xpath(constants.Mothersday).click()


@when(u'i click on jewelleryand wathches')
def jewellery_and_watches(context):
    context.driver.find_element_by_xpath(constants.Jewelleryandwatches).click()


@when(u'i click on bracelet')
def click_0n_bracelet(context):
    context.driver.find_element_by_xpath(constants.Bracelet).click()


@when(u'i click on style')
def click_on_style(context):
    context.driver.find_element_by_xpath(constants.Style).click()
    time.sleep(5)


@then(u'i click on buystyle')
def click_0n_buystyle(context):
    time.sleep(10)
    context.driver.find_element_by_id(constants.Buystyle).click()

