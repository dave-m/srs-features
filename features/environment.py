"""Behave Environment"""
from selenium import webdriver


def after_scenario(context, scenario):
    if hasattr(context, 'browser'):
        context.browser.quit()



