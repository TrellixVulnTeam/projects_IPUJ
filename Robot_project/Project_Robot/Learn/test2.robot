*** Settings ***
Library    SeleniumLibrary
Resource    ../Resources/browser.robot
Library    String
Library    Collections
Library    Dialogs
Library    Screenshot
Suite Setup    open-browser
Suite Teardown    close-browser
*** Variables ***
#${line}=   Helloworld
*** Keywords ***
*** Test Cases ***
#Test case 1
#    ${check}    get webelement    css:input[id='bmwcheck']
#    select checkbox    ${check}
#    sleep    3 seconds
#    page should contain    Practice Page
#
#Test case 1
#    ${check}    get webelement    xpath://*[@id="product"]/tbody/tr[4]/td[2]
#    ${check1}    get text    ${check}
#    log    Text is "${check1.upper()}"
#    log    Text is "${check1.lower()}"
#    log    Text is "${check1.title()}"
Test case 4
    ${title}    get title
    log to console    ${title}
    pass execution if    '${title}'=='Practice Page'    passed
