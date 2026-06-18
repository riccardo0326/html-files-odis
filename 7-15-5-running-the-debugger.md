[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md) > [7.15. Debugger (Integrated Operating System)](7-15-debugger-integrated-operating-system.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.15.5. Running the Debugger</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-15-4-actions-in-debug-mode.md">Prev</a> </td><th align="center" width="60%">7.15. Debugger (Integrated Operating System)</th><td align="right" width="20%"> <a accesskey="n" href="7-15-6-break-points-view.md">Next</a></td></tr></table>

---

#### <a id="Funktionstesteditor.Debugger.Ausfuehren"></a>7.15.5. Running the Debugger

There are two ways of starting the integrated operating system.

- Start test module (or start test module in single step mode): starts an individual function test in the operating system.
- Start GFF: starts diagnostic entry. Vehicle identification takes place first in this case, as in the dedicated operating system. The operating system can start function tests during diagnostic entry. Starting diagnostic entry initiates a debug session (see [Section 7.15.11.1, “Background: Debug Session”](7-15-11-additional-debug-functions.md#Funktionstesteditor.Debugger.DebugSitzung.Hintergrund "7.15.11.1. Background: Debug Session")) that is valid until diagnostic exit. After successful diagnostic entry, individual function tests can be started using "Start test module".

Both options assume there is an open function test as base data. The base data, which can also contain local modifications, can be used as the information supplier for a debug session and made available to the operating system, regardless of the content of the ODIS Creator database. All additional information that the operating system requires during a debug session is retrieved from the ODIS creator database. The actual status of all objects at the time the debug session started is used. The result is that changes, for example to a measured value table, that were made after "Start test module" or "Start GFF" was activated, are not visible in the debug session.

Note: retrieving information during a debug session is significantly more complex in detail. Information is retrieved from various sources and is overlaid or overwritten depending on the priority of the source. The following information sources exist:

- Operating system database: DI databases and test baselines, if necessary, are used as information sources in the operating system (priority 3).
- ODIS Creator database: if there is newer information in the ODIS Creator database compared to the data in the operating system, it will be retrieved from this source (priority 2).
- Base data: with priority 1, the base data will overlay all other sources.

You cannot see which data is retrieved from which source.

Parameters can be set for the frequency of interface updates before and during the debug session. See [Section 7.15.5.3, “Interface Updates Configuration”](7-15-5-running-the-debugger.md#Funktionstesteditor.Debugger.Obergflaechenaktualisierung "7.15.5.3. Interface Updates Configuration").

After starting the debugger using either "Start test module" or "Start test module in single step mode", a window appears where you can configure the default value input (see [Figure 554, “Default value input”](7-15-5-running-the-debugger.md#figure.Funktionstesteditor.Debugger.Ausfuehren "Figure 554. Default value input")). You can either fill the data with values recorded previously from a file, or you can use the runtime values that were read.

<a id="figure.Funktionstesteditor.Debugger.Ausfuehren"></a>

![Image: default value input](images/fte_Debug_Konf.png)

**Figure 554. Default value input**

If diagnostic entry is started with the "Start GFF" function, the following configuration dialog appears.

<a id="figure.Funktionstesteditor.Debugger.Ausfuehren.DiagEntr"></a>

![Image: simulation](images/fte_Debug_DiagEntr_Konf.png)

**Figure 555. Simulation**

While a function test runs in the debug session, a yellow counter indicates the current location of the process. This occurs with both the test steps and the commands.

<a id="figure.Funktionstesteditor.Debugger.Zeiger"></a>

![Image: yellow counter marks the current running position](images/fte_Debug_Zeiger.png)

**Figure 556. Yellow Counter Marks the Current Running Position**

  

Function tests from the ODIS Creator source may be present in the ODIS Creator database in a processing status that cannot be run. If such a function test is used, for example as a sub-program, ODIS Creator will inform you about any compilation errors that occur.

<a id="figure.Funktionstesteditor.Debugger.Kompilierfehler"></a>

![Image: compilation error](images/fte_Debug_Kompilierfehler.png)

**Figure 557. Compilation Error**

Function tests that cannot be compiled are not available in the debug session, because they cannot be run.

The affected function test can be opened in read-only mode in ODIS Creator using the compilation error dialog. Compilation is initiated directly after opening and the results are entered in the Problems view. A function test is compiled exactly once within a debug session. The compilation error dialog appears only once in each debug session and function test.

The debug session continues immediately after closing the dialog or after opening the affected function test. In some cases, the integrated operating system may end the debug session if a function test is not available due to compilation errors.

A compilation is performed at various points within a debug session.

- During the "Determine special functions" phase in diagnostic entry
- Activating an entry in the test plan view
- Encountering a sub-program request in the course of a function test

For other situations where function tests may be accessed, refer to the ODIS Service user handbook.

Depending on the selected debug start, the system either runs to its first interaction 9such as a function selection - see [Figure 558, “Process View”](7-15-5-running-the-debugger.md#figure.Funktionstesteditor.Debugger.View "Figure 558. Process View")) or until the break point. If the debugger was started with "Start test module in single step mode", you can go through the process step-by-step using the Debugger button. See [Figure 553, “Debugger Button”](7-15-4-actions-in-debug-mode.md#figure.Funktionstesteditor.Debugger.Breakpoint_Ablauf "Figure 553. Debugger Button").

<a id="figure.Funktionstesteditor.Debugger.View"></a>

![Image: process view](images/fte_Debug_View.png)

**Figure 558. Process View**

After the debugger reaches the end or it is ended, the process that ran up to that point can be saved (see [Figure 559, “Saving a Simulation”](7-15-5-running-the-debugger.md#figure.Funktionstesteditor.Debugger.Speichern "Figure 559. Saving a Simulation")). The result is an XML file with default values. This file can be used as a default values file the next time the debugger is started.

<a id="figure.Funktionstesteditor.Debugger.Speichern"></a>

![Image: saving a simulation](images/fte_Debug_Speichern.png)

**Figure 559. Saving a Simulation**

##### <a id="Funktionstesteditor.Debugger.Testprocedure"></a>7.15.5.1. Direct Debugging of Test Procedures

Direct debugging of test procedures is not possible with the integrated ODIS Debug. However, ODIS Creator has a workaround for this shortcoming. A main program that executes the test procedure bu that is hidden from the user has been created. This makes it possible to start and perform a test procedure directly in ODIS Debug.

Because a test procedure that is started directly using this method is always treated like a sub-program, it must always be reloaded from the ODIS Creator database for the debug session. As a result, saving changes to the test procedure locally in the function test editor is not sufficient. A check-in must be performed, for example using the "Save and check in” function. Only then will any changes made during the session be visible in the debug session. The dialog ([Figure 560, “Test procedure not checked in”](7-15-5-running-the-debugger.md#figure.Funktionstesteditor.Debugger.Testprocedure.Savedialog "Figure 560. Test procedure not checked in")) appears when starting the debugger only if the test procedure is opened in write mode. “Save and check in” occurs automatically if this dialog was confirmed with “Yes”. Otherwise, the changes will not be saved and the debug procedure will be canceled.

<a id="figure.Funktionstesteditor.Debugger.Testprocedure.Savedialog"></a>

![Image: dialog for checking in test procedures](images/fte_Debug_Save_Prozedur_Dialog.png)

**Figure 560. Test procedure not checked in**

There is a configuration dialog for preselecting parameters in a test procedure. It will be displayed directly after directly starting a debug session for a test procedure. The dialog can also be deactivated under settings.

<a id="figure.Funktionstesteditor.Debugger.Testprocedure.Vorbelegungsdialog"></a>

![Image: preselection dialog for test procedures](images/fte_Debug_Vorbelegungsdialog.png)

**Figure 561. Preselection Dialog**

Variables/keywords (no array variables) can be preselected using the preselection dialog.

Note: only the parameters for the test procedure are listed for preselection (variables and keywords with at least the ‘Accept’ visibility). Variables/keywords that are internal to test procedures are not considered.

The procedure for debugging test procedures is the same as the procedure for debugging function tests.

##### <a id="Funktionstesteditor.Debugger.Generaltest"></a>7.15.5.2. Direct Debugging of "General Tests”

The procedure for debugging general tests is the same as the procedure for debugging function tests. However, it is possible to activate a preselection dialog for “General tests” in order to preselect the corresponding values.

<a id="figure.Funktionstesteditor.Debugger.Generaltest.Vorbelegungsdialog"></a>

![Image: preselection dialog for "General tests”](images/fte_Debug_Generaltest_Vorbelegungsdialog.png)

**Figure 562. Preselection Dialog**

There is a preselection dialog for preselecting parameters of a general test. It will be displayed directly after directly starting a debug session for a “General test”. The dialog can also be deactivated under settings.

Variables/keywords (no array variables) can be preselected using the preselection dialog.

Note: only the parameters for the "General test” are listed for preselection (variables and keywords with at least the ‘Accept’ visibility). Variables/keywords that are internal to a "General test” are not considered.

##### <a id="Funktionstesteditor.Debugger.Obergflaechenaktualisierung"></a>7.15.5.3. Interface Updates Configuration

During a debug session, the Java code generated for the function test runs in the operating ystem and the ODIS Creator interface is continually updated. The user can control the frequency of interface updates. The performance of the debug session can be significantly improved by reducing the updates.

Note: an update consists of setting the yellow position indicators and refreshing the “Variables” and “Call stack” views.

Two different modes can be set:

1. Detailed debug process: there is one interface update for each command in the function test editor. This is the default setting.
2. Quick debug process: during the procedure, ODIS Creator calculates if a command requires user interaction. If user interaction is expected, then an interface update will take place. If interaction is not expected, the update will not take place. In this way, the interface will be up-to-date when the user must interact. A user interaction is either entering a placeholder value or entering necessary data in the Process view. A list of commands that requires a user interaction can be found in [Section 7.15.5.3, “Interface Updates Configuration”](7-15-5-running-the-debugger.md#Funktionstesteditor.Debugger.AnweisungenMitInteraktion).

   There is no differentiation between debugging with real values and with placeholder values, meaning when debugging with real values, no default values appear but the interface is updated anyway.

The setting for the frequency can be changed in two ways:

- Using a button in the ODIS Creator toolbar
- “ODIS debug” settings

The setting in the toolbar is adjusted with the “Quick debug process” button. See [Figure 563, “Debug Display Mode in the Toolbar”](7-15-5-running-the-debugger.md#figure.Funktionstesteditor.Debugger.AblaufsteuerungToolbar "Figure 563. Debug Display Mode in the Toolbar").

<a id="figure.Funktionstesteditor.Debugger.AblaufsteuerungToolbar"></a>

![Image: debug display mode in the toolbar](images/fte_Debug_Ablaufsteuerung.png)

**Figure 563. Debug Display Mode in the Toolbar**

You can switch between the detailed and the quick display modes in the settings under the item “ODIS debug”. See [Figure 564, “ODIS Debug Settings”](7-15-5-running-the-debugger.md#figure.Funktionstesteditor.Debugger.AblaufsteuerungBenutzervorgaben "Figure 564. ODIS Debug Settings").

<a id="figure.Funktionstesteditor.Debugger.AblaufsteuerungBenutzervorgaben"></a>

![Image: ODIS debug settings](images/fte_Debug_Benutzervorgaben.png)

**Figure 564. ODIS Debug Settings**

You can also make other adjustments under settings beyond the detailed mode.

If the preselection dialog is activated, it will be displayed when a test procedure is started in debug mode.

If one or both options

- From first Break Point
- From first Dialog

are set, the detailed process is only activated after reaching the first break point or the first user interaction (substitute value input or input in the Process view). The quick process is performed first

The setting can be changed during a debug session as long as no modal dialog is blocking the interface.

The interface update setting is stored on the user’s PC and applies to all sessions.

To reduce the flickering of the interface due to continuous updates, ODIS Debug waits a few milliseconds before each update. The waiting period can be set in the settings. See [Figure 564, “ODIS Debug Settings”](7-15-5-running-the-debugger.md#figure.Funktionstesteditor.Debugger.AblaufsteuerungBenutzervorgaben "Figure 564. ODIS Debug Settings"). The waiting period is stored on the user’s PC and applies to all sessions. The default value is 30 ms.

<a id="Funktionstesteditor.Debugger.AnweisungenMitInteraktion"></a>**List of commands with user interaction**

- Question
- Input
- Message
- Keyboard input
- Vehicle Status
- Measuring channel
- Lock Button
- Voltage measurement
- Electrical current measurement
- Resistance measurement
- Diode measurement
- Measure pressure
- Measure temperature
- Oscilloscope
- High-voltage block
- High-voltage measurement data
- Sub-Program
- Loop Quit / Loop Timeout
- Read measured values
- Read ASAM measured values
- ASAM identification
- ASAM variant identification
- ASAM hex service
- Login
- Log out
- Write XML/XML IA
- Expand XML
- Expand XML IA
- XML set number
- Read XML sentence
- Read XML
- Read XML IA
- Expand XML IA
- Read XML IA
- Check SecurityKey (VFA)
- Send online
- Receive online
- Send log
- Determining the MBs
- MB connection
- Module data request
- Start balancing procedure
- Request (dis)charging parameters
- MB qualification report
- MB process status request
- Request module hardware info
- MB error message
- MB info request
- MB status request
- MB classification report
- Flash path
- Flash container
- Parallel Flashing
- Create flash control file
- Ecukom
- ASAM Ecukom
- ASAM result
- If equipment / If VCI comparison / If symptoms / If vehicle status
- While (not) equipment / While (not) VCI comparison / While (not) symptoms / While (not) vehicle status
- Case equipment / Case VCI comparison / Case symptoms / Case vehicle status
- Following system functions in declare/define keyword/expression/If condition/While (not) condition/case comparison

  - ACTIONCODE
  - APPLICATIONTYPE
  - COMMUNICATIONTYPE
  - DATE
  - DATETIME
  - DV\_VW\_PART
  - DEALERCODE
  - DEALERJOB
  - DEALERSHIPID
  - DEVICE
  - DEVICETYPE
  - ERROR\_TYPE
  - FINGERPRINT
  - FINGERPRINTDEALER
  - FINGERPRINTDEVICE
  - FINGERPRINTIMPORTER
  - IMPORTEUR
  - LICENCEPLATENUMBER
  - PIN15\_STATE
  - PIN30\_STATE
  - PROGRAMMINGVOLTAGE
  - REPAIRSTATE
  - TIME
  - VCI\_CONNECTION\_TYPE
  - VCI\_CONNECTION\_TYPE
  - VIN
  - UUID\_D3\_EDGEBOX
  - CP\_HAS\_PR\_NUMBER
  - CU\_5BAUDARD\_ARD
  - CU\_5BAUDARD\_INDEX
  - CU\_ADR\_ADR
  - CU\_ADR\_INDEX
  - CU\_BUSTYP\_ADR
  - CU\_BUSTYP\_INDEX
  - CU\_CODED\_ADR
  - CU\_CODED\_INDEX
  - CU\_CODINGTABLE\_ADR
  - CU\_CODINGTABLE\_INDEX
  - CU\_CODING\_STATE
  - CU\_FLASHABLE
  - CU\_HARDWARE\_NUMBER
  - CU\_INSTALLED\_ADR
  - CU\_INSTALLED\_INDEX
  - CU\_SERIAL\_NUMBER
  - CU\_SOFTWARE\_NUMBER
  - CU\_SOFTWARE\_VERSION
  - CU\_STATUSINFO\_ADR
  - CU\_STATUSINFO\_INDEX
  - CU\_STATUSTEXT\_ADR
  - CU\_STATUSTEXT\_INDEX
  - CU\_TIME\_STAMP
  - MAX\_SPECLIST
  - HVMT\_DEVICE\_IDENTIFICATION
  - HVMT\_FMVERSION\_AVAILABLE
  - HVMT\_GDIDDVERSION\_EXPECTED
  - HVMT\_GDIDDVERSION\_AVAILABLE
  - HVMT\_FMVERSION\_EXPECTED
  - STDMT\_DEVICE\_IDENTIFICATION
  - CU\_ASAM\_ODX\_File\_Identifier
  - CU\_ASAM\_ODX\_File\_Version
  - CU\_ASAM\_ODX\_Variante
  - CU\_Anzahl\_Slave
  - CU\_Gatewayverbauliste (gateway components list)
  - CU\_Ident\_Master
  - CU\_Ident\_Slave
  - CU\_SlaveIDs
  - CU\_ISO\_13400\_on\_IEEE\_802\_3
  - CU\_ISO\_14230\_3\_on\_ISO\_15765\_2
  - CU\_ISO\_15765\_3\_on\_ISO\_15765\_2
  - CU\_MCD\_VEHICLE\_INFO
  - CU\_MSP\_KW1281\_on\_ISO\_9141\_2
  - CU\_MSP\_KW1281\_on\_TP16
  - CU\_MSP\_VW2000LP\_on\_ISO\_14230\_2
  - CU\_MSP\_VW2000LP\_on\_TP16
  - CU\_MSP\_VW2000LP\_on\_TP20
  - CU\_PROTOCOL
  - CU\_SystemNameOrEngineType
  - CU\_UDS\_ID\_KWP\_Dienst\_22
  - CU\_VW\_Coding\_Value
  - CU\_VW\_DataSetNumberOrECUDataContainerNumber
  - CU\_VW\_DataSetVersionNumber
  - CU\_VW\_ECU\_HardwareVersionNumber
  - CU\_VW\_FAZITIdentification
  - CU\_VehicleEquipmentCodeAndPRNumberCombination

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-15-4-actions-in-debug-mode.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="7-15-debugger-integrated-operating-system.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="7-15-6-break-points-view.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">7.15.4. Actions in Debug Mode </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 7.15.6. Break Points View</td></tr></table>
