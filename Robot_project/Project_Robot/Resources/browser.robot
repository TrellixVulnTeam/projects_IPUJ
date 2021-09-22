*** Settings ***
Library    SeleniumLibrary
Library    DateTime
*** Variables ***

*** Keywords ***
open-browser
    [Arguments]    ${url}=https://courses.letskodeit.com/practice    ${Browser}= Chrome
    open browser       ${url}    ${Browser}
    maximize browser window
    set selenium implicit wait    10 seconds

close-browser
    close all browsers

current date
    [Arguments]    ${increment}=365 days
    ${current}    get current date    increment=${increment}   result_format=%d/%m/%Y
    [Return]    ${current}


