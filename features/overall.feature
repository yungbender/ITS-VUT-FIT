Feature: Overall Page

    Scenario: Page accessiblity
        Given User has opened browser 
        And is connected to the internet
        When User visits the eshop Page
        Then Website loades without a problem 
        And shows whole Website

    Scenario: Currency change
        Given User is on eshop instance
        When User changes the currency to another
        Then Prices are correctly changed to the chosen currency

    Scenario: Make an order
        Given User is on the cart page 
        And user has some item in the cart
        And user is logged in
        When User checks out 
        And fills out correct info
        And confirms order
        Then Order is completed 
        And registered in database