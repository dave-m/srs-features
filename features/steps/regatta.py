
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait

def _wait_for_all_regattas(context):
    WebDriverWait(context.browser, 1).until(
        lambda x: x.find_element_by_xpath("//h4[text()='Regattas']")
    )



def _create_regatta(context, regatta):
    # Click the "ADD REGATTAS" button
    new_regatta_button = context.browser.find_element_by_xpath(
        "//button/span[text()='Add Regatta']/..")
    new_regatta_button.click()

    # Wait for the js to catch up
    WebDriverWait(context.browser, 1).until(
        lambda x: x.find_element_by_xpath("//h6[text()='Create a new Regatta']")
    )

    # Enter the Regatta Name
    text_entry = context.browser.find_element_by_id("newRegatta")
    text_entry.send_keys(regatta['Regatta Name'])
    # Click the ADD button
    context.browser.find_element_by_xpath("//button/span[text()='Add']/..").click()

    # Wait for the js to catch up
    _wait_for_all_regattas(context)
        

## Read-only steps

@given(u'I am viewing all Regattas')
@when(u'I view all Regattas')
def selenium_view_all_regattas(context):
    """Return to the homepage and view all Regattas"""
    link = context.browser.find_element_by_xpath("//nav/a[text()='Regattas']")
    link.click()
    _wait_for_all_regattas(context)


@then(u'I see there are {num_regattas:d} Regattas')
def selenium_see_regattas(context, num_regattas):
    regattas_selector = "//section//div//h4[text()='Regattas']/..//div[contains(@class, 'regatta-item-card')]"
    regattas = context.browser.find_elements_by_xpath(regattas_selector)

    # Check number
    assert num_regattas == len(regattas), "Found only {} Regattas!".format(len(regattas))
    for row in context.table:
        context.browser.find_element_by_xpath(
            "{0}//h5[contains(@class, 'mdl-card__title-text') and text()='Nationals']".format(
                regattas_selector,
                row['Regatta Name'])
        )


## Data mutation Steps

@given(u'I have the following Regattas')
def selenium_add_regattas(context):
    """Add in all of the supplied regattas"""
    for row in context.table:
        _create_regatta(context, row)


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
