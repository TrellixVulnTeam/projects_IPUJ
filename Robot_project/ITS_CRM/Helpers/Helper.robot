*** Settings ***
Library    SeleniumLibrary



*** Variables ***
${url_preview}    https://avanadepreview.crm.dynamics.com
${url_uat}    https://avanadeuat.crm.dynamics.com
${url_dev}    https://avanadedev.crm.dynamics.com



*** Keywords ***
open-browser
    [Arguments]    ${url}=preview    ${Browser}=Chrome
    IF    '${url}' == 'preview'
        open browser    ${url_preview}     ${Browser}
    ELSE IF    '${url}' == 'uat'
        open browser    ${url_uat}    ${Browser}
    ELSE IF    '${url}' == 'dev'
        open browser    ${url_dev}    ${Browser}
    END
    maximize browser window
    set browser implicit wait    15 seconds

close-browser


