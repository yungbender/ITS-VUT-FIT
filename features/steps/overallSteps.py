from behave import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

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

@given("user has some item in the cart")
def step_impl(context):
    context.driver.get("http://mys01.fit.vutbr.cz:8057/")

    addToCartButton = context.driver.find_element_by_xpath("//div[@id='content']/div[2]/div[2]/div/div[3]/button/i")
    addToCartButton.click()

@given("user is on the cart page")
def step_impl(context):
    cartButton = context.driver.find_element_by_xpath("(//button[@type='button'])[5]")
    cartButton.click()

    goToCartButton = context.driver.find_element_by_xpath("//div[@id='cart']/ul/li[2]/div/p/a/strong")
    goToCartButton.click()

@when("User checks out")
def step_impl(context):
    checkoutButton = context.driver.find_element_by_xpath("//div[@id='content']/div[3]/div[2]/a")
    checkoutButton.click()

@when("fills out correct info")
def step_impl(context):
    # wait for js to make animation and show button
    addressContinueButton = WebDriverWait(context.driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='collapse-payment-address']/div/form/div[5]/div/input")))
    addressContinueButton.click()

     # wait for js to make animation and show button

    shippingAddressContinueButton = WebDriverWait(context.driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='collapse-shipping-address']/div/form/div[5]/div/input")))
    shippingAddressContinueButton.click()

     # wait for js to make animation and show button

    shippingMethodContinueButton = WebDriverWait(context.driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='collapse-shipping-method']/div/div[2]/div/input")))
    shippingMethodContinueButton.click()

    # wait for js to make animation and show button

    agreeButton = WebDriverWait(context.driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='collapse-payment-method']/div/div[2]/div/input")))
    agreeButton.click()

     # wait for js to make animation and show button
    paymentContinueButton = WebDriverWait(context.driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='collapse-payment-method']/div/div[2]/div/input[2]")))
    paymentContinueButton.click()

@when("confirms order")
def step_impl(context):
    WebDriverWait(context.driver, 2)

    orderButton = context.driver.find_element_by_xpath("//input[@id='button-confirm']")
    orderButton.click()

@then("Order is completed")
def step_impl(context):
    context.driver.find_element_by_class_name("checkout-success")

@then("registered in database")
def step_impl(context):
    myAccountButton = context.driver.find_element_by_xpath("//div[@id='top-links']/ul/li[2]/a/i")
    myAccountButton.click()

    orderHistory = context.driver.find_element_by_xpath("//a[contains(text(),'Order History')]")
    orderHistory.click()

    context.driver.find_element_by_class_name("table-responsive")