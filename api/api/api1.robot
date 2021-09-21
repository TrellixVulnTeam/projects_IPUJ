*** Settings ***
Library     RequestsLibrary
Library    JSONLibrary
Library    Collections

*** Variables ***
${base_url}    http://thetestingworldapi.com/




*** Test Cases ***
test case 1
    create session    get_student_details    ${Base_url}
    ${response} =    GET On Session    get_student_details   api/studentsDetails
    log to console  status code = ${response.status_code}
    ${string}=    convert to string  ${response.status_code}
    should be equal   ${string}   200
    log to console  content = ${response.content}
    @{json}=    to json    ${response.content}
    ${get_value}    get value from json    ${json}    [26].date_of_birth
    log to console    ${get_value}




    

