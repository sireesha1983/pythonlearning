from behave import when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pages.deals import BestSeller, Newreases, Moversandshakers, Mostwishedfor, Giftideas, Firstimage, Addingcart, \
    Proceedtocheckout


@when(u'i click on bestsellers')
def click_on_bestseller(context):
    besseller=BestSeller()
    besseller.click()


@when(u'i click on newreases')
def click_on_newreases(context):
    releases=Newreases()
    releases.click()


@when(u'i click on movers and shakers')
def click_on_movers_and_shakers(context):
    movers=Moversandshakers()
    movers.click()


@when(u'i click on most wished for')
def click_on_most_wished_for(context):
    wished=Mostwishedfor()
    wished.click()



@when(u'i click on gift ideas')
def click_on_gift_ideas(context):
    ideas=Giftideas()
    ideas.click()


@when(u'i click on first image')
def click_on_first_image(context):
    first=Firstimage()
    first.click()


@when(u'i click on adding cart button')
def click_on_adding_cart_button(context):
    cart=Addingcart()
    cart.click()


@then(u'i click on proceed to checkout button')
def click_on_proceed_to_check_out_button(context):
    element = WebDriverWait(context.driver, 50).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#hlb-ptc-btn-native")))
    checkout=Proceedtocheckout()
    checkout.click()


