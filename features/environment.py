"""Behave Environment"""
from selenium import webdriver

DEBUG_ON_ERROR = False


def setup_debug_on_error(userdata):
    global DEBUG_ON_ERROR
    DEBUG_ON_ERROR = userdata.getbool("DEBUG_ON_ERROR")


def debug_step(step):
    #: Debug on errors, usage:
    #: behave -D DEBUG_ON_ERROR=yes
    if DEBUG_ON_ERROR and step.status == "failed":
        import pdb
        pdb.set_trace()


def before_all(context):
    setup_debug_on_error(context.config.userdata)

    
def after_scenario(context, scenario):
    if hasattr(context, 'browser'):
        context.browser.quit()


def after_step(context, step):
    debug_step(step)

