*** Settings ***
Library    SeleniumLibrary
Test Setup     Start Test
Test Teardown    End Test
*** Variables ***
${Test1}    Hello
${Test2}    World

*** Keywords ***
Test case 1
    log to console    test is ${Test1}

Test case 2
    log to console    test is ${Test2}

Start Test
    log to console    Running Tests

End Test
    log to console    Running Tests

*** Test Cases ***




Test case 1
    [Tags]    Smoke
    Test case 1
    Test case 2

Test case 2
    [Tags]    Sanity
    Test case 2
    Test case 1

Test case 3
    [Tags]    Smoke
    Test case 1
    Test case 2
    Test case 1

Test case 4
    [Tags]    Sanity
    Test case 2
    Test case 1
    Test case 2

