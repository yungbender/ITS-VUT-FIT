from selenium import webdriver
from behave import fixture
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def before_scenario(context, feature):
    context.driver = webdriver.Remote(command_executor="http://mys01.fit.vutbr.cz:4444/wd/hub", desired_capabilities=DesiredCapabilities.FIREFOX)

def after_scenario(context, feature):
    context.driver.quit()