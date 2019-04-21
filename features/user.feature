Feature: Accounts and User options

    Scenario: Failed account creation/registration - Empty box
        Given User is not logged in
        And is on registration page
        When User does not fill out requisite box
        And confirms privacy policy
        And continues to registrate
        Then Registration will not pass

    Scenario: Failed account creation/registration - Not accepting privacy policy
        Given User is not logged in
        And is on registration page
        When User does fill out requisite box
        And continues to registrate
        Then Registration will not pass

    Scenario: Successful account creation/registration
        Given User is not logged in 
        And is on registration page
        When User fills out correct informations
        And confirms privacy policy
        And continues to registrate
        Then Registration is OK
    
    Scenario: Unsuccessful login
        Given User is not logged in
        And is on login page
        When User fills out incorrect login creditials
        And continues to login
        Then User is not logged in an any account

    Scenario: Successful login
        Given User is not logged in
        And is on login page
        When User fills out correct login creditials
        And continues to login
        Then User is logged in in his account

    Scenario: Successful logout
        Given User is logged in
        And is on eshop page
        When User logsout
        Then User is logged out of his account

    Scenario: Incorrect password change
        Given User is logged in 
        And is on MyAccount page
        When User gets to the change password page
        And fills in wrong password
        And continues to change password
        Then User password has not changed

    Scenario: Correct password change
        Given User is logged in 
        And is on MyAccount page
        When User gets to the change password page
        And fills in new password creditials
        And continues to change password
        Then User password has changed