Feature: Admin panel and features

    Scenario: Admin login
        Given User is not logged in
        And is on admin page
        When User fills in correct admin creditials
        And logs in
        Then User is logged in as Admin on Admin page 

    Scenario: Display all registered customers
        Given There is atleast 1 registered customer
        And user is logged in as Admin
        When Admin clicks Customers
        Then All registered customers will show up

    Scenario: Display all orders
        Given There is atleast 1 order placed
        And User is logged in as Admin
        When Admin clicks orders
        Then All placed orders will show up

    Scenario: Admin logout
        Given User is logged in as Admin
        When User logs out
        Then User is logged out