*** Settings ***
Library    SeleniumLibrary
Resource    ../Resources/browser.robot
Library    String
Library    Collections
Library    Dialogs
Test Setup    open-browser
Test Teardown    close-browser
*** Variables ***

*** Keywords ***



*** Test Cases ***
#Test case 1
#   sleep    2 seconds
#   select radio button    cars    bmw
#   sleep    2 seconds
#   select checkbox    id:bmwcheck
#   sleep    2 seconds
#   select from list by value    id:carselect    honda
#   sleep    2 seconds
#   select from list by label    id:carselect    Benz
#   sleep    2 seconds
#   select from list by index    id:carselect    0
#   sleep    2 seconds

#Test case 1
##   execute javascript    window.scrollBy(0,1000)
#   input text    id:name    Mahesh
#   sleep    2 seconds
#   click button    id:alertbtn
#   sleep    2 seconds
#   handle alert    ACCEPT
#   sleep    2 seconds
#   click button    id:confirmbtn
#   sleep    2 seconds
#   handle alert    DISMISS
#   sleep    2 seconds

#Test case 3
#    sleep    2 seconds
#    click button    id:openwindow
#    sleep    2 seconds
#    ${windows}    get window handles
#    switch window    ${windows}[1]
#    sleep    2 seconds
#    maximize browser window
#    sleep    2 seconds
#    input text    name:course    Java
#    sleep    2 seconds
#    switch window    ${windows}[0]
#    click element    id:opentab
#    sleep    2 seconds
#    ${windows1}    get window handles
#    switch window    ${windows1}[2]
#    input text    name:course    Java
#    sleep    2 seconds
#
#Test case 4
#    execute javascript    window.scrollTo(0,800)
#    select frame    name:iframe-name
#    input text    name:course    Java
#    sleep    2 seconds
#    unselect frame
#    execute javascript    window.scrollTo(0,-800)
#    click element    id:opentab
#    sleep    2 seconds
#    execute javascript    window.open("https://redbus.com")
#    sleep    2 seconds
#    ${windows}    get window handles
#    log to console    windows are ${windows}
#    switch window    ${windows}[1]
#    sleep    2 seconds
#    input text    id:src    Hyder
#    sleep    2 seconds
#    mouse down    id:src
#    press keys    id:src    ENTER
##    press keys  id:src  ARROW_DOWN   ENTER
#    sleep    2 seconds

#Test case 5
#    ${sdn}    set variable    Hello_World
#    ${check}    convert to lower case    ${sdn}
#    log to console    ${check}
#    ${check1}    convert to upper case    ${sdn}
#    log to console    ${check1}
#    ${check2}    convert to title case    ${sdn}
#    log to console    ${check2}
#    ${check3}    get line count    ${sdn}
#    log to console    ${check3}
#    ${check5}    split string    ${sdn}    _
#    log to console    ${check5}
#    ${check4}    fetch from left    ${sdn}    _
#    log to console    ${check4}
#    ${check6}    get substring    ${sdn}    0    7
#    log to console    ${check6}

#Test case 6
#    @{list}    create list    a  b  c  d  f  e  w    e
#    append to list    ${list}    c    s    d
#    ${hello}    remove duplicates   ${list}
#    log to console    ${hello}
#Test case 6
#    @{list1}    create list    a  b  c  d  f  e  w    e
#    append to list    ${list1}    c    s    d
#    ${hello1}    remove duplicates   ${list1}
#    log to console    ${hello1}
#Test case 7
#    &{dict}    create dictionary    Hello=World    1=2sasa
#    log to console    ${dict}
#    @{list}    create list    Hello    sjs    sjh    ahs    uhsuwh    uwhuh
#    log to console    ${list}[0]
#    log to console    ${list[0:2]}
#    ${hello}    set variable    HelloWorld
#    log to console    ${hello}
#    ${len}    get length    ${hello}
#    FOR    ${x}    IN RANGE    ${len}-1    -1    -1
#        log to console    ${hello[${x}]}
#    END
#    @{list2}    create list
#    log to console    ${list2}
#    FOR    ${x}    IN    ${list}:
#        ${y}    run keyword and return status    ${x}    IN    ${list}
#        run keyword unless    ${y}    append to list    ${list2}    ${x}
#    END
#    log to console    ${list2}
#Test case 10
#    &{dict}    create dictionary    first=Hello    last=World    type=string
#    ${check}    get from dictionary    ${dict}    last
#    log to console    ${check}

Test case 11
#    ${test}    get value from user   enter valuest
#    log to console    ${test}
#    ${test1}    get value from user   enter value    default_value=check
#    log to console    ${test1}
#    execute manual step    message=enter chey ra    default_error=OK
#    ${test2}    get selection from user    select from below    Hello    World
#    log to console    ${test2}
#    ${test3}    get selections from user    select from below    Hello    World
#    log to console    ${test3}







