*** Settings ***
Library            Library.py

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
