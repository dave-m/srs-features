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

  Scenario: View all Races for a Regatta
    Given I am viewing the "Nationals" Regatta
    When I click on the "Races" button
    Then I see there are 2 Races:
      | Race Name   | Course    | Laps | Competitors | Completed |
      | First Race  | Triangle  | 3    | 0           | No        |
      | Second Race | Trapezoid | 2    | 0           | No        |

  Scenario: View details for a Race
    Given I am viewing the "Nationals" Regatta
    When I click on the "Races" button
  and I click on the "First Race" link
    Then I see the boats for the "First Race"
  and I see the results for the "First Race"

  Scenario: Create a new Race
    Given I am view the "Nationals" Regatta
    When I click on the "Races" button
      and I click on the "New Race" button
      and I enter in the following race details:
      | Name    | Course      | Laps  |
      | Race 1  | Triangle    | 3     |
      | Race 2  | Triangle    | 3     |
      | Race 3  | Trapezoid   | 3     |
      and I click on the "+" button
    Then I see there are 3 Races:
      | Race Name   | Course    | Laps |
      | First Race  | Triangle  | 3    |
      | Second Race | Trapezoid | 2    |
      | Race 3      | Trapezoid | 3    |

  Scenario: Cancel a Race
    Given I am view the "Nationals" Regatta
  and I have a race with the following details:
  | Name      | Course      | Laps  |
  | Bad Race  | Trapezoid   | 3     |
    When I click on the "Races" button
  and I click on the "Details" button for the Race named "Bad Race"
  and I click on the "Cancel" button
    Then I see there is 1 Races:
      | Race Name | Course   | Laps | Competitors | Completed |
      | Bad Race  | Triangle | 3    | 0           | Cancelled |

