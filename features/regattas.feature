@ui
Feature: Regattas
  As a User
  I want to be able to see a list of all Regattas
  So that I can check my listing

  Background: Log on to the SRS Website
    Given I open a webbrowser


  Scenario: View regattas
    Given I am on the Sail Race Scoring website
    When I view all Regattas
    Then I see there are 2 Regattas:
    | Regatta Name |
    | Nationals |
    | Europeans |

  Scenario: Add a new Regatta
    Given I am on the Sail Race Scoring website
    and I am viewing all Regattas
    When I add a new Regatta with the name "My Regatta"
    Then I see there are 3 Regattas:
    | Regatta Name |
    | Nationals |
    | Europeans |
    | My Regatta |
