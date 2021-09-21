*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${Browser}=    Chrome
${URL}=    https://accounts.google.com/signup/v2/webcreateaccount?hl=en&flowName=GlifWebSignIn&flowEntry=SignUp
${First-Name}   name=firstName
${Last-Name}    id=lastName
${User-Name}    id=username


*** Test Cases ***
Learning Robot Framework
    Fill_yahoo_details


*** Keywords ***
Fill_yahoo_details
    open browser    ${URL}    ${Browser}
    log to console    title is = get title
    maximize browser window
    set selenium speed    0.5Seconds
    [Arguments]    ${FirstName}=hello   ${LastName}=check   ${username}=wait
    input text    ${First-Name}     ${FirstName}
    input text    ${Last-Name}    ${LastName}
    input text    ${User-Name}   ${username}
    close browser

