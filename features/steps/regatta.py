
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait


@given(u'I am viewing all Regattas')
@when(u'I view all Regattas')
def selenium_view_all_regattas(context):
    link = context.browser.find_element_by_xpath("//a[@href='#/regattas']")
    link.click()


@then(u'I see there are {num_regattas:d} Regattas')
def selenium_see_regattas(context, num_regattas):
    regattas = context.browser.find_elements_by_xpath("//section//h4[text()='Current Regattas']/..//h5")
    # Check number
    assert num_regattas == len(regattas), "Found only {} Regattas!".format(len(regattas))
    # Check rows
    found_regattas = [r.text for r in regattas]
    for row in context.table:
        assert row['Regatta Name'] in found_regattas, "{} not found in Regattas!".format(row['Regatta Name'])


@when(u'I add a new Regatta with the name "{new_regatta_name}"')
def selenium_add_new_regatta(context, new_regatta_name):
    """Enter in a new Regatta"""
    text_entry = context.browser.find_element_by_id("newRegatta")
    text_entry.send_keys(new_regatta_name)

    new_regatta_button = context.browser.find_element_by_xpath("//button/i[text()='add']/..")
    new_regatta_button.click()

    # Wait for it to appear, but only accept 1 second of wait
    WebDriverWait(context.browser, 1).until(
        lambda x: x.find_element_by_xpath("//h5[text()='{}']".format(new_regatta_name))
    )