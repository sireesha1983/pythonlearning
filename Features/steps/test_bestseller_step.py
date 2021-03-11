from behave import when, then


@when(u'i click on bestsellers')
def step_impl(context):
    context.driver.find_element_by_xpath("//*[@id='nav-xshop']/a[6]").click()


@when(u'i click on newreases')
def step_impl(context):
    context.driver.find_element_by_xpath("//*[@id='zg_tabs']/ul/li[2]/div/a").click()


@when(u'i click on movers and shakers')
def step_impl(context):
    context.driver.find_element_by_xpath("//*[@id='zg_tabs']/ul/li[3]/div/a").click()


@when(u'i click on most wished for')
def step_impl(context):
    context.driver.find_element_by_xpath("//*[@id='zg_tabs']/ul/li[4]/div/a").click()


@when(u'i click on gift ideas')
def step_impl(context):
    context.driver.find_element_by_xpath("//*[@id='zg_tabs']/ul/li[5]/div/a").click()


@when(u'i click on first image')
def step_impl(context):
    context.driver.find_element_by_xpath("//*[@id='zg_left_col1']/div[1]/div[2]/div/div[2]/a/div[1]/img").click()

@when(u'i click on adding cart button')
def step_impl(context):
    context.driver.find_element_by_id("add-to-cart-button").click()
    print("The peer review")


@then(u'i click on proceed to checkout button')
def step_impl(context):
    context.driver.find_element_by_xpath("//*[@id='attach-sidesheet-checkout-button']/span/input").click()
    print("chceking git")

