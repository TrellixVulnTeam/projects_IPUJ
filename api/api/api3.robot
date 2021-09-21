*** Settings ***
Library     RequestsLibrary
Library    JSONLibrary
Library    Collections

*** Variables ***
${base_url}    http://thetestingworldapi.com/

*** Test Cases ***
test case 2
    create session    delete-request   ${base_url}
    ${request}=    delete on session    delete-request    api/studentsDetails/450279
    log to console    status code = ${request.status_code}
    log to console    content is = ${request.content}
