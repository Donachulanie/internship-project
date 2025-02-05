Feature: Test for filters
  @smoke
  Scenario: User can filter by Out of Stock
    Given Open Reelly main page
    When input valid donachulanie@yahoo.com and Victoria57# on sign in page
    Then Click on the "Continue" button
    Then Verify user is logged in successfully
    When Click on “Off plan” at the left side menu
    Then Verify Presale(EOI) box shown
    When Filter by sale status of “Out of Stock”
    Then Verify each product contains the Out of stock


############################################







