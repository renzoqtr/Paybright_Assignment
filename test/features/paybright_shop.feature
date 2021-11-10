Feature: PayBright Shops
  As a web surfer,
  I want to know if I can pay on my favorites stores,
  So I can pay using PayBright.


  Scenario: PayBright Search
    Given the google canada page is displayed
    And user searches for "PayBright"
    And "paybright.com" result is displayed
    When user navigates to expected results: "https://paybright.com/en/"
    And user go to shop
    And user sorts by "Popular" with merchant "Samsung"
    Then "Samsung" card is shown as result