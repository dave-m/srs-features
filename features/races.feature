Feature: Races
  As a Regatta organizer
  I want to be able to see a list of all Races
  and track their participants
  So that I can manage the event effectively

  Background: I am on the Sail Race Scoring Website
    Given I open a webbrowser
    and I log in to the Sail Race Scoring website
    and I have the following Regattas:
    | Regatta Name |
    | Nationals |
    | Europeans |

  Scenario: Add a race to a Regatta
    Given I am viewing all Regattas
    When I click on the "Races" button for the "Nationals" Regatta
    and I click on the "Add Race" button
    and I enter in the following race details:
    | Name  | Course    | Laps |
    | First | Trapezoid |    1 |
    and I click on the "Add" button
    Then I see there are 1 Races:
    | Name  | Laps | Course    | Status      |
    | First |    1 | Trapezoid | Not Started |

  Scenario: View all Races for a Regatta
    Given I am viewing the "Nationals" Regatta
    When I click on the "Races" button
    Then I see there are 2 Races:
    | Name        | Course    | Laps | Status      |
    | First Race  | Triangle  |    3 | Not Started |
    | Second Race | Trapezoid |    2 | Not Started          |

  Scenario: Cancel a Race
    Given I am view the "Nationals" Regatta
    and I have a race with the following details:
    | Name     | Course    | Laps |
    | Bad Race | Trapezoid |    3 |
    When I click on the "Races" button
    and I click on the "Details" button for the Race named "Bad Race"
    and I click on the "Cancel" button
    Then I see there is 1 Races:
    | Name     | Course   | Laps | Completed |
    | Bad Race | Triangle |    3 | Cancelled |

  Scenario Outline: Create a race for a <Course> Course
    Given I am viewing all Regattas
    When I click on the "Races" button for the "Nationals" Regatta
    and I click on the "Add Race" button
    and I enter in the following race details:
    | Name  | Course    | Laps |
    | First | <Course> |    1 |
    and I click on the "Add" button
    Then I see there are 1 Races:
    | Name  | Laps | Course    | Status      |
    | First |    1 | <Course> | Not Started |

  Examples:
    | Course    |
    | Trapezoid |
    | Sausage   |
    | Triangle  |


