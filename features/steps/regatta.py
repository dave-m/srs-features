from behave import when, then

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