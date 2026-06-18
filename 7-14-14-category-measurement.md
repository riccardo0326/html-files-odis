[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md) > [7.14. Function Test Editor](7-14-function-test-editor.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.14.14. Category - Measurement</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-14-13-category-process.md">Prev</a> </td><th align="center" width="60%">7.14. Function Test Editor</th><td align="right" width="20%"> <a accesskey="n" href="7-14-15-category-ecukom.md">Next</a></td></tr></table>

---

#### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung"></a>7.14.14. Category - Measurement

Various data can be determined using the following action elements:

- [Section 7.14.14.1, “Action Element - Measuring Channel”](7-14-14-category-measurement.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Messkanal "7.14.14.1. Action Element - Measuring Channel")
- [Section 7.14.14.2, “Action Element - Measure Voltage”](7-14-14-category-measurement.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Messen_Spannung "7.14.14.2. Action Element - Measure Voltage")
- [Section 7.14.14.3, “Action Element - Measure Current”](7-14-14-category-measurement.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Messen_Strom "7.14.14.3. Action Element - Measure Current")
- [Section 7.14.14.4, “Action Element - Measure Resistance”](7-14-14-category-measurement.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Messen_Widerstand "7.14.14.4. Action Element - Measure Resistance")
- [Section 7.14.14.5, “Action Element - Measure Diode Voltage”](7-14-14-category-measurement.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Messen_Diodenspannung "7.14.14.5. Action Element - Measure Diode Voltage")
- [Section 7.14.14.6, “Action Element - Measure Pressure”](7-14-14-category-measurement.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Messen_Druck "7.14.14.6. Action Element - Measure Pressure")
- [Section 7.14.14.7, “Action Element - Measure Temperature”](7-14-14-category-measurement.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Messen_Temperatur "7.14.14.7. Action Element - Measure Temperature")
- [Section 7.14.14.8, “Action Element - Oscilloscope”](7-14-14-category-measurement.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Osziloskop "7.14.14.8. Action Element - Oscilloscope")
- [Section 7.14.14.9, “Action Element - High Voltage Block”](7-14-14-category-measurement.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Block_Hochvolt "7.14.14.9. Action Element - High Voltage Block")
- [Section 7.14.14.10, “Action Element - High-Voltage Break”](7-14-14-category-measurement.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Break_Hochvolt "7.14.14.10. Action Element - High-Voltage Break")
- [Section 7.14.14.11, “Action Element - High-Voltage Measurement Data”](7-14-14-category-measurement.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Messdaten_Hochvolt "7.14.14.11. Action Element - High-Voltage Measurement Data")

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Messkanal"></a>7.14.14.1. Action Element - Measuring Channel

The "Measuring channel" action element can be seen in [Figure 433, “Measuring Channel Action Element”](7-14-14-category-measurement.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Messkanal "Figure 433. Measuring Channel Action Element").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Messkanal"></a>

![Image: measuring channel action element](images/fte_arbeitsflaeche_dialog_messkanal.png)

**Figure 433. Measuring Channel Action Element**

The measuring channel action element generates an adaptation command to the user to connect the measuring cable and the sensors. This action element is needed if the measurement should not be displayed on the tester.

If the "Output" checkbox in the "Results" area is not marked in the measuring instructions (NODISPAY mode), there must be a "measuring channel" command before the measuring commands. This prompts the user to select the desired measuring channel and to connect with the measuring points.

<a id="table.hinweis.fte.messkanal.stromzange"></a>

<table border="1" summary="Note for Measuring Channel with Current Probe"><colgroup><col align="center"/><col align="left"/></colgroup><tbody valign="top"><tr><td align="center" valign="top"><span class="inlinemediaobject"><img alt="Note symbol" src="images/info.png"/></span></td><td align="left" valign="top">
<p><span class="bold"><strong>Note:</strong></span> When the current probe is selected, the measuring channel text is not displayed immediately at runtime, but rather the display is delayed to the next measuring command. In standard cases, one or more commands for measuring current with the current probe and without measuring channel output follow the measuring channel with current probe. The measuring channel text is displayed in the process window before the first measurement. If the current probe must be calibrated for the first measurement, then the measuring channel text will be displayed after the calibration and before the measurement.</p>
</td></tr></tbody></table>

**Table 95. Note for Measuring Channel with Current Probe**

###### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Messkanal.UrdMesskanaele"></a>7.14.14.1.1. U/R/D Cable

The "Measuring channel" action element with "U/R/D cable" selection is shown in [Figure 434, “U/R/D Cable Measuring Channel”](7-14-14-category-measurement.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Messkanal.URD "Figure 434. U/R/D Cable Measuring Channel").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Messkanal.URD"></a>

![Image: U/R/D cable measuring channel](images/fte_arbeitsflaeche_dialog_messkanal_urd.png)

**Figure 434. U/R/D Cable Measuring Channel**

**U/R/D Cable**

The measuring channel selects the U/R/D cable and defines a vehicle test point (see [Section 7.14.14.1.4, “Vehicle Test Point”](7-14-14-category-measurement.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.FzgTestpunkt "7.14.14.1.4. Vehicle Test Point")).

**I cable**

The measuring channel selects the I cable and defines a vehicle test point (see [Section 7.14.14.1.4, “Vehicle Test Point”](7-14-14-category-measurement.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.FzgTestpunkt "7.14.14.1.4. Vehicle Test Point")).

<a id="table.hinweis.fte.ikabel"></a>

<table border="1" summary="Note for I Cable and Current Probe 2"><colgroup><col align="center"/><col align="left"/></colgroup><tbody valign="top"><tr><td align="center" valign="top"><span class="inlinemediaobject"><img alt="Note symbol" src="images/info.png"/></span></td><td align="left" valign="top">
<p><span class="bold"><strong>Note:</strong></span> The "I cable" specification (see <a class="xref" href="7-14-14-category-measurement.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Messkanal" title="Figure 433. Measuring Channel Action Element">Figure 433, “Measuring Channel Action Element”</a>) is based on the U/R/D measuring cable for the VAS 5051 in the 10 A position (inline current measurement).</p>
<p>The specification "Current probe 2" is based on the use of the 500 a current probe.</p>
</td></tr></tbody></table>

**Table 96. Note for I Cable and Current Probe 2**

**URDI cable**

Selects the URDI cable as the measuring channel and defines a vehicle test point (see [Section 7.14.14.1.4, “Vehicle Test Point”](7-14-14-category-measurement.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.FzgTestpunkt "7.14.14.1.4. Vehicle Test Point")).

**Current clamp**

Selects a current probe including number as the measuring channel and defines a vehicle test point (see [Section 7.14.14.1.4, “Vehicle Test Point”](7-14-14-category-measurement.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.FzgTestpunkt "7.14.14.1.4. Vehicle Test Point")).

Please see the note under [Table 96, “Note for I Cable and Current Probe 2”](7-14-14-category-measurement.md#table.hinweis.fte.ikabel "Table 96. Note for I Cable and Current Probe 2").

**Pressure sensor**

Selects the pressure sensor as the measuring channel and defines a vehicle test point (see [Section 7.14.14.1.4, “Vehicle Test Point”](7-14-14-category-measurement.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.FzgTestpunkt "7.14.14.1.4. Vehicle Test Point")).

**Temperature sensor**

Selects the temperature sensor as the measuring channel and defines a vehicle test point (see [Section 7.14.14.1.4, “Vehicle Test Point”](7-14-14-category-measurement.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.FzgTestpunkt "7.14.14.1.4. Vehicle Test Point")).

**COM cable**

Selects the COM cable as the measuring channel and defines a vehicle test point (see [Section 7.14.14.1.4, “Vehicle Test Point”](7-14-14-category-measurement.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.FzgTestpunkt "7.14.14.1.4. Vehicle Test Point")).

###### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Messkanal.DsoMesskanaele"></a>7.14.14.1.2. DSO Cable

The "Measuring channel" action element with "DSO cable" selection is shown in [Figure 435, “DSO Cable Measuring Channel”](7-14-14-category-measurement.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Messkanal.DSO "Figure 435. DSO Cable Measuring Channel").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Messkanal.DSO"></a>

![Image: DSO cable measuring channel](images/fte_arbeitsflaeche_dialog_messkanal_dso.png)

**Figure 435. DSO Cable Measuring Channel**

**Channel: A, B, trigger channel**

You can select the oscilloscope channel that should be paired with the vehicle test points using the "A", "B" and "Trigger channel" buttons. The trigger clamp can only be used for the trigger channel.

**DSO1 cable**

Selects the DSO1 cable as the measuring channel and defines a vehicle test point (see [Section 7.14.14.1.4, “Vehicle Test Point”](7-14-14-category-measurement.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.FzgTestpunkt "7.14.14.1.4. Vehicle Test Point")).

**DSO2 cable**

Selects the DSO2 cable as the measuring channel and defines a vehicle test point (see [Section 7.14.14.1.4, “Vehicle Test Point”](7-14-14-category-measurement.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.FzgTestpunkt "7.14.14.1.4. Vehicle Test Point")).

**KV sensor**

Selects the KV sensor as the measuring channel and defines a vehicle test point (see [Section 7.14.14.1.4, “Vehicle Test Point”](7-14-14-category-measurement.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.FzgTestpunkt "7.14.14.1.4. Vehicle Test Point")).

**Current clamp**

Selects a current probe including number as the measuring channel and defines a vehicle test point (see [Section 7.14.14.1.4, “Vehicle Test Point”](7-14-14-category-measurement.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.FzgTestpunkt "7.14.14.1.4. Vehicle Test Point")).

Please see the note under [Table 96, “Note for I Cable and Current Probe 2”](7-14-14-category-measurement.md#table.hinweis.fte.ikabel "Table 96. Note for I Cable and Current Probe 2").

**Trigger clamp**

Prompts the user to connect the trigger clamp to the vehicle test point for the trigger channel (see [Section 7.14.14.1.4, “Vehicle Test Point”](7-14-14-category-measurement.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.FzgTestpunkt "7.14.14.1.4. Vehicle Test Point")).

**Pressure sensor**

Selects the pressure sensor as the measuring channel and defines a vehicle test point (see [Section 7.14.14.1.4, “Vehicle Test Point”](7-14-14-category-measurement.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.FzgTestpunkt "7.14.14.1.4. Vehicle Test Point")).

**Temperature sensor**

Selects the temperature sensor as the measuring channel and defines a vehicle test point (see [Section 7.14.14.1.4, “Vehicle Test Point”](7-14-14-category-measurement.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.FzgTestpunkt "7.14.14.1.4. Vehicle Test Point")).

###### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Messkanal.HochvoltMesskanaele"></a>7.14.14.1.3. High Voltage

The "Measuring channel" action element with "High voltage" selection is shown in [Figure 436, “HV cable measuring channel”](7-14-14-category-measurement.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Messkanal.HV "Figure 436. HV cable measuring channel").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Messkanal.HV"></a>

![Image: HV cable measuring channel](images/fte_arbeitsflaeche_messung_messkanal_hv.png)

**Figure 436. HV cable measuring channel**

**Test probe (+)**

Selects the test probe (+) as the measuring channel and defines a vehicle test point (see [Section 7.14.14.1.4, “Vehicle Test Point”](7-14-14-category-measurement.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.FzgTestpunkt "7.14.14.1.4. Vehicle Test Point")).

**Test probe (-)**

Selects the test probe (-) as the measuring channel and defines a vehicle test point (see [Section 7.14.14.1.4, “Vehicle Test Point”](7-14-14-category-measurement.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.FzgTestpunkt "7.14.14.1.4. Vehicle Test Point")).

###### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.FzgTestpunkt"></a>7.14.14.1.4. Vehicle Test Point

A vehicle test point defines the connection point for a measuring channel. The **Vehicle test point** dialog can be accessed using the **Selection** button for U/R/D cable or high voltage measuring channel. See also [Figure 437, “Vehicle Test Point Dialog”](7-14-14-category-measurement.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Fahrzeugtestpunkt "Figure 437. Vehicle Test Point Dialog").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Fahrzeugtestpunkt"></a>

![Image: vehicle test point selection](images/fte_arbeitsflaeche_messung_messkanal_Fahrzeugtestpunkt.png)

**Figure 437. Vehicle Test Point Dialog**

There are various default settings available. The test point where the DSO1 cable (red probe) should be connected, for example, will be indicate to the technician (adaptation command). The "Contact" or "Socket" option can be used together with "text box", the unlabeled selection, or "text". When measuring with test adapters, the "text box, socket" and the specification of a socket number are needed, for example. Example: connector terminal %SPinBez[z]

A default text can be added using the **Default** button. See also [Section 7.14.3.12, “Default Texts”](7-14-3-use-cases.md#Funktionstesteditor.Allgemeine_Funktionalitaet.Standardtexte "7.14.3.12. Default Texts").

**Note for text translation**

The unlabeled option is used for the output of a string of characters that is not relevant for translation (system string or similar). In contrast, the "Text" fields contains output text that is translated in versions for other languages. The text can also be combined with standard texts, variables, or keywords.

###### <a id="d4e21794"></a>7.14.14.1.5. Additional text

The optional additional text is added after the measuring channel text (see [Figure 438, “Additional Text in Measuring Channel Dialog”](7-14-14-category-measurement.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Zusatztext "Figure 438. Additional Text in Measuring Channel Dialog")). To edit, you must activate the "Edit" button. Use of additional text fields is described in [Section 7.14.7, “Editing Text”](7-14-7-editing-text.md "7.14.7. Editing Text").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Zusatztext"></a>

![Image: additional text in the measuring channel dialog](images/fte_arbeitsflaeche_messung_messkanal_zusatztext.png)

**Figure 438. Additional Text in Measuring Channel Dialog**

###### <a id="d4e21807"></a>7.14.14.1.6. Measuring Sensors Present

Using the **Run test** button (see [Figure 439, “Sensor Test Measuring Channel”](7-14-14-category-measurement.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Messkanal.Messensor "Figure 439. Sensor Test Measuring Channel")), the connected measuring sensors can be checked based on the selection in the measuring channel dialog. The button is not selected by default.

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Messkanal.Messensor"></a>

![Image: sensor test measuring channel](images/fte_arbeitsflaeche_messung_messkanal_messsensor.png)

**Figure 439. Sensor Test Measuring Channel**

The configuration option "Measuring sensor present - run test" must not be using within a high-voltage measurement block. If the function test editor detects that the action element is located within a high-voltage measurement block (or nested within one), an entry with the error status will be displayed in the problem view: "The 'Measuring sensor present' option may not be used in a high-voltage block". The function test with the faulty measuring channel cannot be reported as completed due to this error.

In the operating system, the measuring sensors are then checked with not output. If there is no successful sensor test, an error message in the form of a question is given. The user can repeat the sensor test ("Repeat" button) or cancel it ("Cancel' button).

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Messkanal.Sensorpruefung"></a>

![Image: sensor test measuring channel](images/fte_arbeitsflaeche_messung_messkanal_sensorpruefung.png)

**Figure 440. Sensor Test Measuring Channel**

If the user presses the "Cancel" button, the test program is ended.

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Messen_Spannung"></a>7.14.14.2. Action Element - Measure Voltage

The "Measure voltage" action element can be seen in [Figure 441, “Measure Voltage Action Element”](7-14-14-category-measurement.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Messen_Spannung "Figure 441. Measure Voltage Action Element").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Messen_Spannung"></a>

![Image: Measure_Voltage action element](images/fte_arbeitsflaeche_messung_spannung.png)

**Figure 441. Measure Voltage Action Element**

Using the "Measure voltage" command, you can preset the multimeter integrated in the tester for the voltage measurement and read back a measurement result for the base unit V (volt) in a variable for further processing. Voltage measurement is possible with a test with U/R/D measuring cable up to +/- 50 V and with the DSO measuring cables up to +/- 400 V.

As an example for the measurement category, we will select the "Measure voltage" action element in this document to examine more closely. The other dialogs are structured very similarly.

During the process on the tester, the adaptation command appears first ("Measuring channel output" checkbox marked) and then the actual measurement. If the measurement is to be done without a display (NODISPLAY mode) on the touchscreen ("Output" checkbox in the "Results" field not marked), you must program adaptation prompts for the user with the "Measuring channel" command.

The possible settings reflect the "DC and AC voltage measurement" functionality and are not described in more detail in this location. The functions of the buttons match that of the "Oscilloscope" command.

###### <a id="d4e21847"></a>7.14.14.2.1. U/R/D Cable

There are different measuring channels available. See [Section 7.14.14.1.1, “U/R/D Cable”](7-14-14-category-measurement.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Messkanal.UrdMesskanaele "7.14.14.1.1. U/R/D Cable").

Using the "Measuring channel output" button, you can control if the measuring channel text should be output on the tester.

###### <a id="d4e21852"></a>7.14.14.2.2. DSO Cable

There are different measuring channels available. See [Section 7.14.14.1.2, “DSO Cable”](7-14-14-category-measurement.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Messkanal.DsoMesskanaele "7.14.14.1.2. DSO Cable").

Using the "Measuring channel output" button, you can control if the measuring channel text should be output on the tester.

###### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Messbereich"></a>7.14.14.2.3. Measurement range

The value range of the measurement is specified in the **Measuring range** section. It may be a preconfigured our a user-defined value. A variable (a number type) or an actual number can be entered as a user-defined value.

###### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Ergebnis"></a>7.14.14.2.4. Result

The results value of the measurement can be assigned to a variable (floating decimal type or a whole number variable) in the **Results** tab. In addition to the results value, the measurement status and the error code can be assigned to a whole number variable.

If the measurement is to be done without a display (NODISPLAY) on the touchscreen ("Output" checkbox in the "Results" field not marked), you must program adaptation prompts for the user with the "Measuring channel" command.

<a id="table.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Ergebnis.Fehlercodes"></a>

<a id="d4e21867"></a>

<table border="1" summary="Measuring Equipment Error Codes"><colgroup><col/><col/><col/></colgroup><thead><tr bgcolor="#EEEEEE"><th>Error</th><th>Error code</th><th>Description</th></tr></thead><tbody><tr><td>Sensor Not Connected</td><td>1</td><td>-</td></tr><tr><td>Invalid State</td><td>2</td><td>-</td></tr><tr><td>Bad Object</td><td>3</td><td>-</td></tr><tr><td>Invalid Configuration</td><td>4</td><td>-</td></tr><tr><td>Display Module Error</td><td>5</td><td>-</td></tr><tr><td>Trigger Missing</td><td>6</td><td>-</td></tr><tr><td>GDI Version Mismatch</td><td>7</td><td>-</td></tr><tr><td>GDI Error</td><td>8</td><td>-</td></tr><tr><td>GDI Coordinator Error</td><td>9</td><td>-</td></tr><tr><td>GDI Driver Error</td><td>10</td><td>-</td></tr><tr><td>DCD Mismatch</td><td>11</td><td>-</td></tr><tr><td>Driver Install Error</td><td>12</td><td>-</td></tr><tr><td>Device Not Created</td><td>13</td><td>-</td></tr><tr><td>REF Data Error</td><td>14</td><td>-</td></tr></tbody></table>

**Table 97. Measuring Equipment Error Codes**

###### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.EweUnterdruecken"></a>7.14.14.2.4.1. Suppressing Default Values

The measuring equipment default values dialog can be suppressed using the "Suppress default values" checkbox. This option is deactivated by default, meaning there is a default value entry.

###### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Zusatztext"></a>7.14.14.2.4.2. Additional text

There is the option to formulate additional text if the measurement was performed with an output ("Output" checkbox).

###### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Toleranz"></a>7.14.14.2.5. Tolerance

Enter here a tolerance value for OK or NOT OK (never both at the same time). You can set a tolerance band (from/to) or set a range upward or downward using relative characters (<, >, etc.). The values entered define a threshold for a valid or invalid measurement.

###### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Signalkopplung"></a>7.14.14.2.6. Signal Coupling

You set parameters in the **Signal coupling** tab to define if AC or DC current should be measured. If you do not perform any adaptation, it will start with DC.

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Messen_Strom"></a>7.14.14.3. Action Element - Measure Current

The "Measure current" action element can be seen in [Figure 442, “Measure Current Action Element”](7-14-14-category-measurement.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Messen_Strom "Figure 442. Measure Current Action Element").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Messen_Strom"></a>

![Image: measure current action element](images/fte_arbeitsflaeche_messen_strom.png)

**Figure 442. Measure Current Action Element**

The action element initiates a measurement command, in this case, to measure the current.

Using this command, you can preset the multimeter integrated in the tester for the current measurement (inline measurement, measurement with current probe) and read back a measurement result for the base unit A (ampere) in a variable for further processing. During the process on the tester, the adaptation command appears first ("Measuring channel output" checkbox marked) and then the actual measurement.

The possible settings reflect the functionality

- DC and AC voltage directly
- DC and AC voltage using a current probe

.

###### <a id="d4e21969"></a>7.14.14.3.1. Inline

There are different measuring channels available. See [Section 7.14.14.1.1, “U/R/D Cable”](7-14-14-category-measurement.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Messkanal.UrdMesskanaele "7.14.14.1.1. U/R/D Cable").

Using the "Measuring channel output" button, you can control if the measuring channel text should be output on the tester.

###### <a id="d4e21974"></a>7.14.14.3.2. Current clamp

There are different measuring channels available. See [Section 7.14.14.1.2, “DSO Cable”](7-14-14-category-measurement.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Messkanal.DsoMesskanaele "7.14.14.1.2. DSO Cable").

Using the "Measuring channel output" button, you can control if the measuring channel text should be output on the tester.

The allocation of the current probe numbers is as follows: 1: 50 A, 2: 500 A, 3: 100 A, 4: 1800 A

###### <a id="d4e21980"></a>7.14.14.3.3. Measurement range

See [Section 7.14.14.2.3, “Measurement range”](7-14-14-category-measurement.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Messbereich "7.14.14.2.3. Measurement range").

###### <a id="d4e21984"></a>7.14.14.3.4. Result

See [Section 7.14.14.2.4, “Result”](7-14-14-category-measurement.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Ergebnis "7.14.14.2.4. Result").

###### <a id="d4e21988"></a>7.14.14.3.5. Tolerance

See [Section 7.14.14.2.5, “Tolerance”](7-14-14-category-measurement.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Toleranz "7.14.14.2.5. Tolerance").

###### <a id="d4e21992"></a>7.14.14.3.6. Signal Coupling

See [Section 7.14.14.2.6, “Signal Coupling”](7-14-14-category-measurement.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Signalkopplung "7.14.14.2.6. Signal Coupling").

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Messen_Widerstand"></a>7.14.14.4. Action Element - Measure Resistance

The "Measure resistance" action element can be seen in [Figure 443, “Measure Resistance Action Element”](7-14-14-category-measurement.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Messen_Widerstand "Figure 443. Measure Resistance Action Element").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Messen_Widerstand"></a>

![Image: measure resistance action element](images/fte_arbeitsflaeche_dialog_messen_widerstand.png)

**Figure 443. Measure Resistance Action Element**

The action element initiates a measurement command, in this case, to measure the resistance. Using this command, you can preset the multimeter integrated in the tester for the resistance measurement and read back a measurement result for the base unit Ohms, kOhms, or MOhms in a variable for further processing.

The possible settings reflect the functionality

- Resistance measurement
- Continuity test

.

###### <a id="d4e22016"></a>7.14.14.4.1. Measurement range

See [Section 7.14.14.2.3, “Measurement range”](7-14-14-category-measurement.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Messbereich "7.14.14.2.3. Measurement range").

The unit must also be specified. The result value is automatically converted into the specified unit before assigning to a variable. The reference values of the tolerance are also specified in this unit.

The measuring equipment calibration can be controlled using the "Calibration" button. If the button is activated, then a calibration will be required even when it is not necessary. If the button is not activated, then the measuring equipment components on the process side will determine if a calibration is necessary.

###### <a id="d4e22022"></a>7.14.14.4.2. Measuring channel

There are different measuring channels available. See [Section 7.14.14.1.1, “U/R/D Cable”](7-14-14-category-measurement.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Messkanal.UrdMesskanaele "7.14.14.1.1. U/R/D Cable").

Using the "Measuring channel output" button, you can control if the measuring channel text should be output on the tester.

###### <a id="d4e22027"></a>7.14.14.4.3. Result

See [Section 7.14.14.2.4, “Result”](7-14-14-category-measurement.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Ergebnis "7.14.14.2.4. Result").

###### <a id="d4e22031"></a>7.14.14.4.4. Tolerance

See [Section 7.14.14.2.5, “Tolerance”](7-14-14-category-measurement.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Toleranz "7.14.14.2.5. Tolerance").

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Messen_Diodenspannung"></a>7.14.14.5. Action Element - Measure Diode Voltage

The "Measure diode voltage" action element can be seen in [Figure 444, “Measure Diode Voltage Action Element”](7-14-14-category-measurement.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Messen_Diodenspannung "Figure 444. Measure Diode Voltage Action Element").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Messen_Diodenspannung"></a>

![Image: measure diode voltage action element](images/fte_arbeitsflaeche_dialog_messen_diode.png)

**Figure 444. Measure Diode Voltage Action Element**

Using this command, you can preset the multimeter integrated in the tester for various measurements on a diode and read back a measurement result for further processing. You can use the command for the "Status" operating mode.

###### <a id="d4e22048"></a>7.14.14.5.1. Measuring channel

There are different measuring channels available. See [Section 7.14.14.1.1, “U/R/D Cable”](7-14-14-category-measurement.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Messkanal.UrdMesskanaele "7.14.14.1.1. U/R/D Cable") and [Section 7.14.14.1.2, “DSO Cable”](7-14-14-category-measurement.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Messkanal.DsoMesskanaele "7.14.14.1.2. DSO Cable").

Using the "Measuring channel output" button, you can control if the measuring channel text should be output on the tester.

###### <a id="d4e22054"></a>7.14.14.5.2. Result

The results value of the measurement can be assigned to a variable (floating decimal type or a whole number variable) in the **Results** tab. (see [Section 7.14.14.2.4, “Result”](7-14-14-category-measurement.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Ergebnis "7.14.14.2.4. Result"))

###### <a id="d4e22059"></a>7.14.14.5.3. Status

If you select "Status", specify "OK" or "NOT OK" and then the expected diode status. The test controls the test step status and detects the specified diode status (flow direction, blocking direction, interruption, or short circuit). The first letter is given as a result, such as "F". The complete name, such as "flow direction", appears on the tester with the diode symbol.

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Messen_Druck"></a>7.14.14.6. Action Element - Measure Pressure

The "Measure pressure" action element can be seen in [Figure 445, “Measure Pressure Action Element”](7-14-14-category-measurement.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Messen_Druck "Figure 445. Measure Pressure Action Element").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Messen_Druck"></a>

![Image: measure pressure action element](images/fte_arbeitsflaeche_dialog_messen_druck.png)

**Figure 445. Measure Pressure Action Element**

Using this command, you can preset the multimeter integrated in the tester for the T/D pressure measurements using five sensor types (five measuring ranges) and read back a numerical measurement result in a variable for further processing.

The possible pressure sensor settings reflect the functionality

- Multimeter, pressure T/D

.

###### <a id="d4e22080"></a>7.14.14.6.1. Measuring channel

The pressure sensor measuring channel is available. See [Section 7.14.14.1.1, “U/R/D Cable”](7-14-14-category-measurement.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Messkanal.UrdMesskanaele "7.14.14.1.1. U/R/D Cable").

The measuring channel can use one of our adaptable pressure sensors. The value range is specified in this dialog using the selection fields for the pressure sensors.

In order to receive interpretable results from the pressure measurement under unstable pressure conditions, there is an option to set up a filter. To do this, select option 1. Options 2 and 3 are for filters that can be used in the future.

Using the "Measuring channel output" button, you can control if the measuring channel text should be output on the tester.

###### <a id="d4e22087"></a>7.14.14.6.2. Result

See [Section 7.14.14.2.4, “Result”](7-14-14-category-measurement.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Ergebnis "7.14.14.2.4. Result").

###### <a id="d4e22091"></a>7.14.14.6.3. Tolerance

See [Section 7.14.14.2.5, “Tolerance”](7-14-14-category-measurement.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Toleranz "7.14.14.2.5. Tolerance").

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Messen_Temperatur"></a>7.14.14.7. Action Element - Measure Temperature

The "Measure temperature" action element can be seen in [Figure 446, “Measure Temperature Action Element”](7-14-14-category-measurement.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Messen_Temperatur "Figure 446. Measure Temperature Action Element").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Messen_Temperatur"></a>

![Image: measure temperature action element](images/fte_arbeitsflaeche_dialog_messen_temperatur.png)

**Figure 446. Measure Temperature Action Element**

Using this command, you can preset the multimeter integrated in the tester for the temperature measurements using a selected sensor type and read back a numerical measurement result in a variable for further processing.

The possible settings reflect the functionality

- Multimeter, temperature

.

###### <a id="d4e22113"></a>7.14.14.7.1. Measuring channel

A vehicle test point is available. See [Section 7.14.14.1.4, “Vehicle Test Point”](7-14-14-category-measurement.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.FzgTestpunkt "7.14.14.1.4. Vehicle Test Point").

Using the "Measuring channel output" button, you can control if the measuring channel text should be output on the tester.

###### <a id="d4e22118"></a>7.14.14.7.2. Result

See [Section 7.14.14.2.4, “Result”](7-14-14-category-measurement.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Ergebnis "7.14.14.2.4. Result").

###### <a id="d4e22122"></a>7.14.14.7.3. Tolerance

See [Section 7.14.14.2.5, “Tolerance”](7-14-14-category-measurement.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Toleranz "7.14.14.2.5. Tolerance").

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Osziloskop"></a>7.14.14.8. Action Element - Oscilloscope

The "Oscilloscope" action element can be seen in [Figure 447, “Oscilloscope Action Element”](7-14-14-category-measurement.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Osziloskop "Figure 447. Oscilloscope Action Element").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Osziloskop"></a>

![Image: oscilloscope action element](images/fte_arbeitsflaeche_dialog_oszilloskop.png)

**Figure 447. Oscilloscope Action Element**

The action element contains an oscilloscope measuring command.

Using this command, you can preset the oscilloscope integrated in the tester, generate an adaptation command to the user to connect the measuring cable, display an oscillogram on the touchscreen, and read back measured values for further processing. The measurement can also take place without a display on the touchscreen.

###### <a id="d4e22140"></a>7.14.14.8.1. Mode

The settings for the operating mode for the measuring mode and sampling rate are located in the "Mode" area (see VAS 5051x operating instructions, technical data).

Various measuring points can be selected depending on the mode.

<a id="d4e22144"></a>

<table border="1" summary="Modes"><colgroup><col/><col/><col/></colgroup><thead><tr bgcolor="#EEEEEE"><th align="left">Mode</th><th align="left">Channel A</th><th align="left">Channel B</th></tr></thead><tbody><tr><td align="left">Auto Setup</td><td align="left">DSO, KV sensor, current probe</td><td align="left">DSO, KV sensor, current probe</td></tr><tr><td align="left">Auto Level</td><td align="left">DSO, KV sensor, current probe</td><td align="left">DSO, KV sensor, current probe</td></tr><tr><td align="left">Auto</td><td align="left">Pressure sensor, temperature sensor</td><td align="left">Pressure sensor, temperature sensor</td></tr><tr><td align="left">Normal</td><td align="left">DSO, KV sensor, current probe, pressure sensor, temperature sensor</td><td align="left">DSO, KV sensor, current probe, pressure sensor, temperature sensor</td></tr><tr><td align="left">Single</td><td align="left">DSO, KV sensor, current probe, pressure sensor, temperature sensor</td><td align="left">DSO, KV sensor, current probe, pressure sensor, temperature sensor</td></tr><tr><td align="left">Write mode</td><td align="left">DSO, KV sensor, current probe, pressure sensor, temperature sensor</td><td align="left">DSO, KV sensor, current probe, pressure sensor, temperature sensor</td></tr><tr><td align="left">Default measurement</td><td align="left">DSO, KV sensor, current probe, pressure sensor, temperature sensor</td><td align="left">DSO, KV sensor, current probe, pressure sensor, temperature sensor</td></tr><tr><td align="left">EDIABAS combination measurement</td><td align="left">DSO, pressure sensor, URD, Ecukom</td><td align="left">Ecukom</td></tr><tr><td align="left">ASAM combination measurement</td><td align="left">DSO, pressure sensor, URD, ASAM Ecukom</td><td align="left">ASAM Ecukom</td></tr></tbody></table>

**Table 98. Modes**

###### <a id="d4e22189"></a>7.14.14.8.2. Measuring Channel A and B

Parameters can be set for up to two measuring channels in the measuring channel tabs in the center of the dialog. If measuring channel B should be included in the measurement, the field **Channel B activated** must be selected. The tab for measuring channel B will appear after that. The measuring channels can have parameters set separately. Measuring channel A is pre-selected when you enter the dialog.

The mode is set for the oscilloscope. The table below describes the modes in regard to the input cable or sensors.

<a id="d4e22194"></a>

<table border="1" summary="Settings for the Trigger Channel"><colgroup><col align="left"/><col align="left"/></colgroup><thead><tr bgcolor="#EEEEEE"><th align="left">Channel</th><th align="left">Explanations</th></tr></thead><tbody><tr><td align="left">DSO1 cable</td><td align="left">If the input is through the DSO1 cable (red probe), the connection point must be specified here (normal case).</td></tr><tr><td align="left">DSO2 cable</td><td align="left">If the input is through the DSO2 cable (red probe), the connection point must be specified here.</td></tr><tr><td align="left">DSO cable (-)</td><td align="left">If the input is through the DSO1 or DSO2 cable, the measuring cable (negative, black probe) must always be specified.</td></tr><tr><td align="left">KV sensor</td><td align="left">If the input signal is measured using the KV sensor, the specification about the connection point must be entered here.</td></tr><tr><td align="left">Current clamp</td><td align="left">If the input signal is measured using a 50 A current probe (current probe number 1), a 100 A, a 500 A, or an 1800 A, the specification about the connection point must be given here.</td></tr><tr><td align="left">Signal Coupling</td><td align="left">AC: only alternating current signals are measured. DC: alternating and direct current signals are measured. HF: a high pass (10 kHz) in the input circuit is toggled. This filters out the low-frequency interference signals. LF: a low pass (100 Hz) in the input circuit is toggled. This filters out the high-frequency interference signals.</td></tr><tr><td align="left">Pressure sensor</td><td align="left">If the signal comes through the pressure sensor cable, the sensor type used and the connection point must be specified.</td></tr><tr><td align="left">Temperature sensor</td><td align="left">If the temperature sensor should be used, specify the measurement location.</td></tr><tr><td align="left">Trigger clamp</td><td align="left">If the trigger clamp is used, the connection point, such as ignition cable cylinder 1, must be specified here.</td></tr><tr><td align="left">Trigger slope</td><td align="left">Select the trigger slope here, meaning the trigger occurs when the input curve decreases or increases.</td></tr><tr><td align="left">Trigger level</td><td align="left">The trigger level cannot be used in the "Auto Setup" or "Auto Level" mode. It is at 0 by default in the other modes. Depending on the input, the trigger can be specified in the positive measuring range or the negative.</td></tr><tr><td align="left">Delay</td><td align="left">The trigger delay can be specified here as a positive or negative time value. This causes the trigger to be earlier or later compared to the center point and results in a horizontal move of the curve.</td></tr></tbody></table>

**Table 99. Settings for the Trigger Channel**

  

**Sampling rate**

The following context applies when setting the sampling rate: sampling rate [Hz] = time per division x 10 x 500.

**Measurement range**

The measuring range setting is not based on the volt/division tester setting, but rather on the total measuring range.

**DSO cable measuring channel**

The signal can be routed through the DSO1 or DSO2 measuring cable that is to be specified to measuring channel A. Generally, the signal for channel A is input through the DSO1 cable.

**Vehicle Test Point**

See [Section 7.14.14.1.4, “Vehicle Test Point”](7-14-14-category-measurement.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.FzgTestpunkt "7.14.14.1.4. Vehicle Test Point").

**Measurement range**

The measuring range can also be specified in the "Auto Setup" and "Write Mode" modes by making a selection using the selection field or an entry. The value entered is based on the measuring range that can be displayed and not on the "Division" unit.

**DSO Minmax**

Using the extreme value function checkbox, you can switch channels A and B individually to detect peak values (extreme values), for example with ignition signals. To minimize the effect of disturbances on the result, values that change continually such as sine curves or lambda sensor signals should not have the parameters set with the min/max function.

Normally, 500 results values per channel is enough to display the recorded measured values in a graphic and evaluate them, because a line in the screen can have this exact number of image points. Because the tester always records the measured values with the maximum sampling rate, interim values are determined on the 500 images points in the screen display. If actual extreme values are delivered and not diminished by the mean value algorithm, you can use the extreme value function to record one or both extreme values and to store them. The other values in the plotted curve are then developed from the recorded interim values using a special algorithm.

Measured values are stored in a field variable independently because all results (curve values, extreme values) are always stored.

**Signal Coupling**

Select here if the input signal should be measured as an AC or DC signal. With "AC", only alternating current signals are measured. With "DC", direct and alternating current signals are measured.

**KV sensor measuring channel**

If measuring with the KV sensor, the "KV sensor" option must be set. The adaptation command only takes place for one measuring point. The adjustable options correspond to those for the "DSO cable measuring channel".

**Current probe measuring channel**

Allocation of the current probe numbers: the adjustable options "DSO minmax" are described in more detail above. Measuring with a current probe is possible for all modes except the combination measurement.

**Pressure sensor measuring channel**

When using this input, one of the four selectable pressure sensors and therefore the measuring range must be specified. The tester detects the sensor type based on a coding resistor. If the programming and the coding resistor do not match, an error message appears when the function test runs.

The measurement is done in write mode. When programming, note the unit in which the measurement result should be displayed (bar or lb/in²).

**Temperature measuring channel**

When using one of the two temperature sensors as an input to channel A, the "slow" option can be specified for measuring fluids, and "fast" for measuring gases. The specification is based on the sensor type. The tester detects the sensor type based on a coding resistor. If the programming and the coding resistor do not match, an error message appears when the function test runs.

There is only one measuring range for temperature measurement (-20 to +200 °C). When programming, note the unit in which the measurement result should be displayed (°C or °F).

**U/R/D measuring channel**

The U/R/D cable can only be used in conjunction with the combination measurement. The adjustable options correspond to the settings for the "DSO cable measuring channel".

**Ecukom measuring channel**

When the "Ecukom" option is selected, values such as the temperature value, can serve as the input for the oscilloscope. A similar measurement can be made via U/R/D or DSO cable in parallel. The measurements for both channels run in cycles, so that an allocation of the values is possible.

The Ecukom channel parameters are set using the "Selection" button.

The settings largely match the settings in the Ecukom command. See also [Section 7.14.15.1, “Action Element - Ecukom”](7-14-15-category-ecukom.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_EcuKom.EcuKom "7.14.15.1. Action Element - Ecukom").

###### <a id="d4e22287"></a>7.14.14.8.3. Trigger Channel

A shared trigger channel for the measurement can be defined in this area. The "Edit" button opens the dialog for setting the trigger channel.

The display field shows a summary of the settings for the trigger channel.

###### <a id="d4e22291"></a>7.14.14.8.4. Result

The measuring curve consists of 500 individual measurement results per channel. They can be transferred to a variable field, such as osz[1503]. The required size and the organization of the variable field (arrays) is defined.

The following table shows the display of the results in the field variables and their sizes to be defined. The name "osz[...]" was selected here for the field variable and the numerical values are examples.

"Variable" button: using the "Variable" button, you can enter a field variable of the "Real" type that can record the curves and the min and max values for evaluation later. The size of the field variable depends on the following factors:

- Number of measuring channels used
- Specified curve output
- Short response ("short" parameter set)

<a id="d4e22304"></a>

<table border="1" summary="Division of Field Variables for Oscilloscope Measured Values (Curve Values)"><colgroup><col align="left"/><col align="left"/><col align="left"/><col align="left"/></colgroup><thead><tr bgcolor="#EEEEEE"><th align="left"> </th><th align="left">Field variable</th><th align="left">Content</th><th align="left">Result/comment</th></tr></thead><tbody><tr><td align="left">Channel A (always set)</td><td align="left">osz[0]</td><td align="left">500</td><td align="left">Number of curve values.</td></tr><tr><td align="left"> </td><td align="left">osz[1] through osz[500]</td><td align="left">10.513 through 1.05</td><td align="left">The 500 curve values are in volts.</td></tr><tr><td align="left">Channel B (if active)</td><td align="left">osz[501]</td><td align="left">0 or 500</td><td align="left">Number of curve values (not values set or 500).</td></tr><tr><td align="left"> </td><td align="left">osz[502] through osz[1001]</td><td align="left">-4.99 through 5.39</td><td align="left">The 500 curve values are in volts.</td></tr><tr><td align="left">Specified curve (if active)</td><td align="left">osz[1002]</td><td align="left">0 or 500</td><td align="left">Number of curve values (not values set or 500).</td></tr><tr><td align="left"> </td><td align="left">osz[1003] through osz[1502]</td><td align="left">-5.15 through 5.30</td><td align="left">The 500 curve values are in volts.</td></tr></tbody></table>

**Table 100. Division of Field Variables for Oscilloscope Measured Values (Curve Values)**

<a id="d4e22349"></a>

<table border="1" summary="Division of Field Variables for Oscilloscope Measured Values (Extreme values) for Sample Values from Table 12-16"><colgroup><col align="left"/><col align="left"/><col align="left"/><col align="left"/></colgroup><thead><tr bgcolor="#EEEEEE"><th align="left"> </th><th align="left">Field variable</th><th align="left">Content/value</th><th align="left">Result/comment</th></tr></thead><tbody><tr><td align="left">Minimum channel A (always set)</td><td align="left">osz[1503]</td><td align="left"> </td><td align="left">Time in s relative to trigger time point</td></tr><tr><td align="left"> </td><td align="left">osz[1504]</td><td align="left">1:05 AM</td><td align="left">Curve value in volts.</td></tr><tr><td align="left">Maximum channel A</td><td align="left">osz[1505]</td><td align="left"> </td><td align="left">Time in s relative to trigger time point</td></tr><tr><td align="left"> </td><td align="left">osz[1506]</td><td align="left">10:51 AM</td><td align="left">Curve value in volts.</td></tr><tr><td align="left">Minimum channel B (if active)</td><td align="left">osz[1507]</td><td align="left"> </td><td align="left">Time in s relative to trigger time point</td></tr><tr><td align="left"> </td><td align="left">osz[1508]</td><td align="left">-4.99</td><td align="left">Curve value in volts.</td></tr><tr><td align="left">Maximum channel B</td><td align="left">osz[1509]</td><td align="left"> </td><td align="left">Time in s relative to trigger time point</td></tr><tr><td align="left"> </td><td align="left">osz[1510]</td><td align="left">5:39 AM</td><td align="left">Curve value in volts.</td></tr></tbody></table>

**Table 101. Division of Field Variables for Oscilloscope Measured Values (Extreme values) for Sample Values from Table 12-16**

The extreme values are always included. If the "short" parameter set, no curve values are delivered (see below).

The following minimum lengths are yielded for the variable field. Note that the first value is called osz[0] and not osz[1].

<a id="d4e22406"></a>

<table border="1" summary="Sample Results"><colgroup><col align="left"/><col align="left"/><col align="left"/></colgroup><thead><tr bgcolor="#EEEEEE"><th align="left">Required variable lengths</th><th align="left">Measuring channel A (without channel B)</th><th align="left">Measuring channel A + B (channel B switched on)</th></tr></thead><tbody><tr><td align="left">Result without "short" and without specified curve</td><td align="left">507</td><td align="left">1011</td></tr><tr><td align="left">Result without "short" with specified curve</td><td align="left">1007</td><td align="left">1511</td></tr><tr><td align="left">Result with "short"</td><td align="left">4</td><td align="left">8</td></tr></tbody></table>

**Table 102. Sample Results**

**Output**

Mark this checkbox if the measurement should be visible to the user on the touchscreen. In this case, the adaptation notes for the measuring cable are also visible. If this checkbox is not marked (NODISPLAY mode), you must program the adaptation notes for the measuring cable separately using the "Measuring channel" command. See also [Section 7.14.14.1, “Action Element - Measuring Channel”](7-14-14-category-measurement.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Messkanal "7.14.14.1. Action Element - Measuring Channel").

**Short**

If the "short" checkbox is selected in the results field, only extreme values and the associated time values for the measuring channels used will be given as a result. The "short" specification is only applied when a results variable is set.

**A/B curve shift**

You can move the zero line in each curve (A, B, specified curve) up or down if necessary. You can use a variable or a keyword for this. The numerical value to be applied moves the curve vertically in volt units by default. However, you can also define the unit for the movement as 10-^3 (mV) or as 10^3 (kV) using the "mV, "V" and "kV" option fields. Use the "bar" option for pressure measurements, and use the "degreeC" unit for temperature measurements.

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Block_Hochvolt"></a>7.14.14.9. Action Element - High Voltage Block

The "High voltage block" action element can be seen in [Figure 448, “High Voltage Block Action Element”](7-14-14-category-measurement.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Block_Hochvolt "Figure 448. High Voltage Block Action Element").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Block_Hochvolt"></a>

![Image: high voltage block action element](images/fte_arbeitsflaeche_dialog_block_hochvolt.png)

**Figure 448. High Voltage Block Action Element**

Developments in the field of electric mobility with hybrid and electric vehicles create new requirements for measuring equipment for maintenance and repair of these vehicles in workshops. The voltage currently used for hybrid vehicles is 288V. For safety reasons, this voltage cannot be measured using standard measuring equipment for vehicles with a 12V vehicle electrical system. Furthermore, specific legislation regarding the use of the usual measuring equipment is insufficient. The high-voltage measurement module was developed for this reason. The voltage, resistances, insulation resistances, diodes, and potential equalization can be measured in a vehicle with high-voltage technology using this high-voltage measurement module.

The high voltage block action element initiates a hybrid-specific procedure. The measuring mode for the process area is set with this command. Preliminary outputs for displaying measuring channels or additional texts can also be defined.

###### <a id="d4e22454"></a>7.14.14.9.1. Measuring mode

The following measuring modes are available for selection:

<a id="d4e22457"></a>

<table border="1" summary="Listing of High-Voltage Measuring Modes"><colgroup><col align="left"/><col align="left"/></colgroup><thead><tr bgcolor="#EEEEEE"><th align="left">Measuring mode</th><th align="left">Description</th></tr></thead><tbody><tr><td align="left">Voltage measurement</td><td align="left">
<p>A voltage measurement is initialized with the mode. The mode can be run as a converging or non-converging measurement. "Converging" is set by default for measured value monitoring. An internal resistance (in Ohms) is also specified.</p>
<p>When the "converging voltage measurement" measuring type is selected and run in GFF, the high-voltage measuring module controls the measuring procedure. The measured value is read multiple times until a stable measured value is found or the measurement converges.</p>
<p>With the "non-converging" selection for measured value monitoring that is run in GFF, the user specifies when the measurement starts by pressing the button on the test probe and when it ends by releasing the button. This means that the user controls the measurement in this case and not the high-voltage measuring module.</p>
<p>An internal resistance (in ohms) is specified using the selection. The selection can be between 15 Mohm and 204 kohm. The default value is 15 Mohm. To repeat test sequences, you can enter the internal resistance also as a variable or code. The value for the internal resistance may also either be 15 Mohm or 204 kohm here. Random value input is not supported at this location. The internal resistance can only be modified when the voltage measurement mode is selected. If another mode is selected, then the interface elements for the test voltage are deactivated.</p>
<p>To avoid incorrect measurements, the contact can be displayed with the "Contact check" checkbox. If the contact check is selected, only "converging" is available for the type of voltage measurement. The value "15 Mohm" is also preselected for the internal resistance.</p>
</td></tr><tr><td align="left">Resistance measurement</td><td align="left">
<p>A resistance measurement is initialized with the mode. The mode can be run as a converging or non-converging measurement. The "converging resistance measurement" is selected by default.</p>
<p>When the "converging resistance measurement" measuring type is selected and run in GFF, the high-voltage measuring module controls the measuring procedure. The measured value is read multiple times until a stable measured value is found or the measurement converges.</p>
<p>With the selection for "non-converging resistance measurement" that is run in GFF, the user specifies when the measurement starts by pressing the button on the test probe, and when it ends by releasing the button. This means that the user controls the measurement in this case and not the high-voltage measuring module.</p>
<p>There is the option to block the calibration. There is a checkbox with the label "Block calibration" for this under the resistance measurement next to the measured value monitoring. This checkbox is not enabled by default.</p>
</td></tr><tr><td align="left">Diode test</td><td align="left">A diode measurement is initialized with this mode. No other parameters are specified.</td></tr><tr><td align="left">High voltage isolation measurement</td><td align="left">
<p>A high-voltage isolation measurement is initialized with the mode. A test voltage (in V) is specified. The selection allows voltage values from the range (250V ≤ x ≤ 1000V). 250V is preset as the default value.</p>
<p>As an alternative to manual selection, the test voltage can be controlled using a variable or a keyword at runtime. The variable or keyword must be declared/defined as a whole number value. When specifying a variable/keyword, you must ensure that the upper value range is maintained at runtime.</p>
<p>The test voltage can only be modified when the high-voltage isolation measurement mode is selected. If another mode is selected, then the interface elements for the test voltage are deactivated.</p>
</td></tr><tr><td align="left">High voltage isolation measurement conforming to SAE J1766</td><td align="left">No additional specifications are needed when the high-voltage isolation measurement according to SAE J1766 is selected.</td></tr><tr><td align="left">Potential equalization measurement</td><td align="left">
<p>The additional specification of a test current is necessary when selecting the potential equalization measurement mode. Current values for the test current can be selected.</p>
<p>The test current can be set within the range of 200mA to 1000mA (in increments of 100mA). To repeat test sequences, you can enter the test current also as a variable or code. It is possible to enter any value in the mA section. The test current can only be modified when the potential equalization measurement mode is selected. If another mode is selected, then the interface elements for the test current are deactivated.</p>
<p>The "Block calibration" checkbox offers a parameterization option to control a calibration. If this checkbox is selected, the calibration is blocked (this setting can be applied when performing a 4-terminal measurement). If this checkbox is not selected, a calibration will be performed (this setting can be applied to perform a 2-terminal measurement).</p>
</td></tr><tr><td align="left">Self-test</td><td align="left">Additional specifications are not needed when self-test mode is selected.</td></tr><tr><td align="left">Unit safety test</td><td align="left">Additional specifications are not needed when the device safety test mode is selected.</td></tr></tbody></table>

**Table 103. Listing of High-Voltage Measuring Modes**

  

Additional outputs for measuring channels and additional texts can be specified for all measuring modes except isolation measurement according to SAE J1766, self-test, and device safety test. These texts are displayed before the selected measuring mode is initialized.

###### <a id="d4e22507"></a>7.14.14.9.2. Measuring channel

You can access the **Vehicle test point** dialog in the **Measuring channel** area and make a selection using the selection menu. The vehicle test point for the high-voltage test probes + and - must be selected here. When the **Measuring channel output** is selected, the measuring channel can be read before initializing the selected measuring mode.

###### <a id="d4e22513"></a>7.14.14.9.3. Additional text

See [Section 7.14.14.2.4.2, “Additional text”](7-14-14-category-measurement.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Zusatztext "7.14.14.2.4.2. Additional text").

The text is read out before initializing the selected measuring mode.

###### <a id="d4e22518"></a>7.14.14.9.4. Probe Tip Additional Text

A text for operating the probe tip button can be defined in the **Probe tip additional text** area. This text is displayed in a measuring equipment process window directly before a measurement.

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Break_Hochvolt"></a>7.14.14.10. Action Element - High-Voltage Break

The action element breaks at a specified high-voltage range. There is no other dialog for configuration.

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Messdaten_Hochvolt"></a>7.14.14.11. Action Element - High-Voltage Measurement Data

The "High-voltage measurement data" action element can be seen in [Figure 449, “High-Voltage Measurement Data Action Element”](7-14-14-category-measurement.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Messdaten_Hochvolt "Figure 449. High-Voltage Measurement Data Action Element").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Messung.Messdaten_Hochvolt"></a>

![Image: high-voltage measurement data action element](images/fte_arbeitsflaeche_dialog_messdaten_hochvolt.png)

**Figure 449. High-Voltage Measurement Data Action Element**

The action element allows you to check a measuring status, measured value, error code, or additional information. The action element saves the result in the assigned variables.

###### <a id="d4e22538"></a>7.14.14.11.1. Measuring status:

Depending on the measuring mode set in the high-voltage block, the dialog above may display differently and may offer reduced configuration options:

<a id="d4e22542"></a>

<table border="1" summary="Selection Options for High-Voltage Measurement Data"><colgroup><col/><col/></colgroup><thead><tr bgcolor="#EEEEEE"><th>Selection option</th><th>Description</th></tr></thead><tbody><tr><td>Check measured value</td><td>A measured value can be selected in all modes except self-test and device safety test. The corresponding measured value is read out for each mode. A voltage value (in volts) is measured for the voltage measurement and diode test. For the resistance measurement, high-voltage isolation measurement, high-voltage isolation measurement according to SAE J1766, and potential equalization measurement, a resistance value (in ohms) is measured.</td></tr><tr><td>Checking additional information</td><td>Parameters can be set for the additional information in the diode test, voltage and insulation measurement mode. For the diode test mode, the additional information denotes the result of the continuity test for the diodes.</td></tr><tr><td>Check measuring status</td><td>The measuring status can be checked in all modes. It should always be read out in a high-voltage block in order to check if the initialization of the measurement was performed correctly.</td></tr><tr><td>Check error code</td><td>An error code can also be checked in addition to the measuring status. This denotes the error status of the measuring module and can be used as information for the error correction that will be followed.</td></tr></tbody></table>

**Table 104. Selection Options for High-Voltage Measurement Data**

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-14-13-category-process.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="7-14-function-test-editor.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="7-14-15-category-ecukom.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">7.14.13. Category - Process </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 7.14.15. Category - Ecukom</td></tr></table>
