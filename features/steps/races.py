
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait

def _wait_for_all_races(context):
    """Wait for the All Races section to appear"""
    WebDriverWait(context.browser, 1).until(
        lambda x: x.find_element_by_xpath("//span[text()='All Races']")
    )

@when(u'I click on the "Races" button for the "{regatta_name}" Regatta')
def selenium_click_on_races_for_regatta(context, regatta_name):
    """Select the Races for a Regatta"""
    race_button = (
        "//section//div//h4[text()='Regattas']/"
        "..//div[contains(@class, 'regatta-item-card')]"
        "/div[contains(@class, 'mdl-card__title')]/h5[text()='Nationals']"
        "/../..//button/a[text()='races']")
    WebDriverWait(context.browser, 1).until(
        lambda x: x.find_element_by_xpath(race_button)
    )
    context.browser.find_element_by_xpath(race_button).click()
    _wait_for_all_races(context)


def _create_race(context, race):
    """Add in a new Race via Selenium"""
    # Wait for the js to catch up
    WebDriverWait(context.browser, 1).until(
        lambda x: x.find_element_by_xpath("//h6[text()='Create a new Race']")
    )

    # Enter the Race Name
    text_entry = context.browser.find_element_by_id("addRaceName")
    text_entry.send_keys(race['Name'])

    # Enter the course
    text_entry = context.browser.find_element_by_id("addRaceCourse")
    text_entry.send_keys(race['Course'])

    # Enter the number of laps
    text_entry = context.browser.find_element_by_id("addRaceLaps")
    text_entry.send_keys(race['Laps'])

@when(u'I enter in the following race details')
def selenium_create_race_details(context):
    """Create a new Race"""
    assert len(context.table.rows) == 1, "Currently unable to create > 1 Race"
    for race in context.table:
        _create_race(context, race)


@then(u'I see there are {num_races:d} Races')
def selenium_check_races(context, num_races):
    """Check there are the specified number of races present"""
    race_table_selector = "//section//span[text()='All Races']/../../..//table"
    race_rows_selector = "{0}//tr/td/..".format(race_table_selector)

    # Check number
    races = context.browser.find_elements_by_xpath(race_rows_selector)
    assert num_races == len(races), "Found {} Races!".format(len(races))

    # Check rows
    for row in context.table:
        # Name
        context.browser.find_element_by_xpath(
            "{0}//tr/td[1 and text()='{name}']".format(race_table_selector, name=row['Name'])
        )
        # Laps
        context.browser.find_element_by_xpath(
            "{0}//tr/td[2 and text()='{laps}']".format(race_table_selector, laps=row['Laps'])
        )
        # Course
        context.browser.find_element_by_xpath(
            "{0}//tr/td[3 and text()='{course}']".format(race_table_selector, course=row['Course'])
        )
        # Status
        context.browser.find_element_by_xpath(
            "{0}//tr/td[4 and text()='{status}']".format(race_table_selector, status=row['Status'])
        )
