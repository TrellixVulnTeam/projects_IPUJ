*** Settings ***
Library    SeleniumLibrary
Library    Collections
Resource   ../Resources/BrowserOperations.robot
Test Setup    Open-Browser    https://www.amazon.com/
Test Teardown    close-browser


*** Variables ***

*** Test Cases ***
Test case 1
    ${id}    locate-element    search
    ${search}    run keyword and return status    element should be visible    ${id}
    log    status is "${search}"
    sleep    5 seconds
    run keyword if    ${search}    select-option    ${id}    muscle
    sleep    5 seconds
    wait until page contains element

Test case 2
    ${title}    get title
    log to console    ${title}
