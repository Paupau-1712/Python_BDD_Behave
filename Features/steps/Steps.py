from behave import *
from Methods import *
from selenium import webdriver


@given(u'Launch Chrome browser')
def step_impl(context):
    launch_browser()


@when(u'Type on search')
def step_impl(context):
    print("First try")


@then(u'Search is show')
def step_impl(context):
    print("First try")


@then(u'Close browser')
def step_impl(context):
    print("First try")
