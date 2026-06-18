[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md) > [7.14. Function Test Editor](7-14-function-test-editor.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.14.19. Category - Flash</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-14-18-category-module-balancing.md">Prev</a> </td><th align="center" width="60%">7.14. Function Test Editor</th><td align="right" width="20%"> <a accesskey="n" href="7-14-20-category-miscellaneous.md">Next</a></td></tr></table>

---

#### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Flash"></a>7.14.19. Category - Flash

This category contains the following four action elements:

- [Section 7.14.19.1, “Action Element - Flash Path”](7-14-19-category-flash.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Flash.Flash_Pfad "7.14.19.1. Action Element - Flash Path")
- [Section 7.14.19.2, “Action Element - Flash Container”](7-14-19-category-flash.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Flash.Flash_Container "7.14.19.2. Action Element - Flash Container")
- [Section 7.14.19.3, “Action Element - Creating Flash Control File”](7-14-19-category-flash.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Flash.Flashsteuerdatei_erzeugen "7.14.19.3. Action Element - Creating Flash Control File")
- [Section 7.14.19.4, “Action Element - Parallel Flashing”](7-14-19-category-flash.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Flash.Parallel_Flashen "7.14.19.4. Action Element - Parallel Flashing")
- [Section 7.14.19.5, “ViWi Communication Setup Action Element”](7-14-19-category-flash.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Flash.Kommunikationsaufbau_ViWi "7.14.19.5. ViWi Communication Setup Action Element")
- [Section 7.14.19.6, “Send/Receive ViWi Action Element”](7-14-19-category-flash.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Flash.SendeEmpfange_ViWi "7.14.19.6. Send/Receive ViWi Action Element")
- [Section 7.14.19.7, “Write ViWi Request Action Element”](7-14-19-category-flash.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Flash.Schreibe_ViWi_Request "7.14.19.7. Write ViWi Request Action Element")
- [Section 7.14.19.9, “Action Element - Flash Sequence (VFA)”](7-14-19-category-flash.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Flash.Flashablauf_VFA "7.14.19.9. Action Element - Flash Sequence (VFA)")
- [Section 7.14.19.10, “Action Element - Delete Temporary Directory”](7-14-19-category-flash.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Flash.Loeschen_temp_Verzeichnis "7.14.19.10. Action Element - Delete Temporary Directory")

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Flash.Flash_Pfad"></a>7.14.19.1. Action Element - Flash Path

The "Flash path" action element can be seen in [Figure 507, “Flash Path Action Element”](7-14-19-category-flash.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Flash.Flash_Pfad "Figure 507. Flash Path Action Element").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Flash.Flash_Pfad"></a>

![Image: flash path action element](images/fte_arbeitsflaeche_flash_flashpfad.png)

**Figure 507. Flash Path Action Element**

The action elements in this category serve to detect and adapt data from a control table. In this case, the flash path is added. When a name is given for the flash container (flash name), the function determines the storage path for the flash container, which is can be transferred to a "SetFlashContainer" Ecukom call in another command. If the flash container is on a server drive, it will be loaded on the tester and stored in a temporary directory. The function then returns the path of the temporary directory.

###### <a id="d4e26840"></a>7.14.19.1.1. Flash Name

The name of the flash container is specified here. This is generally determined previously in a function test and transmitted with a variable.

###### <a id="d4e26843"></a>7.14.19.1.2. Search Directory

You can specify an option here so that the source directory of the flash container is searched. The internal search sequence is defined as follows:

1. Online: the flash container is loaded in a temporary directory on the tester.
2. CD-ROM
3. Hard drive

Adjustable options for the search directory:

- Last: the path setting from the "Flash name" command that is always before the "Flash path" command is used.
- Hard drive: the search sequence begins and ends with the hard drive.
- CD-ROM: the search sequence for the flash container begins with the CD-ROM drive.
- D3 server: data sets from the D3 server can be loaded here and transferred to the operating system. The directory name for the local hard drive or a server drive can be specified here. The flash container is searched on the path. If no storage path is specified, the default path will be used or a “zero” will be transmitted to the function.
- Search directory: the directory name for the local hard drive or a server drive can be specified here. The flash container is searched on the path. If it is not located on the specified drive, the search will continue in the internal search sequence.
- URL name: the search path is specified with a predefined URL name. The flash container is searched on a Mirror-Server. If it is not located on the Mirror-Server, the search will continue in the internal search sequence.
- URL: the flash container is searched on a Mirror-Server. If it is not located on the Mirror-Server, the search will continue in the internal search sequence.

###### <a id="d4e26869"></a>7.14.19.1.3. Flash path

Result: contains the storage directory for the flash container. The result is transferred to the "SetFlashContainer" Ecukom call in addition to the flash name as an input parameter. If no path was found, an empty string is transferred.

###### <a id="d4e26872"></a>7.14.19.1.4. Search Status

You can specify a variable here to check the search status. The following results are possible:

- 'OKAY' result: if the flash path parameter is filled, there is a flash container in the storage directory. Otherwise, an empty string will be transferred.
- 'NOT\_OKAY' result: an error occurred when the function was executed.

###### <a id="d4e26880"></a>7.14.19.1.5. Error ID

If an error occurred during runtime, an error ID can be stored here in a variable for further use. The error ID is a whole number value. The following error IDs can occur:

<a id="table.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Flash.Flash_Pfad.FehlerIDs"></a>

<table border="1" summary="Possible Error IDs"><colgroup><col align="left"/><col align="left"/></colgroup><thead><tr bgcolor="#EEEEEE"><th align="left">Error ID</th><th align="left">Meaning</th></tr></thead><tbody valign="top"><tr><td align="left" valign="top">0</td><td align="left" valign="top">No error occurred</td></tr><tr><td align="left" valign="top">1</td><td align="left" valign="top">Flash container was not found on the MirrorServer</td></tr><tr><td align="left" valign="top">2</td><td align="left" valign="top">Flash container was not found on the local hard drive</td></tr><tr><td align="left" valign="top">3</td><td align="left" valign="top">MirrorServer cannot be reached</td></tr><tr><td align="left" valign="top">4</td><td align="left" valign="top">MirrorServer authentication failed</td></tr><tr><td align="left" valign="top">5</td><td align="left" valign="top">Unexpected request from MirrorServer</td></tr><tr><td align="left" valign="top">6</td><td align="left" valign="top">Unexpected response from MirrorServer</td></tr><tr><td align="left" valign="top">7</td><td align="left" valign="top">Not enough local memory space available to store the flash container.</td></tr><tr><td align="left" valign="top">8</td><td align="left" valign="top">Unknown error</td></tr></tbody></table>

**Table 119. Possible Error IDs**

###### <a id="d4e26920"></a>7.14.19.1.6. KWP Programming Sequence

The usual process for a KWP flash procedure is as follows:

1. Check Ecukom control module version, evaluate VARIANTS result
2. Determine software number using expression with CU\_SOFTWARE\_NUMBER
3. Determine software version using expression with CU\_SOFTWARE\_VERSION
4. If KW1281: repeat Ecukom FlashXXX1 and step 1
5. Flash name command
6. Flash path command
7. Ecukom FlashProg2 (check requirements)
8. Ecukom FlashProg3 (evaluate job status)

###### <a id="d4e26940"></a>7.14.19.1.7. ASAM ODX Programming Sequence

The usual process for an ODX flash procedure is as follows:

1. Determine flash name
2. Flash path
3. Connect flash container
4. "SinglJob\_FlashJobUDS" order
5. Disconnect flash container

###### <a id="d4e26954"></a>7.14.19.1.8. Control Table Structure

```
------------------------------------------- ; Steuertabelle für programmierbare Steuergeräte ; Gateway D3 ; AGW (TEMIC) ; Ersteller: F. Hiller ; 4E0910468; 4E0910468_0040.SGO; 4E0910469; 4E0910469_0040.SGO; update; 4E0910469; 4E0910469_0040.SGO; -------------------------------------------
```

- Row 1, column 1: current software part number that is to be flashed
- Row 1, column 2: current software version or data container
- Row 1, column 3: new software part number, possibly changed
- Row 1, column 4: name of the new data container
- Row 1, column 5: possible comments to follow
- Row 2, column 1: new software part number
- Row 2, column 2: new data container
- Row 1 displays old and new, row 2 specifies the flash data that is used.

If the new software part number is changed, as in the example, it will be flashed. If the software part number is the same, the software version number of the control module will be compared with the data container. If there is a newer version, it will be flashed.

Data containers are encrypted \*.sgo files that are references in the flash control tables.

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Flash.Flash_Container"></a>7.14.19.2. Action Element - Flash Container

The "Flash container" action element can be seen in [Figure 508, “Flash Container Action Element”](7-14-19-category-flash.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Flash.Flash_Container "Figure 508. Flash Container Action Element").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Flash.Flash_Container"></a>

![Image: flash container action element](images/fte_arbeitsflaeche_flash_flashcontainer.png)

**Figure 508. Flash Container Action Element**

You can connect or disconnect the flash container using this command. The flash path must be known when connecting. The results status must also be entered.

###### <a id="d4e26989"></a>7.14.19.2.1. Connect/disconnect all connections

Adjustable options for connecting or disconnecting the flash container:

- Connect: the flash container is connected using this selection.
- Disconnect all connections: the flash container is disconnected using this selection.

###### <a id="d4e26997"></a>7.14.19.2.2. Flash path

Contains the storage directory for the flash container. If the Logical Link is specified, the flash path from the last time the flash path was accessed will be used.

###### <a id="d4e27000"></a>7.14.19.2.3. Logical link

A “Logical Link” can be entered here. Entering it is optional. It is entered using Variable, Stringliteral, or selection dialog.

###### <a id="d4e27003"></a>7.14.19.2.4. Flash mode

In this action element, you can set parameters about which flash mode should be used.

- No specification (OC setting config.ini will be used)
- Not partial
- Partial

“Partial” is used as the default value for setting flash mode parameters. Flash mode parameters can only be set if “Logical Link” is specified.

###### <a id="d4e27014"></a>7.14.19.2.5. Memory space (in MB)

In this group, the available and/or required memory space can be checked and stored in a variable of the whole number type.

###### <a id="d4e27017"></a>7.14.19.2.6. Available

To check the available memory space, a variable of the whole number type can be specified here. The variable will then be filled with the amount of memory space in MB that is still free on the local workstation computer. The number will be rounded down to the nearest whole number.

###### <a id="d4e27020"></a>7.14.19.2.7. Required

To check the required memory space, a variable of the whole number type can be specified here. The variable will then be filled with the amount of the specified flash container in MB. The number will be rounded up to the nearest whole number.

###### <a id="d4e27023"></a>7.14.19.2.8. Status

You can enter a string variable here to check the results status if no “Logical Link” is entered. The following results are possible:

- 'OKAY' result: the function could be executed successfully.
- 'NOT\_OKAY' result: an error occurred when the function was executed.

If a “Logical Link” is entered, an integer variable must be entered to check the DTC status. The following results are possible:

- 'FLASHLINK\_BINARY\_NO\_ERROR' result: the function could be executed successfully.
- 'UNKNOWN\_ERROR’' result: an error occurred when the function was executed.

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Flash.Flashsteuerdatei_erzeugen"></a>7.14.19.3. Action Element - Creating Flash Control File

The "Create flash control file" action element can be seen in [Figure 509, “Create Flash Control File Action Element”](7-14-19-category-flash.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Flash.Flashsteuerdatei_erzeugen "Figure 509. Create Flash Control File Action Element").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Flash.Flashsteuerdatei_erzeugen"></a>

![Image: create flash control file action element](images/fte_arbeitsflaeche_flash_flashsteuerdateierzeugen.png)

**Figure 509. Create Flash Control File Action Element**

You can create a flash control file using this command.

###### <a id="d4e27050"></a>7.14.19.3.1. Alias Name of Response XML / Control File Path / Overall Result / Individual Result

Specification for the variables for the alias name of the response XML and the name and path of the control file:

- Alias name of the response XML: here the author can present the response XML alias. The diagnostic system filters the quantity of control modules that should be flashed automatically from the response XML. Only relevant content is considered for this. Alias name of the response XML is a required field.
- Control file path: the author can specify the control file path here. The diagnostic system creates a control file automatically and stores it at the location specified in the field. The control file path is an optional field.

Specification of the variables for the overall result and individual result:

- Overall result: the overall result of flash container creation can be saved here in an integer variable. The possible return values for further evaluation are contained in [Section 7.14.19.4.2, “Parallel Flash Fault Code”](7-14-19-category-flash.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Flash.Fehlercodes_Parallel_Flashen_Flash_Steuerdatei_erzeugen "7.14.19.4.2. Parallel Flash Fault Code"). Checking the overall result is optional.
- Individual result: the individual results from creating the flash container for affected control modules can be checked here. A two-dimensional array variable from the type string can be specified for this. It contains the return values of the individual control modules that are part of the flash process. The result array is structured based on the following schema:

  <a id="d4e27065"></a>

  <table border="1" summary="Structure of the Individual Result Array for ‘Create Flash Control File’"><colgroup><col align="left"/><col align="left"/></colgroup><thead><tr bgcolor="#EEEEEE"><th align="left">Position in the second array dimension</th><th align="left">Content</th></tr></thead><tbody><tr><td align="left">1</td><td align="left">5 baud address as hex value (without leading ‘0x’). Example: 0001.</td></tr><tr><td align="left">2</td><td align="left">The individual control module fault code as fault code according to <a class="xref" href="7-14-19-category-flash.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Flash.Fehlercodes_Parallel_Flashen_Flash_Steuerdatei_erzeugen" title="7.14.19.4.2. Parallel Flash Fault Code">Section 7.14.19.4.2, “Parallel Flash Fault Code”</a>.</td></tr></tbody></table>

  **Table 120. Structure of the Individual Result Array for ‘Create Flash Control File’**

  Because the specified array is described in whole (or depending on the number of control modules involved in the flash procedure), an array index cannot be specified.

  Checking the individual result is optional.

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Flash.Parallel_Flashen"></a>7.14.19.4. Action Element - Parallel Flashing

The "Parallel Flashing" action element can be seen in [Figure 510, “Parallel Flashing Action Element”](7-14-19-category-flash.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Flash.Parallel_Flashen "Figure 510. Parallel Flashing Action Element").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Flash.Parallel_Flashen"></a>

![Image: Parallel Flashing Action Element](images/fte_arbeitsflaeche_flash_parallelflashen.png)

**Figure 510. Parallel Flashing Action Element**

You can activate parallel flashing with this command. The flash control file path must be known.

###### <a id="d4e27097"></a>7.14.19.4.1. Flash Control File Path / Overall Result / Individual Result

Specifications for the flash control file path, the overall result, and the individual result:

- Flash control file path: the flash control file location is set with this specification. A variable of the string type is expected. Flash control file path is a required field.
- Overall result: the overall result of the flash procedure can be saved here in an integer variable. The possible return values for further evaluation are contained in [Section 7.14.19.4.2, “Parallel Flash Fault Code”](7-14-19-category-flash.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Flash.Fehlercodes_Parallel_Flashen_Flash_Steuerdatei_erzeugen "7.14.19.4.2. Parallel Flash Fault Code"). Checking the overall result is optional.
- Individual result: checks the individual result of the flash procedure. A two-dimensional array variable from the type string can be specified. It contains the return values of the individual control modules that are part of the flash process. The result array is structured based on the following schema:

  <a id="d4e27108"></a>

  <table border="1" summary="Structure of the Individual Result Array for Parallel Flashing"><colgroup><col align="left"/><col align="left"/></colgroup><thead><tr bgcolor="#EEEEEE"><th align="left">Position in the second array dimension</th><th align="left">Content</th></tr></thead><tbody><tr><td align="left">1</td><td align="left">5 baud address as hex value (without leading ‘0x’). Example: 0001.</td></tr><tr><td align="left">2</td><td align="left">The individual control module fault code as fault code according to <a class="xref" href="7-14-19-category-flash.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Flash.Fehlercodes_Parallel_Flashen_Flash_Steuerdatei_erzeugen" title="7.14.19.4.2. Parallel Flash Fault Code">Section 7.14.19.4.2, “Parallel Flash Fault Code”</a>.</td></tr><tr><td align="left">3</td><td align="left">Value of the OPA_JobComplStatu parameter</td></tr><tr><td align="left">4</td><td align="left">Value of the OPA_JobResul parameter</td></tr><tr><td align="left">5</td><td align="left">Value of the OPA_JobStatu parameter</td></tr><tr><td align="left">6</td><td align="left">Value of the OPA_JobMessa parameter</td></tr><tr><td align="left">7</td><td align="left">Value of the OPA_UnfulPreco parameter</td></tr><tr><td align="left">8</td><td align="left">Value of the OPA_NegatRespoInfor parameter</td></tr><tr><td align="left">From 9</td><td align="left">Name and value of all additional parameters in the form Name=Value</td></tr></tbody></table>

  **Table 121. Structure of the Individual Result Array for Parallel Flashing**

  Because the specified array is described in whole (or depending on the number of control modules involved in the flash procedure), an array index cannot be specified.

###### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Flash.Fehlercodes_Parallel_Flashen_Flash_Steuerdatei_erzeugen"></a>7.14.19.4.2. Parallel Flash Fault Code

The following table lists fault codes that can occur in the [Section 7.14.19.3, “Action Element - Creating Flash Control File”](7-14-19-category-flash.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Flash.Flashsteuerdatei_erzeugen "7.14.19.3. Action Element - Creating Flash Control File") and [Section 7.14.19.4, “Action Element - Parallel Flashing”](7-14-19-category-flash.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Flash.Parallel_Flashen "7.14.19.4. Action Element - Parallel Flashing") action elements.

<a id="d4e27152"></a>

<table border="1" summary="Flash Fault Codes"><colgroup><col align="left"/><col align="left"/></colgroup><thead><tr bgcolor="#EEEEEE"><th align="left">Error code</th><th align="left">Meaning</th></tr></thead><tbody><tr><td align="left">0</td><td align="left">NO_ERROR</td></tr><tr><td align="left">1</td><td align="left">ECU_SPECIFIC_ERROR</td></tr><tr><td align="left">2</td><td align="left">CONTROLFILE_NOT_FOUND</td></tr><tr><td align="left">3</td><td align="left">INVALID_CONTROLFILE</td></tr><tr><td align="left">4</td><td align="left">S42_RESPONSE_NOT_FOUND</td></tr><tr><td align="left">5</td><td align="left">PROCESSING_ERROR</td></tr><tr><td align="left">6</td><td align="left">COULD_NOT_WRITE_CONTROLFILE</td></tr><tr><td align="left">7</td><td align="left">NO_ECUS_TO_FLASH</td></tr><tr><td align="left">21</td><td align="left">CONTAINER_SPECIFIC_ERROR</td></tr><tr><td align="left">22</td><td align="left">NO_RESPONSE_FROM_ECU</td></tr><tr><td align="left">23</td><td align="left">UNKNOWN_ECU_SHORTNAME</td></tr><tr><td align="left">24</td><td align="left">UNSUPPORTED_DIAG_PROT</td></tr><tr><td align="left">25</td><td align="left">UNFULFILLED_FLASH_PRECONDITIONS</td></tr><tr><td align="left">41</td><td align="left">FLASHCONTAINER_NOT_FOUND</td></tr><tr><td align="left">42</td><td align="left">FLASHSESSION_NOT_FOUND</td></tr><tr><td align="left">43</td><td align="left">NO_UNIQUE_FLASHSESSION</td></tr><tr><td align="left">44</td><td align="left">NEGATIVE_FLASH_JOB_RESULT</td></tr><tr><td align="left">45</td><td align="left">FLASH_EXECUTION_ERROR</td></tr><tr><td align="left">46</td><td align="left">BINARY_FILE_NOT_FOUND</td></tr><tr><td align="left">50</td><td align="left">LINK_CONTAINER_ERROR</td></tr></tbody></table>

**Table 122. Flash Fault Codes**

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Flash.Kommunikationsaufbau_ViWi"></a>7.14.19.5. ViWi Communication Setup Action Element

The "ViWi communication setup" action element can be seen in [Figure 511, “ViWi Communication Setup Action Element”](7-14-19-category-flash.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Flash.Kommunikationsaufbau_ViWi "Figure 511. ViWi Communication Setup Action Element").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Flash.Kommunikationsaufbau_ViWi"></a>

![Image: ViWi communication setup action element](images/fte_arbeitsflaeche_flash_kommunikationsaufbau_viwi.png)

**Figure 511. ViWi Communication Setup Action Element**

‘ViWi’ stands for Volkswagen Infotainment Web Interface protocol, and describes the communication protocol within the whole vehicle onboard data input in the workshop (GOBW). The “ViWi communication setup” command establishes the connection to the RPC server. The connection can be made either via VCI or LAN. When ‘VCI connection’ is selected, a checkbox for “Allow USD communication” becomes available. If it is activated, the corresponding “Logical link SOD master” text field is deactivated. If the checkbox is deactivated, the text field can be filled out manually. Parameters can be set for the text field using free text, variables (string), and the logical link selection dialog. When ‘LAN connection’ is selected, parameters are set for the server URL.

'Communication status’ and ‘Server URL’ can be defined as variables as optional return parameters. The ‘Server URL’ return value contains the URL that should be used for the connection. The ‘Communication status’ return value indicates if communication was successfully established.

- 0: successful
- -1: not successful (URL missing or incorrect, timeout, etc.)

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Flash.SendeEmpfange_ViWi"></a>7.14.19.6. Send/Receive ViWi Action Element

The "Send/ Receive ViWi" action element can be seen in [Figure 512, “Send/Receive ViWi Action Element”](7-14-19-category-flash.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Flash.SendeEmpfange_ViWi "Figure 512. Send/Receive ViWi Action Element").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Flash.SendeEmpfange_ViWi"></a>

![Image: send/receive ViWi action element](images/fte_arbeitsflaeche_flash_sendeempfange_viwi.png)

**Figure 512. Send/Receive ViWi Action Element**

By parameterizing the dialog, ViWi requests can be sent and ViWi responses received. Direct communication results and headers can be evaluated.

###### <a id="d4e27254"></a>7.14.19.6.1. URI

Contains the URI that should be used for the ViWi request. Input is entered either by variable or using stringliteral. There is also a selection dialog to help with input. The URI specification is required.

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Flash.uriauswahl_ViWi"></a>

![Image: URI selection dialog](images/fte_arbeitsflaeche_flash_uriauswahl_viwi.png)

**Figure 513. URI selection dialog**

###### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Flash.SendeEmpfange_ViWi_Request_Methode"></a>7.14.19.6.2. Request method

The method that will be used to send the request must be defined here. The following methods can be selected: GET, POST, PUT, DELETE.

The request name/value pairs can also be given in the header. The specification is entered using the request header button. The following illustration shows the request header selection dialog.

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Flash.requestheader_ViWi"></a>

![Image: request header selection dialog](images/fte_arbeitsflaeche_flash_requestheader_viwi.png)

**Figure 514. Request Header Selection Dialog**

###### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Flash.SendeEmpfange_ViWi_Referenz_Request"></a>7.14.19.6.3. Request reference

The reference for the request that should be sent is specified here. This specification is optional.

###### <a id="d4e27280"></a>7.14.19.6.4. Response reference

Contains the reference that should receive the response for further evaluation. This specification is optional.

###### <a id="d4e27283"></a>7.14.19.6.5. Communication status

The status value for the connection is written in the specified variable. This specification is optional.

- 0: successful
- -1: general error
- -2: VCI error
- -3: HTTP body is empty

###### <a id="d4e27296"></a>7.14.19.6.6. ViWi status

The status value from the response (“/status”) is written in the specified variable. This specification is optional.

###### <a id="d4e27299"></a>7.14.19.6.7. ViWi status code

The HTTP status code for the response is written in the specified variable. This specification is optional.

###### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Flash.SendeEmpfange_ViWi_Response_Header"></a>7.14.19.6.8. Response header

Gives the option to read values out from the response header. Headers to be read out are defined using the name. This specification is optional.

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Flash.Schreibe_ViWi_Request"></a>7.14.19.7. Write ViWi Request Action Element

The "Write ViWi Request" action element can be seen in [Figure 515, “Write ViWi Request Action Element”](7-14-19-category-flash.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Flash.Schreibe_ViWi_Request "Figure 515. Write ViWi Request Action Element").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Flash.Schreibe_ViWi_Request"></a>

![Image: write ViWi request action element](images/fte_arbeitsflaeche_flash_schreibe_viwi.png)

**Figure 515. Write ViWi Request Action Element**

ViWi requests can be created and expanded by entering a reference in this dialog. The dialog can be used successively, e.g. in a For loop, to generate a ViWi request. From a technical perspective, a ViWi request consists of a JSON payload, which is put together or populated in this dialog screen using parameters and paths.

###### <a id="d4e27318"></a>7.14.19.7.1. Request reference

Contains the name that should be used for the ViWi request. The specification of the request reference is mandatory.

###### <a id="d4e27321"></a>7.14.19.7.2. Service

A ViWi service must be selected here. The parameterization is based on this.

If the service is locked in the Administration interface, it will not be available for selection in the drop-down list.

###### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Flash.Schreibe_ViWi_Request_Requestparameter"></a>7.14.19.7.3. Request Parameter

Contains the parameters for the request that should be sent. This specification is mandatory. There must be at least one request parameter.

To define a request parameter, a service must be selected from the drop-down list first.

A request parameter consists of multiple parts:

- Name: the JSON name of the parameter
- Path: the path to the parameter within the JSON tree
- Type: the data type of the parameter
- Substitution: the value that the parameter should take on

Entering a path is mandatory and can be done either manually by entering directly in the table, or using the “ViWi request parameter selection dialog”.

If using the “ViWi request parameter selection dialog”, the path will be calculated differently depending on the selection.

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Flash.Schreibe_ViWi_Request_Path"></a>

![Image: path calculation of the ViWi request parameter selection dialog](images/fte_arbeitsflaeche_flash_schreibe_viwi_path_mapping.png)

**Figure 516. Path Calculation of the ViWi Request Parameter Selection Dialog**

The following variants of the cases are taken into account (see figure above):

- 1: selection of an element without additional sub-elements
- 2: selection of an intermediate node with additional sub-elements (JSON object)
- 3: selection of an element without additional sub-elements (within a JSON object)
- 4: selection of an intermediate node with additional sub-elements (JSON object list)
- 5: selection of a list with additional sub-elements (list element)
- 6: selection of an element from a list with the list index specified
- 7: selection of a nested list (JSON primitive list)
- 8: selection from a nested list (element from a JSON primitive list)

If the type of the selected parameter is ‘Object’ or 'Object[]', no substitution can be defined for it. For all other types, a substitution depending on the data type must be selected.

The view in the “ViWi request parameter selection dialog” can be switched by pressing the “Expanded/reduced view” button. In this way, the element descriptions can be displayed or hidden. The "reduced view” is selected by default.

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Flash.Schreibe_ViWi_Request_Param_Reduce"></a>

![Image: reduced view of the ViWi request parameter selection dialog](images/fte_arbeitsflaeche_flash_viwi_request_parameter_reduce.png)

**Figure 517. Reduced View of the ViWi Request Parameter Selection Dialog**

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Flash.Schreibe_ViWi_Request_Param_Extend"></a>

![Image: expanded view of the ViWi request parameter selection dialog](images/fte_arbeitsflaeche_flash_viwi_request_parameter_extend.png)

**Figure 518. Expanded View of the ViWi Request Parameter Selection Dialog**

If a service has already been selected and request parameters have been created, they can be reused using a convenience function when a new service selection is made. When the service is changed, a request dialog appears that can be used to decide if the request parameters should be kept or cleared.

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Flash.Schreibe_ViWi_Request_Comfort"></a>

![Image: ViWi write request convenience function](images/fte_arbeitsflaeche_flash_schreibe_viwi_service_change.png)

**Figure 519. ViWi Write Request Convenience Function**

The specification of the type is mandatory. If using the “ViWi request parameter selection dialog”, the type will be calculated automatically and cannot be edited. If the path is entered manually, there will be a check to determine if the path is defined in the JSON schema of the selected ViWi service. If the path is contained in the JSON schema, the type will be filled in automatically and it will not be possible to edit it. If the path is not contained in the JSON schema, the type will be deleted and must be selected manually using a combination box. The following values are offered for selection in the combination box.

- Integer
- Integer[]
- Number
- Number[]
- Object
- Object[]
- String
- String[]
- Boolean
- Boolean[]

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Flash.Lese_ViWi_Request"></a>7.14.19.8. Read ViWi Response Action Element

The "Read ViWi Response" action element can be seen in [Figure 520, “Read ViWi Response Action Element”](7-14-19-category-flash.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Flash.Lese_ViWi_Response "Figure 520. Read ViWi Response Action Element").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Flash.Lese_ViWi_Response"></a>

![Image: read ViWi response action element](images/fte_arbeitsflaeche_flash_lese_viwi.png)

**Figure 520. Read ViWi Response Action Element**

A ViWi response can be evaluated using this command. The command can be executed successively, e.g. in a For loop, in order to read all parts of the response one after the other.

###### <a id="d4e27428"></a>7.14.19.8.1. Response reference

The reference of the response that is to be read must be specified here. The specification of the response reference is mandatory.

###### <a id="d4e27431"></a>7.14.19.8.2. Service

A ViWi service must be selected here. The parameterization is based on this.

If the service is locked in the Administration interface, it will not be available for selection in the drop-down list.

###### <a id="d4e27435"></a>7.14.19.8.3. Response parameter

Contains parameters in table form that must be evaluated. To define a response parameter, a ViWi service must be selected from the drop-down list.

A response parameter consists of multiple parts:

- Name: the JSON name of the parameter
- Path: the path to the parameter within the JSON tree
- Type: the data type of the parameter
- Status: status of the parameter evaluation
- Variable: variable in which the value of the parameter should be written
- Interpretation: determines how the parameter should be evaluated (value or file)

Entering the path is mandatory and can be done either directly or selected using the “ViWi response parameter selection dialog”.

Input of the variable is mandatory and depends on the type.

The status of the parameter evaluation can have the following values:

- 0: parameter present and the data type of the associated received value is not compatible with the “Variable” and “Interpretation” data fields for the data set
- 1: parameter present and the data type of the associated received value is compatible with the “Variable” and “Interpretation” data fields for the data set
- -1: parameter is not present

If using the “ViWi response parameter selection dialog”, the path will be calculated differently depending on the selection.

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Flash.Lese_ViWi_Request_Path"></a>

![Image: path calculation of the ViWi response parameter selection dialog](images/fte_arbeitsflaeche_flash_lese_viwi_path_mapping.png)

**Figure 521. Path Calculation of the ViWi Response Parameter Selection Dialog**

The following cases are taken into account when calculating the path (see figure above):

- 1: selection of an element without additional sub-elements
- 2: selection of a sub-element without additional sub-elements
- 3: selection of an ‘Element number’ (saves the number of entries present in the JSON list)
- 4: selection of an element from a list
- 5: selection of an ‘Element number’ (saves the number of entries present in the JSON list)
- 6: selection of a list from a nested list (element from a JSON primitive list)
- 7: selection of an element from a list with the list index specified (JSON primitive list)
- 8-10: selection not possible

If the type of the selected parameter is “Object” or “Object[]", no substitution can be defined for it. For all other types, a substitution that is typical for the type must be selected.

The view in the “ViWi response parameter selection dialog” can be switched by pressing the “Expanded/reduced view” button. In this way, the element descriptions can be displayed or hidden. The "reduced view” is selected by default.

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Flash.Lese_ViWi_Request_Param_Reduce"></a>

![Image: reduced view of the ViWi response parameter selection dialog](images/fte_arbeitsflaeche_flash_viwi_response_parameter_reduce.png)

**Figure 522. Reduced View of the ViWi Response Parameter Selection Dialog**

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Flash.Lese_ViWi_Request_Param_Extend"></a>

![Image: expanded view of the ViWi response parameter selection dialog](images/fte_arbeitsflaeche_flash_viwi_response_parameter_extend.png)

**Figure 523. Expanded View of the ViWi Response Parameter Selection Dialog**

If response parameters have already been created, they can be reused using a convenience function when the ViWi service is changed. When the service is changed, a request dialog appears that can be used to decide if the response parameters should be kept or cleared.

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Flash.Lese_ViWi_Request_Comfort"></a>

![Image: ViWi read response convenience function](images/fte_arbeitsflaeche_flash_lese_viwi_service_change.png)

**Figure 524. ViWi Read Response Convenience Function**

The specification of the type is mandatory. If using the “ViWi response parameter selection dialog”, the type will be calculated automatically and cannot be edited. If the path is entered manually, there will be a check to determine if the path is defined in the JSON schema of the selected ViWi service. If the path is contained in the JSON schema, the type will be filled in automatically and it will not be possible to edit it. If the path is not contained in the JSON schema, the type will be deleted and must be selected manually using a combination box. The following values are offered for selection in the combination box.

- Integer
- Integer[]
- Number
- Number[]
- String
- String[]
- Boolean
- Boolean[]

When reading out the values from the JSON response and assigning them to variables, there is a strict check of the compatibility between the data type of the variable and the data type of the value returned by the API of the test language from the JSON response according to the following table.

When doing this,

1. the value + means:

   the data types are compatible
2. the value - means:

   the data types are not compatible

   Variables are filled with the default value of the respective data type.

   If a variable is also assigned for the status, the value 0 is set in the status variable.

<a id="table.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Flash.Lese_ViWi_Request.Typpruefung"></a>

<table border="1" summary="Compatibility Between the Data Type of the Variable and the Data Type of the Value from the JSON Response"><colgroup><col align="left"/><col align="left"/><col align="left"/><col align="left"/><col align="left"/><col align="left"/></colgroup><thead><tr bgcolor="#EEEEEE"><th align="left" rowspan="2">
<p>Data type of the</p>
<p>Variables</p>
</th><th align="left" colspan="4">Data type of the JSON response value</th><th align="left" rowspan="2">Comments</th></tr><tr bgcolor="#EEEEEE"><th align="left">String</th><th align="left">Integer</th><th align="left">Float</th><th align="left">Boolean</th></tr></thead><tbody valign="top"><tr><td align="left" valign="top">String</td><td align="left" valign="top">+</td><td align="left" valign="top">-</td><td align="left" valign="top">-</td><td align="left" valign="top">-</td><td class="auto-generated"> </td></tr><tr><td align="left" valign="top">Long</td><td align="left" valign="top">-</td><td align="left" valign="top">+</td><td align="left" valign="top">-</td><td align="left" valign="top">-</td><td align="left" rowspan="3" valign="top">
<p>Only integer values​that are supplied by the API of the test language as long, integer, short, or byte</p>
<p>No very large whole numbers (BigInteger)</p>
<p>There is no distinction between the variable types long, integer, short, since the long data type is always used internally in the FTE</p>
</td></tr><tr><td align="left" valign="top">Integer</td><td align="left" valign="top">-</td><td align="left" valign="top">+</td><td align="left" valign="top">-</td><td align="left" valign="top">-</td></tr><tr><td align="left" valign="top">Short</td><td align="left" valign="top">-</td><td align="left" valign="top">+</td><td align="left" valign="top">-</td><td align="left" valign="top">-</td></tr><tr><td align="left" valign="top">Byte</td><td align="left" valign="top">-</td><td align="left" valign="top">+</td><td align="left" valign="top">-</td><td align="left" valign="top">-</td><td align="left" valign="top">
<p>Only integer values​that are supplied by the API of the test language as long, integer, short, or byte and contain a value between -128 and + 127</p>
</td></tr><tr><td align="left" valign="top">Double</td><td align="left" valign="top">-</td><td align="left" valign="top">+</td><td align="left" valign="top">+</td><td align="left" valign="top">-</td><td align="left" rowspan="2" valign="top">
<p>Any numerical values (number) as well as very large whole numbers (BigInteger)</p>
</td></tr><tr><td align="left" valign="top">Float</td><td align="left" valign="top">-</td><td align="left" valign="top">+</td><td align="left" valign="top">+</td><td align="left" valign="top">-</td></tr><tr><td align="left" valign="top">Boolean</td><td align="left" valign="top">-</td><td align="left" valign="top">-</td><td align="left" valign="top">-</td><td align="left" valign="top">+</td><td class="auto-generated"> </td></tr></tbody></table>

**Table 123. Compatibility Between the Data Type of the Variable and the Data Type of the Value from the JSON Response**

  

The same compatibility checks are carried out when reading an array from the JSON response into an array variable.

If the array of the variable contains more elements than the array read out from the JSON response, all elements from the variable array that are not filled with values from the JSON response are filled with the default value according to the data type.

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Flash.Flashablauf_VFA"></a>7.14.19.9. Action Element - Flash Sequence (VFA)

The “Flash sequence (VFA)” action element can be seen in [Figure 525, “Flash Sequence (VFA) Action Element”](7-14-19-category-flash.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Flash.Flashablauf_VFA "Figure 525. Flash Sequence (VFA) Action Element").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Flash.Flashablauf_VFA"></a>

![Figure: flash sequence (VFA) action element](images/fte_arbeitsflaeche_flash_flashablauf.png)

**Figure 525. Flash Sequence (VFA) Action Element**

You can start the VFA flash sequence using this command. The flash sequence uses control module communication via functionalities of the ASAM Ecukom action element. The action element contains all of the necessary parameters for reliable flashing.

###### <a id="d4e27639"></a>7.14.19.9.1.

The input of control module variants, operation and request/response parameters correspond to the functionality of the ASAM Ecukom action element.

###### <a id="d4e27642"></a>7.14.19.9.1.1. Control Module Variants, Logical Link

See [Section 7.14.15.16.1, “Control Module Variants”](7-14-15-category-ecukom.md#Funktionstesteditor.Allgemeine_Funktionalitaet.SG-Gruppe "7.14.15.16.1. Control Module Variants").

###### <a id="d4e27646"></a>7.14.19.9.1.2. Diagnostic Service/Order

See [Section 7.14.15.16.2, “Diagnostic Service/Order Selection”](7-14-15-category-ecukom.md#Funktionstesteditor.Allgemeine_Funktionalitaet.Auswahl-Dienst "7.14.15.16.2. Diagnostic Service/Order Selection").

###### <a id="d4e27650"></a>7.14.19.9.1.3. Request Parameter

See [Section 7.14.15.16.4, “Request Parameter”](7-14-15-category-ecukom.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.Allgemein.Requests "7.14.15.16.4. Request Parameter").

###### <a id="d4e27654"></a>7.14.19.9.1.4. Positive/Negative Response Parameter

See [Section 7.14.15.16.6, “Positive/Negative Response Parameter”](7-14-15-category-ecukom.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.Allgemein.Antwortparameter "7.14.15.16.6. Positive/Negative Response Parameter").

###### <a id="d4e27658"></a>7.14.19.9.2. ModuleAddress, VIN and PartNumber

ODIS Service uses the parameters **ModuleAddress**, **VIN**, and **PartNumber** for the callback function of the ECF flash job. The parameters are transferred from the GFS to ODIS via the action element "VFA Flash Sequence.” The input of parameters is optional. If nothing has been selected, an empty string is transferred to ODIS.

The **ModuleAddress** parameter is used to determine the directory path. If the parameter is set, the content of the parameter is used to form the directory path instead of the CAD ID. Otherwise the CAN ID from the control module is determined and used to form the directory path.

###### <a id="d4e27666"></a>7.14.19.9.3. Variable

The description for selecting variables is found in [Section 7.14.6, “Using Variables”](7-14-6-using-variables.md "7.14.6. Using Variables"). The definition of variables is found in [Section 7.14.11.1, “Action Element - Declare Variable”](7-14-11-category-definition.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Definition.Deklariere_Variablen "7.14.11.1. Action Element - Declare Variable").

###### <a id="d4e27671"></a>7.14.19.9.4. Keyword

The description for selecting keywords is found in [Section 7.14.6, “Using Variables”](7-14-6-using-variables.md "7.14.6. Using Variables"). The definition of keywords is found in [Section 7.14.11.4, “Action Element - Define Keyword”](7-14-11-category-definition.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Definition.Definiere_Kennwort "7.14.11.4. Action Element - Define Keyword").

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Flash.Loeschen_temp_Verzeichnis"></a>7.14.19.10. Action Element - Delete Temporary Directory

The temporary directory osgi/../dms2 in the operating system can be deleted using the “Delete temporary directory” action element.

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-14-18-category-module-balancing.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="7-14-function-test-editor.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="7-14-20-category-miscellaneous.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">7.14.18. Category - Module balancing </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 7.14.20. Category - Miscellaneous</td></tr></table>
