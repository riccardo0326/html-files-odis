[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md) > [7.14. Function Test Editor](7-14-function-test-editor.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.14.9. Desktop</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-14-8-use-switchkey-variables.md">Prev</a> </td><th align="center" width="60%">7.14. Function Test Editor</th><td align="right" width="20%"> <a accesskey="n" href="7-14-10-category-dialog.md">Next</a></td></tr></table>

---

#### <a id="Funktionstesteditor.Arbeitsflaeche"></a>7.14.9. Desktop

There is a test module in the second level of editing on the desktop. It is divided at a high level into test steps in the first level. Each test step must now be filled with content. A test step can contain up to 125 action elements.

A test step is displayed graphically in a vertical structure on the desktop. To edit it, you can call up the functions using:

- the menu bar
- the buttons in the toolbar
- a context menu

**Dialogs**

Dialogs from the right side of the function test editor desktop open as separate windows that are listed separately in the operating system task bar. The dialogs can be moved to the background and back to the foreground, as with normal window applications. While a dialog is open, a second one from the same function test cannot be opened (exactly one dialog may be opened for each function test). While a dialog is open, the editing functions for the function test editor are restricted. For example, the delete/add/move/cut functions and undo/redo mechanism cannot be used.

Dialogs for the test step view behave differently: they are opened within the function test editor and nothing else can be edited at the same time.

**Brief notes**

If you move the mouse cursor over an action element and hold it there for approximately 2 seconds without executing a function, a brief message will appear as with a test step.

The following table gives an overview about the tools available in the toolbar and the functions of the menu bar **Add >> New action element**, with which you can add action elements in the work area.

Note the restrictions for using action elements in identification programs. Note the restrictions in **Start (background) modules**. Refer to [Abschnitt 7.5.3.1, „Permitted Action Elements in Start (background) Modules“](7-5-3-specify-the-used-relationship.md#verwendet.beziehung.spezifizieren.Konsistenz "7.5.3.1. Permitted Action Elements in Start (background) Modules").

<a id="d4e16250"></a>

<table border="1" summary="Action Elements"><colgroup><col align="left"/><col align="left"/><col align="left"/></colgroup><thead><tr bgcolor="#EEEEEE"><th align="left">Action element</th><th align="left">Group in menu</th><th align="left">Purpose</th></tr></thead><tbody><tr><td align="left">Set test module title</td><td align="left">Dialog</td><td align="left">Change the content of the left information window 3 (LIW3) on the tester.</td></tr><tr><td align="left">Question (only up to three responses for identification programs)</td><td align="left">Dialog</td><td align="left">Create a question for the user Yes/no/unknown decisions or a selection from up to eight options is possible as a response.</td></tr><tr><td align="left">Input (not for identification programs)</td><td align="left">Dialog</td><td align="left">Input option for data on the tester using a virtual keyboard. Transfer the data into a variable.</td></tr><tr><td align="left">Help (not for identification programs)</td><td align="left">Dialog</td><td align="left">Create a help for the user that can be called up when needed using "Function test help".</td></tr><tr><td align="left">Message</td><td align="left">Dialog</td><td align="left">Create a message text with different continuations depending on the confirmation.</td></tr><tr><td align="left">Vehicle Status</td><td align="left">Dialog</td><td align="left">Create a system default text for recurring situations, such as "Ignition on".</td></tr><tr><td align="left">Lock Button</td><td align="left">Dialog</td><td align="left">Lock or unlock buttons on the tester.</td></tr><tr><td align="left">Progress Bars</td><td align="left">Dialog</td><td align="left">Create a progress bar in a message. Control bars in a loop using variables or start/stop.</td></tr><tr><td align="left">BZD</td><td align="left">Dialog</td><td align="left">Triggers the equipment status documentation and saves the results for additional processing.</td></tr><tr><td align="left">Declare</td><td align="left">Definition</td><td align="left">Declaration and value allocation of variables in a selectable type.</td></tr><tr><td align="left">Keyword</td><td align="left">Definition</td><td align="left">Definition and value allocations of keywords.</td></tr><tr><td align="left">Expression</td><td align="left">Mapping</td><td align="left">Create mathematical, logical, or alphanumeric (string) expressions.</td></tr><tr><td align="left">Set Status</td><td align="left">Mapping</td><td align="left">Set test status (OK, NOT OK, unknown, diagnosis created and component repaired) and "Select". Manage a dynamic suspicion or OK list. Set the "VIN" and "Equipment" to support automatic identification.</td></tr><tr><td align="left">If... Then... Else</td><td align="left">Procedure</td><td align="left">Create a branch, depending on a two-part condition (status, "Select", mathematical comparison, vehicle status or immobilizer, DTC memory, or ERE).</td></tr><tr><td align="left">Loop, Break Loop</td><td align="left">Procedure</td><td align="left">Create a loop with different interruption options (conformation, number, timeout)</td></tr><tr><td align="left">While, While Not, Break While</td><td align="left">Procedure</td><td align="left">Create a loop with a condition included (test status: "Select", mathematical comparison or vehicle status).</td></tr><tr><td align="left">Wait</td><td align="left">Procedure</td><td align="left">Create a wait loop with the time specified in milliseconds.</td></tr><tr><td align="left">Switch</td><td align="left">Procedure</td><td align="left">Begins a multiple branch. The reaction can be set to String, Select, Constant, Vehicle status, Immobilizer, DTC memory, ERE, or Equipment. The "Switch" action element follows "Case" action elements.</td></tr><tr><td align="left">Case</td><td align="left">Procedure</td><td align="left">Division of a multiple branch. There are multiple "Case" action elements one after the other after a "Switch" action element in a program.</td></tr><tr><td align="left">Measuring channel</td><td align="left">Measurements</td><td align="left">Generates an adaptation command to the user to connect the measuring cable and sensors. The action element is only needed if the display of a measurement on the tester should be suppressed (NODISPLAY).</td></tr><tr><td align="left">Measure voltage, measure current, measure resistance, measure diode</td><td align="left">Measurements</td><td align="left">Creates measuring commands for voltage, current, and resistance measurements as well as diode tests. The settings for the measuring devices and the specification of results variables is done in individual customized action elements.</td></tr><tr><td align="left">Measure pressure</td><td align="left">Measurements</td><td align="left">Creates a measuring command for one of four adaptable pressure sensors.</td></tr><tr><td align="left">Measure temperature</td><td align="left">Measurements</td><td align="left">Creates a measuring command for temperature measurement.</td></tr><tr><td align="left">Oscilloscope</td><td align="left">Measurements</td><td align="left">Creates measuring commands for DSO.</td></tr><tr><td align="left">High-voltage block</td><td align="left">Measurements</td><td align="left">Creates a procedure that is specifically for high voltage.</td></tr><tr><td align="left">High-voltage break</td><td align="left">Measurements</td><td align="left">Ends a procedure that is specifically for high voltage.</td></tr><tr><td align="left">High-voltage measurement data</td><td align="left">Measurements</td><td align="left">Checks high-voltage measured values or the high-voltage measurement status.</td></tr><tr><td align="left">Ecukom, Ecukom fault message</td><td align="left">Ecukom</td><td align="left">Creates a communication command to a control module. All parameters are called up from selection lists. The fault codes for a control module can be hidden if needed using the "Ecukom fault message" action element.</td></tr><tr><td align="left">Code gateway</td><td align="left">Ecukom</td><td align="left">Calls up "Coding 2" OBD function, calls up "Check specified components list" job, or calls up "Check specified components list with equipment network update" job.</td></tr><tr><td align="left">Read measured values</td><td align="left">Ecukom</td><td align="left">Creates an action element to read KWP measured values according to the specifications from the measured value table (Administration).</td></tr><tr><td align="left">Read ASAM measured values</td><td align="left">Ecukom</td><td align="left">Creates an action element to display UDS measured values.</td></tr><tr><td align="left">ASAM Ecukom</td><td align="left">Ecukom</td><td align="left">Creates a communication command to an ASAM ODX control module. All parameters are called up from selection lists. The stored results can be evaluated using the "ASAM result" action element.</td></tr><tr><td align="left">ASAM result</td><td align="left">Ecukom</td><td align="left">Creates an action element for evaluating results from an ASAM Ecukom action element.</td></tr><tr><td align="left">ASAM identification</td><td align="left">Ecukom</td><td align="left">Creates an action element for determining the control module group ID</td></tr><tr><td align="left">ASAM variant identification</td><td align="left">Ecukom</td><td align="left">Creates an action element for determining the control module variant</td></tr><tr><td align="left">ASAM hex service</td><td align="left">Ecukom</td><td align="left">Creates an action element for setting parameters for a physical/functional protocol data unit (PDU)</td></tr><tr><td align="left">Update log book</td><td align="left">Ecukom</td><td align="left">Generates an action element for updating the log book with identification data from master and sub-systems</td></tr><tr><td align="left">Recalculate test plan</td><td align="left">Ecukom</td><td align="left">Generates an action element to recalculate the test plan</td></tr><tr><td align="left">Qualify Test Plan</td><td align="left">Ecukom</td><td align="left">Generates an action element to qualify the test plan</td></tr><tr><td align="left">Read file</td><td align="left">File</td><td align="left">Reads data from a file.</td></tr><tr><td align="left">Write file</td><td align="left">File</td><td align="left">Writes data in a file.</td></tr><tr><td align="left">Delete file</td><td align="left">File</td><td align="left">Deletes data in a file.</td></tr><tr><td align="left">Login</td><td align="left">Online connection</td><td align="left">Creates a connection to the online database.</td></tr><tr><td align="left">Log out</td><td align="left">Online connection</td><td align="left">Disconnects a connection to the online database.</td></tr><tr><td align="left">Write XML/XML IA</td><td align="left">Online connection</td><td align="left">Transfers data from the function test to an XML working file.</td></tr><tr><td align="left">Expand XML</td><td align="left">Online connection</td><td align="left">Transfers data of the same type from the function test to an XML working file.</td></tr><tr><td align="left">Expand XML IA</td><td align="left">Online connection</td><td align="left">Transfers data of the same type from the function test to an XML working file.</td></tr><tr><td align="left">XML set count</td><td align="left">Online connection</td><td align="left">Specifies the number of data sets in an XML working file.</td></tr><tr><td align="left">Read XML sentence</td><td align="left">Online connection</td><td align="left">Reads data of the same type from the XML working file into a function test.</td></tr><tr><td align="left">Read XML</td><td align="left">Online connection</td><td align="left">Transmits variables from a working file.</td></tr><tr><td align="left">Read XML IA</td><td align="left">Online connection</td><td align="left">Transmits variables from a working file.</td></tr><tr><td align="left">Send online</td><td align="left">Online connection</td><td align="left">Sends the working file to the online database.</td></tr><tr><td align="left">Receive online</td><td align="left">Online connection</td><td align="left">Receives the working file from the online database.</td></tr><tr><td align="left">Expand log</td><td align="left">Online connection</td><td align="left">Expands the online diagnostic log to include variables and their content.</td></tr><tr><td align="left">Send log</td><td align="left">Online connection</td><td align="left">Selection of a DTC memory or diagnostic log.</td></tr><tr><td align="left">Check PR numbers</td><td align="left">Online connection</td><td align="left">Generates an action element to check the PR numbers in the operating system</td></tr><tr><td align="left">Check SecurityKey (VFA)</td><td align="left">Online connection</td><td align="left">Generates an action element to check the SecurityKey for Cyclone in the operating system</td></tr><tr><td align="left">Request Download (VFA)</td><td align="left">Online connection</td><td align="left">Generates an action element to request the control module software update from the cooperation partner via the D³ server.</td></tr><tr><td align="left">Delete flash files (VFA)</td><td align="left">Online connection</td><td align="left">Generates an action element to delete the flash folder on the tester.</td></tr><tr><td align="left">Write JSON</td><td align="left">Online connection</td><td align="left">Generate an action element to create and enhance a JSON request by specifying a reference.</td></tr><tr><td align="left">Send/receive JSON</td><td align="left">Online connection</td><td align="left">Generate an action element to send a JSON request and receive a JSON response.</td></tr><tr><td align="left">Read JSON</td><td align="left">Online connection</td><td align="left">Generate an action element to evaluate a JSON response.</td></tr><tr><td align="left">Determining the MBs</td><td align="left">Module balancing</td><td align="left">Creates an action element for determining the usable module balancers.</td></tr><tr><td align="left">MB connection</td><td align="left">Module balancing</td><td align="left">Creates an action element for establishing or ending the connection to the module balancer.</td></tr><tr><td align="left">Module data request</td><td align="left">Module balancing</td><td align="left">Creates an action element for determining the tool number of the adapter cable that is suitable for the HV module.</td></tr><tr><td align="left">Start balancing procedure</td><td align="left">Module balancing</td><td align="left">Creates an action item for initiating the charging/discharging process in the module balancer.</td></tr><tr><td align="left">Request (dis)charging parameters</td><td align="left">Module balancing</td><td align="left">Creates an action element for the (cyclical) query of the charging/discharging parameters for the balancing process.</td></tr><tr><td align="left">MB qualification report</td><td align="left">Module balancing</td><td align="left">Creates an action element for calling up the qualification data of the module balancer and for the module balancer release.</td></tr><tr><td align="left">MB process status request</td><td align="left">Module balancing</td><td align="left">Creates an action element for determining the balancing process status.</td></tr><tr><td align="left">Request module hardware info</td><td align="left">Module balancing</td><td align="left">Creates an action element for determining the parts and serial number as well as the type of input made.</td></tr><tr><td align="left">MB error message</td><td align="left">Module balancing</td><td align="left">Creates an action element for suppressing the MB error and notice messages.</td></tr><tr><td align="left">MB info request</td><td align="left">Module balancing</td><td align="left">Creates an action element for querying the version and calibration information of the module balancer.</td></tr><tr><td align="left">MB status request</td><td align="left">Module balancing</td><td align="left">Creates an action element for querying the status of the module balancer.</td></tr><tr><td align="left">MB classification report</td><td align="left">Module balancing</td><td align="left">Creation of an action element to call up classification data from the new module to be classified by the module balancer and for initiation of classification on the module balancer.</td></tr><tr><td align="left">Flash path</td><td align="left">Flash</td><td align="left">Determines the flash path from a control table.</td></tr><tr><td align="left">Flash container</td><td align="left">Flash</td><td align="left">Determines the flash container from a control table.</td></tr><tr><td align="left">Create flash control file</td><td align="left">Flash</td><td align="left">Creation of flash control file.</td></tr><tr><td align="left">Parallel Flashing</td><td align="left">Flash</td><td align="left">Performing parallel flashing using a flash control file.</td></tr><tr><td align="left">Documents</td><td align="left">Other</td><td align="left">Command to display documents on the tester.</td></tr><tr><td align="left">Comment</td><td align="left">Other</td><td align="left">Creates a "Comment" action element in order to introduce notices in the structure of the test program; no display on the tester.</td></tr><tr><td align="left">Java box</td><td align="left">Other</td><td align="left">Direct embedding of a Java source code.</td></tr><tr><td align="left">Sub-Program</td><td align="left">Other</td><td align="left">Creates a sub-program that calls up other function tests.</td></tr><tr><td align="left">Log</td><td align="left">Other</td><td align="left">Activates or deactivates the diagnostic log.</td></tr></tbody></table>

**Table 73. Action Elements**

##### <a id="Funktionstesteditor.Arbeitsflaeche.Einstellungen"></a>7.14.9.1. Settings

Any settings are retained once they have been saved. This means that a newly-opened function test will have the same settings, such as in regard to the palette, as the last saved function test.

##### <a id="Funktionstesteditor.Arbeitsflaeche.Bearbeitungshistorie"></a>7.14.9.2. Revision History (Undo/Repeat)

In the function test graphic display, user actions can be undone or repeated by right-clicking the mouse on a context menu. The keyboard shorts CTRL+Z and CTRL+Y, and the corresponding functions in the menu bar and the buttons can also be used. See [Figure 374, “Editing History”](7-14-9-desktop.md#figure.Funktionstesteditor.Arbeitsflaeche.Bearbeitungshistorie "Figure 374. Editing History").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Bearbeitungshistorie"></a>

![Image: Redo/Undo revision history](images/fte_Bearbeitungshistorie.png)

**Figure 374. Editing History**

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Anlegen"></a>7.14.9.3. Create Action Element

To create, an action element is selected from the palette and is added between two existing elements or at the start/end point of the test step by clicking the arrow. The following add modes are available:

- Adding with the Shift key pressed opens the dialog for the action element after adding.
- Adding with the CTRL key pressed allows you to enter action elements multiple times.

The action element appears in the corresponding location in the test sequence, but still has a red border and text. See [Figure 375, “New Action Element Created”](7-14-9-desktop.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Anlegen "Figure 375. New Action Element Created"). The function test can still be saved with the unedited action elements.

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Anlegen"></a>

![Image: new action element created](images/fte_rote_Elemente.png)

**Figure 375. New Action Element Created**

The unedited action elements are listed in the [Problem view](7-14-25-problems-view.md "7.14.25. Problems (View)"). See [Figure 376, “Problem View - Unedited Elements”](7-14-9-desktop.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Anlegen2 "Figure 376. Problem View - Unedited Elements").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Anlegen2"></a>

![Image: problem view - unedited elements](images/fte_Problem_unbearbeitet.png)

**Figure 376. Problem View - Unedited Elements**

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselement_Dialog"></a>7.14.9.4. Edit Action Element

Parameters can be set for the attributes of an action element using the respective dialog.

The dialog can be opened by double-clicking on the respective action element. Or the element can also be marked and then the "Edit" item can be selected in the context menu. See [Figure 377, “Edit Action Element”](7-14-9-desktop.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselement_Dialog "Figure 377. Edit Action Element").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselement_Dialog"></a>

![Image: edit action element](images/fte_Kontext_Bearbeiten.png)

**Figure 377. Edit Action Element**

As a third option, the dialog can be opened using the Edit main menu (menu item: Edit).

The associated attributes can be changed in the dialog. After closing the dialog, the attributes are validated and, if the validation was successful, the action element is then shown with a red border and black text. See [Figure 378, “Valid Action Element”](7-14-9-desktop.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselement_Dialog2 "Figure 378. Valid Action Element"). The corresponding entry in the problem view is removed.

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselement_Dialog2"></a>

![Image: valid action element](images/fte_Valide.png)

**Figure 378. Valid Action Element**

If the validation could not be completed successfully, the dialog cannot be closed unless the entire editing procedure is canceled. This means you can only edit the attributes of an action element in a valid form.

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselement_Kopieren"></a>7.14.9.5. Copy Action Element

Action elements can be selected by clicking on them and by area selection. The copying is done using the menu bar, the keyboard shortcut CTRL+C, the context menu, or by dragging and dropping.

When dragging and dropping, the selected element is moved into the area between two action elements while the left mouse button is pressed and held.

Action elements can be moved from the editor onto a test step in the test step view by dragging and dropping. They are added at the beginning of the test step.

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselement_Ausschneiden"></a>7.14.9.6. Cut Action Element

Action elements can be selected by clicking on them and by area selection. The cutting is done using the menu bar, the keyboard shortcut CTRL + X, or the context menu.

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselement_Einfuegen"></a>7.14.9.7. Insert Action Element

To insert, the arrow between two action elements or the start/end point must be selected. This is indicated by a thicker line.

The adding is done using the menu bar, the keyboard shortcut CTRL + V, or the context menu.

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselement_Selektieren"></a>7.14.9.8. Select Action Element

Action elements can be selected by clicking on them and by area selection.

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Loeschen"></a>7.14.9.9. Delete Action Elements

Action elements can be selected by clicking on them and by area selection. The deleting can be done using the menu bar, the delete button, or the context menu.

##### <a id="Funktionstesteditor.Arbeitsflaeche.Tooltips"></a>7.14.9.10. Tool tips

If you move the mouse cursor over a test step and hold it there for approximately two seconds without triggering a function, a yellow text field that lists the current parameters for the selected symbol appears.

Tool tips appear if the mouse cursor is held over the action element for an extended period of time. See [Figure 379, “Tool tips”](7-14-9-desktop.md#figure.Funktionstesteditor.Arbeitsflaeche.Tooltips "Figure 379. Tool tips").

The tool tip contains the same information as the properties view (see [Section 7.14.21, “Properties (View)”](7-14-21-properties-view.md "7.14.21. Properties (View)")), namely the name and the attributes of the action element.

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Tooltips"></a>

![Image: tool tips](images/fte_Tooltip.png)

**Figure 379. Tool tips**

##### <a id="Funktionstesteditor.Arbeitsflaeche.Palette"></a>7.14.9.11. Palette

The action elements are displayed in the palette on the right side of the screen. To insert, select the desired action element in the palette (click with left mouse button). Then, position the mouse cursor at the location in the function test (at the connecting lines) where the action element should be inserted. Then press the left mouse button again.

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Palette"></a>

![Image: palette](images/fte_arbeitsflaeche_allgemein_Palette.png)

**Figure 380. Palette**

The action elements are organized in the palette in multiple categories (sections):

- [Section 7.14.10, “Category - Dialog”](7-14-10-category-dialog.md "7.14.10. Category - Dialog")
- [Section 7.14.11, “Category - Definition”](7-14-11-category-definition.md "7.14.11. Category - Definition")
- [Section 7.14.12, “Category - Mapping”](7-14-12-category-mapping.md "7.14.12. Category - Mapping")
- [Section 7.14.13, “Category - Process”](7-14-13-category-process.md "7.14.13. Category - Process")
- [Section 7.14.14, “Category - Measurement”](7-14-14-category-measurement.md "7.14.14. Category - Measurement")
- [Section 7.14.15, “Category - Ecukom”](7-14-15-category-ecukom.md "7.14.15. Category - Ecukom")
- [Section 7.14.16, “Category - File”](7-14-16-category-file.md "7.14.16. Category - File")
- [Section 7.14.17, “Category - Connection”](7-14-17-category-connection.md "7.14.17. Category - Connection")
- [Section 7.14.18, “Category - Module balancing”](7-14-18-category-module-balancing.md "7.14.18. Category - Module balancing")
- [Section 7.14.19, “Category - Flash”](7-14-19-category-flash.md "7.14.19. Category - Flash")
- [Section 7.14.20, “Category - Miscellaneous”](7-14-20-category-miscellaneous.md "7.14.20. Category - Miscellaneous")

The palette is a separate window in ODIS Creator. If multiple function tests are opened at the same time, the palette will only be displayed once. If the palette is closed, you can display it again using the "Reset view" function.

The width of the palette can be changed manually. The categories (sections) can be opened, pinned, and closed. These changes to the display, location, and size of the palette are not saved.

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Palette.Kontextmenue"></a>

![Image: palette context menu](images/fte_arbeitsflaeche_allgemein_Palette_kontextmenue.png)

**Figure 381. Palette Context Menu**

The following technical functions can be accessed using the palette context menu:

- [the section called “Modify Palette”](7-14-9-desktop.md#Funktionstesteditor.Arbeitsflaeche.Palette.anpassen "Modify Palette")
- [the section called “Adjust Palette”](7-14-9-desktop.md#Funktionstesteditor.Arbeitsflaeche.Palette.einstellen "Adjust Palette")
- [the section called “Reset Palette”](7-14-9-desktop.md#Funktionstesteditor.Arbeitsflaeche.Palette.zuruecksetzen "Reset Palette")

###### <a id="Funktionstesteditor.Arbeitsflaeche.Palette.anpassen"></a>Modify Palette

The dialog that follows will open after selecting the "Modify..." menu item.

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Palette.anpassen"></a>

![Image: modify palette](images/fte_arbeitsflaeche_allgemein_Palette_anpassen.png)

**Figure 382. Modify Palette**

The dialog can be used to change the entries in the palette:

- Create, edit, and delete palette entries (including sections or palette groups and separating lines).
- Sort the entries with the "Move down" and "Move up" buttons.
- Delete or hide palette entries (including sections and separating lines).

The modifications to the palette are saved in the working area for that Windows user across all sessions.

###### <a id="Funktionstesteditor.Arbeitsflaeche.Palette.einstellen"></a>Adjust Palette

The dialog that follows will open after selecting the "Settings..." menu item.

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Palette.einstellen"></a>

![Image: adjust palette](images/fte_arbeitsflaeche_allgemein_Palette_einstellen.png)

**Figure 383. Adjust Palette**

The text type, the layout, and the options for the sections or palette groups can be changed using the palette settings dialog. The settings are saved for that Windows user across all sessions.

###### <a id="Funktionstesteditor.Arbeitsflaeche.Palette.zuruecksetzen"></a>Reset Palette

The default palette is restored after selecting the "Reset palette" menu item.

##### <a id="Funktionstesteditor.Arbeitsflaeche.Layout"></a>7.14.9.12. Layout

The layout describes the display type for action elements and their textual additional information. The action elements each contain a title and brief command information. Additional information is also given at the edges of the branches and blocks. The default is shown in the following image.

<a id="figure.Funktionstesteditor.Arbeitsflaeche.DefaultLayout"></a>

![Image: default layout](images/fte_Arbeitsflaeche_Layout.png)

**Figure 384. Default Layout**

The layout can be changed under settings. This way, you can configure your own layout according to your needs. The settings are located in the dialog under “Function test editor >> Layout”. The settings are opened as usual in the menu under “Help >> User settings”. The settings are stored locally in the user directory on the computer and only apply to that user on the same computer.

<a id="figure.Funktionstesteditor.Arbeitsflaeche.DefaultLayout.Benutzervorgaben.Default"></a>

![Image: default layout](images/fte_Arbeitsflaeche_Layout_Benutzervorgaben_Default.png)

**Figure 385. Default Layout**

The user settings for the commands layout are considered expert settings and may result in desired information no longer being visible in the function test editor. The user settings apply to the print settings and the SVG export as well as the display in the function test editor.

<a id="figure.Funktionstesteditor.Arbeitsflaeche.DefaultLayout.Benutzervorgaben.LayoutGroessen"></a>

![Image: layout sizes for configuration](images/fte_Arbeitsflaeche_Layout_Benutzervorgaben_LayoutGroessen.png)

**Figure 386. Layout Sizes for Configuration**

The following settings can be changed:

- Command width and height
- Horizontal and vertical grid spacing (grid X, grid Y)
- Activating and deactivating content in the commands (title, brief information, +/- symbol, command icon)

After applying the user settings, only some of the settings will be applied immediately in the open function test editor. To apply the layout completely, you must close the affected function test editor and reopen it.

<a id="table.hinweis.fte.benutzervorgabe"></a>

<table border="1" summary="Note about Known Eclipse Error"><colgroup><col align="center"/><col align="left"/></colgroup><tbody valign="top"><tr><td align="center" valign="top"><span class="inlinemediaobject"><img alt="Note symbol" src="images/info.png"/></span></td><td align="left" valign="top"><span class="bold"><strong>Note:</strong></span> There is a known eclipse error when selecting the font type in the settings. Additional fields for color and script are displayed in the system dialog. These do not have any effect on the selected color in the settings. There is an additional selection for color in the settings (for command title and the brief command information).</td></tr></tbody></table>

**Table 74. Note about Known Eclipse Error**

The modified user settings for layout can be reset to the default values under settings.

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-14-8-use-switchkey-variables.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="7-14-function-test-editor.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="7-14-10-category-dialog.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">7.14.8. Use SwitchKey Variables </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 7.14.10. Category - Dialog</td></tr></table>
