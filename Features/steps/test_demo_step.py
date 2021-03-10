import time

from behave import given, then, when
from selenium import webdriver


@given(u'I login with url')
def step_impl(context):
    print()
   # context.driver= webdriver.Chrome(executable_path=r".\Drivers\chromedriver.exe")
   # context.driver.get("https://www.amazon.com")
   # context.driver.maximize_window()
   # time.sleep(3)

@when(u'I click on sign in button')
def step_impl(context):
    context.driver.find_element_by_xpath("//*[@id='nav-signin-tooltip']/a/span").click()
    time.sleep(3)


@when(u'I click on create amazon button')
def step_impl(context):
    context.driver.find_element_by_id("createAccountSubmit").click()
    time.sleep(3)


@when(u'i enter username')
def step_impl(context):
    context.driver.find_element_by_id("ap_customer_name").send_keys("mahan")
    time.sleep(3)


@when(u'i enter e-mail')
def step_impl(context):
    context.driver.find_element_by_id("ap_email").send_keys("saim08621709@gmail.com")
    time.sleep(3)


@when(u'i enter pwd')
def step_impl(context):
    context.driver.find_element_by_id("ap_password").send_keys("password#1")
    time.sleep(3)


@when(u'i enter re enter pwd')
def step_impl(context):
    context.driver.find_element_by_id("ap_password_check").send_keys("password#1")
    time.sleep(3)


@then(u'I click on create your amazon account button')
def step_impl(context):
    context.driver.find_element_by_id("continue").click()
    time.sleep(3)

@when(u'i click on continue button')
def step_impl(context):
    context.driver.find_element_by_id("continue").click()
    time.sleep(3)

@when(u'i click on password')
def step_impl(context):
    context.driver.find_element_by_id("ap_password").send_keys("password#1")
    time.sleep(5)

@when(u'I click on sign_in button')
@then(u'I click on sign_in button')
def step_impl(context):
    context.driver.find_element_by_id("signInSubmit").click()
    time.sleep(50)












