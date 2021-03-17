from behave import when, then

import constants


@when(u'i click on todays deals')
def click_on_todaydeals(context):
    context.driver.find_element_by_xpath(constants.TodayDeals).click()


@when(u'i click on first video')
def click_on_firstvideo(context):
    context.driver.find_element_by_xpath(constants.Dealimage).click()
    context.driver.find_element_by_xpath(constants.FirstDealImage).click()


@when(u'i click on add to cart')
def click_on_addtocart(context):
    a= context.driver.window_handles[0]
    context.driver.switch_to.window(a)
    context.driver.find_element_by_id(constants.AddToCart).click()


@then(u'i click on proceedcheckout')
def click_on_proceedtocheckout(context):
    context.driver.find_element_by_id(constants.ProceedToCheckout).click()



