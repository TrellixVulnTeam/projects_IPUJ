*** Settings ***
Library     RequestsLibrary
Library    JSONLibrary
Library    Collections

*** Variables ***
${base_url}    https://thetestingworldapi.com/



*** Test Cases ***
test case 4
    create session    get-request    ${base_url}
    &{data}=    create dictionary    first_name=Hello    middle_name=World    last_name=lets    date_of_birth=12/12/2022
    log to console    dictionary is ${data}
    ${response}    post on session    get-request    /api/studentsDetails    data=${data}
    log to console    status code = ${response.status_code}
    log to console    content = ${response.content}
#    @{json}=    to json    ${response.content}
#    ${get_value}    get value from json    ${json}    [26].date_of_birth
#    log to console    ${get_value}

