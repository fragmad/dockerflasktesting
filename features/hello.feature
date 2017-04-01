Feature: Hello is an application which says hello in various ways.

    Scenario: Hello World! 
    Given Hello is set up
        When we connect to "/"
        Then we should see a message saying "Hello World"

    Scenario: Hello to a name
       Given Hello is set up 
       When we connect to "/hello/Jane%20Doe"
       Then we should see a message saying "Hello Jane Doe"

