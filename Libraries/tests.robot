*** Settings ***
Library            Library.py

*** Test Cases ***
Argument conversion
    Conversion
    ...    42
    ...    ${CURDIR}/tests.robot
    ...    1 minute 7 seconds
