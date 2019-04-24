from behave import *

@when("User clicks the item category")
def step_impl(context):
    componentsDropdown = context.driver.find_element_by_xpath("//a[contains(text(),'Components')]")
    componentsDropdown.click()

    monitorsSection = context.driver.find_element_by_xpath("//a[contains(text(),'Monitors (2)')]")
    monitorsSection.click()

@then("List of items shows up for order")
def step_impl(context):
    monitors = context.driver.find_elements_by_class_name("product-thumb")
    # there are 2 monitors in the section
    assert len(monitors) == 2, "There are not 2 monitors - Test Failed"