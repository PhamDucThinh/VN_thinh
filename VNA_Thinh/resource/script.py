*** Settings ***
Library           Selenium2Library    10    10    Capture Page Screenshot
Library           String
Library           Collections

*** Variables ***
${URL}            http://vietnam-airline.org/
${BUTTON_CHECK}    ${EMPTY}

*** Test Cases ***
Booking your trip
    SetUp
    NavigationProduct_oneway
    Search_flight
    Run Keyword if    '${BUTTON_CHECK}'=='False'    Resume_if have ticket
    [Teardown]

Booking your trip_Search flight without destination
    SetUp
    NavigationProduct_oneway
    Search_flight_without_des
    Sleep    10s
    Alert Should Be Present    Please select departure city
    Close Browser

Booking your trip_Search flight without arri
    SetUp
    NavigationProduct_oneway
    Search_flight_without_arr
    Sleep    10s
    Alert Should Be Present    Please select arrival city
    Close Browser

Booking your trip_invalid email
    SetUp
    NavigationProduct_oneway
    Search_flight
    Run Keyword if    '${BUTTON_CHECK}'=='False'    Resume_if have ticket_invalid email
    [Teardown]

Booking your trip_invalid confirm email
    SetUp
    NavigationProduct_oneway
    Search_flight
    Run Keyword if    '${BUTTON_CHECK}'=='False'    Resume_if have ticket_invalid \ confirm email
    [Teardown]

Booking your trip_confirm email not match email
    SetUp
    NavigationProduct_oneway
    Search_flight
    Run Keyword if    '${BUTTON_CHECK}'=='False'    Resume_if have ticket_invalid \ email not match email
    [Teardown]

*** Keywords ***
SetUp
    Open Browser    ${URL}    gc
    Maximize Browser Window
    Wait Until Page Contains    BOOK YOUR TRIP
    [Teardown]

NavigationProduct_oneway
    Select Checkbox    css=input[type='radio'][value='One Way']

Get A Value from Dictionary By Random
    [Arguments]    ${dictName}    ${key}=[Any]
    ${val}    Run Keyword If    '${key}'!='[Any]'    Get From Dictionary    ${dictName}    ${key}
    Return From Keyword If    '${val}'!='None'    ${val}
    ${keys}    Get Dictionary Keys    ${dictName}
    ${dicLen}    Get Length    ${keys}
    ${ranIndex}    Evaluate    random.randint(0, ${dicLen}-${1})    random
    ${ranKey}    Set Variable    ${keys[${ranIndex}]}
    ${val}    Get From Dictionary    ${dictName}    ${ranKey}

Select An Item from Listbox by Random
    [Arguments]    ${locator}    ${dictName}    ${key}=[Any]
    Wait Until Element Is Visible    ${locator}
    ${value}    Get A Value from Dictionary By Random    ${dictName}    ${key}
    Select From List By Value    ${locator}    ${value}

Select any value from combobox by random
    [Arguments]    ${locator}
    [Documentation]    Select any value from combobox by random
    ...
    ...    if Item have value which contain '*' character. random index will return with index+1
    ${keys}    Get List Items    ${locator}
    Comment    ${keys}    Get Dictionary Keys    ${Mang}
    ${dicLen}    Get Length    ${keys}
    ${ranIndex}    Evaluate    random.randint(0, ${dicLen}-${1})    random
    #Convert To String    ${ranIndex}
    ${ranKey}    Set Variable    ${keys[${ranIndex}]}
    #    Select From List By Value    ${ranKey}
    ${ranIndex}    Set Variable If    '${ranKey}'=='Select'    ${ranIndex}+2    ${ranIndex}
    ${ignore first}    Get Substring    ${ranKey}    0    1
    ${ranIndex}    Set Variable If    '${ignore first}'=='*'    ${ranIndex}+1    ${ranIndex}
    ${ranIndex}    Evaluate    str(${ranIndex})
    Select From List By Index    ${locator}    ${ranIndex}

Fill_PAG_Info
    Execute Javascript    	var kit= document.getElementsByTagName('input'); \	for(var i=0; i < kit.length; i++) \	{	if(kit[i].type=='submit') \	\	{} \	\	else if (kit[i].placeholder=='Enter email') \	\	{kit[i].value=stringGen(12)+'@'+stringGen(12)+'.com';} \	\	else if (kit[i].placeholder=='Repeat email') \	\	{kit[i].value= kit[i-1].value} \	\	else if(kit[i].placeholder=='Enter your phone number') \	\	{kit[i].value=stringGen1(10);} \	\	else if(kit[i].placeholder=='Date of Birth') \	\	{kit[i].value='10/04/2015';} \	\	else \	\	{kit[i].value=stringGen(12);} \	} \	var kit1=document.getElementsByTagName('Select'); \	for(var i=0; i < kit1.length; i++) \	{ \	\	var items = kit1[i].getElementsByTagName('option'); \	\	var index = Math.floor(Math.random() * items.length); \	\	\ \	\	\ \	\	if (kit1[i].placeholder=='Male or Female') AND (index==0) \	\	{ \	\	\	index=2; \	\	} \	\	kit1[i].selectedIndex = index; \	} \	var kit2=document.getElementsByTagName('textarea'); \	kit2[0].value=stringGen(100); function stringGen(len) { \ \ \ \ var text = " "; \	\ \ \ \ \ var charset = "abcdefghijklmnopqrstuvwxyz0123456789"; \ \ \ \ \ for( var i=0; i < len; i++ ) \ \ \ \ \ \ \ \ text += charset.charAt(Math.floor(Math.random() * charset.length)); \ \ \ \ return text; } function stringGen1(len) { \ \ \ \ var text = " "; \	\ \ \ \ \ var charset = "0123456789"; \ \ \ \ \ for( var i=0; i < len; i++ ) \ \ \ \ \ \ \ \ text += charset.charAt(Math.floor(Math.random() * charset.length)); \ \ \ \ return text; }
    Click Element    type=submit

Search_flight
    #${val}    Select An Item from Listbox by Random    name=ctl00$ContentPlaceHolder1$drop_from    ${From}    #from
    #${val1}    Select An Item from Listbox by Random    name=ctl00$ContentPlaceHolder1$drop_from_day    ${Depart}
    #${val2}    Select An Item from Listbox by Random    name=ctl00$ContentPlaceHolder1$drop_from_month    ${MonY}
    #${val3}    Select An Item from Listbox by Random    name=ctl00$ContentPlaceHolder1$drop_to    ${To}    #to
    #Select From List By Value    id=ContentPlaceHolder1_drop_to    ${MANG}
    #${val4}    Select An Item from Listbox by Random    name=ctl00$ContentPlaceHolder1$drop_adults    ${Ad}    #adults
    #${val5}    Select An Item from Listbox by Random    name=ctl00$ContentPlaceHolder1$drop_child    ${Ch}    #Children
    #${val6}    Select An Item from Listbox by Random    name=ctl00$ContentPlaceHolder1$drop_infant    ${Inf}    #Infants
    Select any value from combobox by random    name=ctl00$ContentPlaceHolder1$drop_from    #Select
    Select any value from combobox by random    name=ctl00$ContentPlaceHolder1$drop_from_month
    Select any value from combobox by random    name=ctl00$ContentPlaceHolder1$drop_from_day
    Select any value from combobox by random    name=ctl00$ContentPlaceHolder1$drop_to
    Select any value from combobox by random    name=ctl00$ContentPlaceHolder1$drop_adults
    Select any value from combobox by random    name=ctl00$ContentPlaceHolder1$drop_child
    Select any value from combobox by random    name=ctl00$ContentPlaceHolder1$drop_infant
    Click Element    id=cmd_find
    ${BUTTON_CHECK}    Execute Javascript    var button_check= document.getElementsByTagName('button'); if (button_check.length==1) {return true;} else {return false;}
    Run Keyword If    ${BUTTON_CHECK}    Close Browser

Search_flight_without_des
    #${val}    Select An Item from Listbox by Random    name=ctl00$ContentPlaceHolder1$drop_from    ${From}    #from
    #${val1}    Select An Item from Listbox by Random    name=ctl00$ContentPlaceHolder1$drop_from_day    ${Depart}
    #${val2}    Select An Item from Listbox by Random    name=ctl00$ContentPlaceHolder1$drop_from_month    ${MonY}
    #${val3}    Select An Item from Listbox by Random    name=ctl00$ContentPlaceHolder1$drop_to    ${To}    #to
    #${val4}    Select An Item from Listbox by Random    name=ctl00$ContentPlaceHolder1$drop_adults    ${Ad}    #adults
    #${val5}    Select An Item from Listbox by Random    name=ctl00$ContentPlaceHolder1$drop_child    ${Ch}    #Children
    #${val6}    Select An Item from Listbox by Random    name=ctl00$ContentPlaceHolder1$drop_infant    ${Inf}    #Infants
    Select any value from combobox by random    name=ctl00$ContentPlaceHolder1$drop_from_month
    Select any value from combobox by random    name=ctl00$ContentPlaceHolder1$drop_from_day
    Select any value from combobox by random    name=ctl00$ContentPlaceHolder1$drop_to
    Select any value from combobox by random    name=ctl00$ContentPlaceHolder1$drop_adults
    Select any value from combobox by random    name=ctl00$ContentPlaceHolder1$drop_child
    Select any value from combobox by random    name=ctl00$ContentPlaceHolder1$drop_infant
    Click Element    id=cmd_find

Search_flight_without_arr
    #${val}    Select An Item from Listbox by Random    name=ctl00$ContentPlaceHolder1$drop_from    ${From}    #from
    #${val1}    Select An Item from Listbox by Random    name=ctl00$ContentPlaceHolder1$drop_from_day    ${Depart}
    #${val2}    Select An Item from Listbox by Random    name=ctl00$ContentPlaceHolder1$drop_from_month    ${MonY}
    #${val3}    Select An Item from Listbox by Random    name=ctl00$ContentPlaceHolder1$drop_to    ${To}    #to
    #Select From List By Value    id=ContentPlaceHolder1_drop_to    ${MANG}
    #${val4}    Select An Item from Listbox by Random    name=ctl00$ContentPlaceHolder1$drop_adults    ${Ad}    #adults
    #${val5}    Select An Item from Listbox by Random    name=ctl00$ContentPlaceHolder1$drop_child    ${Ch}    #Children
    #${val6}    Select An Item from Listbox by Random    name=ctl00$ContentPlaceHolder1$drop_infant    ${Inf}    #Infants
    Select any value from combobox by random    name=ctl00$ContentPlaceHolder1$drop_from    #Select
    Select any value from combobox by random    name=ctl00$ContentPlaceHolder1$drop_from_month
    Select any value from combobox by random    name=ctl00$ContentPlaceHolder1$drop_from_day
    Select any value from combobox by random    name=ctl00$ContentPlaceHolder1$drop_adults
    Select any value from combobox by random    name=ctl00$ContentPlaceHolder1$drop_child
    Select any value from combobox by random    name=ctl00$ContentPlaceHolder1$drop_infant
    Click Element    name=cmd_find

Fill_PAG_Info_invalid email
    Execute Javascript    var kit= document.getElementsByTagName('input'); \	for(var i=0; i < kit.length; i++) \	{	if(kit[i].type=='submit') \	\	{} \	\	else if (kit[i].placeholder=='Enter email') \	\	{kit[i].value=stringGen(12)+'.com';} \	\	else if (kit[i].placeholder=='Repeat email') \	\	{kit[i].value= kit[i-1].value} \	\	else if(kit[i].placeholder=='Enter your phone number') \	\	{kit[i].value=stringGen1(10);} \	\	else if(kit[i].placeholder=='Date of Birth') \	\	{kit[i].value='10/04/2015';} \	\	else \	\	{kit[i].value=stringGen(12);} \	} \	var kit1=document.getElementsByTagName('Select'); \	for(var i=0; i < kit1.length; i++) \	{ \	\	var items = kit1[i].getElementsByTagName('option'); \	\	var index = Math.floor(Math.random() * items.length); \	\	\ \	\	\ \	\	if (kit1[i].placeholder=='Male or Female') AND (index==0) \	\	{ \	\	\	index=2; \	\	} \	\	kit1[i].selectedIndex = index; \	} \	var kit2=document.getElementsByTagName('textarea'); \	kit2[0].value=stringGen(100); function stringGen(len) { \ \ \ \ var text = " "; \	\ \ \ \ \ var charset = "abcdefghijklmnopqrstuvwxyz0123456789"; \ \ \ \ \ for( var i=0; i < len; i++ ) \ \ \ \ \ \ \ \ text += charset.charAt(Math.floor(Math.random() * charset.length)); \ \ \ \ return text; } function stringGen1(len) { \ \ \ \ var text = " "; \	\ \ \ \ \ var charset = "0123456789"; \ \ \ \ \ for( var i=0; i < len; i++ ) \ \ \ \ \ \ \ \ text += charset.charAt(Math.floor(Math.random() * charset.length)); \ \ \ \ return text; }
    Click Element    type=submit

Fill_PAG_Info_invalid confirm email
    Execute Javascript    var kit= document.getElementsByTagName('input'); \	for(var i=0; i < kit.length; i++) \	{	if(kit[i].type=='submit') \	\	{} \	\	else if (kit[i].placeholder=='Enter email') \	\	{kit[i].value=stringGen(12)+'@'+stringGen(12)+'.com';} \	\	else if (kit[i].placeholder=='Repeat email') \	\	{kit[i].value= 'aaaaaaa'} \	\	else if(kit[i].placeholder=='Enter your phone number') \	\	{kit[i].value=stringGen1(10);} \	\	else if(kit[i].placeholder=='Date of Birth') \	\	{kit[i].value='10/04/2015';} \	\	else \	\	{kit[i].value=stringGen(12);} \	} \	var kit1=document.getElementsByTagName('Select'); \	for(var i=0; i < kit1.length; i++) \	{ \	\	var items = kit1[i].getElementsByTagName('option'); \	\	var index = Math.floor(Math.random() * items.length); \	\	\ \	\	\ \	\	if (kit1[i].placeholder=='Male or Female') AND (index==0) \	\	{ \	\	\	index=2; \	\	} \	\	kit1[i].selectedIndex = index; \	} \	var kit2=document.getElementsByTagName('textarea'); \	kit2[0].value=stringGen(100); function stringGen(len) { \ \ \ \ var text = " "; \	\ \ \ \ \ var charset = "abcdefghijklmnopqrstuvwxyz0123456789"; \ \ \ \ \ for( var i=0; i < len; i++ ) \ \ \ \ \ \ \ \ text += charset.charAt(Math.floor(Math.random() * charset.length)); \ \ \ \ return text; } function stringGen1(len) { \ \ \ \ var text = " "; \	\ \ \ \ \ var charset = "0123456789"; \ \ \ \ \ for( var i=0; i < len; i++ ) \ \ \ \ \ \ \ \ text += charset.charAt(Math.floor(Math.random() * charset.length)); \ \ \ \ return text; }
    Click Element    type=submit

Fill_PAG_Info_email not match
    Execute Javascript    var kit= document.getElementsByTagName('input'); \	for(var i=0; i < kit.length; i++) \	{	if(kit[i].type=='submit') \	\	{} \	\	else if (kit[i].placeholder=='Enter email') \	\	{kit[i].value=stringGen(12)+'@'+stringGen(12)+'.com';} \	\	else if (kit[i].placeholder=='Repeat email') \	\	{kit[i].value= stringGen(13)+'@'+stringGen(12)+'.com';} \	\	else if(kit[i].placeholder=='Enter your phone number') \	\	{kit[i].value=stringGen1(10);} \	\	else if(kit[i].placeholder=='Date of Birth') \	\	{kit[i].value='10/04/2015';} \	\	else \	\	{kit[i].value=stringGen(12);} \	} \	var kit1=document.getElementsByTagName('Select'); \	for(var i=0; i < kit1.length; i++) \	{ \	\	var items = kit1[i].getElementsByTagName('option'); \	\	var index = Math.floor(Math.random() * items.length); \	\	\ \	\	\ \	\	if (kit1[i].placeholder=='Male or Female') AND (index==0) \	\	{ \	\	\	index=2; \	\	} \	\	kit1[i].selectedIndex = index; \	} \	var kit2=document.getElementsByTagName('textarea'); \	kit2[0].value=stringGen(100); function stringGen(len) { \ \ \ \ var text = " "; \	\ \ \ \ \ var charset = "abcdefghijklmnopqrstuvwxyz0123456789"; \ \ \ \ \ for( var i=0; i < len; i++ ) \ \ \ \ \ \ \ \ text += charset.charAt(Math.floor(Math.random() * charset.length)); \ \ \ \ return text; } function stringGen1(len) { \ \ \ \ var text = " "; \	\ \ \ \ \ var charset = "0123456789"; \ \ \ \ \ for( var i=0; i < len; i++ ) \ \ \ \ \ \ \ \ text += charset.charAt(Math.floor(Math.random() * charset.length)); \ \ \ \ return text; }
    Click Element    type=submit

Choose_An_AirPlane
    ${RadioPrice}    Execute JavaScript    var arrVals = new Array();var iradios = document.getElementsByName("s01");for(var i=0; i < iradios.length; i++){arrVals.push(iradios[i].value);}return arrVals;
    ${RadioPricelen}    Get Length    ${RadioPrice}
    ${PriceRandindex}    Evaluate    random.randint(0, ${RadioPricelen}-${1})    random
    ${ranKey}    Set Variable    ${RadioPrice[${PriceRandindex}]}
    Select Radio Button    s01    ${ranKey}
    Click Element    name=ctl00$ContentPlaceHolder1$cmd_next

Resume_if have ticket
    Choose_An_AirPlane    #Page 2: Choose an airplain for flying
    Fill_PAG_Info    #Submit data
    Element Should Be Visible    class=light-blue

Resume_if have ticket_invalid email
    Choose_An_AirPlane    #Page 2: Choose an airplain for flying
    Fill_PAG_Info_invalid email    #Submit data
    Alert Should Be Present    Inavlid email
    Close Browser

Resume_if have ticket_invalid \ confirm email
    Choose_An_AirPlane    #Page 2: Choose an airplain for flying
    Fill_PAG_Info_invalid confirm email    #Submit data
    Alert Should Be Present    Inavlid email
    Close Browser

Resume_if have ticket_invalid \ email not match email
    Choose_An_AirPlane    #Page 2: Choose an airplain for flying
    Fill_PAG_Info_email not match    #Submit data
    Alert Should Be Present    Your confirm email is not match with your email.
    Close Browser
