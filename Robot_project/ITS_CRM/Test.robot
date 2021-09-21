*** Settings ***
Library    SeleniumLibrary
Resource    ../ITS_CRM/Helpers/Helper.robot
Test Setup    open-browser    uat
Test Teardown    close-browser

*** Variables ***


*** Test Cases ***
Test case 1
    sleep    10 seconds
    ${title}    get title
    log    ${title}
    open browser
    close browser
    get title


