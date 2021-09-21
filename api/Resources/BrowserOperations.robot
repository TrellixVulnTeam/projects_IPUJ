*** Settings ***
Library    SeleniumLibrary
Library    ../Pythonfiles/helper.py

*** Variables ***


*** Keywords ***
Open-Browser
    [Arguments]    ${url}= https://courses.letskodeit.com/practice    ${browser}= Chrome
    open browser  ${url}  ${browser}
    maximize browser window
    set browser implicit wait    20 seconds

get-title
    ${title}=    get title
    [Return]    ${title}

close-browser
    close all browsers

select-option
    [Arguments]    ${locator}    ${text}
    input text    ${locator}    ${text}
    sleep    4 seconds
    press keys    ${locator}    ARROW_DOWN    ENTER
    sleep    4 seconds

locate-element
    [Arguments]    ${json}
    ${element}=    read_element    ${json}
    [Return]    ${element}

