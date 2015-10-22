"""Common steps such as opening the website"""
from behave import given
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


@given(u'I open a webbrowser')
def selenium_open_browser(context):
    """Open a selenium browser"""
    context.browser = webdriver.Chrome('/usr/lib/chromium/chromedriver')
    context.browser.implicitly_wait(2)


@given(u'I am on the Sail Race Scoring website')
@given(u'I log in to the Sail Race Scoring website')
def selenium_open_srs_website(context):
    """Use the context browser to open the supplied page"""
    context.browser.get("http://localhost:3449/")
    # Wait for the js to catch up
    WebDriverWait(context.browser, 1).until(
        lambda x: x.find_element_by_xpath("//span[text()='Sail Regatta Scoring']")
    )

@when(u'I click on the "{button_name}" button')
def selenium_click_button(context, button_name):
    """Click on the defined button"""
    WebDriverWait(context.browser, 1).until(
        lambda x: x.find_element_by_xpath("//button/span[text()='{0}']".format(button_name))
    )
    context.browser.find_element_by_xpath("//button/span[text()='{0}']/..".format(button_name)).click()
