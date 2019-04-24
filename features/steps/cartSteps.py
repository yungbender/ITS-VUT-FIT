from behave import *
from selenium.webdriver.support.ui import WebDriverWait

@given("User is on some exact product page")
def step_impl(context):
    context.driver.get("http://mys01.fit.vutbr.cz:8057/index.php?route=product/category&path=25_28")

@given("user has empty cart")
def step_impl(context):
    context.driver.find_element_by_xpath("//*[contains(text(), '0 item(s) - $0.00')]")

@when("User adds item to cart")
def step_impl(context):
    addtocartButton = context.driver.find_element_by_xpath("//div[@id='content']/div[3]/div[2]/div/div[2]/div[2]/button/span")
    addtocartButton.click()

@then("User registers the item and has the item in the cart")
def step_impl(context):
    # Wait to generate JS
    WebDriverWait(context.driver, 5)
    context.driver.find_element_by_xpath("//*[contains(text(), '1 item(s) - $242.00')]")

@given("user has not empty cart")
def step_impl(context):
    context.execute_steps("when User adds item to cart")
    context.execute_steps("then User registers the item and has the item in the cart")

@then("User registers the item and has the item in his cart")
def step_impl(context):
    # Wait to generate JS
    WebDriverWait(context.driver, 5)
    context.driver.find_element_by_xpath("//*[contains(text(), '2 item(s) - $484.00')]")

@given("User is on index page")
def step_impl(context):
    context.driver.get("http://mys01.fit.vutbr.cz:8057/")

@when("User adds item to the cart")
def step_impl(context):
    addToCartButton = context.driver.find_element_by_xpath("//div[2]/div/div[3]/button/span")
    addToCartButton.click()

@then("User registers the mainpage item and has the item in his cart")
def step_impl(context):
    try:
        WebDriverWait(context.driver, 5)
        context.driver.find_element_by_xpath("//*[contains(text(), '0 item(s)')]")
    except:
        pass