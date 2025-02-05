Feature: Test for left side menu buttons
  @smoke
  Scenario: User can click on the side menu buttons
    Given Open Reelly main page
    When input valid donachulanie@yahoo.com and Victoria57# on sign in page
    Then Click on the "Continue" button
    Then Verify user is logged in successfully
    When Click on "Filter" button
    When Click on "close x" filter window
    When Click on "Main menu"
    When Click on "Secondary"
    When Click on "My-listing" button from the header
    When Click on "Income"
