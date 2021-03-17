import time

from behave import when, then


@when(u'i click on prime')
def step_impl(context):
    context.driver.find_element_by_xpath("//*[@id='nav-link-prime']/span[1]").click()



@when(u'i click on entertainment')
def step_impl(context):
    context.driver.find_element_by_xpath("//*[@id='prime-benefit-cards']/div[2]/div[1]/div").click()
    time.sleep(10)


@when(u'i click on amazon music unlimited')
def step_impl(context):
    time.sleep(10)
    a = context.driver.window_handles[0]
    context.driver.switch_to.window(a)
    # a = context.driver.current_window_handle
    print("the vaue is"+a)
    # context.driver.switch_to.window(a)
    context.driver.find_element_by_css_selector("#anonCarousel2 > ol > li:nth-child(5) > div > a > div.a-row.card-image > img").click()
    time.sleep(4)


@then(u'i click on get started')
def step_impl(context):
    time.sleep(10)
    context.driver.find_element_by_xpath("//*[@id='dmusicLandingButton']/span/a").click()
    time.sleep(4)
