[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md) > [7.14. Function Test Editor](7-14-function-test-editor.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.14.18. Category - Module balancing</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-14-17-category-connection.md">Prev</a> </td><th align="center" width="60%">7.14. Function Test Editor</th><td align="right" width="20%"> <a accesskey="n" href="7-14-19-category-flash.md">Next</a></td></tr></table>

---

#### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ModulBalancing"></a>7.14.18. Category - Module balancing

This category contains action elements for communication between the ODIS tester and the module balancer. The following action elements are used:

- [Section 7.14.18.1, “Request module hardware info”](7-14-18-category-module-balancing.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ModulBalancing.Abfrage_Modul_Hardware_Info "7.14.18.1. Request module hardware info")
- [Section 7.14.18.2, “Action Element - Module Data Request”](7-14-18-category-module-balancing.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ModulBalancing.Abfrage_Module_Daten "7.14.18.2. Action Element - Module Data Request")
- [Section 7.14.18.3, “Action element - MB determination”](7-14-18-category-module-balancing.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ModulBalancing.Ermittlung_MBs "7.14.18.3. Action element - MB determination")
- [Section 7.14.18.4, “Action Element - MB Connection”](7-14-18-category-module-balancing.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ModulBalancing.Verbindung_MB "7.14.18.4. Action Element - MB Connection")
- [Section 7.14.18.5, “Action Element - Request MB Info”](7-14-18-category-module-balancing.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ModulBalancing.Abfrage_MB_Info "7.14.18.5. Action Element - Request MB Info")
- [Section 7.14.18.6, “Action Element - Request MB Status”](7-14-18-category-module-balancing.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ModulBalancing.Abfrage_MB_Status "7.14.18.6. Action Element - Request MB Status")
- [Section 7.14.18.7, “Action Element - Initiate MB Self-Test”](7-14-18-category-module-balancing.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ModulBalancing.Selbsttest_MB_Initiieren "7.14.18.7. Action Element - Initiate MB Self-Test")
- [Section 7.14.18.8, “Action Element - Start Balancing Procedure”](7-14-18-category-module-balancing.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ModulBalancing.Start_Balancing_Vorgang "7.14.18.8. Action Element - Start Balancing Procedure")
- [Section 7.14.18.9, “Action Element - Request (Dis)charging Parameters”](7-14-18-category-module-balancing.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ModulBalancing.EntLadeparameter_Abfragen "7.14.18.9. Action Element - Request (Dis)charging Parameters")
- [Section 7.14.18.10, “Action Element - MB Process Status Request”](7-14-18-category-module-balancing.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ModulBalancing.Statusabfrage_MB_Vorgang "7.14.18.10. Action Element - MB Process Status Request")
- [Section 7.14.18.11, “MB error message”](7-14-18-category-module-balancing.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ModulBalancing.Fehlermeldung_unterdr%C3%BCcken "7.14.18.11. MB error message")
- [Section 7.14.18.12, “Action Element - MB Qualification Report”](7-14-18-category-module-balancing.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ModulBalancing.Qualifizierungsbericht_MB "7.14.18.12. Action Element - MB Qualification Report")
- [Section 7.14.18.13, “Action Element - MB Classification Report”](7-14-18-category-module-balancing.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ModulBalancing.Klassifizierungsbericht_MB "7.14.18.13. Action Element - MB Classification Report")

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ModulBalancing.Abfrage_Modul_Hardware_Info"></a>7.14.18.1. Request module hardware info

The "Request module hardware info" action element can be seen in [Figure 495, “Request module hardware info”](7-14-18-category-module-balancing.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ModulBalancing.Abfrage_Modul_Hardware_Info "Figure 495. Request module hardware info").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ModulBalancing.Abfrage_Modul_Hardware_Info"></a>

![Figure: Request module hardware info](images/fte_arbeitsflaeche_module_balancing_abfrage_module_hardware_info.png)

**Figure 495. Request module hardware info**

You can use this action element to request the part and serial number as well as the type of input made.

###### <a id="d4e26094"></a>7.14.18.1.1. Part number

In this mandatory field, the part number is set as the response parameter. The variable must have a string type.

###### <a id="d4e26097"></a>7.14.18.1.2. Serial number

In this mandatory field, the part number is set as the response parameter. The variable must have a string type.

###### <a id="d4e26100"></a>7.14.18.1.3. Entry type

In this mandatory field, the entry type is set as the response parameter. A string is required here as the type. Possible values are “A” (for scanned), “E” (for edited), “M” (for manually added) and “” (empty string in case of cancellation).

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ModulBalancing.Abfrage_Module_Daten"></a>7.14.18.2. Action Element - Module Data Request

The "Module data request" action element can be seen in [Figure 496, “Module Data Request Action Element”](7-14-18-category-module-balancing.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ModulBalancing.Abfrage_Module_Daten "Figure 496. Module Data Request Action Element").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ModulBalancing.Abfrage_Module_Daten"></a>

![Image : Module data request action element](images/fte_arbeitsflaeche_module_balancing_abfrage_module_daten.png)

**Figure 496. Module Data Request Action Element**

You can initiate determination of charging and discharging parameters (characteristic curves) and the suitable adapter cable using this action element.

###### <a id="d4e26116"></a>7.14.18.2.1. Part number

The part number of the HV module is set as the input parameter in this field. The variable must have a string type (variable and literal are permitted)

###### <a id="d4e26119"></a>7.14.18.2.2. Tool number

The tool number of the suitable adapter cable is set as the response parameter in this field. A string is required here as the type.

###### <a id="d4e26122"></a>7.14.18.2.3. Error code

In this mandatory field, the error code is set as the response parameter. An integer is required here as the type.

See [Section 7.14.18.14.1, “Error Code and Error Text”](7-14-18-category-module-balancing.md#Funktionstesteditor.Allgemeine_Funktionalitaet.Fehlercode "7.14.18.14.1. Error Code and Error Text").

###### <a id="d4e26127"></a>7.14.18.2.4. Error text

In this optional field, the error text can also be set as the response parameter. The variable must have a string type.

See [Section 7.14.18.14.1, “Error Code and Error Text”](7-14-18-category-module-balancing.md#Funktionstesteditor.Allgemeine_Funktionalitaet.Fehlercode "7.14.18.14.1. Error Code and Error Text").

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ModulBalancing.Ermittlung_MBs"></a>7.14.18.3. Action element - MB determination

The "MB determination" action element can be seen in [Figure 497, “MB Determination Action Element”](7-14-18-category-module-balancing.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ModulBalancing.Ermittlung_MBs "Figure 497. MB Determination Action Element").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ModulBalancing.Ermittlung_MBs"></a>

![Figure: MB determination action element](images/fte_arbeitsflaeche_module_balancing_ermittlung_mbs.png)

**Figure 497. MB Determination Action Element**

You can use this action element to determine the usable module balancers with the corresponding aliases.

###### <a id="d4e26145"></a>7.14.18.3.1. Connection aliases

The list of usable aliases is written in the array variable connection aliases. The array must be a ‘string’ data type and it is mandatory to enter the array variable. Every element of the array corresponds to an alias. An alias can be selected in [Section 7.14.18.4, “Action Element - MB Connection”](7-14-18-category-module-balancing.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ModulBalancing.Verbindung_MB "7.14.18.4. Action Element - MB Connection") to establish the connection to the matching module balancer.

###### <a id="d4e26149"></a>7.14.18.3.2. Error code

In this field, an error code is set as the response parameter. An integer is required here as the type.

See [Section 7.14.18.14.1, “Error Code and Error Text”](7-14-18-category-module-balancing.md#Funktionstesteditor.Allgemeine_Funktionalitaet.Fehlercode "7.14.18.14.1. Error Code and Error Text").

###### <a id="d4e26154"></a>7.14.18.3.3. Error text

In this field, the error text can also be set as the response parameter. The variable must have a string type.

See [Section 7.14.18.14.1, “Error Code and Error Text”](7-14-18-category-module-balancing.md#Funktionstesteditor.Allgemeine_Funktionalitaet.Fehlercode "7.14.18.14.1. Error Code and Error Text").

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ModulBalancing.Verbindung_MB"></a>7.14.18.4. Action Element - MB Connection

The "MB connection" action element can be seen in [Figure 498, “MB Connection Action Element”](7-14-18-category-module-balancing.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ModulBalancing.Verbindung_MB "Figure 498. MB Connection Action Element").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ModulBalancing.Verbindung_MB"></a>

![Image: MB connection action element](images/fte_arbeitsflaeche_module_balancing_verbindung_mb.png)

**Figure 498. MB Connection Action Element**

You can establish or end a connection between the ODIS tester and module balancer using this action element.

###### <a id="d4e26172"></a>7.14.18.4.1. Establishing a Connection

If the connection to a free MB is to be made, this is possible and optional by selecting one of the determined connection aliases from the array variable.

If the connection to an active MB is to be made, this is possible by specifying the process identifier. The field for the process identifier is a string type and is mandatory.

###### <a id="d4e26176"></a>7.14.18.4.2. Disconnect

If the connection should be ended.

###### <a id="d4e26179"></a>7.14.18.4.3. Error code

In this field, an error code is set as the response parameter. An integer is required here as the type.

See [Section 7.14.18.14.1, “Error Code and Error Text”](7-14-18-category-module-balancing.md#Funktionstesteditor.Allgemeine_Funktionalitaet.Fehlercode "7.14.18.14.1. Error Code and Error Text").

###### <a id="d4e26184"></a>7.14.18.4.4. Error text

In this field, the error text can also be set as the response parameter. The variable must have a string type.

See [Section 7.14.18.14.1, “Error Code and Error Text”](7-14-18-category-module-balancing.md#Funktionstesteditor.Allgemeine_Funktionalitaet.Fehlercode "7.14.18.14.1. Error Code and Error Text").

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ModulBalancing.Abfrage_MB_Info"></a>7.14.18.5. Action Element - Request MB Info

The "Request MB Info" action element can be seen in [Figure 499, “Request MB Info Action Element”](7-14-18-category-module-balancing.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ModulBalancing.Abfrage_MB_Info "Figure 499. Request MB Info Action Element").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ModulBalancing.Abfrage_MB_Info"></a>

![Figure: Request MB Info](images/fte_arbeitsflaeche_module_balancing_abfrage_mb_info.png)

**Figure 499. Request MB Info Action Element**

You can request the version and calibration information of the module balancer with this action element.

###### <a id="d4e26202"></a>7.14.18.5.1. Driver version

In this field, the driver version is set as the response parameter. The variable must have a string type.

###### <a id="d4e26205"></a>7.14.18.5.2. Hardware version

In this field, the hardware version is set as the response parameter. The variable must have a string type.

###### <a id="d4e26208"></a>7.14.18.5.3. Software version

In this field, the software version is set as the response parameter. The variable must have a string type.

###### <a id="d4e26211"></a>7.14.18.5.4. Tool number

In this field, the tool number is set as the response parameter. The variable must have a string type

###### <a id="d4e26214"></a>7.14.18.5.5. Calibration status

The calibration status is set as the response parameter in this field. The variable must have a Boolean type. If the Boolean value is true, the device is calibrated and can be used. If the Boolean value is false, calibration must occur before further use.

###### <a id="d4e26217"></a>7.14.18.5.6. Date of last calibration

The date of the last calibration is set as the response parameter in this field. The variable must have a string type.

###### <a id="d4e26220"></a>7.14.18.5.7. Date of next calibration

The date of the last calibration is set as the response parameter in this field. The variable must have a string type.

###### <a id="d4e26223"></a>7.14.18.5.8. Error code

In this mandatory field, the error code is set as the response parameter. An integer is required here as the type.

See [Section 7.14.18.14.1, “Error Code and Error Text”](7-14-18-category-module-balancing.md#Funktionstesteditor.Allgemeine_Funktionalitaet.Fehlercode "7.14.18.14.1. Error Code and Error Text").

###### <a id="d4e26228"></a>7.14.18.5.9. Error text

In this field, the error text can also be set as the response parameter. The variable must have a string type.

See [Section 7.14.18.14.1, “Error Code and Error Text”](7-14-18-category-module-balancing.md#Funktionstesteditor.Allgemeine_Funktionalitaet.Fehlercode "7.14.18.14.1. Error Code and Error Text").

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ModulBalancing.Abfrage_MB_Status"></a>7.14.18.6. Action Element - Request MB Status

The "Request MB Status" action element can be seen in [Figure 500, “Action Element Request MB Status”](7-14-18-category-module-balancing.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ModulBalancing.Abfrage_MB_Status "Figure 500. Action Element Request MB Status").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ModulBalancing.Abfrage_MB_Status"></a>

![Image: Request MB Status](images/fte_arbeitsflaeche_module_balancing_abfrage_mb_status.png)

**Figure 500. Action Element Request MB Status**

You can request the status of the module balancer with this action element.

###### <a id="d4e26246"></a>7.14.18.6.1. Status

In this mandatory field, the status is set as the response parameter. The variable must have a string type.

###### <a id="d4e26249"></a>7.14.18.6.2. Error code

In this mandatory field, the error code is set as the response parameter. An integer is required here as the type.

See [Section 7.14.18.14.1, “Error Code and Error Text”](7-14-18-category-module-balancing.md#Funktionstesteditor.Allgemeine_Funktionalitaet.Fehlercode "7.14.18.14.1. Error Code and Error Text").

###### <a id="d4e26254"></a>7.14.18.6.3. Error text

In this field, the error text can also be set as the response parameter. The variable must have a string type.

See [Section 7.14.18.14.1, “Error Code and Error Text”](7-14-18-category-module-balancing.md#Funktionstesteditor.Allgemeine_Funktionalitaet.Fehlercode "7.14.18.14.1. Error Code and Error Text").

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ModulBalancing.Selbsttest_MB_Initiieren"></a>7.14.18.7. Action Element - Initiate MB Self-Test

The action element “Initiate MB Self-Test” gives the GFF author the option to perform a hardware self-test on the connected device. A self-test should only be performed if the device is in the ‘Balancing not active’ state. The [Table 118, “Error Codes and Error Texts during Module Balancing”](7-14-18-category-module-balancing.md#table.fehlercodes "Table 118. Error Codes and Error Texts during Module Balancing") describes the possible errors during the self-test implementation (see the error codes 45, 48, 61).

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ModulBalancing.Start_Balancing_Vorgang"></a>7.14.18.8. Action Element - Start Balancing Procedure

The "Start balancing procedure" action element can be seen in [Figure 501, “Start Balancing Procedure Action Element”](7-14-18-category-module-balancing.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ModulBalancing.Start_Balancing_Vorgang "Figure 501. Start Balancing Procedure Action Element").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ModulBalancing.Start_Balancing_Vorgang"></a>

![Image: Start balancing procedure action element](images/fte_arbeitsflaeche_module_balancing_start_balancing_vorgang.png)

**Figure 501. Start Balancing Procedure Action Element**

You can initiate the charging/discharging process (balancing) on the module balancer using this action element.

###### <a id="d4e26276"></a>7.14.18.8.1. Part number

The part number is set as the input parameter in this mandatory field. The variable must have a string type (variable and literal are permitted).

###### <a id="d4e26279"></a>7.14.18.8.2. Serial number

The serial number is set as the input parameter in this mandatory field. The variable must have a string type (variable and literal are permitted).

###### <a id="d4e26282"></a>7.14.18.8.3. Target voltage

The target voltage calculated from the GFF is set as the input parameter in this mandatory field. The variable must have a double type (variable and literal are permitted).

###### <a id="d4e26285"></a>7.14.18.8.4. Process identifier

In this mandatory field, the process identifier is set as the response parameter. The variable must have a string type.

###### <a id="d4e26288"></a>7.14.18.8.5. Status

The MB status is set as the response parameter in this optional field. The variable must have a string type.

###### <a id="d4e26291"></a>7.14.18.8.6. Error code

In this mandatory field, the error code is set as the response parameter. An integer is required here as the type.

See [Section 7.14.18.14.1, “Error Code and Error Text”](7-14-18-category-module-balancing.md#Funktionstesteditor.Allgemeine_Funktionalitaet.Fehlercode "7.14.18.14.1. Error Code and Error Text").

###### <a id="d4e26296"></a>7.14.18.8.7. Error text

In this optional field, the error text can also be set as the response parameter. The variable must have a string type.

See [Section 7.14.18.14.1, “Error Code and Error Text”](7-14-18-category-module-balancing.md#Funktionstesteditor.Allgemeine_Funktionalitaet.Fehlercode "7.14.18.14.1. Error Code and Error Text").

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ModulBalancing.EntLadeparameter_Abfragen"></a>7.14.18.9. Action Element - Request (Dis)charging Parameters

The "Request (dis)charging parameters" action element can be seen in [Figure 502, “Request (Dis)charging Parameters Action Element”](7-14-18-category-module-balancing.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ModulBalancing.EntLadeparameter_Abfragen "Figure 502. Request (Dis)charging Parameters Action Element").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ModulBalancing.EntLadeparameter_Abfragen"></a>

![Image: Request (dis)charging parameters action element](images/fte_arbeitsflaeche_module_balancing_ent_ladeparameter_abfragen.png)

**Figure 502. Request (Dis)charging Parameters Action Element**

You can request the charging/discharging parameters for the balancing process from the module balancer using this action element. At least one field of the input parameters must be set.

###### <a id="d4e26314"></a>7.14.18.9.1. Voltage [V]

The voltage [V] is set as the response parameter in this field. The variable must have a double type.

###### <a id="d4e26317"></a>7.14.18.9.2. Current [A]

The current [A] is set as the response parameter in this field. The variable must have a double type.

###### <a id="d4e26320"></a>7.14.18.9.3. Resistance [Ohm]

The internal resistance is set as the response parameter in this field. The variable must have a double type.

###### <a id="d4e26323"></a>7.14.18.9.4. Module temperature [Celsius]

The module temperature [Celsius] is set as the response parameter in this field. The variable must have a double type

###### <a id="d4e26326"></a>7.14.18.9.5. Previous charging/discharging duration [sec.]

The previous charging/discharging duration t-gest in [seconds] is set as the response parameter in this field. The variable must have an integer type.

###### <a id="d4e26329"></a>7.14.18.9.6. Remaining charging/discharging duration [sec.]

The calculated remaining time t-rest in [seconds] is set as the response parameter in this field. The variable must have an integer type.

###### <a id="d4e26332"></a>7.14.18.9.7. Error code

In this mandatory field, the error code is set as the response parameter. An integer is required here as the type.

See [Section 7.14.18.14.1, “Error Code and Error Text”](7-14-18-category-module-balancing.md#Funktionstesteditor.Allgemeine_Funktionalitaet.Fehlercode "7.14.18.14.1. Error Code and Error Text").

###### <a id="d4e26337"></a>7.14.18.9.8. Error text

In this field, the error text can also be set as the response parameter. The variable must have a string type.

See [Section 7.14.18.14.1, “Error Code and Error Text”](7-14-18-category-module-balancing.md#Funktionstesteditor.Allgemeine_Funktionalitaet.Fehlercode "7.14.18.14.1. Error Code and Error Text").

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ModulBalancing.Statusabfrage_MB_Vorgang"></a>7.14.18.10. Action Element - MB Process Status Request

The "MB process status request" action element can be seen in [Figure 503, “MB Process Status Request Action Element”](7-14-18-category-module-balancing.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ModulBalancing.Statusabfrage_MB_Vorgang "Figure 503. MB Process Status Request Action Element").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ModulBalancing.Statusabfrage_MB_Vorgang"></a>

![Figure: MB process status request action element](images/fte_arbeitsflaeche_module_balancing_statusabfrage_mb_vorgang.png)

**Figure 503. MB Process Status Request Action Element**

You can determine the status of the balancing process using this action element.

###### <a id="d4e26355"></a>7.14.18.10.1. Process identifier

In this field, the process identifier is set as the response parameter. The variable must have a string type (only variables are permitted).

###### <a id="d4e26358"></a>7.14.18.10.2. Status

The balancing process status is set as the response parameter in this mandatory field. The variable must have a string type (only variables are permitted).

###### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ModulBalancing.Statusabfrage_MB_Vorgang.Statuscode"></a>7.14.18.10.2.1. Status code

The status code supplies a combination of current status information on the balancing process as a four-digit character string, in which every character can adopt a value from 0 - 9. The individual characters have the following meanings:

<a id="table.statuscodes"></a>

<table border="1" summary="Status codes"><colgroup><col/><col/><col/></colgroup><thead><tr bgcolor="#EEEEEE"><th>Status code</th><th>Error text</th><th>Meaning</th></tr></thead><tbody valign="top"><tr><td valign="top">Character 1: x---</td><td valign="top">0</td><td valign="top">No active charging process. Balancer not ready for use. Instruction: ‘Switch on device.’</td></tr><tr><td valign="top">Character 1: x---</td><td valign="top">1</td><td valign="top">No active charging process. Balancer available for a new charging process.</td></tr><tr><td valign="top">Character 1: x---</td><td valign="top">2</td><td valign="top">Charging process active. A module is being balanced.</td></tr><tr><td valign="top">Character 1: x---</td><td valign="top">3</td><td valign="top">Charging process active. Balancing paused.</td></tr><tr><td valign="top">Character 1: x---</td><td valign="top">4</td><td valign="top">No active charging process. Balancing interrupted.</td></tr><tr><td valign="top">Character 1: x---</td><td valign="top">5</td><td valign="top">Charging process active. Balancing ended. Qualification data available.</td></tr><tr><td valign="top">Character 1: x---</td><td valign="top">6</td><td valign="top">No active charging process. Balancer performing a self-test.</td></tr><tr><td valign="top">Character 1: x---</td><td valign="top">7</td><td valign="top">No active charging process. Balancer requires a self-test. Instruction: ‘Disconnect adapter cable, start self-test’</td></tr><tr><td valign="top">Character 1: x---</td><td valign="top">8</td><td valign="top">No active charging process. Balancer creates a classification report.</td></tr><tr><td valign="top">Character 1: x---</td><td valign="top">9</td><td valign="top">The status of the balancer could not be determined after a significant problem.</td></tr><tr><td valign="top">Character 2: -x--</td><td valign="top">0</td><td valign="top">The adapter cable is incorrect or is not connected.</td></tr><tr><td valign="top">Character 2: -x--</td><td valign="top">1</td><td valign="top">The correct adapter cable is connected.</td></tr><tr><td valign="top">Character 2: -x--</td><td valign="top">2</td><td valign="top">There is currently no information available about the adapter cable to be used.</td></tr><tr><td valign="top">Character 3: --x-</td><td valign="top">0</td><td valign="top">The cover guard has not been properly attached.</td></tr><tr><td valign="top">Character 3: --x-</td><td valign="top">1</td><td valign="top">The cover guard has been properly attached.</td></tr><tr><td valign="top">Character 3: --x-</td><td valign="top">2</td><td valign="top">No cover guard is installed on the device.</td></tr><tr><td valign="top">Character 4: ---x</td><td valign="top">0</td><td valign="top">Reverse feed is switched off.</td></tr><tr><td valign="top">Character 4: ---x</td><td valign="top">1</td><td valign="top">Reverse feed is switched on but all requirements for reverse feed are not met.</td></tr><tr><td valign="top">Character 4: ---x</td><td valign="top">2</td><td valign="top">Reverse feed is switched on, all requirements are met, and the feature is active in case of a discharge.</td></tr><tr><td valign="top">Character 4: ---x</td><td valign="top">3</td><td valign="top">Reverse feed is switched on and currently active.</td></tr><tr><td valign="top">Character 4: ---x</td><td valign="top">9</td><td valign="top">The status of the reverse feed could not be determined after a significant problem.</td></tr></tbody></table>

**Table 116. Status codes**

<a id="d4e26462"></a>

<table border="1" summary="Status Codes - Examples"><colgroup><col/><col/></colgroup><thead><tr bgcolor="#EEEEEE"><th>Status code</th><th>Meaning</th></tr></thead><tbody valign="top"><tr><td valign="top">2123</td><td valign="top">Module is being balanced, adapter cable OK, no protective cover installed, reverse feed active.</td></tr><tr><td valign="top">0220</td><td valign="top">Balancer is not switched on, no information about the adapter cable, no protective cover installed, reverse feed switched off.</td></tr><tr><td valign="top">5122</td><td valign="top">Balancing ended, adapter cable OK, no protective cover installed, reverse feed switched on.</td></tr></tbody></table>

**Table 117. Status Codes - Examples**

###### <a id="d4e26481"></a>7.14.18.10.3. Error code

In this mandatory field, the error code is set as the response parameter. An integer is required here as the type.

See [Section 7.14.18.14.1, “Error Code and Error Text”](7-14-18-category-module-balancing.md#Funktionstesteditor.Allgemeine_Funktionalitaet.Fehlercode "7.14.18.14.1. Error Code and Error Text").

###### <a id="d4e26486"></a>7.14.18.10.4. Error text

In this field, the error text can also be set as the response parameter. The variable must have a string type.

See [Section 7.14.18.14.1, “Error Code and Error Text”](7-14-18-category-module-balancing.md#Funktionstesteditor.Allgemeine_Funktionalitaet.Fehlercode "7.14.18.14.1. Error Code and Error Text").

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ModulBalancing.Fehlermeldung_unterdr%C3%BCcken"></a>7.14.18.11. MB error message

The "MB error message" action element can be seen in [Figure 504, “MB error message”](7-14-18-category-module-balancing.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ModulBalancing.Fehlermeldung_unterdr%C3%BCcken "Figure 504. MB error message").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ModulBalancing.Fehlermeldung_unterdr%C3%BCcken"></a>

![Figure: MB error message](http://127.0.0.1:55991/help/topic/MasterData_Client_Control/html/images/fte_arbeitsflaeche_module_balancing_fehlermeldung_unterdr%C3%83%C2%BCcken.png)

**Figure 504. MB error message**

You can use this action element to switch the output of error / message dialogs on or off. “On” means the error / message dialogs are permitted, while “off” means they are suppressed.

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ModulBalancing.Qualifizierungsbericht_MB"></a>7.14.18.12. Action Element - MB Qualification Report

The "MB qualification report" action element can be seen in [Figure 505, “MB Qualification Report Action Element”](7-14-18-category-module-balancing.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ModulBalancing.Qualifizierungsbericht_MB "Figure 505. MB Qualification Report Action Element").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ModulBalancing.Qualifizierungsbericht_MB"></a>

![Image: MB qualification report action element](images/fte_arbeitsflaeche_module_balancing_qualifizierunsbericht_mb.png)

**Figure 505. MB Qualification Report Action Element**

With this action element, you can request the qualification data, the status of the qualification data of the balanced module and the release status of the module balancer as well as release the module balancer.

###### <a id="d4e26517"></a>7.14.18.12.1. Qualification data status

The qualification data status is set as the response parameter in this mandatory field. The variable must have a Boolean type.

###### <a id="d4e26520"></a>7.14.18.12.2. Module balance release status

The MB status release is set as the response parameter in this mandatory field. The variable must have a Boolean type.

###### <a id="d4e26523"></a>7.14.18.12.3. Module voltage reached [V]

The module voltage reached [V] is set as the response parameter in this mandatory field. The variable must have a double type.

###### <a id="d4e26526"></a>7.14.18.12.4. Cell voltages reached [V]

The cell voltages reached [V] are set as the response parameter in this mandatory field. The variable must have a double array type.

###### <a id="d4e26529"></a>7.14.18.12.5. Maximum charge/discharge current reached [A]

The maximum reached charge/discharge current [A] is set as the response parameter in this mandatory field. The variable must have a double type.

###### <a id="d4e26532"></a>7.14.18.12.6. Maximum overcurrent [A]

the maximum current exceedance [A] is set as the response parameter in this mandatory field. The variable must have a double type.

###### <a id="d4e26535"></a>7.14.18.12.7. Maximum charge/discharge voltage reached [V]

The maximum reached charge/discharge voltage [V] is set as the response parameter in this mandatory field. The variable must have a double type.

###### <a id="d4e26538"></a>7.14.18.12.8. Maximum voltage overload [V]

The maximum voltage exceedance [V] is set as the response parameter in this mandatory field. The variable must have a double type.

###### <a id="d4e26541"></a>7.14.18.12.9. Maximum temperature reached [Celsius]

The maximum temperature reached [Celsius] is set as the response parameter in this mandatory field. The variable must have a double type.

###### <a id="d4e26544"></a>7.14.18.12.10. Maximum temperature overshoot [Kelvin]

The maximum temperature exceedance [Kelvin] is set as the response parameter in this mandatory field. The variable must have a double type.

###### <a id="d4e26547"></a>7.14.18.12.11. Duration of the Balancing Process [sec]

The duration of the balancing process [sec] is set as the response parameter in this mandatory field. The variable must have a short type.

###### <a id="d4e26550"></a>7.14.18.12.12. Error code

In this mandatory field, the error code is set as the response parameter. An integer is required here as the type.

See [Section 7.14.18.14.1, “Error Code and Error Text”](7-14-18-category-module-balancing.md#Funktionstesteditor.Allgemeine_Funktionalitaet.Fehlercode "7.14.18.14.1. Error Code and Error Text").

###### <a id="d4e26555"></a>7.14.18.12.13. Error text

In this field, the error text can also be set as the response parameter. The variable must have a string type.

See [Section 7.14.18.14.1, “Error Code and Error Text”](7-14-18-category-module-balancing.md#Funktionstesteditor.Allgemeine_Funktionalitaet.Fehlercode "7.14.18.14.1. Error Code and Error Text").

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ModulBalancing.Klassifizierungsbericht_MB"></a>7.14.18.13. Action Element - MB Classification Report

The "MB classification report" action element can be seen in [Figure 506, “MB Classification Report Action Element”](7-14-18-category-module-balancing.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ModulBalancing.Klassifizierungsbericht_MB "Figure 506. MB Classification Report Action Element").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ModulBalancing.Klassifizierungsbericht_MB"></a>

![Image: MB classification report action element](images/fte_arbeitsflaeche_module_balancing_klassifizierungsbericht_mb.png)

**Figure 506. MB Classification Report Action Element**

Using this action element, classification data of the module to be classified can be queried and classification can be initiated.

###### <a id="d4e26573"></a>7.14.18.13.1. Part number

The part number of the module to be classified is set as the input parameter in this mandatory field. The variable must have a string type (variable and literal are permitted).

###### <a id="d4e26576"></a>7.14.18.13.2. Serial number

The serial number of the module to be classified is set as the input parameter in this mandatory field. The variable must have a string type (variable and literal are permitted).

###### <a id="d4e26579"></a>7.14.18.13.3. Module voltage [V]

The module voltage reached [V] is set as the response parameter in this mandatory field. The variable must have a double type.

###### <a id="d4e26582"></a>7.14.18.13.4. Cell voltages [V]

The cell voltages reached [V] (cell voltage of each individual cell) are set as the response parameter in this mandatory field. The variable must have a double array type.

###### <a id="d4e26585"></a>7.14.18.13.5. Average cell voltages [V]

The average value [V] of all voltages is set as the response parameter in this mandatory field. The variable must have a double type.

###### <a id="d4e26588"></a>7.14.18.13.6. Maximum voltage difference [V]

The maximum voltage difference [V] between the lowest and highest cell voltage is set as the response parameter in this mandatory field. The variable must have a double type.

###### <a id="d4e26591"></a>7.14.18.13.7. Module charge level [%]

The charge level of the module [%] is set as the response parameter in this mandatory field. The variable must have a double type.

###### <a id="d4e26594"></a>7.14.18.13.8. Cell charge levels [%]

The charge level of each individual cell [%] is set as the response parameter in this mandatory field. The variable must have a double type.

###### <a id="d4e26597"></a>7.14.18.13.9. Module temperature [Celsius]

The module temperature [Celsius] is set as the response parameter in this field. The variable must have a double type.

###### <a id="d4e26600"></a>7.14.18.13.10. Error code

In this mandatory field, the error code is set as the response parameter. An integer is required here as the type.

See [Section 7.14.18.14.1, “Error Code and Error Text”](7-14-18-category-module-balancing.md#Funktionstesteditor.Allgemeine_Funktionalitaet.Fehlercode "7.14.18.14.1. Error Code and Error Text").

###### <a id="d4e26605"></a>7.14.18.13.11. Error text

In this field, the error text can also be set as the response parameter. The variable must have a string type.

See [Section 7.14.18.14.1, “Error Code and Error Text”](7-14-18-category-module-balancing.md#Funktionstesteditor.Allgemeine_Funktionalitaet.Fehlercode "7.14.18.14.1. Error Code and Error Text").

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ModulBalancing.Anhang"></a>7.14.18.14. General Module Balancing Functions

###### <a id="Funktionstesteditor.Allgemeine_Funktionalitaet.Fehlercode"></a>7.14.18.14.1. Error Code and Error Text

The following error codes and error texts are possible as response parameters.

<a id="table.fehlercodes"></a>

<table border="1" summary="Error Codes and Error Texts during Module Balancing"><colgroup><col/><col/><col/></colgroup><thead><tr bgcolor="#EEEEEE"><th>Error code</th><th>Error text</th><th>Meaning</th></tr></thead><tbody valign="top"><tr><td valign="top">0</td><td valign="top">NO_ERROR</td><td valign="top">There was no error.</td></tr><tr><td valign="top">1</td><td valign="top">ERR_MODULEDATA_MISSING</td><td valign="top">No module database has been specified yet.</td></tr><tr><td valign="top">2</td><td valign="top">ERR_MODULDATA_FORMAT</td><td valign="top">The module database does not match the specified format.</td></tr><tr><td valign="top">3</td><td valign="top">ERR_SOFTWARE</td><td valign="top">An unexpected software error has occurred (this can occur if an exception occurred and was not corrected).</td></tr><tr><td valign="top">4</td><td valign="top">ERR_VERSION_MISMATCH</td><td valign="top">A component that is used does not meet the specified version requirements.</td></tr><tr><td valign="top">5</td><td valign="top">ERR_SERVICE_NOT_AVAILABLE</td><td valign="top">All necessary services are not available.</td></tr><tr><td valign="top">7</td><td valign="top">ERR_SERVICE_NOT_RELEASED</td><td valign="top">All services could not be released.</td></tr><tr><td valign="top">8</td><td valign="top">ERR_ACCESS_DENIED</td><td valign="top">The work station does not have sufficient access to the required services.</td></tr><tr><td valign="top">9</td><td valign="top">ERR_NOT_IMPLEMENTED</td><td valign="top">The functions required for the process have not been fully implemented.</td></tr><tr><td valign="top">10</td><td valign="top">ERR_SERVICE_ABORTED</td><td valign="top">The procedure was canceled.</td></tr><tr><td valign="top">11</td><td valign="top">ERR_SERVICE</td><td valign="top">A service is reporting an error.</td></tr><tr><td valign="top">12</td><td valign="top">ERR_SERVICE_TIMEOUT</td><td valign="top">A service is not replying to requests in time.</td></tr><tr><td valign="top">13</td><td valign="top">ERR_MODULEDATA_CHECK</td><td valign="top">The module database contains values that are not permitted.</td></tr><tr><td valign="top">14</td><td valign="top">ERR_MODULEDATA_NOT_FOUND</td><td valign="top">The module is not registered in the database.</td></tr><tr><td valign="top">20</td><td valign="top">ERR_ALIAS</td><td valign="top">The alias specified for the device connection was not configured.</td></tr><tr><td valign="top">21</td><td valign="top">ERR_DEVICE_NOT_CONNECTED</td><td valign="top">No device connection was established.</td></tr><tr><td valign="top">22</td><td valign="top">ERR_DEVICE_NOT_FOUND</td><td valign="top">No device was found for the desired task.</td></tr><tr><td valign="top">23</td><td valign="top">ERR_DEVICE_BUSY</td><td valign="top">The desired device is being used elsewhere.</td></tr><tr><td valign="top">24</td><td valign="top">ERR_PROCESS_ABORTED</td><td valign="top">The device has aborted the process.</td></tr><tr><td valign="top">25</td><td valign="top">ERR_PROCESS_NOT_FINISHED</td><td valign="top">The process is not completed yet.</td></tr><tr><td valign="top">26</td><td valign="top">ERR_PROCESS_NOT_STARTED</td><td valign="top">The process could not be started.</td></tr><tr><td valign="top">27</td><td valign="top">ERR_CABLE_NOT_READY</td><td valign="top">An adapter cable required for the process is not connected correctly.</td></tr><tr><td valign="top">28</td><td valign="top">ERR_CHARGING_NOT_USEFUL</td><td valign="top">The process was successfully completed. Qualification values are available.</td></tr><tr><td valign="top">29</td><td valign="top">ERR_TARGET_VOLTAGE_TOO_HIGH</td><td valign="top">The target voltage is too high for the module to be balanced.</td></tr><tr><td valign="top">30</td><td valign="top">ERR_TARGET_VOLTAGE_TOO_LOW</td><td valign="top">The target voltage is too low for the module to be balanced.</td></tr><tr><td valign="top">31</td><td valign="top">ERR_DEVICE_STILL_CONNECTED</td><td valign="top">A device connection that needs to be closed is still active.</td></tr><tr><td valign="top">32</td><td valign="top">ERR_CABLE_RESISTANCE</td><td valign="top">The line resistance of a connected line is too high.</td></tr><tr><td valign="top">33</td><td valign="top">ERR_CABLE_RESISTANCE</td><td valign="top">At least one connected cable must be removed to perform the action.</td></tr><tr><td valign="top">40</td><td valign="top">ERR_FIRMWARE</td><td valign="top">The installed device firmware returned an unexpected error.</td></tr><tr><td valign="top">41</td><td valign="top">ERR_CALIBRATION_REQUIRED</td><td valign="top">The validity date of the last calibration has been exceeded. A calibration is needed.</td></tr><tr><td valign="top">44</td><td valign="top">ERR_MB</td><td valign="top">The module balancer is not functioning correctly.</td></tr><tr><td valign="top">45</td><td valign="top">ERR_MB_SELFTEST_FAILED</td><td valign="top">The self-test could not be successfully completed.</td></tr><tr><td valign="top">46</td><td valign="top">ERR_MB_COVER_NOT_READY</td><td valign="top">The cover guard was not closed correctly.</td></tr><tr><td valign="top">47</td><td valign="top">ERR_MB_TEMPERATURE</td><td valign="top">The temperature of the module balancer is outside the permitted range.</td></tr><tr><td valign="top">48</td><td valign="top">ERR_MB_SELFTEST_REQUIRED</td><td valign="top">The self-test could not be successfully completed.</td></tr><tr><td valign="top">49</td><td valign="top">ERR_MB_NOT_READY</td><td valign="top">The module balancer is in standby mode. Switch on if necessary.</td></tr><tr><td valign="top">50</td><td valign="top">ERR_MODULE_INTERNAL_CONNECTION</td><td valign="top">A connection inside the module or battery has been interrupted.</td></tr><tr><td valign="top">51</td><td valign="top">ERR_MODULE_TEMPERATURE</td><td valign="top">The temperature of the module is outside the permitted range.</td></tr><tr><td valign="top">52</td><td valign="top">ERR_MODULE</td><td valign="top">There is a problem with the module to be charged.</td></tr><tr><td valign="top">60</td><td valign="top">ERR_NO_PROCESS</td><td valign="top">The device is not in balancing mode.</td></tr><tr><td valign="top">61</td><td valign="top">ERR_SELFTEST_ACTIVE</td><td valign="top">The device is in self-test mode.</td></tr><tr><td valign="top">62</td><td valign="top">ERR_FIRMWAREUPDATE_ACTIVE</td><td valign="top">The device is currently performing a firmware update.</td></tr></tbody></table>

**Table 118. Error Codes and Error Texts during Module Balancing**

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-14-17-category-connection.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="7-14-function-test-editor.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="7-14-19-category-flash.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">7.14.17. Category - Connection </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 7.14.19. Category - Flash</td></tr></table>
