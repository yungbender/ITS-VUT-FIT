from selenium import webdriver
from behave import fixture
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def before_scenario(context, feature):
    # Connect to hub
    context.driver = webdriver.Remote(command_executor="http://mys01.fit.vutbr.cz:4444/wd/hub", desired_capabilities=DesiredCapabilities.FIREFOX)
    # Dom timeout
    context.driver.set_page_load_timeout(15)
    # Handling unexpected alert (Make an order test)
    webdriver.DesiredCapabilities.FIREFOX["unexpectedAlertBehaviour"] = "accept"

def after_scenario(context, feature):
    context.driver.quit()