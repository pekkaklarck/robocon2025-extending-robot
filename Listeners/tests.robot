*** Settings ***
Library           LibraryListener.py

*** Test Cases ***
Passing
    Log    Hello, world!
    Log    Hello, again!
    Library keyword

Failing
    Fail    Something bad happened!
    Log    Is this run?
    Log    What about this?

Passing again
    Log    Hello, again!
    User keyword

*** Keywords ***
User keyword
    Log    Hello!
