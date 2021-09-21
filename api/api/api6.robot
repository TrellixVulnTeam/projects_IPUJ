*** Settings ***
Library    RequestsLibrary
Library    JSONLibrary
Library    Collections

*** Variables ***
${base_url}    https://thetestingworldapi.com/
${or_first_name}    HelloWorld
${up_first_name}    TestingAPIworld

*** Test Cases ***
E2E Testing
    #Creating post data
    create session    get_request    ${base_url}
    &{data1}    create dictionary    first_name=${or_first_name}    middle_name=api    last_name=lets    date_of_birth=12/12/4444
    ${response1}  post on session    get_request    api/studentsDetails    data=${data1}
    log to console    status response of post = ${response1.status_code}
    log to console    content of post = ${response1.content}
    &{json}    to json    ${response1.content}
    log to console    json file of post is ${json}
    @{list}    get value from json    ${json}    id
    ${id}    get from list    ${list}    0
    log to console    id of post is ${id}

    #using the id from post as input to update the same json
    &{data2}    create dictionary    id=${id}    first_name=${up_first_name}    middle_name=created    last_name=lets    date_of_birth=12/12/5555
    ${response2}  put on session    get_request    api/studentsDetails/${id}    data=${data2}
    log to console    status response of put = ${response2.status_code}
    log to console    content of put = ${response2.content}

    #calling the same json through id
    ${response3}  get on session    get_request    api/studentsDetails/${id}
    log to console    status response of get = ${response3.status_code}
    log to console    content of get = ${response3.content}
    &{json1}    to json    ${response3.content}
    log to console    json file of get is ${json1}
    @{list1}    get value from json    ${json1}    data.first_name
    ${first_name}    get from list    ${list1}    0
    log to console    fist name is ${first_name}
    #using the id as input to delete the data

    ${response4}  delete on session    get_request    api/studentsDetails/${id}
    log to console    status response of delete = ${response4.status_code}
    log to console    content of delete = ${response4.content}
    ${json2}    to json    ${response4.content}
    log to console    json file of delete is ${json2}
    ${list2}    get value from json    ${json2}    status
    ${status}    get from list    ${list2}    0
    log to console    deleted status is "${status}"




