import time

from behave import when, then


@when(u'i click on primevideo')
def step_impl(context):
    context.driver.find_element_by_xpath("//*[@id='nav-xshop']/a[1]").click()




@when(u'i click on categories')
def step_impl(context):
    context.driver.find_element_by_xpath("//*[@id='a-page']/div[2]/div/div[1]/ul[1]/li[4]/a").click()





@when(u'i click on tv')
def step_impl(context):
    context.driver.find_element_by_xpath("//*[@id='a-page']/div[2]/div/div[1]/ul[1]/li[4]/ul/div/div[1]/div/ul/li[4]/a").click()
    time.sleep(5)

@when(u'i click on firstvideo')
def step_impl(context):
    context.driver.find_element_by_xpath("//*[@id='aiv-cl-main-middle']/div/div[3]/div/div[1]/div/div[2]/div/div/ul/li[1]/div/div/div").click()
    time.sleep(10)

@then(u'i click on seasons')
def click_on_seasons(context):
    context.driver.find_element_by_xpath("//*[@id='a-page']/div[4]/div[2]/div/div/div[2]/div[3]/div/div[1]/div/label").click()
    time.sleep(3)
    a=context.driver.find_element_by_tag_name("ul")
    items = a.find_elements_by_tag_name("li")
    print(len(items))
    for item in range(1,len(items)):
        context.driver.find_element_by_xpath("//*[@id='a-page']/div[4]/div[2]/div/div/div[2]/div[3]/div/div[1]/div/ul/li["+str(item)+"]/a/span[1]").click()
        print(context.driver.find_element_by_xpath(
            "//*[@id='a-page']/div[4]/div[2]/div/div/div[2]/div[3]/div/div[1]/div/ul/li[" + str(item) + "]/a/span[1]").getText())

        time.sleep(3)
        try:
         context.driver.find_element_by_xpath(
                "//*[@id='a-page']/div[4]/div[2]/div/div/div[2]/div[3]/div/div[1]/div/label").click()

         time.sleep(3)
        except:
            context.driver.find_element_by_xpath(
                "//*[@id='a-page']/div[4]/div[2]/div/div/div[2]/div[2]/div/div[1]/div/label").click()
            time.sleep(3)






