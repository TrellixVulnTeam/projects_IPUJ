*** Settings ***
Library     RequestsLibrary
Library    JSONLibrary
Library    Collections

*** Variables ***
${base_url}    https://thetestingworldapi.com/



*** Test Cases ***
test case 4
    create session    get-request    ${base_url}
    &{data}=    create dictionary    id=450279    first_name=data    middle_name=OKOK    last_name=wait    date_of_birth=12/12/3025
    log to console    dictionary is ${data}
    ${response}    put on session    get-request    /api/studentsDetails/450279    data=${data}
    log to console    status code = ${response.status_code}
    log to console    content = ${response.content}
    ${response1}    get on session    get-request    /api/studentsDetails/450279
    log to console    data is ${response1.status_code}
    log to console    content is ${response1.content}


