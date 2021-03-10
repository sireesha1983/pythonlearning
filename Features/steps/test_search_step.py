import time

from behave import then, given, when
from selenium import webdriver


@then(u'i enter "{value}" in search button')
def step_impl(context, value):
     context.driver.find_element_by_id("twotabsearchtextbox").send_keys(value)
     time.sleep(3)


@when(u'i enter "{value}" in search button')
def step_impl(context,value):
     context.driver.find_element_by_id("twotabsearchtextbox").send_keys(value)
     time.sleep(3)


@when(u'i click on search button')
def step_impl(context):
     context.driver.find_element_by_id("nav-search-submit-button").click()
     time.sleep(5)


@when(u'i click on awardwinner')
def step_impl(context):
     context.driver.find_element_by_xpath("//*[@id='a-page']/div[2]/div[2]/div[2]/div[1]/div[1]/ul[1]/li[1]/a").click()
     time.sleep(5)



@when(u'i click on firstbook')
def step_impl(context):
     context.driver.find_element_by_xpath("//*[@id='acs-product-block-0']/div[1]/a/img").click()



@when(u'i click on add to cart button')
def step_impl(context):
     time.sleep(10)
     context.driver.find_element_by_xpath("//*[@id='add-to-cart-button']").click()
     time.sleep(10)




@when(u'i click on cart')
def step_impl(context):
     context.driver.find_element_by_xpath("//*[@id='hlb-view-cart-announce']").click()
     time.sleep(10)


@then(u'i click on delete button')
def step_impl(context):
     context.driver.find_element_by_xpath("//div[4]/div/div[1]/div/div/div[2]/div[1]/span[2]").click()
     time.sleep(10)