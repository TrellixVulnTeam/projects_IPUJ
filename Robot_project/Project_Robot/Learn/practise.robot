*** Settings ***
Library    SeleniumLibrary
Library    String
Library    Collections
Library    Dialogs
Resource    ../Resources/browser.robot
Library    DateTime

*** Variables ***
${url}    https://courses.letskodeit.com/practice

*** Test Cases ***
test case 1
    [Documentation]    This will open the browser
    open browser    ${url}    Chrome
    close all browsers
