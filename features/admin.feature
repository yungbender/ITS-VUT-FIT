Feature: Admin panel and features

    Scenario: Admin login
        Given User is not logged in
        And is on admin page
        When User fills in correct admin creditials
        And logs in
        Then User is logged in as Admin on Admin page 

    Scenario: Display all registered customers
        Given User is logged in as Admin
        And There is atleast 1 registered customer
        When Admin clicks Customers
        Then All registered customers will show up

    Scenario: Display all orders
        Given User is logged in as Admin
        And There is atleast 1 order placed
        When Admin clicks orders
        Then All placed orders will show up

    Scenario: Admin logout
        Given User is logged in as Admin
        And is on admin page
        When User logs out
        Then User is logged out