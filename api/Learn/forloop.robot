*** Settings ***
Library    SeleniumLibrary
Resource   ../Resources/BrowserOperations.robot
Documentation    This file will run robot framework
Test Setup    Open-Browser
Test Teardown    close-browser


*** Variables ***

*** Test Cases ***
Test case 1
#    [Documentation]    Test case 1
#    ${button}  set variable    xpath://input[@type='radio']
#    @{radios} =    Get WebElements    ${button}
#    log to console    radios are @{radios}
#    FOR    ${x}    IN    @{radios}
#        ${status}    run keyword and return status    checkbox should be selected    ${x}
#        run keyword unless    ${status}    select checkbox    ${x}
#        sleep    3 seconds
#    END

    [Documentation]    Test case 1
    ${button}  set variable    xpath://input[@type='radio']
    @{radios} =    Get WebElements    ${button}
    FOR    ${x}    IN    @{radios}
        ${status}    run keyword and return status    checkbox should be selected    ${x}
        IF    ${status}==False
            select checkbox    ${x}
            log to console    checkbox is selected
            sleep    5 seconds
        END
    END








