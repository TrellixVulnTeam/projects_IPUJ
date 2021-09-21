*** Settings ***
Library  Collections
Library    String
Library    SeleniumLibrary
Library    Dialogs
Library    DateTime

*** Test Cases ***
test1
    ${input}    get value from user    Enter string    hidden=True
    ${length}    get length    ${input}
    log to console    ${input}[::-1]
    switch window
*** Keywords ***
reverse string
    [Arguments]    ${data}
    log to console    string is ${data}[::-1]