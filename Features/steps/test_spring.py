from behave import when, then


@when(u'i click on springclean withlowprices')
def step_impl(context):
    context.driver.find_element_by_xpath("//*[@id='swm-link']").click()



@when(u'i click on gardening')
def step_impl(context):
    context.driver.find_element_by_css_selector("div > div:nth-child(3) > div:nth-child(1) > div > div > a > img").click()



@when(u'i click on turtle planter')
def step_impl(context):
    context.driver.find_element_by_xpath("//*[@id='gcx-gf-section-0']/div/section/div[6]/figure/div/a/div/div/img").click()



@when(u'i click on large')
def step_impl(context):
    context.driver.find_element_by_xpath("//*[@id='a-autoid-24-announce']/div/div[1]/span").click()


@then(u'i click on buyturtle')
def step_impl(context):
    next = context.driver.find_element_by_xpath("//*[@id='buy-now-button']")
    context.driver.execute_script("arguments[0].click()", next)
    # context.driver.find_element_by_xpath("//*[@id='buy-now-button']").click()