*** Settings ***
Library            Library.py    ORIGINAL

*** Test Cases ***
Argument conversion
    Conversion
    ...    0.3
    ...    ${CURDIR}/tests.robot
    ...    1 minute 7 seconds

Restricted values using Literal
    Move    UP
    Move    left
    Move    BAD

Restricted values using Enum
    Turn    LEFT
    Turn    right
    Turn    wrong

Custom converts
    Birthday    6.4.1975

Library state 1
    Set state    NEW
    Set state    NEWER

Library state 2
    Set state    NEWEST

Custom keyword name
    🤖

Embedded arguments
    This is a "good" example
    This is a "bad" example
    This is a "ugly" example

Mixed arguments
    Number of horses is    6
    Number of dogs is    2

Skipping
    Skip me

Continuing on failure
    Continuable failure    first
    Continuable failure    second
    Continuable failure    third

HTML error messages
    HTML error
