Feature: Chrome Browser
  Scenario: Successfully launch chrome browser
    Given Launch Chrome browser
    When Type on search
    Then Search is show
    And Close browser