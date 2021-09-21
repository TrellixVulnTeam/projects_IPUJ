*** Settings ***
Library     RequestsLibrary

*** Variables ***
${Base_url}    http://thetestingworldapi.com/



*** Keywords ***
Get-Request
    [Arguments]    ${url}
    create session    get_student_details    ${Base_url}
    ${response} =    GET On Session    get_student_details    ${url}
    log to console  status code = ${response.status_code}
    log to console  content = ${response.content}