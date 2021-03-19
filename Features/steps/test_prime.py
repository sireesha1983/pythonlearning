from behave import when, then

import constants


@when(u'i click on prime')
def click_on_prime(context):
    context.driver.find_element_by_xpath(constants.ClickOnPrime).click()


@when(u'i click on entertainment')
def click_on_entertainment(context):
    context.driver.find_element_by_xpath(constants.ClickOnEntertainment).click()


@when(u'i click on amazon music unlimited')
def click_on_amazon_music_unlimited(context):
    a = context.driver.window_handles[0]
    context.driver.switch_to.window(a)
    # a = context.driver.current_window_handle
    print("the vaue is"+a)
    # context.driver.switch_to.window(a)
    context.driver.find_element_by_css_selector(constants.ClickOnAmazonmusicUnlimited).click()



@then(u'i click on get started')
def click_on_get_started(context):
    a = context.driver.window_handles[1]
    # # a = context.driver.current_window_handle
    context.driver.switch_to.window(a)
    context.driver.find_element_by_css_selector(constants.ClickOnGetStarted).click()

