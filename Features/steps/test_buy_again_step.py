import time

from behave import when, then

@when(u'i click on buyagain')
def step_impl(context):
    context.driver.find_element_by_xpath("//*[@id='nav-xshop']/a[9]").click()



@when(u'i click on third item')
def step_impl(context):
    context.driver.find_element_by_xpath("//*[@id='anonCarousel1']/ol/li[3]/div/div[1]/a/div/img").click()



@when(u'i click on save for later')
def step_impl(context):
    context.driver.find_element_by_xpath("(//div[4]/div/div[1]/div/div/div[2]/div[1]/span[3]/span/input)[1]").click()



@then(u'i click on move to cart')
def step_impl(context):
    context.driver.find_element_by_xpath("//input[contains(@value,'Move to cart')]").click()
