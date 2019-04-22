from behave import *

@given("User has opened browser")
def step_impl(context):
    pass

@given("is connected to the internet")
def step_impl(context):
    context.driver.get("http://amiconnectedtotheinternet.com/")
    context.driver.find_element_by_xpath("//*[contains(text(), 'Yes')]")

@when("User visits the eshop Page")
def step_impl(context):
    context.driver.get("http://mys01.fit.vutbr.cz:8057/")

@then("Website loades without a problem")
def step_impl(context):
    context.driver.find_element_by_class_name("common-home")

@then("shows whole Website")
def step_impl(context):
    context.driver.save_screenshot("whole_website.png")

@given("User is on eshop instance")
def step_impl(context):
    context.driver.get("http://mys01.fit.vutbr.cz:8057/")

@when("User changes the currency to another")
def step_impl(context):
    currencyButton = context.driver.find_element_by_xpath("//span[contains(.,'Currency')]")
    currencyButton.click()

    euroButton = context.driver.find_element_by_xpath("//button[@name='EUR']")
    euroButton.click()

@then("Prices are correctly changed to the chosen currency")
def step_impl(context):
    # search the prices translated to euro
    context.driver.find_element_by_xpath("//*[contains(text(), '556.79€')]")
    context.driver.find_element_by_xpath("//*[contains(text(), '113.95€')]")
    context.driver.find_element_by_xpath("//*[contains(text(), '101.74€')]")
    context.driver.find_element_by_xpath("//*[contains(text(), '90.64€')]")