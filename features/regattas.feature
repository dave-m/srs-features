Feature: Regattas
  As a Regatta organizer
  I want to be able to see a list of all Regattas
  and track their races and participants
  So that I can manage the even effectively

  Background: I am on the Sail Race Scoring Website
    Given I open a webbrowser
  and I log in to the Sail Race Scoring website
  and I have the following Regattas:
  | Regatta Name |
  | Nationals |
  | Europeans |

  Scenario: View regattas
    Given I am on the Sail Race Scoring Website
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

