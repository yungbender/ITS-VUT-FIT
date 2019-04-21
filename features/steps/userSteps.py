from behave import *

@given("User is not logged in")
def step_impl(context):
    context.driver.get("http://mys01.fit.vutbr.cz:8057/")

@given("is on registration page")
def step_impl(context):
    dropdownMenu = context.driver.find_element_by_xpath("//span[contains(.,'My Account')]")
    dropdownMenu.click() 
    registerButton = context.driver.find_element_by_xpath("//a[contains(text(),'Register')]")
    registerButton.click()

@when("User does not fill out requisite box")
def step_impl(context):
    nameBar = context.driver.find_element_by_xpath("//input[@id='input-firstname']")
    nameBar.send_keys("Meno")
    
@when("confirms privacy policy")
def step_impl(context):
    privacyPolicy = context.driver.find_element_by_xpath("//form/div/div/input")
    privacyPolicy.click()

@when("continues to registrate")
def step_impl(context):
    registrateButton = context.driver.find_element_by_xpath("//div/input[2]")
    registrateButton.click()

@then("Registration will not pass")
def step_impl(context):
    failedLastName = context.driver.find_element_by_class_name("account-register")

@then("Registration is OK")
def step_impl(context):
    successPage = context.driver.find_element_by_class_name("account-success")


@when("User does fill out requisite box")
def step_impl(context):
    nameBar = context.driver.find_element_by_xpath("//fieldset[@id='account']/div[2]/div/input")
    nameBar.send_keys("Name")

    surnameBar = context.driver.find_element_by_xpath("//fieldset[@id='account']/div[3]/div/input")
    surnameBar.send_keys("Surname")

    emailBar = context.driver.find_element_by_xpath("//fieldset[@id='account']/div[4]/div/input")
    emailBar.send_keys("menopriezvisko@menopriezvisko.menopriezvisko")

    phoneBar = context.driver.find_element_by_xpath("//fieldset[@id='account']/div[5]/div/input")
    phoneBar.send_keys("123456789")

    addressBar = context.driver.find_element_by_xpath("//fieldset[@id='address']/div[2]/div/input")
    addressBar.send_keys("Adress")

    cityBar = context.driver.find_element_by_xpath("//fieldset[@id='address']/div[4]/div/input")
    cityBar.send_keys("City")

    postcodeBar = context.driver.find_element_by_xpath("//fieldset[@id='address']/div[5]/div/input")
    postcodeBar.send_keys("12345")

    provinceBar = context.driver.find_element_by_xpath("//fieldset[@id='address']/div[7]/div/select")
    provinceBar.click()
    provinceChoice = context.driver.find_element_by_xpath("//div[7]/div/select/option[2]")
    provinceChoice.click()

    passwordBar = context.driver.find_element_by_xpath("//div[@id='content']/form/fieldset[3]/div/div/input")
    passwordBar.send_keys("123456789")

    passwordConfirmBar = context.driver.find_element_by_xpath("//div[@id='content']/form/fieldset[3]/div[2]/div/input")
    passwordConfirmBar.send_keys("123456789")

@when("User fills out correct informations")
def step_impl(context):
    nameBar = context.driver.find_element_by_xpath("//fieldset[@id='account']/div[2]/div/input")
    nameBar.send_keys("Miro")

    surnameBar = context.driver.find_element_by_xpath("//fieldset[@id='account']/div[3]/div/input")
    surnameBar.send_keys("Vančo")

    emailBar = context.driver.find_element_by_xpath("//fieldset[@id='account']/div[4]/div/input")
    emailBar.send_keys("mirovanco@mirovanco.sk")

    phoneBar = context.driver.find_element_by_xpath("//fieldset[@id='account']/div[5]/div/input")
    phoneBar.send_keys("123456789")

    addressBar = context.driver.find_element_by_xpath("//fieldset[@id='address']/div[2]/div/input")
    addressBar.send_keys("Manesky 2")

    cityBar = context.driver.find_element_by_xpath("//fieldset[@id='address']/div[4]/div/input")
    cityBar.send_keys("Brno")

    postcodeBar = context.driver.find_element_by_xpath("//fieldset[@id='address']/div[5]/div/input")
    postcodeBar.send_keys("61200")

    provinceBar = context.driver.find_element_by_xpath("//fieldset[@id='address']/div[7]/div/select")
    provinceBar.click()
    provinceChoice = context.driver.find_element_by_xpath("//div[7]/div/select/option[2]")
    provinceChoice.click()

    passwordBar = context.driver.find_element_by_xpath("//div[@id='content']/form/fieldset[3]/div/div/input")
    passwordBar.send_keys("123456789")

    passwordConfirmBar = context.driver.find_element_by_xpath("//div[@id='content']/form/fieldset[3]/div[2]/div/input")
    passwordConfirmBar.send_keys("123456789")

@given("is on login page")
def step_impl(context):
    dropdownMenu = context.driver.find_element_by_xpath("//span[contains(.,'My Account')]")
    dropdownMenu.click() 
    loginButton = context.driver.find_element_by_xpath("//a[contains(text(),'Login')]")
    loginButton.click()

@when("User fills out incorrect login creditials")
def step_impl(context):
    emailBar = context.driver.find_element_by_xpath("//div[@id='content']/div/div[2]/div/form/div/input")
    emailBar.send_keys("wrongemail@wrongemail.com")

    passwordBar = context.driver.find_element_by_xpath("//input[@id='input-password']")
    passwordBar.send_keys("123456798")

@when("continues to login")
def step_impl(context):
    loginButton = context.driver.find_element_by_xpath("//div[@id='content']/div/div[2]/div/form/input")
    loginButton.click()

@then("User is not logged in an any account")
def step_impl(context):
    failedLoginPage = context.driver.find_element_by_class_name("account-login")

@when("User fills out correct login creditials")
def step_impl(context):
    emailBar = context.driver.find_element_by_xpath("//div[@id='content']/div/div[2]/div/form/div/input")
    emailBar.send_keys("mirovanco@mirovanco.sk")

    passwordBar = context.driver.find_element_by_xpath("//input[@id='input-password']")
    passwordBar.send_keys("123456789")

@then("User is logged in in his account")
def step_impl(context):
    successLoginPage = context.driver.find_element_by_class_name("account-account")

@given("User is logged in")
def step_impl(context):
    # connect to site
    context.driver.get("http://mys01.fit.vutbr.cz:8057/")

    # get to login page
    dropdownMenu = context.driver.find_element_by_xpath("//span[contains(.,'My Account')]")
    dropdownMenu.click() 
    loginButton = context.driver.find_element_by_xpath("//a[contains(text(),'Login')]")
    loginButton.click()

    emailBar = context.driver.find_element_by_xpath("//div[@id='content']/div/div[2]/div/form/div/input")
    emailBar.send_keys("mirovanco@mirovanco.sk")

    passwordBar = context.driver.find_element_by_xpath("//input[@id='input-password']")
    passwordBar.send_keys("123456789")

    loginButton = context.driver.find_element_by_xpath("//div[@id='content']/div/div[2]/div/form/input")
    loginButton.click()

@given("is on eshop page")
def step_impl(context):
    context.driver.get("http://mys01.fit.vutbr.cz:8057/")

@when("User logsout")
def step_impl(context):
    dropdownMenu = context.driver.find_element_by_xpath("//div[@id='top-links']/ul/li[2]/a/span")
    dropdownMenu.click()
    logoutButton = context.driver.find_element_by_xpath("//a[contains(text(),'Logout')]")
    logoutButton.click()

@then("User is logged out of his account")
def step_impl(context):
    successLogoutPage = context.driver.find_element_by_class_name("account-logout")

@given("is on MyAccount page")
def step_impl(context):
    pass

@when("User gets to the change password page")
def step_impl(context):
    passwordChangeButton = context.driver.find_element_by_xpath("//a[contains(text(),'Change your password')]")
    passwordChangeButton.click()

@when("fills in wrong password")
def step_impl(context):
    passwordBar = context.driver.find_element_by_xpath("//input[@id='input-password']")
    passwordBar.send_keys("123")

    passwordConfirmBar = context.driver.find_element_by_xpath("//input[@id='input-confirm']")
    passwordConfirmBar.send_keys("123")

@when("fills in new password creditials")
def step_impl(context):
    passwordBar = context.driver.find_element_by_xpath("//input[@id='input-password']")
    passwordBar.send_keys("1234567890")

    passwordConfirmBar = context.driver.find_element_by_xpath("//input[@id='input-confirm']")
    passwordConfirmBar.send_keys("1234567890")

@when("continues to change password")
def step_impl(context):
    confirmButton = context.driver.find_element_by_xpath("//input[@value='Continue']")
    confirmButton.click()

@then("User password has changed")
def step_impl(context):
    successPasswordChangePage = context.driver.find_element_by_class_name("account-account")

@then("User password has not changed")
def step_impl(context):
    failedPasswordChangePage = context.driver.find_element_by_class_name("account-password")