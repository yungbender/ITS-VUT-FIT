Feature: Cart

    Scenario: User adds some item from offer to the empty cart
        Given User is on some exact product page 
        And user has empty cart
        When User adds item to cart
        Then User registers the item and has the item in the cart

    Scenario: User adds some item from offer to the not-empty cart
        Given User is on some exact product page
        And user has not empty cart
        When User adds item to cart
        Then User registers the item and has the item in his cart

    Scenario: User adds item from mainpage offer to the cart - instant
        Given User is on index page
        When User adds item to the cart
        Then User registers the mainpage item and has the item in his cart