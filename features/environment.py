"""Behave Environment"""
from selenium import webdriver

def after_tag(context, tag):
    if hasattr(context, 'browser'):
        context.browser.quit()


