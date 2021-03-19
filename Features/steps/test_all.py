from behave import when, then
import constants


@when(u'i click on all')
def step_impl(context):
    context.driver.find_element_by_xpath(constants.ClickOnAll).click()


@when(u'i click on appstore for android')
def step_impl(context):
    context.driver.find_element_by_xpath(constants.ClickOnAppstoreAndriod).click()


@when(u'i click on all apps and games')
def step_impl(context):
    context.driver.find_element_by_css_selector(constants.ClickOnAllAppsAndGames).click()


@when(u'i click on last 30 days')
def step_impl(context):
    context.driver.find_element_by_xpath(constants.ClickOnLast30Days).click()


@when(u'i click on first image app')
def step_impl(context):
    context.driver.find_element_by_xpath(constants.ClickOnFirstImageApp).click()



@then(u'i click on continue')
def step_impl(context):
    context.driver.find_element_by_xpath(constants.ClickOnContinue).click()

