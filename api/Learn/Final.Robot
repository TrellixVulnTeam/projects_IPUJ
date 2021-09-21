*** Settings ***
Library    SeleniumLibrary
Resource    ../Resources/BrowserOperations.robot
Test Setup    Open-Browser
Test Teardown    Close-Browser
*** Variables ***
*** Keywords ***
*** Test Cases ***
test
    sleep    10 Seconds


