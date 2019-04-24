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
    logoutButton = context.driver.find_element_by_xpath("//header[@id='header']/ul/li[4]/a/span")
    logoutButton.click()

@then("User is logged out")
def step_impl(context):
    context.driver.find_element_by_xpath("//*[contains(text(), 'Please enter your login details.')]")

@given("There is atleast 1 registered customer")
def step_impl(context):
    # try to register subject
    try:
        context.execute_steps("given User is not logged in")
        context.execute_steps("given is on registration page")
        context.execute_steps("when User fills out correct informations")
        context.execute_steps("when confirms privacy policy")
        context.execute_steps("when continues to registrate")
    finally:
        pass

@when("Admin clicks Customers")
def step_impl(context):
    customersButton = context.driver.find_element_by_xpath("//div[@id='content']/div[2]/div/div[3]/div/div[3]/a")
    customersButton.click()

@then("All registered customers will show up")
def step_impl(context):
    # Find the registered subject
    context.driver.find_element_by_xpath("//*[contains(text(), 'Miro Vančo')]")
    context.driver.find_element_by_xpath("//*[contains(text(), 'mirovanco@mirovanco.sk')]")

@given("There is atleast 1 order placed")
def step_impl(context):
    # order something
    context.execute_steps("given User is logged in")
    context.execute_steps("given user has some item in the cart")
    context.execute_steps("given user is on the cart page")
    context.execute_steps("when User checks out")
    context.execute_steps("when fills out correct info")
    context.execute_steps("when confirms order")
    context.execute_steps("then order is completed")

@when("Admin clicks orders")
def step_impl(context):
    ordersButton = context.driver.find_element_by_xpath("//a[contains(text(),'View more...')]")
    ordersButton.click()

@then("All placed orders will show up")
def step_impl(context):
    context.driver.find_element_by_xpath("//*[contains(text(), 'Miro Vančo')]")
    context.driver.find_element_by_xpath("//*[contains(text(), 'Pending')]")
