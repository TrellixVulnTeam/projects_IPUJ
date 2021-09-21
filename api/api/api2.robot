*** Settings ***
Library     RequestsLibrary
Library    JSONLibrary
Library    Collections

*** Variables ***
${base_url}    https://reqres.in



*** Test Cases ***
test case 2
    create session    get-request    ${base_url}
    &{dict}=    create dictionary    page=2
    ${response}    get on session    get-request    /api/users    params=&{dict}
    log to console    status is ${response.status_code}
    log to console    content is  ${response.content}

