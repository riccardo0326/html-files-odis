[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md) > [7.14. Function Test Editor](7-14-function-test-editor.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.14.15. Category - Ecukom</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-14-14-category-measurement.md">Prev</a> </td><th align="center" width="60%">7.14. Function Test Editor</th><td align="right" width="20%"> <a accesskey="n" href="7-14-16-category-file.md">Next</a></td></tr></table>

---

#### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom"></a>7.14.15. Category - Ecukom

This category contains action elements for communication with control modules. The following action elements are used:

- [Section 7.14.15.1, “Action Element - Ecukom”](7-14-15-category-ecukom.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.EcuKom "7.14.15.1. Action Element - Ecukom")
- [Section 7.14.15.2, “Action Element - Ecukom Error Message”](7-14-15-category-ecukom.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.EcuKom_Fehlermeldung "7.14.15.2. Action Element - Ecukom Error Message")
- [Section 7.14.15.3, “Action Element - Ecukom Gateway”](7-14-15-category-ecukom.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.EcuKom_Gateway "7.14.15.3. Action Element - Ecukom Gateway")
- [Section 7.14.15.4, “Action Element - Read Measured Values”](7-14-15-category-ecukom.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.Messwerte_Lesen "7.14.15.4. Action Element - Read Measured Values")
- [Section 7.14.15.5, “Action Element - Read ASAM Measured Values”](7-14-15-category-ecukom.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.AsamMesswerte_Lesen "7.14.15.5. Action Element - Read ASAM Measured Values")
- [Section 7.14.15.6, “Action Element - ASAM Ecukom”](7-14-15-category-ecukom.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.Asam_EcuKom "7.14.15.6. Action Element - ASAM Ecukom")
- [Section 7.14.15.7, “Action Element - ASAM Result”](7-14-15-category-ecukom.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.Asam_Ergebnis "7.14.15.7. Action Element - ASAM Result")
- [Section 7.14.15.8, “Action Element - ASAM Identification”](7-14-15-category-ecukom.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.Asam_Identifikation "7.14.15.8. Action Element - ASAM Identification")
- [Section 7.14.15.9, “Action Element - ASAM Variant Identification”](7-14-15-category-ecukom.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.Asam_Varianten "7.14.15.9. Action Element - ASAM Variant Identification")
- [Section 7.14.15.10, “Action Element - ASAM Hex Service”](7-14-15-category-ecukom.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.AsamHex_Service "7.14.15.10. Action Element - ASAM Hex Service")
- [Section 7.14.15.11, “Action Element - Update Log Book”](7-14-15-category-ecukom.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.Identifikationsdaten_Auslesen "7.14.15.11. Action Element - Update Log Book")
- [Section 7.14.15.12, “Action Element - Recalculate Test Plan”](7-14-15-category-ecukom.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.Pruefplan_Neuberechnen "7.14.15.12. Action Element - Recalculate Test Plan")
- [Section 7.14.15.13, “Set Communication Type Action Element”](7-14-15-category-ecukom.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.Kommunikationsweg_Setzen "7.14.15.13. Set Communication Type Action Element")
- [Section 7.14.15.14, “Action Element - Qualify Test Plan”](7-14-15-category-ecukom.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.Pruefplan_Qualifizieren "7.14.15.14. Action Element - Qualify Test Plan")
- [Section 7.14.15.15, “Action Element - Close All Logical Links”](7-14-15-category-ecukom.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.Alle_Logicallinks_schlie%C3%9Fen "7.14.15.15. Action Element - Close All Logical Links")

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.EcuKom"></a>7.14.15.1. Action Element - Ecukom

The "Ecukom" action element can be seen in [Figure 450, “Ecukom Action Element”](7-14-15-category-ecukom.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.EcuKom "Figure 450. Ecukom Action Element").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.EcuKom"></a>

![Image: Ecukom action element](images/fte_arbeitsflaeche_ecukom_ecukom.png)

**Figure 450. Ecukom Action Element**

Using this action, you can conduct communication with a control module, execute functions (such as checking the DTC memory), and read back results for further processing. The type of orders, names of the communication parameters, and the work sequence to be followed come from the interface description of the EcuComFramework API for the protocols KW1281/2000/6000.

The action element uses the central EcuComFramework API internally for communication with the control module or the control module group. The EcuComFramework replaces the old communication logic with parameterization using control module description files.

###### <a id="d4e22627"></a>7.14.15.1.1. Control Module Variants, Logical Link

See [Section 7.14.15.16.1, “Control Module Variants”](7-14-15-category-ecukom.md#Funktionstesteditor.Allgemeine_Funktionalitaet.SG-Gruppe "7.14.15.16.1. Control Module Variants").

###### <a id="d4e22631"></a>7.14.15.1.2. Diagnostic Service/Order

See [Section 7.14.15.16.2, “Diagnostic Service/Order Selection”](7-14-15-category-ecukom.md#Funktionstesteditor.Allgemeine_Funktionalitaet.Auswahl-Dienst "7.14.15.16.2. Diagnostic Service/Order Selection").

###### <a id="d4e22635"></a>7.14.15.1.3. Request Parameter

See [Section 7.14.15.16.4, “Request Parameter”](7-14-15-category-ecukom.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.Allgemein.Requests "7.14.15.16.4. Request Parameter").

###### <a id="d4e22639"></a>7.14.15.1.4. Positive Response Parameter

See [Section 7.14.15.16.5, “Positive Response Parameter”](7-14-15-category-ecukom.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.SGPositiveAntwortparameter "7.14.15.16.5. Positive Response Parameter").

###### <a id="d4e22643"></a>7.14.15.1.5. Output

With this selection, the tester displays results parameters when the "Read" button is pressed. The cycle is canceled if the user presses the "Read" button again or continues the program with "Next".

###### <a id="d4e22646"></a>7.14.15.1.5.1. Results Text

Only with the "Output" option: using the "Edit" button, you can specify an accompanying text for the measurement in the "Results text" field, which the user will see when there is output on the touchscreen.

###### <a id="SGAntwortstatus"></a>7.14.15.1.6. Response status

You can specify a variable for evaluating the response status for the control module communication performed. "OKAY" is returned when communication is successful.

###### <a id="SGSet0Satzanzahl"></a>7.14.15.1.7. Sentence number

The set number delivers the number of possible results sets for specific diagnostic services.

###### <a id="SGSet0Variante"></a>7.14.15.1.8. Version

The Variants option can be used for the service/job "Identify control module" to evaluate special control module variants.

###### <a id="SGSet0Zuendungszustand"></a>7.14.15.1.9. Ignition status

By specifying a variable, the ignition status of the vehicle can be evaluated.

###### <a id="d4e22661"></a>7.14.15.1.10. Progress Bars

If you mark this option, a message will appear in front with the "Bars" option selected that displays bar indicators labeled 0 to 100%. When running, the duration of the Ecukom command is determined automatically and this controls the progress shown by the progress bars.

###### <a id="d4e22664"></a>7.14.15.1.11. Variable

The description for selecting variables is found in [Section 7.14.6, “Using Variables”](7-14-6-using-variables.md "7.14.6. Using Variables"). The definition of variables is found in [Section 7.14.11.1, “Action Element - Declare Variable”](7-14-11-category-definition.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Definition.Deklariere_Variablen "7.14.11.1. Action Element - Declare Variable").

###### <a id="d4e22669"></a>7.14.15.1.12. Keyword

The description for selecting keywords is found in [Section 7.14.6, “Using Variables”](7-14-6-using-variables.md "7.14.6. Using Variables"). The definition of keywords is found in [Section 7.14.11.4, “Action Element - Define Keyword”](7-14-11-category-definition.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Definition.Definiere_Kennwort "7.14.11.4. Action Element - Define Keyword").

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.EcuKom_Fehlermeldung"></a>7.14.15.2. Action Element - Ecukom Error Message

The "Ecukom error message" action element can be seen in [Figure 451, “Ecukom Error Message Action Element”](7-14-15-category-ecukom.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.EcuKom_Fehlermeldung "Figure 451. Ecukom Error Message Action Element").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.EcuKom_Fehlermeldung"></a>

![Image: Ecukom_ErrorMessage action element](images/fte_arbeitsflaeche_ecukom_ecukomfehlermeldung.png)

**Figure 451. Ecukom Error Message Action Element**

You can disable system error messages with this command. This function is necessary for traversal tests. If a control module does not respond, an error message would appear automatically on the touchscreen. To prevent this, you can set the "Ecukom error message" command to "off" before an "Ecukom" command that you use in the vehicle identification, and then set it back to "on" after the "Ecukom" command.

The on/off action fields activate or deactivate the Ecukom error messages for the commands that follow.

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.EcuKom_Gateway"></a>7.14.15.3. Action Element - Ecukom Gateway

The "Ecukom gateway" action element can be seen in [Figure 452, “Ecukom Gateway Action Element”](7-14-15-category-ecukom.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.EcuKom_Gateway "Figure 452. Ecukom Gateway Action Element").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.EcuKom_Gateway"></a>

![Image: Ecukom gateway action element](images/fte_arbeitsflaeche_ecukom_ecukomgateway.png)

**Figure 452. Ecukom Gateway Action Element**

You can perform the tester functions "Code gateway specified components list", "Update specified components list" and "Update equipment network" using the "Ecukom gateway" action element.

###### <a id="d4e22701"></a>7.14.15.3.1. Code Gateway Specified Components List

If you select this option, the "Read/write long coding" OBD function runs on the tester.

###### <a id="d4e22704"></a>7.14.15.3.2. Update Specified Components List

If you select this option, the "Check\_SpecifiedComponentsList" job runs and the tester log book is updated.

###### <a id="d4e22707"></a>7.14.15.3.3. Update Equipment Network

If you select this option, the "Check\_SpecifiedComponentsList" job runs, the tester log book is updated, and then the identification results for the vehicle system test are updated.

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.Messwerte_Lesen"></a>7.14.15.4. Action Element - Read Measured Values

The "Read measured values" action element can be seen in [Figure 453, “Read Measured Values Action Element”](7-14-15-category-ecukom.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.Messwerte_Lesen "Figure 453. Read Measured Values Action Element").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.Messwerte_Lesen"></a>

![Image: read measured values action element](images/fte_arbeitsflaeche_ecukom_messwertelesen.png)

**Figure 453. Read Measured Values Action Element**

Using the "Read measured values" command, you can access available KWP measured value tables and transfer them into the command. This action element changes the test step status (OK/NOT OK). As long as a measured value lies outside of the tolerance, the NOT OK status remains.

<a id="table.hinweis.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.Messwerte_Lesen"></a>

<table border="1" summary="Read Measured Values Note"><colgroup><col align="center"/><col align="left"/></colgroup><tbody valign="top"><tr><td align="center" valign="top"><span class="inlinemediaobject"><img alt="Note symbol" src="images/info.png"/></span></td><td align="left" valign="top"><span class="bold"><strong>Note:</strong></span> Note that the display frequency in the operating system corresponds at most with the display in OBD if the measured values come from from the same vehicle system and the same group number. If measured values should be read from different vehicle systems or group numbers, limitations in performance and synchronization must be expected.</td></tr></tbody></table>

**Table 105. Read Measured Values Note**

  

###### <a id="d4e22738"></a>7.14.15.4.1. Measured Values Table

The measured value tables selected using the "Selection" button are displayed in this field. If multiple entries are available, the entries in the list field below only apply to the selected measured values table.

###### <a id="d4e22741"></a>7.14.15.4.1.1. Selection

If you click this button, a selection list of available measured values tables that are created and managed in editing appears.

###### <a id="d4e22744"></a>7.14.15.4.1.2. Delete

You can delete a measured value table that was already entered using this function.

###### <a id="d4e22747"></a>7.14.15.4.1.3. List and Results Field

A measured values table for selecting measured values appears in the tester without any entries. You can use the entries to make a pre-selection for the measured values, meaning the "Read measured values" screen appears on the tester immediately. The measured values are only output if the "Output" option (at the bottom of the dialog) is selected [Section 7.14.15.4.9, “Executing Read Measured Values in ODIS Service”](7-14-15-category-ecukom.md#option.ausgabe.gesetzt).

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.Messwerte_Lesen_Tabelleneintrag"></a>

![Image: measured value table entry selection](images/fte_arbeitsflaeche_ecukom_messwertelesen_tabelleneintrag.png)

**Figure 454. Measured Value Table Entry Selection**

A new entry is added to the list field using the "+" button. Depending on the type of measured value table (UDS or KWP), it may also be possible to add the entry by selecting from the measured value table using the (...) button in the first column. The selected data set is entered in the table. Complete the entries in the columns "Variable value", "Variable unit", "Status", "Dimension", and OK/NOT OK here. The entries have the following functions:

- Group (KWP control modules only): the display group is shown here.
- Field (KWP control modules only): the display field is entered here.
- Name (ASAM-ODX control modules only): refers to the measured value in the measured value table using the system names.
- Variable value: enter a variable defined in the function test if necessary using the "Variable" button, which will apply the numerical value (MV\_value) that was read from the vehicle system for furthering processing in the program.
- Variable unit: enter a variable defined in the function test if necessary using the "Variable" button, which will apply the physical unit (MVUnit\_text) that was read from the vehicle system for furthering processing in the program.
- Variable status, optional: if you are working with tolerances, you can add a variable defined in the function test for a result status using the "Variable" button. Because you can program multiple measurements in a command, you can evaluate an individual measured value status within the tolerance = 1 or outside of the tolerance = 0 later in the program.
- Dimension: enter a variable (string) defined in the function test here if necessary, which will receive the dimension for the selected measured value from the measured values table.
- OK/NOT OK: enter the conditions for the measured value tolerance here, if necessary. The result of the tolerance evaluation can be assigned to a variable under "Status". The specifications in the "Read measured values" command take priority over the specifications in the measured values table.

###### <a id="d4e22777"></a>7.14.15.4.2. Cycle Time

Alternative to cycle number/cycle OK: you can enter the cycle time for the measuring procedure here. The default value is 1 s. The value can be specified using a variable. For example, if you enter 10 s, the entire measuring procedure will run for 10 seconds.

###### <a id="d4e22780"></a>7.14.15.4.3. Cycle Number

Alternative to cycle number/cycle OK: you can enter the cycle number for the measuring procedure here. The value can be specified using a variable. For example, if you enter 15, then 15 measuring cycles will be performed. The time for a measuring cycle depends on the application.

###### <a id="d4e22783"></a>7.14.15.4.4. Cycle OK

Alternative to cycle time/number: the measuring procedure is canceled if all measured values in the command have reached the OK status or if the adjustable time limit (max time) was reached. The max time value can be specified using a variable.

###### <a id="d4e22786"></a>7.14.15.4.5. Additional text

You can enter a message text here that will only be displayed in display mode.

###### <a id="d4e22789"></a>7.14.15.4.5.1. Output

The command can be implement with output on the tester (control field activated = display mode) or without output (control field not activated = NoDisplay mode). The effects are described in ["Output" option activated](7-14-15-category-ecukom.md#option.ausgabe.gesetzt) and ["Output" option not activated](7-14-15-category-ecukom.md#option.ausgabe.nicht.gesetzt).

###### <a id="d4e22794"></a>7.14.15.4.6. Suspicion List Evaluation

If you mark this selection, available suspicion lists will be considered when there are NOT OK results.

- Display mode:

  The "Test program" button appears when the measured value is selected. If the "Test program" button is pressed and the measurement result is NOT OK, the specified suspicion list will be processed immediately after ending the test program (without routing to the test plan). After completing all test programs, the status of the individual test programs will be entered in the test plan.
- No Display mode:

  The references diagnostic objects are set in the test plan and must be started from there.

###### <a id="d4e22805"></a>7.14.15.4.7. Variable

The description for selecting variables is found in [Section 7.14.6, “Using Variables”](7-14-6-using-variables.md "7.14.6. Using Variables"). The definition of variables is found in [Section 7.14.11.1, “Action Element - Declare Variable”](7-14-11-category-definition.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Definition.Deklariere_Variablen "7.14.11.1. Action Element - Declare Variable").

###### <a id="d4e22810"></a>7.14.15.4.8. Keyword

The description for selecting keywords is found in [Section 7.14.6, “Using Variables”](7-14-6-using-variables.md "7.14.6. Using Variables"). The definition of keywords is found in [Section 7.14.11.4, “Action Element - Define Keyword”](7-14-11-category-definition.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Definition.Definiere_Kennwort "7.14.11.4. Action Element - Define Keyword").

###### <a id="d4e22815"></a>7.14.15.4.9. Executing Read Measured Values in ODIS Service

If the "Read measured values" command does not contain any explicit measured value presets, the operating system will generate a selection menu with the specified data sets from the measured value tables. Measured values that appear in multiple display groups with the same name will also appear multiple times for selection. Measured values in a measured value block are displayed in groups with the display group/field and the same background color.

You can select any number of measured values for the following cyclical display. You can cancel the display using the "Go to" function and select the measured values again.

Manual selection is not possible when there is an explicit measured value preset. The values preset in the command are read and evaluated (regardless of the "Output" setting).

After a manual or preset measured value selection, the measured value function reads the measured values according to the cycle parameters using the "Read\_measured value block" job.

<a id="option.ausgabe.gesetzt"></a>**"Output" activated**

The selected measured values are displayed on the tester. Note: if no measured value was selected, all measured values in the table are displayed.

<a id="option.ausgabe.nicht.gesetzt"></a>**"Output" not activated**

If the "Output" option is not activated (No Display mode), the measures values are read as in display mode but not displayed, and they are stored in the specified variables. If at lease one measured value is outside the tolerance, then the entire command is "NOT OK". If diagnostic objects are in the suspicion list, they will be placed in the test plan for further processing after the function test ends.

**Measuring cycle restriction**

The following rules apply for the measuring cycle restriction:

"Output" option activated (display mode):

- no cycle parameter specified: display until operation is continued
- cycle time or number specified: measure until the cycle parameters are met or until the "Next" button is pressed
- specified cycle status parameter: measure until all values are OK, the preset time has elapsed, or until the "Next" button is pressed

"Output option" not activated (NoDisplay mode):

- no cycle parameter specified: one measuring cycle
- specified cycle time or number: measure until the cycle parameter is met
- specified cycle status parameter: measure until all values are OK or until the preset time (max time) in the "Cycle OK" field has elapsed.

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.AsamMesswerte_Lesen"></a>7.14.15.5. Action Element - Read ASAM Measured Values

The "Read ASAM measured values" action element can be seen in [Figure 455, “Read ASAM Measured Values Action Element”](7-14-15-category-ecukom.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.AsamMesswerte_Lesen "Figure 455. Read ASAM Measured Values Action Element").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.AsamMesswerte_Lesen"></a>

![Image: read ASAM measured values action element](images/fte_arbeitsflaeche_ecukom_asammesswertelesen.png)

**Figure 455. Read ASAM Measured Values Action Element**

You can display UDS measured values in the operating system using the "Read ASAM measured values" command. The available measured values are determined automatically by the operating system from the ODX control module descriptions for the base version of the control module.

###### <a id="d4e22859"></a>7.14.15.5.1. Logical Link

If you press the **Selection** button, then a selection list containing the available UDS control modules that are managed in Editing appears. See also [Section 7.14.15.16.1, “Control Module Variants”](7-14-15-category-ecukom.md#Funktionstesteditor.Allgemeine_Funktionalitaet.SG-Gruppe "7.14.15.16.1. Control Module Variants"). After selecting a base version, the associated Logical Link is written into the text field.

The “Variable” button can also be used to transfer the Logical Link as a string variable to the test language.

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.Asam_EcuKom"></a>7.14.15.6. Action Element - ASAM Ecukom

The "ASAM Ecukom" action element can be seen in [Figure 456, “ASAM Ecukom Action Element”](7-14-15-category-ecukom.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.Asam_EcuKom "Figure 456. ASAM Ecukom Action Element").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.Asam_EcuKom"></a>

![Image: ASAM Ecukom action element](images/fte_arbeitsflaeche_ecukom_asamecukom.png)

**Figure 456. ASAM Ecukom Action Element**

Using this command, you can conduct communication with an ASAM Ecukom control module, execute functions (such as checking the DTC memory), and read back results for further processing.

###### <a id="d4e22878"></a>7.14.15.6.1. Control Module Variants, Logical Link

See [Section 7.14.15.16.1, “Control Module Variants”](7-14-15-category-ecukom.md#Funktionstesteditor.Allgemeine_Funktionalitaet.SG-Gruppe "7.14.15.16.1. Control Module Variants").

###### <a id="d4e22882"></a>7.14.15.6.2. Diagnostic Service/Order

See [Section 7.14.15.16.2, “Diagnostic Service/Order Selection”](7-14-15-category-ecukom.md#Funktionstesteditor.Allgemeine_Funktionalitaet.Auswahl-Dienst "7.14.15.16.2. Diagnostic Service/Order Selection").

###### <a id="d4e22886"></a>7.14.15.6.3. Request Parameter

See [Section 7.14.15.16.4, “Request Parameter”](7-14-15-category-ecukom.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.Allgemein.Requests "7.14.15.16.4. Request Parameter").

The dialog can also be concluded with unfilled request parameters. When the dialog is confirmed, then only a warning message will be displayed.

###### <a id="d4e22891"></a>7.14.15.6.4. Positive/Negative Response Parameter

See [Section 7.14.15.16.6, “Positive/Negative Response Parameter”](7-14-15-category-ecukom.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.Allgemein.Antwortparameter "7.14.15.16.6. Positive/Negative Response Parameter").

###### <a id="d4e22895"></a>7.14.15.6.5. Output

With this selection, the tester displays results parameters when the "Read" button is pressed. The cycle is canceled if the user presses the "Read" button again or continues the program with "Next".

###### <a id="d4e22898"></a>7.14.15.6.5.1. Results Text

Only with the "Output" option: using the "Edit" button, you can specify an accompanying text for the measurement in the "Results text" field, which the user will see when there is output on the touchscreen.

###### <a id="ASAM_SGAntwortstatus"></a>7.14.15.6.6. Response status

With diagnostic services, a whole-number variable (integer) should be specified for the response status via the control module communication that was performed. If there is successful communication with a positive response, "1" is returned. With a negative response, "0" is returned. If the control module does not give any response, then the value "-1" is returned.

Depending on this, either positive or negative parameter values (results) can then be read out.

###### <a id="ASAM_SGGesamtstatus"></a>7.14.15.6.7. Overall status

The option "overall status" status field (technical type integer - all variables with a whole-number type such as Bool can be used) can be used in order to determined the overall status of the response parameter evaluation. The status indicates if all specified response parameters could be assigned to a variable. For further details on the overall status, see [Section 7.14.15.16.7, “Overall status”](7-14-15-category-ecukom.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.Allgemein.Gesamtstatus "7.14.15.16.7. Overall status").

The ASAM Ecukom overall status is calculated using the following algorithm:

- The "overall status" is 1 if the response status is not equal to -1 and all response parameter variables can be set depending on the positive or negative response.
- The "overall status" is 0 if no communication could be performed (response status is -1), or at least one response parameter variable could not be set.

Response parameters without a variable are not included in the evaluation. When there is a positive or negative response, only the respective positive or negative response parameters are evaluated.

###### <a id="ASAM_Parameterauswertung"></a>7.14.15.6.8. Forcing a Positive Parameter Evaluation

The “Force positive parameter evaluation” switch triggers GFF to set the values for the response parameter independently of the overall status in the specified variables. In this way, return values can be evaluated even if the communication returns a -1 as the overall status. The switch can only be used if setting parameters against a functional control module group.

###### <a id="d4e22920"></a>7.14.15.6.9. Progress Bars

If you mark this option, a message will appear in front with the "Bars" option selected that displays bar indicators labeled 0 to 100%. When running, the duration of the Ecukom command is determined automatically and this controls the progress shown by the progress bars.

###### <a id="SGAlsXMLSpeichern"></a>7.14.15.6.10. Save As XML File

This function can be used to check all results parameters at once and to save a later evaluation in an XML file. This function is especially useful for more complex results structures. The programming of positive and negative response parameters in the "ASAM Ecukom" command can then be omitted. It is also possible to use both solutions in parallel.

Specify a name for the file that conforms to the naming conventions in MS Windows. The ".xml" file does not need to be included. For the duration of the function test, the XML file will be saved under:

- ...\Client\_D\_\_V10.0\TEMP\ (ODIS Creator)
- C:\HOME\lng.ger\dia\OnlineXML\ (Tester)

You can read out results from the XML file again using the "ASAM result" command.

###### <a id="SFD-Zugriffsschutz"></a>7.14.15.6.11. Vehicle Diagnostic Protection (SFD) Access Protection

ODIS Service provides the ability to enable or block control modules using the "SFD Enabling” diagnostic function.

By activating the checkbox (SFD access protection) in ODIS Creator, there is the option to evaluate an error message if there is a malfunction with enabling SFD. It is possible to save the response status of the error localization in a variable (“Integer” type) using the "SFD status” variable field and in text form in a variable (“String” type) using the “SFD text” variable field.

Enabling SFD may lead to the following errors:

<a id="d4e22939"></a>

<table border="1" summary="GFF Fault Codes when Enabling SFD Fails"><colgroup><col align="center"/><col align="center"/><col align="center"/></colgroup><thead><tr bgcolor="#EEEEEE"><th align="center">Error code</th><th align="center">Constants</th><th align="center">Description</th></tr></thead><tbody valign="top"><tr><td align="center" valign="top">1</td><td align="center" valign="top">SFD_NO_ERROR</td><td align="center" valign="top">No error occurred.</td></tr><tr><td align="center" valign="top">-1</td><td align="center" valign="top">SFD_MCD_SERVICE_NOT_FOUND</td><td align="center" valign="top">MCD service "DiagnServi_ RoutiContrProteOfVehicDiagn" not populated with data.</td></tr><tr><td align="center" valign="top">-2</td><td align="center" valign="top">SFD_READ_STATE_MEASUREMENT_ERROR</td><td align="center" valign="top">An error occurred when determining the SFD status measured value.</td></tr><tr><td align="center" valign="top">-3</td><td align="center" valign="top">SFD_USER_LOGON_ERROR</td><td align="center" valign="top">No authentication or no logon service available.</td></tr><tr><td align="center" valign="top">-4</td><td align="center" valign="top">SFD_READ_UNLOCK_REQUEST_ERROR</td><td align="center" valign="top">An error occurred when determining the SFD request structure.</td></tr><tr><td align="center" valign="top">-5</td><td align="center" valign="top">SFD_NO_TOKEN_RECEIVED</td><td align="center" valign="top">No valid SFD token was received from the SFD backend or there is no/a faulty backend connection.</td></tr><tr><td align="center" valign="top">-6</td><td align="center" valign="top">SFD_WRITE_TOKEN_ERROR</td><td align="center" valign="top">Error when writing the SFD token in the control module.</td></tr></tbody></table>

**Table 106. GFF Fault Codes when Enabling SFD Fails**

Each of these six potential errors has its own fault code, which can be checked using the GFF response result. A specific error text can also be determined there. The fault code will be returned as “Integer” and the text as “String”.

**SFD status**

In the SFD status field, an integer variable can be specified in which the status of the fault localization can be stored after communication. See the table "GFF Fault Codes when Enabling SFD Fails”, “Fault Code” column

**SFD text**

In the SFD text field, a string variable can be specified in which the error message of the fault localization can be stored after communication. See the table "GFF Fault Codes when Enabling SFD Fails”, “Constants” column

###### <a id="SGFlashen"></a>7.14.15.6.12. Using a Flash Project

This button is no longer used.

###### <a id="Variantenvergleich"></a>7.14.15.6.13. Control Module Variant Comparison

Before a filled ASAM-Ecukom can be transferred via EV variant or to other vehicle projects, the “Variant comparison” function should check whether the filled out ASAM-Ecukom would work in different EV variants across vehicle projects. The “Variant comparison” button in the ASAM Ecukom dialog is available for this purpose, which can be used to perform the comparison.

To trigger the function, ASAM Ecukom must be filled out with a control module variant, a diagnostic service and a request parameter beforehand. Once all prerequisites are filled out, the editorial objects selection dialog opens. The control module parameterized in the ASAM-Ecukom dialog is pre-selected in the dialog.

The selection dialog permits multiple selections of EVs, both in the navigation as well as in the vehicle project view. The selection of EVs across vehicle projects is only possible in the navigation view. Only one vehicle project can be selected in the vehicle project view. Only the EVs in the dialog can be selected. Once the user has correctly selected the desired EVs for comparison, the comparison starts and the result is shown in the variant comparison dialog ([Figure 457, “Control Module Variants”](7-14-15-category-ecukom.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.Asam_Ecukom "Figure 457. Control Module Variants")).

<a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.Asam_Ecukom"></a>

![Image: control module variants](images/fte_variantenvergleich_ergebnis_dialog.png)

**Figure 457. Control Module Variants**

The figure above shows the result of the variant comparison. The matching control module variants are shown in green and non-matching control module variants are shown in red.

To turn green, all request parameters (name, type, value of enum entry) and response parameters (path, type) must be identical in the ASAM Ecukom dialog in the selected ECU variants.

###### <a id="Variantenvergleich_Exportieren"></a>7.14.15.6.14. Exporting the Variant Comparison Result

The result of the control module variant comparison can be exported in a csv file. To start the export, the user should click the “Start export” button. A dialog window prompts the user to select a target directory for saving the export result. Following a successful export, the user is given feedback.

The csv file contains the following information:

- The data classification
- The columns (Control Module Variant, Vehicle Project, Control Module Version, Operation Name, Response Parameter, Request Parameter, Value, Missing Request Parameter, Missing Value, Missing Response Parameter, Result)
- The pre-parameterized control module variant, vehicle project, version number of the control module variant, operation, request parameter and/or response parameter
- The list of the control module variants selected for comparison (including the vehicle project, control module version number)
- Missing Request and Response Parameter are listed in the corresponding column. The entry “NOK” is in the result column for this purpose. Identical parameters are listed with “-” and “OK” is entered in the result column.
- If the operation does not exist for an EV variant, the column “Operation Name” contains the text “The operation was not found”. Otherwise “-” is entered.

###### <a id="d4e23023"></a>7.14.15.6.15. Variable

The description for selecting variables is found in [Section 7.14.6, “Using Variables”](7-14-6-using-variables.md "7.14.6. Using Variables"). The definition of variables is found in [Section 7.14.11.1, “Action Element - Declare Variable”](7-14-11-category-definition.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Definition.Deklariere_Variablen "7.14.11.1. Action Element - Declare Variable").

###### <a id="d4e23028"></a>7.14.15.6.16. Keyword

The description for selecting keywords is found in [Section 7.14.6, “Using Variables”](7-14-6-using-variables.md "7.14.6. Using Variables"). The definition of keywords is found in [Section 7.14.11.4, “Action Element - Define Keyword”](7-14-11-category-definition.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Definition.Definiere_Kennwort "7.14.11.4. Action Element - Define Keyword").

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.Asam_Ergebnis"></a>7.14.15.7. Action Element - ASAM Result

The "ASAM Result" action element can be seen in [Figure 458, “ASAM Result Action Element”](7-14-15-category-ecukom.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.Asam_Ergebnis "Figure 458. ASAM Result Action Element").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.Asam_Ergebnis"></a>

![Image: ASAM result action element](images/fte_arbeitsflaeche_ecukom_asamergebnis.png)

**Figure 458. ASAM Result Action Element**

Using this command, you can read out results that were saved in an XML file with an ASAM Ecukom command.

<a id="table.hinweis.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.Asam_Ergebnis"></a>

<table border="1" summary="ASAM Result Note"><colgroup><col align="center"/><col align="left"/></colgroup><tbody valign="top"><tr><td align="center" valign="top"><span class="inlinemediaobject"><img alt="Note symbol" src="images/info.png"/></span></td><td align="left" valign="top"><span class="bold"><strong>Note:</strong></span> You can only evaluate XML files that were saved during a function test. The XML files are automatically deleted from the tester after the function test ends.</td></tr></tbody></table>

**Table 107. ASAM Result Note**

  

###### <a id="d4e23061"></a>7.14.15.7.1. XML File

Enter the correct file name with no extension here. The function test editor automatically specifies the name, which matches the last "ASAM Ecukom" command.

###### <a id="ASAMErg_SGGesamtstatus"></a>7.14.15.7.2. Overall status

The option "overall status" status field (technical type integer - all variables with a whole-number type such as Bool can be used) can be used in order to determined the overall status of the response parameter evaluation. The status indicates if all specified response parameters could be assigned to a variable. For further details on the overall status, see [Section 7.14.15.16.7, “Overall status”](7-14-15-category-ecukom.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.Allgemein.Gesamtstatus "7.14.15.16.7. Overall status").

The ASAM Ecukom overall status is calculated using the following algorithm:

- The "overall status" is 1 if the response status is not equal to -1 and all response parameter variables can be set depending on the positive or negative response.
- The "overall status" is 0 if no communication could be performed (response status is -1), or at least one response parameter variable could not be set.

Response parameters without a variable are not included in the evaluation. When there is a positive or negative response, only the respective positive or negative response parameters are evaluated.

###### <a id="d4e23076"></a>7.14.15.7.3. Control Module Variants, Logical Link

See [Section 7.14.15.16.1, “Control Module Variants”](7-14-15-category-ecukom.md#Funktionstesteditor.Allgemeine_Funktionalitaet.SG-Gruppe "7.14.15.16.1. Control Module Variants").

###### <a id="d4e23080"></a>7.14.15.7.4. Diagnostic Service/Order

See [Section 7.14.15.16.2, “Diagnostic Service/Order Selection”](7-14-15-category-ecukom.md#Funktionstesteditor.Allgemeine_Funktionalitaet.Auswahl-Dienst "7.14.15.16.2. Diagnostic Service/Order Selection").

###### <a id="d4e23084"></a>7.14.15.7.5. Request Parameter

See [Section 7.14.15.16.4, “Request Parameter”](7-14-15-category-ecukom.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.Allgemein.Requests "7.14.15.16.4. Request Parameter").

###### <a id="d4e23088"></a>7.14.15.7.6. Positive Response Parameter

See [Section 7.14.15.16.5, “Positive Response Parameter”](7-14-15-category-ecukom.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.SGPositiveAntwortparameter "7.14.15.16.5. Positive Response Parameter").

###### <a id="d4e23092"></a>7.14.15.7.7. Variable

The description for selecting variables is found in [Section 7.14.6, “Using Variables”](7-14-6-using-variables.md "7.14.6. Using Variables"). The definition of variables is found in [Section 7.14.11.1, “Action Element - Declare Variable”](7-14-11-category-definition.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Definition.Deklariere_Variablen "7.14.11.1. Action Element - Declare Variable").

###### <a id="d4e23097"></a>7.14.15.7.8. Keyword

The description for selecting keywords is found in [Section 7.14.6, “Using Variables”](7-14-6-using-variables.md "7.14.6. Using Variables"). The definition of keywords is found in [Section 7.14.11.4, “Action Element - Define Keyword”](7-14-11-category-definition.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Definition.Definiere_Kennwort "7.14.11.4. Action Element - Define Keyword").

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.Asam_Identifikation"></a>7.14.15.8. Action Element - ASAM Identification

The "ASAM identification" action element can be seen in [Figure 459, “ASAM Identification Action Element”](7-14-15-category-ecukom.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.Asam_Identifikation "Figure 459. ASAM Identification Action Element").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.Asam_Identifikation"></a>

![Image: ASAM identification action element](images/fte_arbeitsflaeche_ecukom_asamidentifikation.png)

**Figure 459. ASAM Identification Action Element**

This action element enables control module identification.

###### <a id="d4e23115"></a>7.14.15.8.1. Control Module Variants

See [Section 7.14.15.16.1, “Control Module Variants”](7-14-15-category-ecukom.md#Funktionstesteditor.Allgemeine_Funktionalitaet.SG-Gruppe "7.14.15.16.1. Control Module Variants").

###### <a id="Aktionselemente_Kategorie_EcuKom.Asam_Identifikation.Variable"></a>7.14.15.8.2. Variable

Enter a results variable in this field. As a result of the identification, the control module name is assigned to the variables. The description for selecting variables is found in [Section 7.14.6, “Using Variables”](7-14-6-using-variables.md "7.14.6. Using Variables"). The definition of variables is found in [Section 7.14.11.1, “Action Element - Declare Variable”](7-14-11-category-definition.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Definition.Deklariere_Variablen "7.14.11.1. Action Element - Declare Variable").

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.Asam_Varianten"></a>7.14.15.9. Action Element - ASAM Variant Identification

The "ASAM variant identification" action element can be seen in [Figure 460, “ASAM Variant Identification Action Element”](7-14-15-category-ecukom.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.Asam_Varianten "Figure 460. ASAM Variant Identification Action Element").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.Asam_Varianten"></a>

![Image: ASAM variant identification action element](images/fte_arbeitsflaeche_ecukom_asamvariantenidentifikation.png)

**Figure 460. ASAM Variant Identification Action Element**

This action element enables identification of ASAM control module variants.

###### <a id="d4e23137"></a>7.14.15.9.1. Control Module Variants

See [Section 7.14.15.16.1, “Control Module Variants”](7-14-15-category-ecukom.md#Funktionstesteditor.Allgemeine_Funktionalitaet.SG-Gruppe "7.14.15.16.1. Control Module Variants").

###### <a id="Aktionselemente_Kategorie_EcuKom.Asam_Varianten.Variable"></a>7.14.15.9.2. Variable

Enter a results variable in this field. As a result of the identification, the control module name is assigned to the variables.

The description for selecting variables is found in [Section 7.14.6, “Using Variables”](7-14-6-using-variables.md "7.14.6. Using Variables"). The definition of variables is found in [Section 7.14.11.1, “Action Element - Declare Variable”](7-14-11-category-definition.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Definition.Deklariere_Variablen "7.14.11.1. Action Element - Declare Variable").

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.AsamHex_Service"></a>7.14.15.10. Action Element - ASAM Hex Service

The "ASAM hex service" action element can be seen in [Figure 461, “ASAM Hex Service Action Element”](7-14-15-category-ecukom.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.Asam_Hexservice "Figure 461. ASAM Hex Service Action Element").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.Asam_Hexservice"></a>

![Image: ASAM hex service action element](images/fte_arbeitsflaeche_ecukom_asamhexservice.png)

**Figure 461. ASAM Hex Service Action Element**

This action element makes it possible to set parameters for a physical/functional protocol data unit (PDU).

###### <a id="d4e23160"></a>7.14.15.10.1. Logical Link

See [Section 7.14.15.16.1, “Control Module Variants”](7-14-15-category-ecukom.md#Funktionstesteditor.Allgemeine_Funktionalitaet.SG-Gruppe "7.14.15.16.1. Control Module Variants").

###### <a id="Aktionselemente_Kategorie_EcuKom.Asam_Hexservice.RequestPDU"></a>7.14.15.10.2. Request PDU

The request PDU is set as the input parameter in this field. A byte array is required here as the type.

The description for selecting variables is found in [Section 7.14.6, “Using Variables”](7-14-6-using-variables.md "7.14.6. Using Variables"). The definition of variables is found in [Section 7.14.11.1, “Action Element - Declare Variable”](7-14-11-category-definition.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Definition.Deklariere_Variablen "7.14.11.1. Action Element - Declare Variable").

###### <a id="Aktionselemente_Kategorie_EcuKom.Asam_Hexservice.5BaudAddress"></a>7.14.15.10.3. 5-baud address

The 5 baud address is set as the response parameter in this field. A string array is required here as the type.

###### <a id="Aktionselemente_Kategorie_EcuKom.Asam_Hexservice.ResponsePDU"></a>7.14.15.10.4. Response PDU

The response PDU is set as the input parameter in this field. A two-dimensional byte array is required here as the type. The length of the first index corresponds to the length of the array of the 5 baud address.

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.Identifikationsdaten_Auslesen"></a>7.14.15.11. Action Element - Update Log Book

The "Update log book" action element can be seen in [Figure 462, “Update Log Book Action Element”](7-14-15-category-ecukom.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.Identifikationsdaten_Auslesen "Figure 462. Update Log Book Action Element").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.Identifikationsdaten_Auslesen"></a>

![Image: update log book action element](images/fte_arbeitsflaeche_ecukom_identifikationsdaten_auslesen.png)

**Figure 462. Update Log Book Action Element**

This action element controls the updating of the log book with identification data from the master or control module-specific systems. A control module identification is performed. In earlier versions of ODIS Creator (OC 9.1.1 and older), the action element was also called “Read out identification data”. You can select if sub-systems should also be read out. The GFF author can update the “LiveVehicle” or “LiveVehicle” and “FrozenVehicle” elements for specific control modules. Parameters can be set for a control module-specific update to identification data in the Diagnostic address field. The diagnostic address input for the control module-specific update can be done as:

- String Literal
- String Variable
- String Array (one-dimensional)

The strings for the control-module specific update must display the short name.

The following is an example for possible short names:

- Address 0001: EnginContrModul1
- Address 0002: TransContrModul
- Address 0047: SoundSyste
- Address 005F: InforContrUnit1

To transfer multiple control modules, a one-dimensional string array must be used.

- Example preconfiguration of a one-dimensional string array in a declare command: {'EnginContrModul1', 'TransContrModul', 'SoundSyste','InforContrUnit1'}

If a list of short names should be used, the array must be entered in the diagnostic address field without brackets and indexes.

Parameters can also be set for reading out DTC memory entries. You can set parameters for whether or not the DTC memory entries should be read out and in internal ODIS data (“LiveVehicle” or “LiveVehicle & FrozenVehicle”) the DTC memory entries should be overwritten.

Using the access control for functions, the GFF author can control if the function used delivers the requested value from “LiveVehicle” or “FrozenVehicle”.

###### <a id="d4e23213"></a>7.14.15.11.1. Status

Enter a results variable for the status in this field. The status describes the result of the update. Possible return values:

- No control module was identified: 0
- One or more control modules were identified: 1

The variable must have an integer type.

The description for selecting variables is found in [Section 7.14.6, “Using Variables”](7-14-6-using-variables.md "7.14.6. Using Variables"). The definition of variables is found in [Section 7.14.11.1, “Action Element - Declare Variable”](7-14-11-category-definition.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Definition.Deklariere_Variablen "7.14.11.1. Action Element - Declare Variable").

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.Pruefplan_Neuberechnen"></a>7.14.15.12. Action Element - Recalculate Test Plan

Using the “Recalculate test plan” action element, the GFF author can have the operating system test plan recalculated from a function test based on the current vehicle status (LiveVehicle). The test plan is calculated after the test program that is called up ends. DTC memory entries that are present when entering GFF are still taken into account when the test plan is calculated even if there are no longer present after updates using the “Update log book” function. Test programs that have already run or test programs that were added to the test plan manually are handled similarly to a test plan calculation that was triggered using the “Read all DTC memories” function in the control module list. After recalculating the test plan from a function test, the “new” test plan will be run in the diagnostic protocol. It will be logged in the “Test plans” area.

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.Kommunikationsweg_Setzen"></a>7.14.15.13. Set Communication Type Action Element

The "Set communication type" action element can be seen in [Figure 463, “Set Communication Type Action Element”](7-14-15-category-ecukom.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.Kommunikationsweg_Setzen "Figure 463. Set Communication Type Action Element").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.Kommunikationsweg_Setzen"></a>

![Image: set communication type action element](images/fte_arbeitsflaeche_ecukom_kommunikationsweg_setzen.png)

**Figure 463. Set Communication Type Action Element**

The communication type can be switched within a diagnostic session using the “Set communication type” action element.

###### <a id="d4e23242"></a>7.14.15.13.1. Communication Types

The user must select a communication type to be used in GFF. The type of communication is detected by the operating system during diagnostic entry and is updated during the diagnostic session if necessary. The communication type can be changed within a diagnosis if no diagnostic communication is taking place. ODIS Creator offers the following communication types for selection:

- CAN

  The CAN communication type is selected by default.
- CANFD
- DoIP
- Reset to the original communication type

###### <a id="d4e23255"></a>7.14.15.13.2. Response status

The response status contains information about the result of the communication type switch and must be entered. This response is stored in a variable (“Integer” type). A failed switch can lead to these fault types:

<a id="d4e23259"></a>

<table border="1" summary="Fault Codes when Switching the Communication Type"><colgroup><col/><col/><col/></colgroup><thead><tr bgcolor="#EEEEEE"><th>Error ID</th><th>Constants</th><th>Meaning</th></tr></thead><tbody valign="top"><tr><td valign="top">0</td><td valign="top">SWITCH_COMMUNICATION_TYPE_NO_ERROR</td><td valign="top">Switch successful.</td></tr><tr><td valign="top">1</td><td valign="top">SWITCH_COMMUNICATION_TYPE_ ALREADY_ACTIVE</td><td valign="top">The communication type is already active.</td></tr><tr><td valign="top">2</td><td valign="top">SWITCH_COMMUNICATION_TYPE_ NOT_SUPPORTED_BY_VCI</td><td valign="top">The VCI does not support the desired communication type.</td></tr><tr><td valign="top">3</td><td valign="top">SWITCH_COMMUNICATION_TYPE_ NOT_SUPPORTED_BY_PROJECT</td><td valign="top">The vehicle project does not support the desired communication type.</td></tr><tr><td valign="top">4</td><td valign="top">SWITCH_COMMUNICATION_TYPE_ NOT_ALLOWED_BECAUSE_COMMUNICATION</td><td valign="top">The switch is not possible because communication is still active.</td></tr><tr><td valign="top">5</td><td valign="top">SWITCH_COMMUNICATION_TYPE_ UNKNOWN_ERROR</td><td valign="top">Unknown error.</td></tr><tr><td valign="top">6</td><td valign="top">SWITCH_COMMUNICATION_TYPE_ NOT_SUPPORTED</td><td valign="top">The function is not supported in the current context.</td></tr><tr><td valign="top">7</td><td valign="top">SWITCH_COMMUNICATION_TYPE_ NOT_ALLOWED_BECAUSE_VCI_ NOT_CONNECTED</td><td valign="top">VCI connection not available.</td></tr></tbody></table>

**Table 108. Fault Codes when Switching the Communication Type**

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.Pruefplan_Qualifizieren"></a>7.14.15.14. Action Element - Qualify Test Plan

With the “Qualify test plan” action element, the GFF author has the option to trigger the qualification of a test plan from a GFF test program in the operating system.

Test plan entries can be qualified again after each subsequent execution of a test program or error correction. The DTC memory entries that were read out during diagnostic entry are read out again and the before and after state are compared. For a new qualification (before and after comparison), ODIS Service must temporarily store the DTC memory entries that were read out during diagnostic entry. Test plan entries that are based on DTC memory entries whose status has changed from “static” to “sporadic”, from “static” to “not present”, or from “sporadic” to “not present” are interpreted as related errors. If multiple logical and/or linked DTC memory entries have led to a diagnostic object, there must be an overall improvement in the status in order to qualify a test plan entry as a related error.

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.Alle_Logicallinks_schlie%C3%9Fen"></a>7.14.15.15. Action Element - Close All Logical Links

Open logical links can be closed during a control module update in the workshop (GOBW) using the “Close all logical links” action element.

The action element prevents communication problems for individual control modules that could occur during simultaneous access by internal and external diagnostic testers.

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.Anhang"></a>7.14.15.16. General Ecukom Functions

###### <a id="Funktionstesteditor.Allgemeine_Funktionalitaet.SG-Gruppe"></a>7.14.15.16.1. Control Module Variants

This function is used in the Ecukom, ASAM Ecukom, ASAM result, ASAM identification, ASAM variant identification, and ASAM hex service action elements: if you press the selection button, a dialog where you can select a corresponding editorial object appears ([Figure 464, “Control Module Variants”](7-14-15-category-ecukom.md#figure.Funktionstesteditor.Allgemeine_Funktionalitaet.SG-Gruppe "Figure 464. Control Module Variants")).

<a id="figure.Funktionstesteditor.Allgemeine_Funktionalitaet.SG-Gruppe"></a>

![Image: control module variants](images/fte_sg.png)

**Figure 464. Control Module Variants**

You can switch between various selection views in the upper section of the selection dialog. Using the "Via navigation" and "Via vehicle project" option fields, you can specify if the selection should be made using the general navigation tree or by pre-selecting a vehicle project. The illustration shows selection via the general navigation tree.

The baseline selection is located below. The current baseline can be selected here as well as the last baseline in order to use the affected control modules from that baseline if they are no longer contained in the current baseline.

You can specify the content of the views mentioned above using the "Not approved" control field. If the control field is active, only non-approved control modules or vehicle projects are displayed. If the control field is not selected, you can select from approved control modules or vehicle projects. This control field selection does not depend on the selected view.

**Parameter template control**

The options "New parameter template" and "Retain variables" can be selected in the "Parameter template control".

You can use the "New parameter template" control field to switch the operation or control module below it to parameterization without having to enter all of the parameters again.

When "Retain variables" is selected, a variable that is in the "Logical Link" field will not be overwritten in the Ecukom dialog.

###### <a id="Funktionstesteditor.Allgemeine_Funktionalitaet.Auswahl-Dienst"></a>7.14.15.16.2. Diagnostic Service/Order Selection

This function contains a dialog that contains all services available in the previously-selected control module variant. It can then be selected again or canceled.

<a id="figure.Funktionstesteditor.Allgemeine_Funktionalitaet.Auswahl-Dienst"></a>

![Image: service selection](images/fte_Dienst_Auswahl.png)

**Figure 465. Diagnostic Service Selection**

###### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.EcuKom_DienstInformation"></a>7.14.15.16.3. Service Properties Dialog Screen

The information button below the selection area for the service opens a dialog with detailed information. The following details are shown in the dialog screen:

- Name of the service and its description (if available)
- Previous name of the service (if available)
- List of request and response parameters, divided into positive and negative response parameters (UDS), including

  1. Parameter type
  2. Previous name of the parameter (if available)
  3. Range of values (not with Object, Response state, Void and Boolean parameter type)
  4. With Enum parameters, all literals including their meaning (if available) are listed
  5. Description
  6. With Struct parameters, the first level of the content is listed

The dialog screen is not modal. It can be moved aside during parameterization of the Ecukom dialog screen. Content from the dialog can be copied into the clipboard for further use, either using the context menu or a keyboard shortcut.

<a id="d4e23371"></a>

![Image: service properties dialog screen](images/fte_EcukomDienstEigenschaften.png)

**Figure 466. Service Properties Dialog Screen**

###### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.Allgemein.Requests"></a>7.14.15.16.4. Request Parameter

To execute a diagnostic service/order, the request parameters must be transmitted to the control module. They are preselected when the diagnostic service/order is selected. The request parameters consist of a name, a data type, a dimension, and a default value. They are prepared from the ODX data.

The "default value'" can be replaced with a value of your choosing. To do this, click in the "Value" field. A button labeled "..." appears. If you press this button, a menu with additional selection options appears. The content of this menu depends on the request parameter.

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ecukom_requests"></a>

![Image: request parameter](images/fte_arbeitsflaeche_ecukom_asam_request_auswahl.png)

**Figure 467. Request Parameter**

Depending on the type of the request parameter, you can enter the value as a number, as a system string, or using a variable. With some request parameters, there is an entry selection. If you click the "Entry" button in the menu, then you select the entry from a list. An "entry selection" dialog appears after the selection. You can enter a value as a system string (ID) in this dialog. If you click on the arrow (if present) in the "ID" or "RDID" field, all available system strings are provided for selection.

You can assign the request parameters to system variables. To do this, select the "System variables" entry in the selection menu. Allocation of system variables is needed especially for the IPA\_VWDevicNumb", "IPA\_ImporNumbe" and "IPA\_WorksNumbe" request parameters. You can use the system variables "FINGERPRINTDEVICE", "FINGERPRINTIMPORTER" and "FINGERPRINTDEALER" for this.

An overview of the available functions can be found in [Section 7.14.12.3, “Functions”](7-14-12-category-mapping.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Zuordnung_Funktionen "7.14.12.3. Functions").

###### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.SGPositiveAntwortparameter"></a>7.14.15.16.5. Positive Response Parameter

[Response parameters](7-14-15-category-ecukom.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.Allgemein.Antwortparameter "7.14.15.16.6. Positive/Negative Response Parameter") from the control module communication can be checked using this table. Response parameters can be added using the "Plus" button. A list of response parameters can be displayed in the "Path" input field using the "..." button and a value can be selected. The number and the names depend on the service that is selected. You can transfer the results into variables to be defined in order to process the values in the test program further.

###### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.Allgemein.Antwortparameter"></a>7.14.15.16.6. Positive/Negative Response Parameter

Results parameters from the control module communication can be checked using this function. You can enter positive parameter values in the event that control module communication is successful, and negative values if it is faulty. The response status will then branch off accordingly as the function test runs.

You can switch between positive and negative response values when setting parameters by clicking the corresponding tab.

You can enter new results parameters using the "Plus" button. The input is done the same way as entering the positive response parameters from Ecukom. See also [Section 7.14.15.1, “Action Element - Ecukom”](7-14-15-category-ecukom.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.EcuKom "7.14.15.1. Action Element - Ecukom").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ecukom_antwort"></a>

![Image: positive response parameter](images/fte_arbeitsflaeche_ecukom_asam_iupr_auswahl.png)

**Figure 468. Positive Response Parameter**

If a functional group is selected as a control module variant, the "Control module" column will appear in the "Positive response parameter" and "Negative response parameter" tabs. A control module can then be selected for each results parameter. There is a selection field for this for each parameter (see [Figure 468, “Positive Response Parameter”](7-14-15-category-ecukom.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ecukom_antwort "Figure 468. Positive Response Parameter")). As an alternative to specifying directly, a variable or a keyword can also be used for control module transmission.

The short names of all control modules (with UDS Logical Link) for the selected vehicle project is listed under the selection. If a literal is entered in the "Control module" column, then the input will be checked against the selection list. If the selection list is empty, any short name can be entered without checking.

###### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.Allgemein.Gesamtstatus"></a>7.14.15.16.7. Overall status

The response status with ASAM Ecukom only returns the classification if a positive or negative response came from the control module, or if communication could be established. The available response status does not return any information on whether all response parameters from the response could be read. For this reason, there is an **Overall status** field that can be evaluated as an option. This status field does return information on whether all response parameters from the response could be read.

For example, when checking the engine temperature, it is possible that engine temperature 1 is read for one control module variant, and engine temperature 2 is read for another control module variant. [Figure 469, “Overall Status Example”](7-14-15-category-ecukom.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ecukom_gesamtstatus "Figure 469. Overall Status Example") shows the example of the engine temperature.

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ecukom_gesamtstatus"></a>

![Image: overall status example](images/fte_arbeitsflaeche_ecukom_gesamtstatus.png)

**Figure 469. Overall Status Example**

###### <a id="d4e23429"></a>7.14.15.16.7.1. Calculation of the Overall Status

The ASAM Ecukom overall status is calculated according to the following algorithm:

- The "overall status" is 1 if the response status is not equal to -1 and all response parameter variables can be set depending on the positive or negative response.
- The "overall status" is 0 if no communication could be performed (response status is -1), or at least one response parameter variable could not be set.

Response parameters without a variable are not included in the evaluation. When there is a positive or negative response, only the respective positive or negative response parameters are evaluated.

The overall status field cannot be selected in the default values dialog within a debug session. In the case of default values, one value is always returned for each response parameter (empty string if nothing was entered). In this way, all response parameters can be read from the response in the event of default values.

###### <a id="d4e23439"></a>7.14.15.16.7.2. Overall Status Processing Example

The engine temperature example can be triggered with the **Overall status** status field. With the ASAM Ecukom command, initially only the first temperature in a variable is written. If the overall status is negative, then the second engine temperature can be assigned using an additional ASAM result command. [Figure 470, “Overall Status Processing Example”](7-14-15-category-ecukom.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ecukom_gesamtstatus_ablauf "Figure 470. Overall Status Processing Example") shows how the process of evaluating the temperature using a case distinction can be carried out.

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ecukom_gesamtstatus_ablauf"></a>

![Image: overall status processing example](images/fte_arbeitsflaeche_ecukom_gesamtstatus_ablauf.png)

**Figure 470. Overall Status Processing Example**

###### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ecukom_bit0"></a>7.14.15.16.8. 0 Bit Request Parameter

In the ASAM comments (ASAM Ecukom, ASAM result and oscilloscope combination measurement ASAM), operations can be selected with special 0 bit request parameters. These request parameters have a data length of 0 bit (the "bit length" attribute has the value "0") and are required by ODX schema.

The 0 bit request parameters should not be assigned a value. So that the author recognizes a request parameter that is 0 bit during parameterization, then these parameterization are indicated for the authors: in the default value column, the text "do not fill out (0 bit parameter)" is displayed.

[Figure 471, “0 Bit Parameter”](7-14-15-category-ecukom.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ecukom_bit0 "Figure 471. 0 Bit Parameter") shows an example with a 0 bit request parameter.

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ecukom_bit0"></a>

![Image: example with 0 bit request parameter](images/fte_arbeitsflaeche_ecukom_0bit_parameter.png)

**Figure 471. 0 Bit Parameter**

The technical processing of the detection of 0 bit request parameters occurs on the basis of the MCD-3D interface. A request parameter is a 0 bit request parameter, if the following technical criteria apply at the same time:

- Accessing the MCD-3D-API methods getByteLength() delivers the value "0".
- Accessing the MCD-3D-API methods getMinLength() delivers the value "0".
- Accessing the MCD-3D-API methods getMaxLength() delivers the value "0".
- Accessing the MCD-3D-API methods isVariableLength() delivers the value "false".

###### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ecukom_endofpdu"></a>7.14.15.16.9. List Parameters (END-OF-PDU-FIELD)

###### <a id="d4e23479"></a>7.14.15.16.9.1. Request Parameter

There are specific operations with list parameters (END-OF-PDU-FIELD) for the ASAM dialogs (ASAM Ecukom, ASAM result and oscilloscope ASAM combination measurement). The END-OF-PDU-FIELD specifies the repetition of a certain object structure. For this reason, the number of repetitions can be specified as a fixed value in the input screen. If the minimum and/or maximum number of repetitions in ODX are specified, then a verification against the values margin occurs after a fixed value is entered.

A special list parameter appears in the request parameter table. This list parameter has the type "object and no value can be entered. In the "Dimension" column, the range (minimum, maximum) of the possible amount of list elements is displayed.

The [Figure 472, “List Parameters (END-OF-PDU)”](7-14-15-category-ecukom.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ecukom_endofpdu "Figure 472. List Parameters (END-OF-PDU)") shows an example with a list parameter (END-OF-PDU-FIELD).

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ecukom_endofpdu"></a>

![Image: example with list parameter in the request parameters](images/fte_arbeitsflaeche_ecukom_asam_endofpdu.png)

**Figure 472. List Parameters (END-OF-PDU)**

In the "Amount" column, the amount of the list elements to be transferred can be set. The amount is checked after entering, if the amount falls between the minimum and maximum range. If this is the case, then the amount is transferred. The underlying structure elements in the list element are repeated multiple times in the table, until the amount is reached:

- Every list element contains an index for this, which is added in the path behind the list element. The other path elements will then continue according to the underlying structures.
- The index starts with the value '0' and ends with the value 'Amount - 1'.

The list parameters are also not transferred to the operating system. The technical processing of the END-OF-PDU-FIELD occurs based on the following MCD-3D interface:

- The minimum amount of items for a END-OF-PDU-FIELD is requested through the MCD-3D methods MCDDbParameter::getMinLength. The determined value is displayed in the "Dimension" column as the minimum.
- The maximum amount of items for a END-OF-PDU-FIELD is requested through the MCD-3D methods MCDDbParameter::getMaxLength. The determined value is displayed in the "Dimension" column as the maximum.

The following special exception applies to the END-OF-PDU-FIELD: an END-OF-PDU-FIELD that is hierarchically structured under ENV-DATA-DESC, will not be considered.

###### <a id="d4e23508"></a>7.14.15.16.9.2. Positive and Negative Response Parameters

For response parameters, the END-OF-PDU-FIELD is displayed as a list parameter in the response structure. A node with an index entry appears under the list parameter, with which an index can be entered as a variable or a fixed value. Under the index parameter, the other hierarchy levels of the parameter structures are given.

The [Figure 473, “List Parameters (END-OF-PDU-FIELD)”](7-14-15-category-ecukom.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ecukom_endofpdu_response "Figure 473. List Parameters (END-OF-PDU-FIELD)") shows an example with a list parameter (END-OF-PDU-FIELD).

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_ecukom_endofpdu_response"></a>

![Image: example with list parameters in the response structure](images/fte_arbeitsflaeche_ecukom_asam_endofpdu_response.png)

**Figure 473. List Parameters (END-OF-PDU-FIELD)**

The list parameter ("Param\_ECUCoded" here) can be selected from the "Object" type, in order to, for example, determine the amount of response structure entries included for run time (filter: amount).

###### <a id="d4e23522"></a>7.14.15.16.10. Tables

The following table lists the control module versions that can be selected under [Section 7.14.15.16.1, “Control Module Variants”](7-14-15-category-ecukom.md#Funktionstesteditor.Allgemeine_Funktionalitaet.SG-Gruppe "7.14.15.16.1. Control Module Variants").

<a id="d4e23527"></a>

<table border="1" summary="SGBD Variants"><colgroup><col align="left"/><col align="left"/><col align="left"/><col align="left"/></colgroup><thead><tr bgcolor="#EEEEEE"><th align="left">Group Address</th><th align="left">Name in ODIS</th><th align="left">SGBD Groups</th><th align="left">Vehicle System</th></tr></thead><tbody><tr><td align="left">0001</td><td align="left">EnginContrModul1</td><td align="left">Mot_01</td><td align="left">Engine Electronics</td></tr><tr><td align="left">0002</td><td align="left">TransContrModul</td><td align="left">Get_02</td><td align="left">Transmission Electronics</td></tr><tr><td align="left">0003</td><td align="left">Brake1</td><td align="left">Bre_03</td><td align="left">Brake Electronics</td></tr><tr><td align="left">0004</td><td align="left">SteerAngleSende</td><td align="left">LKP_04</td><td align="left">Steering Angle Sender</td></tr><tr><td align="left">0005</td><td align="left">Kessy</td><td align="left">Zus_05</td><td align="left">Access/Start Authorization</td></tr><tr><td align="left">0006</td><td align="left">SeatAdjusPasseSide</td><td align="left">Sbv_06</td><td align="left">Front Passenger Seat Adjustment</td></tr><tr><td align="left">0007</td><td align="left">DisplContrUnit</td><td align="left">Abe_07</td><td align="left">Display/Control Head</td></tr><tr><td align="left">0008</td><td align="left">AirCondi</td><td align="left">Klh_08</td><td align="left">Climate Control Electronics</td></tr><tr><td align="left">0009</td><td align="left">CentrElect</td><td align="left">Eze_09</td><td align="left">Central Electronics</td></tr><tr><td align="left">000A</td><td align="left">AlterFuelEngin</td><td align="left">ABA_0A</td><td align="left">Alternative Fuel Engine</td></tr><tr><td align="left">000B</td><td align="left">AuxilAirHeate</td><td align="left">LZH_0B</td><td align="left">Auxiliary Air Heater</td></tr><tr><td align="left">000D</td><td align="left">SlidiDoorLeft</td><td align="left">Stl_0D</td><td align="left">Left Sliding Door</td></tr><tr><td align="left">000E</td><td align="left">MediaPlayePosit1</td><td align="left">M1p_0E</td><td align="left">Media Player in Position 1</td></tr><tr><td align="left">000F</td><td align="left">RadioTunerDigit</td><td align="left">Rtd_0F</td><td align="left">Digital Radio Tuner</td></tr><tr><td align="left">0010</td><td align="left">ParkiAssis2</td><td align="left">PLA_10</td><td align="left">Parking Assistance 2</td></tr><tr><td align="left">0011</td><td align="left">EnginContrModul2</td><td align="left">M2b_11</td><td align="left">Engine Electronics II</td></tr><tr><td align="left">0012</td><td align="left">ClutcContrUnit</td><td align="left">Kup_12</td><td align="left">Clutch Electronics</td></tr><tr><td align="left">0013</td><td align="left">AdaptCruisContr</td><td align="left">Dis_13</td><td align="left">Adaptive Cruise Control</td></tr><tr><td align="left">0014</td><td align="left">WheelDampeElect</td><td align="left">Rad_14</td><td align="left">Wheel Damping Electronics</td></tr><tr><td align="left">0015</td><td align="left">Airba</td><td align="left">Air_15</td><td align="left">Airbag</td></tr><tr><td align="left">0016</td><td align="left">SteerColumElect</td><td align="left">Lre_16</td><td align="left">Steering Column Electronics</td></tr><tr><td align="left">0017</td><td align="left">DashBoard</td><td align="left">Sch_17</td><td align="left">Instrument Cluster</td></tr><tr><td align="left">0018</td><td align="left">AuxilParkiHeate</td><td align="left">Zst_18</td><td align="left">Auxiliary/Parking Heater</td></tr><tr><td align="left">0019</td><td align="left">Gatew</td><td align="left">Did_19</td><td align="left">Data bus diagnostic interface</td></tr><tr><td align="left">001A</td><td align="left">FuelCellEngin</td><td align="left">BZA_1A</td><td align="left">Fuel Cell Engine</td></tr><tr><td align="left">001B</td><td align="left">ActivSteer</td><td align="left">AKL_1B</td><td align="left">Active Steering</td></tr><tr><td align="left">001C</td><td align="left">VehicPositDetec</td><td align="left">Lgk_1C</td><td align="left">Vehicle Position Detection</td></tr><tr><td align="left">001D</td><td align="left">DriveIdent</td><td align="left">Idf_1D</td><td align="left">Driver Identification</td></tr><tr><td align="left">001E</td><td align="left">MediaPlayePosit2</td><td align="left">M2p_1E</td><td align="left">Media Player in Position 2</td></tr><tr><td align="left">001F</td><td align="left">RadioTunerSatel</td><td align="left">Rts_1F</td><td align="left">Satellite Radio Tuner</td></tr><tr><td align="left">0020</td><td align="left">HighBeamAssis</td><td align="left">FLA_20</td><td align="left">High Beam Assistance</td></tr><tr><td align="left">0021</td><td align="left">EnginContrModul3</td><td align="left">M3b_21</td><td align="left">Engine Electronics III</td></tr><tr><td align="left">0022</td><td align="left">AllWheelContr</td><td align="left">Alr_22</td><td align="left">AWD Electronics</td></tr><tr><td align="left">0023</td><td align="left">BrakeBoost</td><td align="left">Bkv_23</td><td align="left">Brake Booster</td></tr><tr><td align="left">0024</td><td align="left">AntiSlipRegul</td><td align="left">Ant_24</td><td align="left">Anti-Slip Regulation</td></tr><tr><td align="left">0025</td><td align="left">Immob</td><td align="left">Weg_25</td><td align="left">Immobilizer</td></tr><tr><td align="left">0026</td><td align="left">ElectRoofContr</td><td align="left">ELD_26</td><td align="left">Electronic Roof Control</td></tr><tr><td align="left">0027</td><td align="left">DisplContrUnitRear</td><td align="left">Abh_27</td><td align="left">Rear Display/Control Head</td></tr><tr><td align="left">0028</td><td align="left">ClimaContrUnitRear</td><td align="left">Kbh_28</td><td align="left">Rear A/C controls</td></tr><tr><td align="left">0029</td><td align="left">LightContrLeft</td><td align="left">Lsl_29</td><td align="left">Left Light Control</td></tr><tr><td align="left">002B</td><td align="left">SteerColumLocki</td><td align="left">LSV_2B</td><td align="left">Steering Column Locking</td></tr><tr><td align="left">002C</td><td align="left">SeatAllocDetec</td><td align="left">SBE_2C</td><td align="left">Seat Allocation Detection</td></tr><tr><td align="left">002D</td><td align="left">VoiceAmpli</td><td align="left">Spv_2D</td><td align="left">Voice Amplification</td></tr><tr><td align="left">002E</td><td align="left">MediaPlayePosit3</td><td align="left">M3p_2E</td><td align="left">Media Player in Position 3</td></tr><tr><td align="left">002F</td><td align="left">TVTunerDigit</td><td align="left">Tdf_2F</td><td align="left">Digital TV Tuner</td></tr><tr><td align="left">0030</td><td align="left">SpeciFunct2</td><td align="left">SFZ_30</td><td align="left">Special Function 2</td></tr><tr><td align="left">0031</td><td align="left">EnginElectGroup</td><td align="left">Mov_31</td><td align="left">Engine Electronics Group</td></tr><tr><td align="left">0032</td><td align="left">LockElect</td><td align="left">Spr_32</td><td align="left">Locking Electronics</td></tr><tr><td align="left">0033</td><td align="left">AllOBDSyste</td><td align="left">OBDII</td><td align="left">All OBD Systems</td></tr><tr><td align="left">0034</td><td align="left">RideContrSyste</td><td align="left">Niv_34</td><td align="left">Level Control System</td></tr><tr><td align="left">0035</td><td align="left">CentrLockiContrModul</td><td align="left">Zen_35</td><td align="left">Central Locking</td></tr><tr><td align="left">0036</td><td align="left">SeatAdjusDriveSide</td><td align="left">Svf_36</td><td align="left">Driver Seat Adjustment</td></tr><tr><td align="left">0037</td><td align="left">Navig</td><td align="left">Nav_37</td><td align="left">Navigation</td></tr><tr><td align="left">0038</td><td align="left">RoofElectContr</td><td align="left">Del_38</td><td align="left">Roof Electronics</td></tr><tr><td align="left">0039</td><td align="left">LightContrRight</td><td align="left">Lsr_39</td><td align="left">Right Light Control</td></tr><tr><td align="left">003B</td><td align="left">SensoElect</td><td align="left">SNE_3B</td><td align="left">Sensor Electronics</td></tr><tr><td align="left">003C</td><td align="left">LaneChangAssis</td><td align="left">Swa_3C</td><td align="left">Lane Change Assistance</td></tr><tr><td align="left">003D</td><td align="left">SpeciFunct</td><td align="left">Sof_3D</td><td align="left">Special function</td></tr><tr><td align="left">003E</td><td align="left">MediaPlayePosit4</td><td align="left">M4p_3E</td><td align="left">Media Player in Position 4</td></tr><tr><td align="left">0040</td><td align="left">AirCondiCompr</td><td align="left">KKP_40</td><td align="left">Air Conditioning Compressor</td></tr><tr><td align="left">0041</td><td align="left">DiesePumpContrUnit</td><td align="left">Die_41</td><td align="left">Diesel Pump Electronics</td></tr><tr><td align="left">0042</td><td align="left">DoorElectDriveSide</td><td align="left">Tfa_42</td><td align="left">Driver Door Electronics</td></tr><tr><td align="left">0043</td><td align="left">BrakeAssis</td><td align="left">Bku_43</td><td align="left">Brake Assist</td></tr><tr><td align="left">0044</td><td align="left">SteerAssis</td><td align="left">Lkh_44</td><td align="left">Power Steering</td></tr><tr><td align="left">0045</td><td align="left">InterMonit</td><td align="left">Ira_45</td><td align="left">Interior Monitoring</td></tr><tr><td align="left">0046</td><td align="left">DoorElectPasseSide</td><td align="left">zks_46</td><td align="left">Convenience System Central Module</td></tr><tr><td align="left">0047</td><td align="left">SoundSyste</td><td align="left">Sou_47</td><td align="left">Sound System</td></tr><tr><td align="left">0048</td><td align="left">SeatAdjusRearDriveSide</td><td align="left">Shf_48</td><td align="left">Driver Side Rear Seat Adjustment</td></tr><tr><td align="left">0049</td><td align="left">AutomLightSwitc</td><td align="left">Als_49</td><td align="left">Automatic Light Switch</td></tr><tr><td align="left">004B</td><td align="left">MultiModul</td><td align="left">MFM_4B</td><td align="left">Multifunction Module</td></tr><tr><td align="left">004C</td><td align="left">TirePressMonit2</td><td align="left">RDZ_4C</td><td align="left">Tire Pressure Monitoring 2</td></tr><tr><td align="left">004D</td><td align="left">DataTrans</td><td align="left">DTU_4D</td><td align="left">Data Transmission</td></tr><tr><td align="left">004E</td><td align="left">ContrHeadRearRight</td><td align="left">Ahr_4E</td><td align="left">Right Rear Display/Control Head</td></tr><tr><td align="left">004F</td><td align="left">CentrElect2</td><td align="left">Ezz_4F</td><td align="left">Central Electronics II</td></tr><tr><td align="left">0050</td><td align="left">SeatAdjus3rdRow</td><td align="left">SDR_50</td><td align="left">Seat Adjustment 3rd Row</td></tr><tr><td align="left">0051</td><td align="left">DriveMotorContrModul</td><td align="left">Ela_51</td><td align="left">Electric Drive</td></tr><tr><td align="left">0052</td><td align="left">DoorElectPasseSide</td><td align="left">TBF_52</td><td align="left">Door Electronics Passenger Side</td></tr><tr><td align="left">0053</td><td align="left">ParkiBrake</td><td align="left">Bfs_53</td><td align="left">Parking Brake</td></tr><tr><td align="left">0054</td><td align="left">RearSpoil</td><td align="left">Hsk_54</td><td align="left">Rear Spoiler</td></tr><tr><td align="left">0055</td><td align="left">HeadlRegul</td><td align="left">Lwr_55</td><td align="left">Headlamp Range Control</td></tr><tr><td align="left">0056</td><td align="left">Radio</td><td align="left">Rio_56</td><td align="left">Radio</td></tr><tr><td align="left">0057</td><td align="left">TVTuner</td><td align="left">Tvt_57</td><td align="left">TV Tuner</td></tr><tr><td align="left">0058</td><td align="left">FuelSuppl</td><td align="left">Ksz_58</td><td align="left">Auxiliary Fuel Tank</td></tr><tr><td align="left">0059</td><td align="left">TowinProte</td><td align="left">Ass_59</td><td align="left">Towing Protection</td></tr><tr><td align="left">005B</td><td align="left">SeatAdjusRearPasseSide</td><td align="left">SHB_5B</td><td align="left">Seat Adjustment Rear Passenger Side</td></tr><tr><td align="left">005C</td><td align="left">LaneDeparWarniSyste</td><td align="left">Sha_5c</td><td align="left">Lane Departure Warning System</td></tr><tr><td align="left">005D</td><td align="left">Opera</td><td align="left">Bed_5d</td><td align="left">Operation</td></tr><tr><td align="left">005E</td><td align="left">ContrHeadRearLeft</td><td align="left">Ahl_5E</td><td align="left">Left Rear Display/Control Head</td></tr><tr><td align="left">005F</td><td align="left">InforContrUnit1</td><td align="left">IFE_5F</td><td align="left">Information Control Unit 1</td></tr><tr><td align="left">0060</td><td align="left">Tacho</td><td align="left">FSR_60</td><td align="left">Tachograph</td></tr><tr><td align="left">0061</td><td align="left">BatteRegul</td><td align="left">Bar_61</td><td align="left">Battery Regulation</td></tr><tr><td align="left">0062</td><td align="left">DoorElectRearLeft</td><td align="left">Thl_62</td><td align="left">Left Rear Door Electronics</td></tr><tr><td align="left">0063</td><td align="left">EntryAssisDriveSide</td><td align="left">Esf_63</td><td align="left">Driver Side Entry Assistance</td></tr><tr><td align="left">0064</td><td align="left">Stabi</td><td align="left">Stb_64</td><td align="left">Stabilizers</td></tr><tr><td align="left">0065</td><td align="left">TirePressMonit1</td><td align="left">Rel_65</td><td align="left">Tire Pressure Monitoring System</td></tr><tr><td align="left">0066</td><td align="left">SeatAdjusRear</td><td align="left">Ssv_66</td><td align="left">Seat/mirror Adjustment</td></tr><tr><td align="left">0067</td><td align="left">VoiceContr</td><td align="left">Sps_67</td><td align="left">Voice Control</td></tr><tr><td align="left">0068</td><td align="left">WiperContrUnit</td><td align="left">Wie_68</td><td align="left">Wiper Electronics</td></tr><tr><td align="left">0069</td><td align="left">TrailFunct</td><td align="left">Ahf_69</td><td align="left">Trailer Function</td></tr><tr><td align="left">006B</td><td align="left">AerodContrUnit</td><td align="left">ADS_6B</td><td align="left">Aerodynamics Control Unit</td></tr><tr><td align="left">006C</td><td align="left">CamerSysteRearView</td><td align="left">Rfk_6C</td><td align="left">Rearview Camera System</td></tr><tr><td align="left">006D</td><td align="left">DeckLidContrUnit</td><td align="left">Hde_6D</td><td align="left">Rear Lid Electronics</td></tr><tr><td align="left">006E</td><td align="left">DisplContrRoof</td><td align="left">Abd_6E</td><td align="left">Roof Display/Control Head</td></tr><tr><td align="left">006F</td><td align="left">CentrModulComfoSyste2</td><td align="left">Zkz_6F</td><td align="left">Convenience System Central Module II</td></tr><tr><td align="left">0071</td><td align="left">BatteCharg</td><td align="left">Bal_71</td><td align="left">Battery Charger</td></tr><tr><td align="left">0072</td><td align="left">DoorElectRearRight</td><td align="left">Thr_72</td><td align="left">Right Rear Door Electronics</td></tr><tr><td align="left">0073</td><td align="left">ChassContr</td><td align="left">Stf_74</td><td align="left">Suspension Control</td></tr><tr><td align="left">0074</td><td align="left">EntryAssisPasseSide</td><td align="left">Esb_73</td><td align="left">Front Passenger Side Entry Assistance</td></tr><tr><td align="left">0075</td><td align="left">Telem</td><td align="left">Not_75</td><td align="left">Emergency Call Module</td></tr><tr><td align="left">0076</td><td align="left">ParkiAssis</td><td align="left">Eph_76</td><td align="left">Parking Aid</td></tr><tr><td align="left">0077</td><td align="left">Telep</td><td align="left">Tel_77</td><td align="left">Phone</td></tr><tr><td align="left">0078</td><td align="left">SlidiDoorRight</td><td align="left">Sbt_78</td><td align="left">Right Sliding Door</td></tr><tr><td align="left">007B</td><td align="left">SubbuSysteInter</td><td align="left">IFS_7B</td><td align="left">Subbus Systems Interface</td></tr><tr><td align="left">007D</td><td align="left">AuxilHeate</td><td align="left">zuh_7D</td><td align="left">Auxiliary heater</td></tr><tr><td align="left">007E</td><td align="left">DashBoardDisplUnit</td><td align="left">Ast_7E</td><td align="left">Instrument Cluster Display Unit</td></tr><tr><td align="left">007F</td><td align="left">InforContrUnit2</td><td align="left">IFZ_7F</td><td align="left">Information Control Unit 2</td></tr><tr><td align="left">0081</td><td align="left">GearShiftContrModul</td><td align="left">WHB_81</td><td align="left">Gear Shift Control Module</td></tr><tr><td align="left">0082</td><td align="left">HeadUpDispl</td><td align="left">HUD_82</td><td align="left">Head Up Display</td></tr><tr><td align="left">0083</td><td align="left">FrontObserModul</td><td align="left">OVF_83</td><td align="left">Front Observation Module</td></tr><tr><td align="left">0084</td><td align="left">NightVisio</td><td align="left">WBK_84</td><td align="left">Night Vision</td></tr><tr><td align="left">0085</td><td align="left">OnBoardCamer</td><td align="left">KST_85</td><td align="left">On-Board Camera</td></tr><tr><td align="left">0088</td><td align="left">MultiContoSeatDriveSide</td><td align="left">MKF_88</td><td align="left">Multi Contour Seat Driver Side</td></tr><tr><td align="left">0089</td><td align="left">MultiContoSeatPasseSide</td><td align="left">MKB_89</td><td align="left">Multi Contour Seat Passenger Side</td></tr><tr><td align="left">008A</td><td align="left">MultiContoSeatRearDriveSide</td><td align="left">MHF_8A</td><td align="left">Multi Contour Seat Rear Driver Side</td></tr><tr><td align="left">008B</td><td align="left">AdaptCruisContr2</td><td align="left">DIR_8B</td><td align="left">Adaptive Cruise Control 2</td></tr><tr><td align="left">008C</td><td align="left">BatteEnergContrModul</td><td align="left">HBM_8C</td><td align="left">Battery Energy Control Module</td></tr><tr><td align="left">008D</td><td align="left">MultiContoSeatRearPasseSide</td><td align="left">MHB_8D</td><td align="left">Multi Contour Seat Rear Passenger Side</td></tr><tr><td align="left">008E</td><td align="left">ImageProceElect</td><td align="left">BVS_8E</td><td align="left">Image Processing Electronics</td></tr><tr><td align="left">008F</td><td align="left">PreteFrontLeft</td><td align="left">GSL_8F</td><td align="left">Pretensioner Front Left</td></tr><tr><td align="left">0090</td><td align="left">PreteFrontRight</td><td align="left">GSR_90</td><td align="left">Pretensioner Front Right</td></tr><tr><td align="left">0091</td><td align="left">EnginContrModulLT3</td><td align="left">YMO_01</td><td align="left">Engine Control Module LT3</td></tr><tr><td align="left">0092</td><td align="left">TransElectLT3</td><td align="left">ASG906</td><td align="left">Transmission Electronics LT3</td></tr><tr><td align="left">0093</td><td align="left">ImmobLT3</td><td align="left">YWE_25</td><td align="left">Immobilizer LT3</td></tr><tr><td align="left">0094</td><td align="left">AirbaLT3</td><td align="left">ARCADE906</td><td align="left">Airbag LT3</td></tr><tr><td align="left">0095</td><td align="left">ElectStabiProgrLT3</td><td align="left">ESP906</td><td align="left">Electronic Stability Program LT3</td></tr><tr><td align="left">0096</td><td align="left">DashBoardLT3</td><td align="left">KI906</td><td align="left">Dash Board LT3</td></tr><tr><td align="left">0097</td><td align="left">TachoLT3</td><td align="left">MTCO906</td><td align="left">Tachograph LT3</td></tr><tr><td align="left">0098</td><td align="left">TirePressMonitLT3</td><td align="left">TPM906</td><td align="left">Tire Pressure Monitoring LT3</td></tr><tr><td align="left">0099</td><td align="left">ElectIgnitStartSwitcLT3</td><td align="left">EZS_LT3</td><td align="left">Electronic Ignition Starter Switch LT3</td></tr><tr><td align="left">009A</td><td align="left">RemotContrLT3</td><td align="left">YFF_93</td><td align="left">Remote Control LT3</td></tr><tr><td align="left">009B</td><td align="left">DoorElectDriveSideLT3</td><td align="left">TF906</td><td align="left">Door Electronics Driver Side LT3</td></tr><tr><td align="left">009C</td><td align="left">AirCondiLT3</td><td align="left">KLA906</td><td align="left">Air Conditioning LT3</td></tr><tr><td align="left">009D</td><td align="left">AuxilHeateFuelLT3</td><td align="left">ZHZ906</td><td align="left">Auxilary Heater Fuel LT3</td></tr><tr><td align="left">009E</td><td align="left">AuxilHeateElectLT3</td><td align="left">PTC9063</td><td align="left">Auxiliary Heater Electric LT3</td></tr><tr><td align="left">009F</td><td align="left">ParkiHeateWaterLT3</td><td align="left">STH906</td><td align="left">Parking Heater Water LT3</td></tr><tr><td align="left">00A0</td><td align="left">RadioAudio5LT3</td><td align="left">XHUAGW</td><td align="left">Radio Audio 5 LT3</td></tr><tr><td align="left">00A1</td><td align="left">NavigLT3</td><td align="left">XHU_S</td><td align="left">Navigation LT3</td></tr><tr><td align="left">00A2</td><td align="left">CompaDiscChangLT3</td><td align="left">XCDC_S</td><td align="left">Compact Disc Changer LT3</td></tr><tr><td align="left">00A3</td><td align="left">TelepLT3</td><td align="left">XUHI_S</td><td align="left">Telephone LT3</td></tr><tr><td align="left">00A4</td><td align="left">Armre</td><td align="left">ARL_A4</td><td align="left">Armrest</td></tr><tr><td align="left">00A5</td><td align="left">FrontSensoDriveAssisSyste</td><td align="left">FFF_A5</td><td align="left">Front Sensors Driver Assistance System</td></tr><tr><td align="left">00A6</td><td align="left">MicroContrUnit</td><td align="left">MSG_A6</td><td align="left">Microphone Control Unit</td></tr><tr><td align="left">00A7</td><td align="left">InfotInter</td><td align="left">IFI_A7</td><td align="left">Infotainment Interface</td></tr><tr><td align="left">00A8</td><td align="left">ExterCommuInter</td><td align="left">IFK_A8</td><td align="left">External Communication Interface</td></tr><tr><td align="left">00A9</td><td align="left">ActuaForStrucBorneSound</td><td align="left">AFK_A9</td><td align="left">Actuator For Structure-Borne Sound</td></tr><tr><td align="left">00AA</td><td align="left">WheelBrakeRearRight</td><td align="left">HRR_AA</td><td align="left">Wheel Brake Rear Right</td></tr><tr><td align="left">00AB</td><td align="left">WheelBrakeRearLeft</td><td align="left">HRL_AB</td><td align="left">Wheel Brake Rear Left</td></tr><tr><td align="left">00AC</td><td align="left">ReducContrModul</td><td align="left">RDS_AC</td><td align="left">Reductant Control Module</td></tr><tr><td align="left">00AD</td><td align="left">SensoBrakeSyste</td><td align="left">SFB_AD</td><td align="left">Sensors Brake Systems</td></tr><tr><td align="left">00B0</td><td align="left">DisplContrUnitRoofLT3</td><td align="left">DBE906</td><td align="left">Display Control Unit Roof LT3</td></tr><tr><td align="left">00B1</td><td align="left">UpperOperaFieldLT3</td><td align="left">OBF906</td><td align="left">Upper Operating Field LT3</td></tr><tr><td align="left">00B2</td><td align="left">ParkiAidLT3</td><td align="left">PTS906</td><td align="left">Parking Aid LT3</td></tr><tr><td align="left">00B3</td><td align="left">TrailFunctLT3</td><td align="left">AAG169</td><td align="left">Trailer Function LT3</td></tr><tr><td align="left">00B4</td><td align="left">VehicElectSysteContrModulLT3</td><td align="left">SAM906</td><td align="left">Vehicle Electrical System Control Module LT3</td></tr><tr><td align="left">00B5</td><td align="left">ProgrSpeciModulLT3</td><td align="left">PSM906</td><td align="left">Programmable Special Module LT3</td></tr><tr><td align="left">00B6</td><td align="left">SteerColumTubeSwitcModulLT3</td><td align="left">MRM906</td><td align="left">Steering Column Tube Switch Module LT3</td></tr><tr><td align="left">00B7</td><td align="left">AccesStartInter</td><td align="left">IZS_B7</td><td align="left">Access Startsystem Interface</td></tr><tr><td align="left">00B8</td><td align="left">ElectRoofContr2</td><td align="left">EL2_B8</td><td align="left">Electronic Roof Control 2</td></tr><tr><td align="left">00B9</td><td align="left">AuxilDisplContrUnit</td><td align="left">ZAB_B9</td><td align="left">Auxiliary Display Control Unit</td></tr><tr><td align="left">00BA</td><td align="left">AssemMount</td><td align="left">AGL_BA</td><td align="left">Assembly Mounting</td></tr><tr><td align="left">00BB</td><td align="left">DoorElectRearDriveSide</td><td align="left">TFH_BB</td><td align="left">Door Electronics Rear Driver Side</td></tr><tr><td align="left">00BC</td><td align="left">DoorElectRearPasseSide</td><td align="left">TBH_BC</td><td align="left">Door Electronics Rear Passenger Side</td></tr><tr><td align="left">00BD</td><td align="left">HighVoltaBatteChargManag</td><td align="left">HOB_BD</td><td align="left">High Voltage Battery Charge Management</td></tr><tr><td align="left">00BE</td><td align="left">SlidiDoorRearLeft</td><td align="left">SRL_BE</td><td align="left">Sliding Door Rear Left</td></tr><tr><td align="left">00BF</td><td align="left">SlidiDoorRearRight</td><td align="left">SRR_BF</td><td align="left">Sliding Door Rear Right</td></tr><tr><td align="left">00C0</td><td align="left">ActuaForExterNoise</td><td align="left">AFA_C0</td><td align="left">Actuator For Exterior Noise</td></tr><tr><td align="left">00C1</td><td align="left">BatteRegulLT3</td><td align="left">BA3_C1</td><td align="left">Battery Regulation LT3</td></tr><tr><td align="left">00C2</td><td align="left">TransContrModul2</td><td align="left">GE2_C2</td><td align="left">Transmission Control Module 2</td></tr><tr><td align="left">00C3</td><td align="left">DriveMotorContrModul2</td><td align="left">EA2_C3</td><td align="left">Drive Motor Control Module 2</td></tr><tr><td align="left">00C4</td><td align="left">ConveForDriveMotorContrModul</td><td align="left">SPE_C4</td><td align="left">Converter For Drive Motor Control Module</td></tr><tr><td align="left">00C5</td><td align="left">ThermManag</td><td align="left">THE_C5</td><td align="left">Thermal Management</td></tr><tr><td align="left">00C6</td><td align="left">BatteChargContrModul</td><td align="left">HBL_C6</td><td align="left">Battery Charger Control Module</td></tr><tr><td align="left">00C7</td><td align="left">PedesProte</td><td align="left">FGS_C7</td><td align="left">Pedestrian Protection</td></tr><tr><td align="left">00C8</td><td align="left">AuxilDisplContrUnit2</td><td align="left">ZA2_C9</td><td align="left">Auxiliary Display Control Unit 2</td></tr><tr><td align="left">00C9</td><td align="left">RearMirro</td><td align="left">RUE_C9</td><td align="left">Rear Mirror</td></tr><tr><td align="left">FEA0</td><td align="left">RadioSound50LT3</td><td align="left">XAGW</td><td align="left">Radio Sound 50 LT3</td></tr><tr><td align="left">FF01</td><td align="left">EnginContrModul1Skoda</td><td align="left">MO2_01</td><td align="left">Engine Control Module 1 Skoda</td></tr><tr><td align="left">FF07</td><td align="left">DisplContrUnitPhaetGP2</td><td align="left">AB2_07</td><td align="left">Display Control Unit Phaeton GP2</td></tr><tr><td align="left">FFA0</td><td align="left">RadioSound20LT3</td><td align="left">XCDR_VAN</td><td align="left">Radio Sound 20 LT3</td></tr></tbody></table>

**Table 109. SGBD Variants**

The following table lists the diagnostic operations/services that can be selected under [Section 7.14.15.16.3, “Service Properties Dialog Screen”](7-14-15-category-ecukom.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.EcuKom_DienstInformation "7.14.15.16.3. Service Properties Dialog Screen").

<a id="d4e24489"></a>

<table border="1" summary="Diagnostic Service Listing"><colgroup><col align="left"/><col align="left"/><col align="left"/><col align="left"/><col align="left"/></colgroup><thead><tr bgcolor="#EEEEEE"><th align="left">Serial Number</th><th align="left">ODIS Name</th><th align="left">Job Name</th><th align="left">Comment</th><th align="left">SGBD</th></tr></thead><tbody><tr><td align="left">1</td><td align="left">AbsBleed</td><td align="left">ABS Bleed</td><td align="left">ABS Bleeding</td><td align="left">Bas1bre</td></tr><tr><td align="left">2</td><td align="left">ClearDtcBroadcast</td><td align="left">Erase_allDTC</td><td align="left">Erase all DTC memories</td><td align="left">Brd6cast</td></tr><tr><td align="left">3</td><td align="left">ReadAdaption</td><td align="left">Read_adaptation</td><td align="left">Read the adaptation value</td><td align="left">Bas1281</td></tr><tr><td align="left">4</td><td align="left">SaveAdaption</td><td align="left">Save_adaptation</td><td align="left">Save the adaptation value</td><td align="left">Bas1281</td></tr><tr><td align="left">5</td><td align="left">TestAdaption</td><td align="left">Test_adaptation</td><td align="left">Test the adaptation value</td><td align="left">Bas1281</td></tr><tr><td align="left">6</td><td align="left">Adaption</td><td align="left">Anpassung2</td><td align="left">Anpassung2</td><td align="left">Bas2000 6000</td></tr><tr><td align="left">7</td><td align="left">EndCommunication</td><td align="left">End_output</td><td align="left">End output</td><td align="left">Bas1281</td></tr><tr><td align="left">8</td><td align="left"> </td><td align="left">User_application</td><td align="left">User application</td><td align="left">Bas1281</td></tr><tr><td align="left">9</td><td align="left">ReadChallenge</td><td align="left">Read_challenge</td><td align="left">Rad out the challenge code</td><td align="left">Bas2WFS, Bas6WFS</td></tr><tr><td align="left">10</td><td align="left">Select_ECU</td><td align="left">Select_ECU</td><td align="left">Select ECU</td><td align="left">MoV2000</td></tr><tr><td align="left">11</td><td align="left">Check_ECUlist</td><td align="left">Check_ECUlist</td><td align="left">Check ECU list</td><td align="left">MoV2000</td></tr><tr><td align="left">12</td><td align="left">ReadEEPROM</td><td align="left">Read_EEPROM</td><td align="left">Read out EEPROM</td><td align="left">Bas1281</td></tr><tr><td align="left">13</td><td align="left">ReadEEPROMSerial</td><td align="left">Read_EEPROM_serial</td><td align="left">Read out EEPROM, serial</td><td align="left">Bas1281</td></tr><tr><td align="left">14</td><td align="left">WriteEEPROM</td><td align="left">Write_EEPROM</td><td align="left">Write EEPROM</td><td align="left">Bas1281</td></tr><tr><td align="left">15</td><td align="left">WriteEEPROMSerial</td><td align="left">Write_EEPROM_serial</td><td align="left">Write EEPROM, serial</td><td align="left">Bas1281</td></tr><tr><td align="left">16</td><td align="left">EndCommunication</td><td align="left">End</td><td align="left">End</td><td align="left">Bas1281 2000 6000</td></tr><tr><td align="left">17</td><td align="left">ReadECUExtended Identification</td><td align="left">Check_EnhIdentification</td><td align="left">Check enhanced identification</td><td align="left">Bas2000 6000</td></tr><tr><td align="left">18</td><td align="left">ReadVehicleIdentification Number</td><td align="left">Check_VIN</td><td align="left">Check VIN</td><td align="left">Bas2000 6000</td></tr><tr><td align="left">19</td><td align="left">ReadDTC</td><td align="left">Check_DTCmemory</td><td align="left">Check DTC memory</td><td align="left">Bas1281 2000 6000</td></tr><tr><td align="left">20</td><td align="left">ClearDiagnosticInformation</td><td align="left">Erase_DTCmemory</td><td align="left">Erase DTC memory</td><td align="left">Bas1281 2000 6000</td></tr><tr><td align="left">21</td><td align="left">ReadDTCEnvironmental Conditions</td><td align="left">DTC memory details</td><td align="left">Check DTC memory, details</td><td align="left">Bas2000 6000</td></tr><tr><td align="left">22</td><td align="left">FlashInit</td><td align="left">FlashInit</td><td align="left">Flash initialization</td><td align="left">Bas2flsh, Bas6flsh</td></tr><tr><td align="left">23</td><td align="left">FlashProg2</td><td align="left">FlashProg2</td><td align="left">Flash program 2</td><td align="left">Bas2flsh, Bas6flsh</td></tr><tr><td align="left">24</td><td align="left">FlashEcu</td><td align="left">FlashProg3</td><td align="left">Flash program 3</td><td align="left">Bas2flsh, Bas6flsh</td></tr><tr><td align="left">25</td><td align="left">ReadFlashStatus</td><td align="left">Check_FlashStatus</td><td align="left">Check flash status</td><td align="left">Bas2000 6000</td></tr><tr><td align="left">26</td><td align="left"> </td><td align="left">FlashVer2</td><td align="left">Flash Version 2</td><td align="left">Bas2flsh, Bas6flsh</td></tr><tr><td align="left">27</td><td align="left"> </td><td align="left">FlashVer3</td><td align="left">Flash Version 3</td><td align="left">Bas2flsh, Bas6flsh</td></tr><tr><td align="left">28</td><td align="left">FlashXXX1</td><td align="left">FlashXXX1</td><td align="left">Flash XXX1</td><td align="left">Bas1281 2000 6000</td></tr><tr><td align="left">29</td><td align="left"> </td><td align="left">RdFlsh Baud rates</td><td align="left">Read flash, baud rates</td><td align="left">Bas2flsh, Bas6flsh</td></tr><tr><td align="left">30</td><td align="left"> </td><td align="left">SetFlsh baud rates</td><td align="left">Set flash, baud rates</td><td align="left">Bas2flsh, Bas6flsh</td></tr><tr><td align="left">31</td><td align="left">TrainGVA</td><td align="left">Train_GFA</td><td align="left">Train global authentication</td><td align="left">Bas2000 6000</td></tr><tr><td align="left">32</td><td align="left">WriteFSC</td><td align="left">Write_FSC</td><td align="left">Write FSC</td><td align="left">Bas2000 6000</td></tr><tr><td align="left">33</td><td align="left">BasicSetting</td><td align="left">Basic Setting</td><td align="left">Basic Setting</td><td align="left">Bas1281</td></tr><tr><td align="left">34</td><td align="left">BasicSetting2</td><td align="left">Grundeinstellung2</td><td align="left">Basic setting 2</td><td align="left">Bas2000 6000</td></tr><tr><td align="left">35</td><td align="left">BasicSetting3</td><td align="left">Grundeinstellung3</td><td align="left">Basic setting 3</td><td align="left">Bas2000 6000</td></tr><tr><td align="left">36</td><td align="left">ReadVehicleManufacturer ECUHardwareNumber</td><td align="left">Check_HardwarePartNo</td><td align="left">Check hardware part number</td><td align="left">Bas2000 6000</td></tr><tr><td align="left">37</td><td align="left"> </td><td align="left">Identification</td><td align="left">Identification</td><td align="left">only groups - SGBD</td></tr><tr><td align="left">38</td><td align="left"> </td><td align="left">Check_IdentificationData</td><td align="left">Check identification data</td><td align="left">Bas2000 6000</td></tr><tr><td align="left">39</td><td align="left">TrainICA</td><td align="left">Program_IKA</td><td align="left">Train individual authentication components</td><td align="left">Bas2000 6000</td></tr><tr><td align="left">40</td><td align="left"> </td><td align="left">Initialization</td><td align="left">Initialization</td><td align="left">All</td></tr><tr><td align="left">41</td><td align="left">SendKey</td><td align="left">Send_key</td><td align="left">Send a key for security access with level 1</td><td align="left">Bas2000 6000</td></tr><tr><td align="left">42</td><td align="left">ReadCodingValueLong</td><td align="left">Read_LongCoding</td><td align="left">Read long coding</td><td align="left">Bas2000 6000</td></tr><tr><td align="left">43</td><td align="left">WriteCodingValueLong</td><td align="left">Write_LongCoding</td><td align="left">Write long coding</td><td align="left">Bas2000 6000</td></tr><tr><td align="left">44</td><td align="left">ReadLifeCycleInformation</td><td align="left">Check_LifeCycleData</td><td align="left">Check life cycle data</td><td align="left">Bas2000 6000</td></tr><tr><td align="left">45</td><td align="left">Login</td><td align="left">Login</td><td align="left">Login</td><td align="left">Bas1281 2000 6000</td></tr><tr><td align="left">46</td><td align="left">ReadMeasurementValue</td><td align="left">Read_measured_value</td><td align="left">Read measured value</td><td align="left">Bas1281</td></tr><tr><td align="left">47</td><td align="left">ReadMeasurementValue Block</td><td align="left">Read_measured_value_block</td><td align="left">Read measured value block</td><td align="left">Bas1281 2000 6000</td></tr><tr><td align="left">48</td><td align="left">ReadSystemNameOr EngineType</td><td align="left">Check_EngineOrSystemNo</td><td align="left">Check engine or system number</td><td align="left">Bas2000 6000</td></tr><tr><td align="left">49</td><td align="left">ReadRAM</td><td align="left">Read_RAM</td><td align="left">Read RAM</td><td align="left">Bas1281</td></tr><tr><td align="left">50</td><td align="left">ReadROM</td><td align="left">Read_ROM</td><td align="left">Read ROM</td><td align="left">Bas1281</td></tr><tr><td align="left">51</td><td align="left">RequestSeed</td><td align="left">Request_seed</td><td align="left">Send a seed for security access with level 1</td><td align="left">Bas2000 6000</td></tr><tr><td align="left">52</td><td align="left">SelectiveActuator Diagnosis</td><td align="left">Selective output diagnostic test mode</td><td align="left">Selective output diagnostic test mode</td><td align="left">Bas2000 6000</td></tr><tr><td align="left">53</td><td align="left">ReadSoftwareVersion Number</td><td align="left">Check_SoftwareVersion</td><td align="left">Check software version</td><td align="left">Bas2000 6000</td></tr><tr><td align="left">54</td><td align="left">SpecialAdaption</td><td align="left">SonderAnpassung2</td><td align="left">Special Adaptation2</td><td align="left">Bas2son</td></tr><tr><td align="left">55</td><td align="left">SpecialReadAdaption</td><td align="left">Read_SpecialAdaptation</td><td align="left">Read special adaptation</td><td align="left">Bas1son</td></tr><tr><td align="left">56</td><td align="left">SpecialTestAdaption</td><td align="left">Test_SpecialAdaptation</td><td align="left">Test special adaptation</td><td align="left">Bas1son</td></tr><tr><td align="left">57</td><td align="left">SpecialSaveAdaption</td><td align="left">Save_SpecialAdaptation</td><td align="left">Save special adaptation</td><td align="left">Bas1son</td></tr><tr><td align="left">58</td><td align="left">SpecialWriteCoding Value2</td><td align="left">SonderCodierung2</td><td align="left">Special Coding2</td><td align="left">Bas2son</td></tr><tr><td align="left">59</td><td align="left">SpecialLogin</td><td align="left">SpecialLogin</td><td align="left">Special login</td><td align="left">Bas1son</td></tr><tr><td align="left">60</td><td align="left">WriteMemoryBlock</td><td align="left">Write_MemoryBlock</td><td align="left">Write memory block</td><td align="left">Bas2000 6000</td></tr><tr><td align="left">61</td><td align="left">WriteMemory</td><td align="left">Write_memory</td><td align="left">Write memory</td><td align="left">Bas2000 6000</td></tr><tr><td align="left">62</td><td align="left">ReadMemory</td><td align="left">Read_memory</td><td align="left">Read memory</td><td align="left">Bas2000 6000</td></tr><tr><td align="left">63</td><td align="left">StartDiagnosticSession</td><td align="left">StartDiagnostic Session</td><td align="left">Start Diagnostic Session</td><td align="left">Bas2000 6000</td></tr><tr><td align="left">64</td><td align="left">ReadErrorPaths</td><td align="left">Check_StatusFaultPaths</td><td align="left">Check StatusFaultPaths</td><td align="left">Bas2000 6000</td></tr><tr><td align="left">65</td><td align="left">SequentialActuator Diagnosis</td><td align="left">Output Diagnostic Test Mode</td><td align="left">Output Diagnostic Test Mode</td><td align="left">Bas1281</td></tr><tr><td align="left">66</td><td align="left">SequentialActuator Diagnosis2</td><td align="left">Stellglieddiagnose2</td><td align="left">Actuator diagnosis 2</td><td align="left">Bas2000 6000</td></tr><tr><td align="left">67</td><td align="left">SequentialActuator Diagnosis3</td><td align="left">Stellglieddiagnose3</td><td align="left">Actuator diagnosis 3</td><td align="left">Bas2000 6000</td></tr><tr><td align="left">68</td><td align="left">WriteCodingValue</td><td align="left">Code_ControlModule</td><td align="left">Code control module</td><td align="left">Bas1281 2000 6000</td></tr><tr><td align="left">69</td><td align="left">WriteCodingValue2</td><td align="left">Steuergeraet_codieren2</td><td align="left">Code control module2</td><td align="left">Bas2000 6000</td></tr><tr><td align="left">70</td><td align="left">ReadECUIdentification</td><td align="left">Check_ControlModuleVersion</td><td align="left">Check control module version</td><td align="left">Bas1281 2000 6000</td></tr><tr><td align="left">71</td><td align="left">ReadECUIdentification2</td><td align="left">Steuergeraeteversion_abfragen2</td><td align="left">Check control module version2</td><td align="left">Bas2000 6000</td></tr><tr><td align="left">72</td><td align="left">TransportmodeOnBroadcast</td><td align="left">Activate_TransportMode</td><td align="left">Switch transport mode on</td><td align="left">Brd6cast</td></tr><tr><td align="left">73</td><td align="left">ReadExhaustRegulation OrTypeApprovalNumber</td><td align="left">Check_TypeApprovalNo</td><td align="left">Check type approval number</td><td align="left">Bas2000 6000</td></tr><tr><td align="left">74</td><td align="left">SupportedFunctions</td><td align="left">Check_SuppFunctions</td><td align="left">Check supported functions</td><td align="left">Bas2000 6000 and further</td></tr><tr><td align="left">75</td><td align="left">ReadGateway ComponentList</td><td align="left">Check_ComponentsList</td><td align="left">Check components list</td><td align="left">DiD2000 6000</td></tr><tr><td align="left">76</td><td align="left">UnlockImmobiliser</td><td align="left">Disable_Immobilizer</td><td align="left">Disable immobilizer</td><td align="left">Bas2WFS, Bas6WFS</td></tr><tr><td align="left">77</td><td align="left">UnlockImmobiliser2</td><td align="left">WFS_freischalten2</td><td align="left">Disable immobilizer 2</td><td align="left">Bas2000 6000</td></tr></tbody></table>

**Table 110. Diagnostic Service Listing**

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-14-14-category-measurement.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="7-14-function-test-editor.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="7-14-16-category-file.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">7.14.14. Category - Measurement </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 7.14.16. Category - File</td></tr></table>
