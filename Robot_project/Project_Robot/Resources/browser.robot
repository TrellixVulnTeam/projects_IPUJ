*** Settings ***
Library    SeleniumLibrary
*** Variables ***

*** Keywords ***
open-browser
    [Arguments]    ${url}=https://courses.letskodeit.com/practice    ${Browser}= Chrome
    open browser       ${url}    ${Browser}
    maximize browser window
    set selenium implicit wait    10 seconds

close-browser
    close all browsers

