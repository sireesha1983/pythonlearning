from behave import when, then

from pythonlearning import constants


@when(u'i click on buyagain')
def click_on_buy_again(context):
    context.driver.find_element_by_xpath(constants.BuyAgain).click()


@when(u'i click on third item')
def click_on_third_item(context):
    context.driver.find_element_by_xpath(constants.ThirdImage).click()


@when(u'i click on save for later')
def click_on_save_for_later(context):
    context.driver.find_element_by_xpath(constants.SaveForLater).click()


@then(u'i click on move to cart')
def click_on_move_on_cart(context):
    context.driver.find_element_by_xpath(constants.MoveToCart).click()
