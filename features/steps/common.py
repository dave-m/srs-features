"""Common steps such as opening the website"""
from behave import given
from selenium import webdriver


@given(u'I open a webbrowser')
def selenium_open_browser(context):
    """Open a selenium browser"""
    context.browser = webdriver.Chrome('/usr/lib/chromium/chromedriver')


@given(u'I am on the Sail Race Scoring website')
def selenium_open_srs_website(context):
    """Use the context browser to open the supplied page"""
    context.browser.get("http://192.168.1.109:3449/")