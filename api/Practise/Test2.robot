*** Settings ***
Library    SeleniumLibrary
Resource   ../Resources/BrowserOperations.robot
Documentation    This file will run robot framework
Test Setup    Open-Browser
Test Teardown    close-browser


*** Variables ***



*** Keywords ***
Test-case
    [Arguments]    ${check}
    ${bmw}=    run keyword and return status    element should be visible  ${check}
    run keyword and return if    ${bmw}    click element   ${check}
    run keyword unless    ${bmw}    log to console    Element not found with locator ${check}

*** Test Cases ***
Test case 1
    [Tags]    Smoke
    Test-case    id:bmwcheck
    sleep   5 seconds


Test case 2
    [Tags]    Smoke    Sanity
    Test-case    hondacheck
    sleep    5 seconds