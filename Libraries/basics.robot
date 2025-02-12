*** Settings ***
Library           basics.py

*** Test Cases ***
Simple keyword
    Simple keyword

Arguments
    One argument    Robot
    Default values    Robot
    Default values    Robot    Hi
    Default values    Robot    greeting=Hi

Status
    Should be positive    1
    Should be positive    1.3
    Should be positive    -1

Logging
    Log using print
    Log using API
