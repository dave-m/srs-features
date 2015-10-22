"""Behave Environment"""
from selenium import webdriver


def after_scenario(context, scenario):
    if hasattr(context, 'browser'):
        pass
        #context.browser.quit()



