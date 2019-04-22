from behave import *

@given("is on admin page")
def step_impl(context):
    context.driver.get("http://mys01.fit.vutbr.cz:8057/admin/")
    context.driver.find_elements_by_xpath("//*[contains(text(), 'Please enter your login details.')]")

@when("User fills in correct admin creditials")
def step_impl(context):
    usernameBar = context.driver.find_element_by_xpath("//input[@id='input-username']")
    usernameBar.send_keys("admin")

    passwordBar = context.driver.find_element_by_xpath("//input[@id='input-password']")
    passwordBar.send_keys("admin")

@when("logs in")
def step_impl(context):
    loginButton = context.driver.find_element_by_xpath("//button[@type='submit']")
    loginButton.click()

@then("User is logged in as Admin on Admin page")
def step_impl(context):
    context.driver.find_element_by_xpath("//*[contains(text(), 'Dashboard')]")
    context.driver.find_element_by_xpath("//*[contains(text(), 'Logout')]")

@given("User is logged in as Admin")
def step_impl(context):
    context.driver.get("http://mys01.fit.vutbr.cz:8057/admin/")

    usernameBar = context.driver.find_element_by_xpath("//input[@id='input-username']")
    usernameBar.send_keys("admin")

    passwordBar = context.driver.find_element_by_xpath("//input[@id='input-password']")
    passwordBar.send_keys("admin")

    loginButton = context.driver.find_element_by_xpath("//button[@type='submit']")
    loginButton.click()

@when("User logs out")
def step_impl(context):
    logoutButton = context.driver.find_element_by_xpath("//header[@id='header']/ul/li[4]/a/i")
    logoutButton.click()

@then("User is logged out")
def step_impl(context):
    context.driver.find_element_by_xpath("//*[contains(text(), 'Please enter your login details.')]")