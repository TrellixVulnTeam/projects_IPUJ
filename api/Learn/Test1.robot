*** Settings ***
Library    SeleniumLibrary
Library    Screenshot
*** Variables ***
${url}    https://courses.letskodeit.com/practice
${username}    id:email
${password}    id:password
${sign}    xpath://a[@href='/login']

*** Test Cases ***
Test browser speed
    open browser    ${url}    Chrome
    maximize browser window
    sleep    4 seconds
    ${check1} =    run keyword and return status    element should not be visible    name:show-hide
    log to console  status = ${check1}
    run keyword unless    ${check1}    click button    id:hide-textbox
    sleep    4 seconds
    ${check2} =    run keyword and return status    element should be visible    name:show-hide
    log to console  status = ${check2}
    run keyword unless    ${check2}    click button    id:show-textbox
    sleep    4 seconds
    close all browsers

