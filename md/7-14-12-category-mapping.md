[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md) > [7.14. Function Test Editor](7-14-function-test-editor.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.14.12. Category - Mapping</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-14-11-category-definition.md">Prev</a> </td><th align="center" width="60%">7.14. Function Test Editor</th><td align="right" width="20%"> <a accesskey="n" href="7-14-13-category-process.md">Next</a></td></tr></table>

---

#### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Zuordnung"></a>7.14.12. Category - Mapping

The **Mapping** category contains two elements:

- [Section 7.14.12.1, “Action Element - Expression”](7-14-12-category-mapping.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Zuordnung.Ausdruck "7.14.12.1. Action Element - Expression")
- [Section 7.14.12.2, “Action Element - Set Status”](7-14-12-category-mapping.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Zuordnung.Setze_Zustand "7.14.12.2. Action Element - Set Status")

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Zuordnung.Ausdruck"></a>7.14.12.1. Action Element - Expression

The "Expression" action element can be seen in [Figure 409, “Action Element - Expression”](7-14-12-category-mapping.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Zuordnung.Ausdruck "Figure 409. Action Element - Expression").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Zuordnung.Ausdruck"></a>

![Image: Expression action element](images/fte_arbeitsflaeche_dialog_ausdruck.png)

**Figure 409. Action Element - Expression**

This action element creates mathematical, logical, or alphanumeric (string) expressions. The result is stored in a variable that must be specified in the corresponding input field.

###### <a id="d4e17740"></a>7.14.12.1.1. Result

The variable in which the mapping result should be stored must be specified in the results field. Variables can be added using a button (see [Section 7.14.6, “Using Variables”](7-14-6-using-variables.md "7.14.6. Using Variables")).

###### <a id="d4e17744"></a>7.14.12.1.2. Mapping

The value of the mapping is found under Mapping. The value can consist of a single number, a string, or a formula. The term "Mapping" corresponds to the equals sign. You can input values directly in the mapping field as well as variables and keywords. Various content can be added using the buttons below the allocation.

###### <a id="ausdruck.textbibliothek"></a>7.14.12.1.3. Text Library

Texts from the text library can be pasted into a printout using the **Text library** button. Using the search field in the open selection dialog, the desired text can be searched for and pasted by double clicking on it.

###### <a id="d4e17751"></a>7.14.12.1.4. From ODX

See [Section 7.14.11.1.1.4.4, “From ODX”](7-14-11-category-definition.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Definition.Asam_Mux_Auswahl "7.14.11.1.1.4.4. From ODX").

###### <a id="d4e17755"></a>7.14.12.1.5. Function

You can select the desired function from a group of seven function types using the **Function** button. The mathematical functions are in the first column. The second column contains the trigonometric functions. The third column contains text and bit operations. The fourth column contains tester data. The fifth column contains the mapping of system results from the log book. The sixth column contains mapping to measuring equipment parameters and the seventh column contains the functions for control module identification.

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Zuordnung.Ausdruck_Auswahl"></a>

![Image: function selection list in dialog](images/fte_Funktion_Auswahl.png)

**Figure 410. Function Selection List in Dialog**

Expressions can also be hierarchically structured using parentheses. For example the expression "String1 CAT (String2 GETCHAR n) reads the n-te character from String2 and links it with String1.

An overview of the available functions can be found in [Section 7.14.12.3, “Functions”](7-14-12-category-mapping.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Zuordnung_Funktionen "7.14.12.3. Functions").

###### <a id="d4e17770"></a>7.14.12.1.5.1. Variable

The description for selecting variables is found in [Section 7.14.6, “Using Variables”](7-14-6-using-variables.md "7.14.6. Using Variables"). The definition of variables is found in [Section 7.14.11.1, “Action Element - Declare Variable”](7-14-11-category-definition.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Definition.Deklariere_Variablen "7.14.11.1. Action Element - Declare Variable").

###### <a id="d4e17775"></a>7.14.12.1.5.2. Keyword

The description for selecting keywords is found in [Section 7.14.6, “Using Variables”](7-14-6-using-variables.md "7.14.6. Using Variables"). The definition of keywords is found in [Section 7.14.11.4, “Action Element - Define Keyword”](7-14-11-category-definition.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Definition.Definiere_Kennwort "7.14.11.4. Action Element - Define Keyword").

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Zuordnung.Setze_Zustand"></a>7.14.12.2. Action Element - Set Status

The "Set Status" action element can be seen in [Figure 411, “Set Status”](7-14-12-category-mapping.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Zuordnung.Setze_Zustand "Figure 411. Set Status").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Zuordnung.Setze_Zustand"></a>

![Image: Zuordnung.Setze_Zustand (allocation.set_status) action element](images/fte_arbeitsflaeche_zuordnung_setze_zustand.png)

**Figure 411. Set Status**

You can use this command to specify a test status, assign a value to the "Select" system variable (here: "SELECT"), enter one or more objects into the Suspicion or OK list, pre-select the "VIN" system variable, or change system names in the equipment network from OK to NOT OK and thus automate the vehicle identification process.

###### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Zuordnung.Setze_Zustand.Testerzustand"></a>7.14.12.2.1. Tester Status

For tester status, you can select from OK, NOT OK, Unknown, "Diagnosis created, component repaired" and Select. One of the four possible test statuses can be generated for the current test step using the first four control fields. The following table lists these test statuses:

<a id="d4e17797"></a>

<table border="1" summary="Test Statuses"><colgroup><col align="left"/><col align="left"/><col align="left"/><col align="left"/></colgroup><thead><tr bgcolor="#EEEEEE"><th align="left">Test status</th><th align="left">Interpreter</th><th align="left">Test plan</th><th align="left">Meaning</th></tr></thead><tbody><tr><td align="left">OK</td><td align="left">OK</td><td align="left"><span class="inlinemediaobject"><img src="images/fte_ok.png"/></span></td><td align="left">In the function test: in the test step: continue with test status "OK", exit the test step using the OK exit. End of the function test: an "OK" appears in the test plan, the diagnostic object is OK. In the traversal test: the object is changed from "unknown" to "OK". This matches its manual selection.</td></tr><tr><td align="left">NOT OK</td><td align="left">NOT OK</td><td align="left"><span class="inlinemediaobject"><img src="images/fte_nok.png"/></span></td><td align="left">In the function test: in the test step: continue with test status "NOT OK", exit the test step using the NOT OK exit. End of the function test: an "X" appears in the test plan, the diagnostic object is not OK. In traversal test: not applicable.</td></tr><tr><td align="left">Unknown</td><td align="left">UB</td><td align="left"><span class="inlinemediaobject"><img src="images/fte_fragezeichen.png"/></span></td><td align="left">In the function test: in the test step: continue with test status "UNKNOWN", exit the test step using the UNKNOWN exit. End of the function test: a "?" appears in the test plan, the test status of the diagnostic object cannot be determined. In the traversal test: verification that the object must still be selected manually. This case occurs if a traversal test that prevents subsequent objects or variants is linked with a vehicle features object. However, the nodes themselves should be provided for selection. In this case, the traversal test must be ended with "Unknown".</td></tr><tr><td align="left">Diagnosis prepared and component repaired</td><td align="left">D</td><td align="left"><span class="inlinemediaobject"><img src="images/fte_repariert.png"/></span></td><td align="left">Only in the function test: in the test step: continue with test status "D", exit the test step using the OK exit. End of the function test: the message "Should the repair be checked?" appears. If you confirm "Yes", the function test is repeated in verification mode. You can check the "Verification" status at the beginning of a function test and use an "If" command (= OK) (see also <a class="xref" href="7-14-13-category-process.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Ablauf.IF-Anweisung" title="7.14.13.1. Action Element - IF Command">Section 7.14.13.1, “Action Element - IF Command”</a>), for example to go to a short test that checks the repair. The user will generally perform a road test after a repair and then return to Guided Fault Finding. The vehicle system test will show if the repair was successful. If the message is closed with "No", "OK!" appears in the test plan. (Quality: "Verification not required - certainly OK")</td></tr></tbody></table>

**Table 79. Test Statuses**

The test status or test step status can be evaluated using the following commands: “If”, “While”, “While NOT”, “Switch/Case”. See also [Section 7.14.13, “Category - Process”](7-14-13-category-process.md "7.14.13. Category - Process").

###### <a id="d4e17846"></a>7.14.12.2.1.1. Select

Using this setting, you can pre-select the "Select" system variable, for example to go to "Select" from a test step. The system variable can also be evaluated in a test step, for example using “Switch/Case”.

In the set state, the value of “Select” can also be set to “-1” or “0”, which means that the test select is exited or called again with Break. These options are available in the following dialogs: “If”, “While”, “While NOT”, “Switch/Case”.

###### <a id="d4e17850"></a>7.14.12.2.2. Lists

When lists are used, suspect or OK lists are determined. There is also the option to determine implicitly OK lists for test programs (see [Figure 412, “Set status - Listen”](7-14-12-category-mapping.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Zuordnung.Setze_Zustand.Listen "Figure 412. Set status - Listen")).

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Zuordnung.Setze_Zustand.Listen"></a>

![Image: Zuordnung.Setze_Zustand (allocation.set_status) action element](images/fte_arbeitsflaeche_zuordnung_setze_zustand_listen.png)

**Figure 412. Set status - Listen**

###### <a id="d4e17862"></a>7.14.12.2.2.1. Suspicion list (dynamic)

The diagnostic objects from a test step can be defined as suspicious in a suspicion list. Suspicions cause the specified diagnostic objects to be re-entered in the test plan under the diagnostic object that is currently being tested, for example:

OK G39 - Heated Oxygen Sensor- J361 - adapt control module to the throttle position actuator and EGR valve If there are entries in the "AFTER-RUN" test step for the "static" suspicion list that were added regardless of the test procedure, the "dynamic" suspicion list will precede the "static" list.

###### <a id="d4e17866"></a>7.14.12.2.2.2. OK list (dynamic)

The OK list is the opposite of the suspicion list. You can only set objects to OK (using their system names) if there is no related suspicion. This function is only used in traversal tests in the equipment network (in which there is no related suspicion) in order to set an object to "OK" (which in this case means "identified"). To add the system name of a diagnostic object to the suspicion or OK list:

1. Open the diagnostic object tree that contains the suspicious diagnostic object.
2. Select the object and execute the "Mark" function using the context menu.
3. Switch back to the "Set status" command and click there on the "Copy from clipboard" symbol.
4. Click the "Add" button.

###### <a id="d4e17878"></a>7.14.12.2.2.3. Implicitly OK List

You can enter one or more functional test objects (using their system names) in the implicitly OK list (see [Figure 413, “Set Status - Implicit OK List”](7-14-12-category-mapping.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Zuordnung.Setze_Zustand_implizit.Listen "Figure 413. Set Status - Implicit OK List")).

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Zuordnung.Setze_Zustand_implizit.Listen"></a>

![Image: Zuordnung.Setze_Zustand_Implizit_IO_List action element](images/fte_arbeitsflaeche_zuordnung_setze_zustand_implizit_listen.png)

**Figure 413. Set Status - Implicit OK List**

Assigned system names are memorized for the duration of the diagnostic session and marked accordingly for test programs. Selection or entry is possible via password, variable, free text or the selection dialog.

###### <a id="d4e17891"></a>7.14.12.2.3. Vehicle Identification Number

The "VIN" system variable can be pre-selected in this location. A variable can be used for this (see [Section 7.14.6, “Using Variables”](7-14-6-using-variables.md "7.14.6. Using Variables")).

###### <a id="d4e17895"></a>7.14.12.2.4. Equipment

You can declare objects in the equipment network valid or invalid with this, and in this way control the automatic vehicle identification. The function is used in the traversal test in order to set basic features, equipment and control modules as present or not present (NOT). The data is transferred into the internal tester log book and used during the vehicle system test, for example.

The selection in the "Set status" screen with configured equipment is filled using the data fro a version and is controlled using a selection field. Each line is divided into three columns (see [Figure 414, “Set status - Equipment”](7-14-12-category-mapping.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Zuordnung.Setze_Zustand.Ausstattung "Figure 414. Set status - Equipment")).

- NOT, in order to mark excluded features
- Node type for specifying the basic features and equipment,
- System name for specifying objects in the equipment network

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Zuordnung.Setze_Zustand.Ausstattung"></a>

![Image: Zuordnung.Setze_Zustand (allocation.set_status) action element](images/fte_arbeitsflaeche_zuordnung_setze_zustand_austattung.png)

**Figure 414. Set status - Equipment**

###### <a id="d4e17915"></a>7.14.12.2.4.1. Buttons above the table

- The plus creates a new equipment identification.
- The minus deletes the equipment definition that was marked.
- The entries can be sorted using the up and down arrows.

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Zuordnung_Funktionen"></a>7.14.12.3. Functions

###### <a id="d4e17926"></a>7.14.12.3.1. Mathematical

<a id="d4e17929"></a>

<table border="1" summary="Mathematical"><colgroup><col align="left"/><col align="left"/></colgroup><thead><tr bgcolor="#EEEEEE"><th align="left">Function</th><th align="left">Description</th></tr></thead><tbody><tr><td align="left">
<p><span class="bold"><strong>a1 + a2</strong></span></p>
<p>(Double)</p>
</td><td align="left">
<p>Adds a1 and a2</p>
<p><span class="bold"><strong>Parameter</strong></span> a1 (Double)</p>
<p><span class="bold"><strong>Parameter</strong></span> a2 (Double)</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>a1 - a2</strong></span></p>
<p>(Double)</p>
</td><td align="left">
<p>Subtracts a1 and a2</p>
<p><span class="bold"><strong>Parameter</strong></span> a1 (Double)</p>
<p><span class="bold"><strong>Parameter</strong></span> a2 (Double)</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>a1 * a2</strong></span></p>
<p>(Double)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>a = 4, b = 2</p>
<p>a * b = 8</p>
</td><td align="left">
<p>Multiplies a1 and a2</p>
<p><span class="bold"><strong>Parameter</strong></span> a1 (Double)</p>
<p><span class="bold"><strong>Parameter</strong></span> a2 (Double)</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>a1 / a2</strong></span></p>
<p>(Double)</p>
</td><td align="left">
<p>Divides a1 and a2</p>
<p><span class="bold"><strong>Parameter</strong></span> a1 (Double)</p>
<p><span class="bold"><strong>Parameter</strong></span> a2 (Double)</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>a1 MOD a2</strong></span></p>
<p>(Integer)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>a = 10, b = 6</p>
<p>a MOD(b) = 4</p>
</td><td align="left">
<p>Modulo, remaining value of a from a/b division</p>
<p><span class="bold"><strong>Parameter</strong></span> a1 (Integer)</p>
<p><span class="bold"><strong>Parameter</strong></span> a2 (Integer)</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>a1 ** a2</strong></span></p>
<p>(Double)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>a = 4, b = 2</p>
<p>a ** b = 16</p>
</td><td align="left">
<p>a2-te power of a1</p>
<p><span class="bold"><strong>Parameter</strong></span> a1 (Double)</p>
<p><span class="bold"><strong>Parameter</strong></span> a2 (Double)</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>ABS (Double a1)</strong></span></p>
<p>(Double)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>a = -2.5</p>
<p>ABS(a) = 2.5</p>
</td><td align="left">
<p>Sum of a1</p>
<p><span class="bold"><strong>Parameter</strong></span> a1 (Double)</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>SQRT (Double a1)</strong></span></p>
<p>(Double)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>a = 64</p>
<p>SQRT(a) = 8</p>
</td><td align="left">
<p>Square root of a</p>
<p><span class="bold"><strong>Parameter</strong></span> a1 (Double)</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>EXP (Double a1)</strong></span></p>
<p>(Double)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>a = 4</p>
<p>EXP(a) = 54.598...</p>
</td><td align="left">
<p>Exponent with base a1</p>
<p><span class="bold"><strong>Parameter</strong></span> a1 (Double)</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>LN (Double a1)</strong></span></p>
<p>(Double)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>a = 54.598...</p>
<p>LN(a) = 4</p>
</td><td align="left">
<p>Logarithm with base e</p>
<p><span class="bold"><strong>Parameter</strong></span> a1 (Double)</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>LG (Double a1)</strong></span></p>
<p>(Double)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>a = 100</p>
<p>LG(a) = 2</p>
</td><td align="left">
<p>Logarithm with base 10</p>
<p><span class="bold"><strong>Parameter</strong></span> a1 (Double)</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>LD (Double a1)</strong></span></p>
<p>(Double)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>a = 16</p>
<p>LD(a) = 4</p>
</td><td align="left">
<p>Logarithm with base 2</p>
<p><span class="bold"><strong>Parameter</strong></span> a1 (Double)</p>
</td></tr></tbody></table>

**Table 80. Mathematical**

###### <a id="d4e18095"></a>7.14.12.3.2. Trigonometric

<a id="d4e18098"></a>

<table border="1" summary="Trigonometric"><colgroup><col align="left"/><col align="left"/></colgroup><thead><tr bgcolor="#EEEEEE"><th align="left">Function</th><th align="left">Description</th></tr></thead><tbody><tr><td align="left">
<p><span class="bold"><strong>SIN (Double a1)</strong></span></p>
<p>(Double)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>a = 1.57</p>
<p>SIN(a) = 1</p>
</td><td align="left">
<p>Sine calculated from radius</p>
<p><span class="bold"><strong>Parameter</strong></span> a1 (Double)</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>COS (Double a1)</strong></span></p>
<p>(Double)</p>
</td><td align="left">
<p></p>
<p><span class="bold"><strong>Parameter</strong></span> a1 (Double)</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>TAN (Double a1)</strong></span></p>
<p>(Double)</p>
</td><td align="left">
<p></p>
<p><span class="bold"><strong>Parameter</strong></span> a1 (Double)</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>ASIN (Double a1)</strong></span></p>
<p>(Double)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>a = 1</p>
<p>ASIN(a) = 1,571</p>
</td><td align="left">
<p>Arc sine (radius calculated from the sine value)</p>
<p><span class="bold"><strong>Parameter</strong></span> a1 (Double)</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>ACOS (Double a1)</strong></span></p>
<p>(Double)</p>
</td><td align="left">
<p></p>
<p><span class="bold"><strong>Parameter</strong></span> a1 (Double)</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>ATAN (Double a1)</strong></span></p>
<p>(Double)</p>
</td><td align="left">
<p></p>
<p><span class="bold"><strong>Parameter</strong></span> a1 (Double)</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>SINH (Double a1)</strong></span></p>
<p>(Double)</p>
</td><td align="left">
<p></p>
<p><span class="bold"><strong>Parameter</strong></span> a1 (Double)</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>COSH (Double a1)</strong></span></p>
<p>(Double)</p>
</td><td align="left">
<p></p>
<p><span class="bold"><strong>Parameter</strong></span> a1 (Double)</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>TANH (Double a1)</strong></span></p>
<p>(Double)</p>
</td><td align="left">
<p></p>
<p><span class="bold"><strong>Parameter</strong></span> a1 (Double)</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>ARC (Double a1)</strong></span></p>
<p>(Double)</p>
</td><td align="left">
<p></p>
<p><span class="bold"><strong>Parameter</strong></span> a1 (Double)</p>
</td></tr></tbody></table>

**Table 81. Trigonometric**

###### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Zuordnung_Funktionen.TextUndBit"></a>7.14.12.3.3. Text and bit

<a id="d4e18209"></a>

<table border="1" summary="Text and bit"><colgroup><col align="left"/><col align="left"/></colgroup><thead><tr bgcolor="#EEEEEE"><th align="left">Function</th><th align="left">Description</th></tr></thead><tbody><tr><td align="left">
<p><span class="bold"><strong>STL (String a1)</strong></span></p>
<p>(Long)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>code = "ADFDE"</p>
<p>STL(code) = 5</p>
</td><td align="left">
<p>Calculates the string length of the specified input parameter.</p>
<p><span class="bold"><strong>Parameter</strong></span> a1 (String): a string whose length should be calculated.</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>BFL (String a1)</strong></span></p>
<p>(Long)</p>
</td><td align="left">
<p>Calculates the array length of the specified input parameter.</p>
<p><span class="bold"><strong>Parameter</strong></span> a1 (String): an array whose length should be calculated.</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>a1 CAT a1</strong></span></p>
<p>(String)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>code1 = "ADFDE"code2 = "FG"</p>
<p>code1 CAT code2 = 'ADFDEFG'</p>
</td><td align="left">
<p>Text variable String1 is linked with String2.</p>
<p><span class="bold"><strong>Parameter</strong></span> a1 (String)</p>
<p><span class="bold"><strong>Parameter</strong></span> a1 (String)</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>a1 GETCHAR a2</strong></span></p>
<p>(String)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>code = "ADFDE"n = 2</p>
<p>code GETCHAR n</p>
<p>F</p>
</td><td align="left">
<p>The n-te character is read from the string variable code, 0...255; 1. Character = item 0</p>
<p><span class="bold"><strong>Parameter</strong></span> a1 (String)</p>
<p><span class="bold"><strong>Parameter</strong></span> a2 (Integer)</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>BIT_NOT (Long a1)</strong></span></p>
<p>(Long)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>a = 3</p>
<p>Bit_NOT a = -4</p>
</td><td align="left">
<p>0000 ....0011 becomes 1111 ....1100</p>
<p><span class="bold"><strong>Parameter</strong></span> a1 (Long)</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>a1 BIT_AND a2</strong></span></p>
<p>(Long)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>a = 3, b = 5</p>
<p>a Bit_AND b = 1</p>
</td><td align="left">
<p>LSB is at the left (0011 AND 0101 = 0001)</p>
<p><span class="bold"><strong>Parameter</strong></span> a1 (Long)</p>
<p><span class="bold"><strong>Parameter</strong></span> a2 (Long)</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>a1 BIT_OR a2</strong></span></p>
<p>(Long)</p>
</td><td align="left">
<p></p>
<p><span class="bold"><strong>Parameter</strong></span> a1 (Long)</p>
<p><span class="bold"><strong>Parameter</strong></span> a2 (Long)</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>a1 BIT_XOR a2</strong></span></p>
<p>(Long)</p>
</td><td align="left">
<p></p>
<p><span class="bold"><strong>Parameter</strong></span> a1 (Long)</p>
<p><span class="bold"><strong>Parameter</strong></span> a2 (Long)</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>a1 BIT_SHIFTR a2</strong></span></p>
<p>(Long)</p>
</td><td align="left">
<p></p>
<p><span class="bold"><strong>Parameter</strong></span> a1 (Long)</p>
<p><span class="bold"><strong>Parameter</strong></span> a2 (Long)</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>a1 BIT_SHIFTL a2</strong></span></p>
<p>(Long)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>a = 3, b = 2</p>
<p>a Bit_SHIFTL b = 12</p>
</td><td align="left">
<p>LSB is at the left (0011 Shift L = 1100) b = number of positions by which it will be moved</p>
<p><span class="bold"><strong>Parameter</strong></span> a1 (Long)</p>
<p><span class="bold"><strong>Parameter</strong></span> a2 (Long)</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>a1 BIT_SET a2</strong></span></p>
<p>(Long)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>a = 5</p>
<p>a Bit_SET 2 = 7</p>
</td><td align="left">
<p>0101 becomes 0111</p>
<p><span class="bold"><strong>Parameter</strong></span> a1 (Long)</p>
<p><span class="bold"><strong>Parameter</strong></span> a2 (Long)</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>a1 BIT_CLEAR a2</strong></span></p>
<p>(Long)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>a = 7</p>
<p>a Bit_CLEAR 3 = 3</p>
</td><td align="left">
<p>0111 becomes 0011</p>
<p><span class="bold"><strong>Parameter</strong></span> a1 (Long)</p>
<p><span class="bold"><strong>Parameter</strong></span> a2 (Long)</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>a1 BIT_TEST a2</strong></span></p>
<p>(Long)</p>
</td><td align="left">
<p></p>
<p><span class="bold"><strong>Parameter</strong></span> a1 (Long)</p>
<p><span class="bold"><strong>Parameter</strong></span> a2 (Long)</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>TO_BIN (Long a1)</strong></span></p>
<p>(String)</p>
</td><td align="left">
<p></p>
<p><span class="bold"><strong>Parameter</strong></span> a1 (Long)</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>TO_OCT (Long a1)</strong></span></p>
<p>(String)</p>
</td><td align="left">
<p></p>
<p><span class="bold"><strong>Parameter</strong></span> a1 (Long)</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>TO_HEX (Long a1)</strong></span></p>
<p>(String)</p>
</td><td align="left">
<p></p>
<p><span class="bold"><strong>Parameter</strong></span> a1 (Long)</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>FROM_BIN (String a1)</strong></span></p>
<p>(Long)</p>
</td><td align="left">
<p></p>
<p><span class="bold"><strong>Parameter</strong></span> a1 (String)</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>FROM_OCT (String a1)</strong></span></p>
<p>(Long)</p>
</td><td align="left">
<p></p>
<p><span class="bold"><strong>Parameter</strong></span> a1 (String)</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>FROM_HEX (String a1)</strong></span></p>
<p>(Long)</p>
</td><td align="left">
<p></p>
<p><span class="bold"><strong>Parameter</strong></span> a1 (String)</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>Base64StringParseLength (String str)</strong></span></p>
<p>(Integer)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>str = 'SGVsbG8gV29ybGQ='</p>
<p>Base64StringParseLength(str) = 11</p>
</td><td align="left">
<p></p>
<p>Calculates the number of bytes in a byte array. If characters that are not supported by Base64 are used, the method will return -1.</p>
<p><span class="bold"><strong>Parameter</strong></span> str (String)</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>Base64StringToByteArray (String str)</strong></span></p>
<p>(byte[])</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>str = 'SGVsbG8gV29ybGQ='</p>
<p>Base64StringToByteArray(str) = byte[] { 0x48, 0x65, 0x6c, 0x6c, 0x6f, 0x20, 0x57, 0x6f, 0x72, 0x6c, 0x64 }</p>
</td><td align="left">
<p></p>
<p>Converts a string of characters into a byte array. If characters that are not supported by Base64 are used, the method will return an array with length 0.</p>
<p><span class="bold"><strong>Parameter</strong></span> str (String)</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>ByteArrayToHex (byte[] a1)</strong></span></p>
<p>(String)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>a1 = byte[] { 0x48, 0x65, 0x6c, 0x6c, 0x6f, 0x20, 0x57, 0x6f, 0x72, 0x6c, 0x64 }</p>
<p>ByteArrayToHex(a1) = '48656C6C6F20576F726C64'</p>
</td><td align="left">
<p></p>
<p>Converts a byte array into a HEX string.</p>
<p><span class="bold"><strong>Parameter</strong></span> a1 (byte[])</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>ByteArrayToUtf8 (byte[] a1)</strong></span></p>
<p>(String)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>a1 = byte[] { 0xC3, 0xA4 }</p>
<p>ByteArrayToUtf8(a1) = 'ä'</p>
</td><td align="left">
<p></p>
<p>This function can be used to convert a byte array into an UTF8 string. If a byte array that is not coded as UTF-8, that is not supported by UTF-8, or that is empty is provided, the method will return an empty string with length 0.</p>
<p><span class="bold"><strong>Parameter</strong></span> a1 (byte[])</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>Utf8StringToByteArray (String str)</strong></span></p>
<p>(byte[])</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>str = 'Hello World'</p>
<p>Utf8StringToByteArray(str) = byte[]{ 0x48, 0x65, 0x6c, 0x6c, 0x6f, 0x20, 0x57, 0x6f, 0x72, 0x6c, 0x64 }.</p>
</td><td align="left">
<p></p>
<p>This function can be used to convert a UTF8 string into a byte array. If a string that is not coded as UTF8 is transferred or of the string is empty, the method returns an array with the length 0.</p>
<p><span class="bold"><strong>Parameter</strong></span> str (String)</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>HexStringToByteArray (String str)</strong></span></p>
<p>(byte[])</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>str = '48656C6C6F20576F726C64'</p>
<p>HexStringToByteArray(str) = byte[]{ 0x48, 0x65, 0x6c, 0x6c, 0x6f, 0x20, 0x57, 0x6f, 0x72, 0x6c, 0x64 }.</p>
</td><td align="left">
<p></p>
<p>This function can be used to convert a HEX string into a byte array. If a string whose format does not correspond to the HEX string is transferred or of the string is empty, the method returns an array with the length 0.</p>
<p><span class="bold"><strong>Parameter</strong></span> str (String)</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>ByteArrayToBase64 (byte[] a1)</strong></span></p>
<p>(String)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>a1 = byte[] { 0x48, 0x65, 0x6c, 0x6c, 0x6f, 0x20, 0x57, 0x6f, 0x72, 0x6c, 0x64 }</p>
<p>ByteArrayToBase64(a1) = 'SGVsbG8gV29ybGQ='</p>
</td><td align="left">
<p></p>
<p>This function can be used to convert a byte array into an Base64 string. If characters that are not supported by Base64 are used or if the byte array is empty, the method will return an empty string with length 0.</p>
<p><span class="bold"><strong>Parameter</strong></span> a1 (byte[])</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>Utf8StringParseLength (String str)</strong></span></p>
<p>(Long)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>str = 'Hello World'</p>
<p>Utf8StringParseLength(str) = 11</p>
</td><td align="left">
<p></p>
<p>This function can be used to determine the number of bytes in a UTF8 string. If characters that are not supported by UTF8 are used, the method will return -1.</p>
<p><span class="bold"><strong>Parameter</strong></span> str (String)</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>HexStringParseLength (String str)</strong></span></p>
<p>(Long)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>str = '48656C6C6F20576F726C64'</p>
<p>HexStringParseLength(str) = 11</p>
</td><td align="left">
<p></p>
<p>Using this function, the number of bytes in a HEX string can be determined.\nIf characters that are not supposed by the HEX string are used, this method will return -1.</p>
<p><span class="bold"><strong>Parameter</strong></span> str (String)</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>UUID4</strong></span></p>
<p>(String)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>UUID4 = '6a326709-fc71-457d-9741-9ef32130562e'</p>
</td><td align="left">
<p></p>
<p>A UUID4 (random) can be generated using this function.</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>UUID5 (String name)</strong></span></p>
<p>(String)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>UUID5('ftName') = 'cdc559e0-749e-5e55-aa55-285c065c1fe5'</p>
</td><td align="left">
<p></p>
<p>A name-based (SHA-1 Hash) UUID5 can be generated using this function.</p>
<p><span class="bold"><strong>Parameter</strong></span> name (string): name (optional) for generating the UUID. If no parameter is specified, the system name of the respective function test will be used automatically.</p>
</td></tr></tbody></table>

**Table 82. Text and bit**

###### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Ablauf.Ausdruck.Funktionen.Testerdaten"></a>7.14.12.3.4. Tester data

<a id="d4e18596"></a>

<table border="1" summary="Tester data"><colgroup><col align="left"/><col align="left"/></colgroup><thead><tr bgcolor="#EEEEEE"><th align="left">Function</th><th align="left">Description</th></tr></thead><tbody><tr><td align="left">
<p><span class="bold"><strong>PIN15_STATE</strong></span></p>
<p>(Integer)</p>
</td><td align="left">
<p>Delivers the PIN 15 status:</p>
<p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>1: connected</p>
</li><li>
<p>0: not connected</p>
</li><li>
<p>-1: unknown</p>
</li></ul></div><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>PIN30_STATE</strong></span></p>
<p>(Integer)</p>
</td><td align="left">
<p>Delivers the PIN 30 status:</p>
<p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>1: connected</p>
</li><li>
<p>0: not connected</p>
</li><li>
<p>-1: unknown</p>
</li></ul></div><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>DEALERCODE</strong></span></p>
<p>(String)</p>
<p><span class="bold"><strong>Example:</strong></span> DEALERCODE = '12345'</p>
</td><td align="left">
<p>5-digit dealer number that is stored in the tester during initial setup.</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>DEVICE</strong></span></p>
<p>(String)</p>
<p><span class="bold"><strong>Example:</strong></span> DEVICE = '12345' (z. B. VAS 5051)</p>
</td><td align="left">
<p>5-digit device number. The number areas are set at the factory for VAS 505x testers (see /1/ through /5/ of the "Setup" chapter).</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>DEVICETYPE</strong></span></p>
<p>(String)</p>
<p><span class="bold"><strong>Example:</strong></span> DEVICETYPE = for example 'VAS5051', 'VAS5051B'</p>
</td><td align="left">
<p>Provides the tester type as a string. In the function test, different instructions for the VAS 5051 or VAS 5051B may be used due to differing measuring equipment after evaluating the DEVICETYPE.</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>IMPORTER</strong></span></p>
<p>(String)</p>
<p><span class="bold"><strong>Example:</strong></span> IMPORTER = '123'</p>
</td><td align="left">
<p>3-digit importer number that is stored in the tester during initial setup.</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>DEALERSHIPID</strong></span></p>
<p>(String)</p>
<p><span class="bold"><strong>Example:</strong></span> DEALERSHIPID = 'Siemens'</p>
</td><td align="left">
<p>Maximum of 60 characters for the business information (such as name, address) that is currently stored in the tester.</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>VIN</strong></span></p>
<p>(String)</p>
<p><span class="bold"><strong>Example:</strong></span> VIN = 'WVWZZZ1JZXW234152'</p>
</td><td align="left">
<p>Vehicle Identification Number, 17-digit VIN that is added from the online return log, for example. If the VIN is not available in the log book, a virtual keyboard appears on the screen for input.</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>DEALERJOB</strong></span></p>
<p>(String)</p>
</td><td align="left">
<p>DEALERJOB = '123...CD'</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>ACTIONCODE</strong></span></p>
<p>(String)</p>
<p><span class="bold"><strong>Example:</strong></span> ACTIONCODE = '12345'</p>
</td><td align="left">
<p>The 5-digit action code (instruction for warranty cases) is prompted using a virtual keyboard, assigned to the variables, and added to the diagnostic protocol when the work is performed.</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>LICENCEPLATENUMBER</strong></span></p>
<p>(String)</p>
<p><span class="bold"><strong>Example:</strong></span> LICENCEPLATENUMBER = 'RUED-WR 426'</p>
</td><td align="left">
<p>The tester prompts you to enter the vehicle license plate using a virtual keyboard (maximum 16 digits).</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>REPAIRSTATE</strong></span></p>
<p>(String)</p>
<p><span class="bold"><strong>Example:</strong></span> REPAIRSTATE = 'OKAY'</p>
</td><td align="left">
<p>The tester provides a Yes/No question asking if the repair was successful or not. The response "Yes" generates an OKAY, and "No" generates a NOT_OKAY.</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>DATETIME</strong></span></p>
<p>(String)</p>
<p><span class="bold"><strong>Example:</strong></span> DATETIME = '20021215T195210'</p>
</td><td align="left">
<p>Time/date output in the format 'yyyymmttThhmmss'</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>DATE</strong></span></p>
<p>(String)</p>
<p><span class="bold"><strong>Example:</strong></span> DATE = '2002-12-15'</p>
</td><td align="left">
<p>Date output in the format yyyy-mm-dd</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>TIME</strong></span></p>
<p>(String)</p>
<p><span class="bold"><strong>Example:</strong></span> TIME = '19:52:10'</p>
</td><td align="left">
<p>Time output in the format: hh:mm:ss</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>ERROR_TYPE</strong></span></p>
<p>(String)</p>
</td><td align="left">
<p></p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>DC_VW_PART (String a1)</strong></span></p>
<p>(String)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>teilenr_dc = '1695452032'</p>
<p>DC_VW_PART(teilenr_dc) = 'hw_tnE0909123AB'</p>
</td><td align="left">
<p>The DC part number that was read out previously with "CU_HARDWARE_NUMBER( )" is converted to a VW part number. This is done using the XML table "DC_VW_PARTNUMBER.xml". If the DC part number is not available in the XML table, the string will remain unchanged.</p>
<p><span class="bold"><strong>Parameter</strong></span> a1 (String)</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>FINGERPRINT</strong></span></p>
<p>(Object)</p>
</td><td align="left">
<p>Delivers the “fingerprint” for unique identification of the writer, for example for UDS jobs. It is an artificial, unique key, that formerly consisted of importer, dealer, and TesterID.</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>FINGERPRINTDEALER</strong></span></p>
<p>(Object)</p>
</td><td align="left">
<p>The dealer component of the artificial FINGERPRINT. This is used, for example, for UDS jobs that cannot use the entire FINGERPRINT, but only its individual components.</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>FINGERPRINTDEVICE</strong></span></p>
<p>(Object)</p>
</td><td align="left">
<p>The TesterID component of the artificial FINGERPRINT. This is used, for example, for UDS jobs that cannot use the entire FINGERPRINT, but only its individual components.</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>FINGERPRINTIMPORTER</strong></span></p>
<p>(Object)</p>
</td><td align="left">
<p>The importer component of the artificial FINGERPRINT. This is used, for example, for UDS jobs that cannot use the entire FINGERPRINT, but only its individual components.</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>APPLICATIONTYPE</strong></span></p>
<p>(String)</p>
<p><span class="bold"><strong>Example:</strong></span> APPLICATIONTYPE = 'UMB_FLASH'</p>
</td><td align="left">
<p>The APPLICATIONTYPE system variable is used in Guided Fault Finding to differentiate the current operating condition. It can be evaluated by the GFF program to differentiate its functionality depending on the operating condition. The system variable can have the following variables depending on the product configuration.</p>
<p>- Contracted dealer: 'GFF', 'GF', 'FLASH', 'KD', 'BZD'</p>
<p>- UMB: 'UMB', 'UMB_GF', 'UMB_FLASH', 'UMB_KD', 'UMB_BZD'</p>
<p>The information about diagnostic operating mode (diagnosis, flashing) and the contract status (contracted dealer, UMB) is accessed in order to determine the GFF operating mode.</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>COMMUNICATIONTYPE</strong></span></p>
<p>(String)</p>
<p><span class="bold"><strong>Example:</strong></span> COMMUNICATIONTYPE = 'DoIP'</p>
</td><td align="left">
<p>The COMMUNICATIONTYPE system variable returns the communication method for using in GFF. The type of communication method is detected by the operating system during diagnostic entry and is updated if necessary during a diagnostic session. The communication method can be changed within a diagnosis. Possible return values:</p>
<p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>CAN</p>
</li><li>
<p>CANFD</p>
</li><li>
<p>DoIP</p>
</li></ul></div><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>PROGRAMMINGVOLTAGE</strong></span></p>
<p>(Integer)</p>
</td><td align="left">
<p>System variable for setting and reading the programming voltage status.</p>
<p>Possible values are:</p>
<p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>1: programming voltage on</p>
</li><li>
<p>0: programming voltage off</p>
</li><li>
<p>-1: unknown (return value only)</p>
</li></ul></div><p>
</p>
</td></tr><tr><td align="left"><a name="VCI_type"></a>
<p><span class="bold"><strong>VCI_TYPE</strong></span></p>
<p>(String)</p>
<p><span class="bold"><strong>Example:</strong></span> VCI_TYPE = 'VAS6154A'</p>
</td><td align="left">
<p>This function provides the VCI type for the connected VCI.</p>
<p>Possible return values:</p>
<p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>J2534</p>
</li><li>
<p>VAS5054</p>
</li><li>
<p>VAS5055</p>
</li><li>
<p>VAS6154</p>
</li><li>
<p>VAS6154A</p>
</li><li>
<p>UNKNOWN</p>
</li></ul></div><p>
</p>
</td></tr><tr><td align="left"><a name="VCI_Connection_type"></a>
<p><span class="bold"><strong>VCI_CONNECTION_TYPE</strong></span></p>
<p>(String)</p>
<p><span class="bold"><strong>Example:</strong></span> VCI_CONNECTION = 'USB'</p>
</td><td align="left">
<p>This function provides the connection type for the connected VCI.</p>
<p>Possible return values:</p>
<p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>USB</p>
</li><li>
<p>BLUETOOTH</p>
</li><li>
<p>WLAN_INFRASTRUCTURE</p>
</li><li>
<p>WLAN_ACCESSPOINT</p>
</li><li>
<p>ETHERNET</p>
</li><li>
<p>INFRARED</p>
</li><li>
<p>PCMCIA</p>
</li><li>
<p>PCI_EXPRESS</p>
</li><li>
<p>UNKNOWN</p>
</li></ul></div><p>
</p>
</td></tr><tr><td align="left"><a name="UGD_Anzahl_FTest"></a>
<p><span class="bold"><strong>UGD_Anzahl_FTest</strong></span></p>
<p>Integer</p>
<p><span class="bold"><strong>Example:</strong></span> UGD_Anzahl_FTest = 5</p>
</td><td align="left">
<p>The function returns the number of function tests from the UGD test plan.</p>
</td></tr><tr><td align="left"><a name="UGD_Systemnamen_FTest"></a>
<p><span class="bold"><strong>UGD_Systemnamen_FTest</strong></span></p>
<p>String[]</p>
<p><span class="bold"><strong>Example:</strong></span> UGD_Systemnamen_FTest = {'Engine_Transmission_no_Traction@00078', 'Airbag_B101053_sporadic@00078'}</p>
</td><td align="left">
<p>The function returns the system names of the function tests from the UGD test plan (the sequence is the same in all UGD system functions).</p>
</td></tr><tr><td align="left"><a name="UGD_Anzeigenamen_FTest"></a>
<p><span class="bold"><strong>UGD_Anzeigenamen_FTest</strong></span></p>
<p>String[]</p>
<p><span class="bold"><strong>Example:</strong></span> UGD_Anzeigenamen_FTest = {'Engine/Transmission/no traction', 'Airbag: B101053 sporadic'}</p>
</td><td align="left">
<p>The function returns the display name of the function test from the UGD test plan (the sequence is the same in all UGD system functions).</p>
</td></tr><tr><td align="left"><a name="UGD_Wahrscheinlichkeiten_FTest"></a>
<p><span class="bold"><strong>UGD_Wahrscheinlichkeiten_FTest</strong></span></p>
<p>Float[]</p>
<p><span class="bold"><strong>Example:</strong></span> UGD_Wahrscheinlichkeiten_FTest = {0.5, 0.8}</p>
</td><td align="left">
<p>The function returns the probability of the function test from the UGD test plan (the sequence is the same in all UGD system functions).</p>
</td></tr><tr><td align="left"><a name="URL_Datenverteilung"></a>
<p><span class="bold"><strong>URL_DataDistribution</strong></span></p>
<p>(String)</p>
<p><span class="bold"><strong>Example:</strong></span> URL_DataDistribution= 'http://mirror.volkswagen.de'</p>
</td><td align="left">
<p>The function delivers the brand-specific D3 or MirrorServer2 URL stored in ODIS Service Administration that is used as the URL when selecting the “MSDummyURL” alias in the “Flash path” dialog.</p>
</td></tr><tr><td align="left"><a name="UUID_D3_Edgebox"></a>
<p><span class="bold"><strong>UUID_D3_EDGEBOX</strong></span></p>
<p>(String)</p>
<p><span class="bold"><strong>Example:</strong></span> UUID_D3_EDGEBOX = '04faff60-0dbb-421a-a1be-d8c8e501cf2a'</p>
</td><td align="left">
<p>The function supplies the UUID of the D3 Edgebox that was determined in diagnostic entry, so that the D3 Edgebox can be addressed in a targeted manner.</p>
<p>Valid UUID format: 36 byes ASCII</p>
<p>The function returns an empty string in the following cases (no NULL):</p>
<p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>If a response to the request is missing (for example, EdgeBox is not there or no connection to EdgeBox)</p>
</li><li>
<p>Response does not have a valid UUID format</p>
</li></ul></div><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>Status_BackgroundModules</strong></span></p>
<p>(Integer)</p>
</td><td align="left">
<p>System variable for reading out the status of the background start module.</p>
<p>Possible values are:</p>
<p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>1: no background start module is running</p>
</li><li>
<p>0: a background start module is running</p>
</li><li>
<p>-1: error / status cannot be determined</p>
</li></ul></div><p>
</p>
</td></tr></tbody></table>

**Table 83. Tester data**

###### <a id="Funktionstesteditor.Arbeitsflaeche.Funktionen_Logbuchdaten"></a>7.14.12.3.5. Log book data

<a id="d4e18979"></a>

<table border="1" summary="Log book data"><colgroup><col align="left"/><col align="left"/></colgroup><thead><tr bgcolor="#EEEEEE"><th align="left">Function</th><th align="left">Description</th></tr></thead><tbody><tr><td align="left">
<p><span class="bold"><strong>CP_HAS_PR_NUMBER (search term string, vehicle integer)</strong></span></p>
<p>(Integer)</p>
<p><span class="bold"><strong>Examples:</strong></span></p>
<p>CP_HAS_PR_NUMBER (strSystemStringPRNumber) = 0</p>
<p>CP_HAS_PR_NUMBER ('PR0') = 1</p>
</td><td align="left">
<p>With this function, it is possible to check the status of the CarPort request and to retrieve the PR number that is provided by the operating system. The request occurs based on the VehicleBase answer with the CarPort data.</p>
<p>The following return values are possible:</p>
<p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: No, PR number not available</p>
</li><li>
<p>1: Yes, PR number</p>
</li><li>
<p>-1: PR numbers were not read</p>
</li></ul></div><p>
</p>
<p><span class="bold"><strong>Parameters</strong></span></p><p>Search term (string): PR number</p><p>
</p><p>Vehicle (integer): vehicle type (optional) if not entered in LiveVehicle The following values are possible:</p><p>
</p><p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p><p>
</p>
<p><span class="bold"><strong>Return value</strong></span> status of the specified PR number (integer)</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>CU_5BAUDADR_INDEX (Index integer, vehicle integer)</strong></span></p>
<p>(Integer)</p>
</td><td align="left">
<p>K-line 5-baud address word for the control module. Corresponds to the group number, for example 1 for engine electronics.</p>
<p><span class="bold"><strong>Parameter</strong></span> Index (Integer): the 0-based index of the control module in the list.</p><p>Vehicle (integer): vehicle type (optional) if not entered in LiveVehicle The following values are possible:</p><p>
</p><p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>CU_5BAUDADR_ADR (address integer, vehicle integer)</strong></span></p>
<p>(Integer)</p>
</td><td align="left">
<p>K-line 5-baud address word for the control module. Corresponds to the group number, for example 1 for engine electronics.</p>
<p><span class="bold"><strong>Parameter</strong></span> Address (Integer): the 5 baud address of the control module.</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>CU_ADR_INDEX (Index integer, vehicle integer)</strong></span></p>
<p>(Integer)</p>
</td><td align="left">
<p>TP target address of the control module. Communication can be established using this value.</p>
<p><span class="bold"><strong>Parameter</strong></span> Index (Integer): the 0-based index of the control module in the list.</p><p>Vehicle (integer): vehicle type (optional) if not entered in LiveVehicle The following values are possible:</p><p>
</p><p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>CU_ADR_ADR (address integer, vehicle integer)</strong></span></p>
<p>(Integer)</p>
</td><td align="left">
<p>TP target address of the control module. Communication can be established using this value.</p>
<p><span class="bold"><strong>Parameter</strong></span> Address (Integer): the 5 baud address of the control module.</p><p>Vehicle (integer): vehicle type (optional) if not entered in LiveVehicle The following values are possible:</p><p>
</p><p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>CU_BUSTYP_INDEX (Index integer, vehicle integer)</strong></span></p>
<p>(Integer)</p>
</td><td align="left">
<p>Bus system to which the control module is connected.</p>
<p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: powertrain system</p>
</li><li>
<p>1: convenience system</p>
</li><li>
<p>2: Infotainment</p>
</li><li>
<p>3: instrument cluster system</p>
</li><li>
<p>4: MOST Bus (Media Oriented System Transport)</p>
</li><li>
<p>5: Extended Bus</p>
</li><li>
<p>6: K-wire</p>
</li><li>
<p>7: LIN Bus</p>
</li><li>
<p>8: non-networked components (not found in the gateway).</p>
</li></ul></div><p>
</p>
<p><span class="bold"><strong>Parameter</strong></span> Index (Integer): the 0-based index of the control module in the list.</p><p>Vehicle (integer): vehicle type (optional) if not entered in LiveVehicle The following values are possible:</p><p>
</p><p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>CU_BUSTYP_ADR(address integer, vehicle integer)</strong></span></p>
<p>(Integer)</p>
</td><td align="left">
<p>Bus system to which the control module is connected.</p>
<p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: powertrain system</p>
</li><li>
<p>1: convenience system</p>
</li><li>
<p>2: Infotainment</p>
</li><li>
<p>3: instrument cluster system</p>
</li><li>
<p>4: MOST Bus (Media Oriented System Transport)</p>
</li><li>
<p>5: Extended Bus</p>
</li><li>
<p>6: K-wire</p>
</li><li>
<p>7: LIN Bus</p>
</li><li>
<p>8: non-networked components (not found in the gateway).</p>
</li></ul></div><p>
</p>
<p><span class="bold"><strong>Parameter</strong></span> Address (Integer): the 5 baud address of the control module.</p><p>Vehicle (integer): vehicle type (optional) if not entered in LiveVehicle The following values are possible:</p><p>
</p><p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>CU_INSTALLED_INDEX (Index integer, vehicle integer)</strong></span></p>
<p>(Integer)</p>
</td><td align="left">
<p>Indication whether the control module should be installed (specified components info).</p>
<p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: control module should not be installed.</p>
</li><li>
<p>1: control module should be installed (coded).</p>
</li></ul></div><p>
</p>
<p><span class="bold"><strong>Parameter</strong></span> Index (Integer): the 0-based index of the control module in the list.</p><p>Vehicle (integer): vehicle type (optional) if not entered in LiveVehicle The following values are possible:</p><p>
</p><p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>CU_INSTALLED_ADR (address integer, vehicle integer)</strong></span></p>
<p>(Integer)</p>
</td><td align="left">
<p>Indication whether the control module should be installed (specified components info).</p>
<p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: control module should not be installed.</p>
</li><li>
<p>1: control module should be installed (coded).</p>
</li></ul></div><p>
</p>
<p><span class="bold"><strong>Parameter</strong></span> Address (Integer): the 5 baud address of the control module.</p><p>Vehicle (integer): vehicle type (optional) if not entered in LiveVehicle The following values are possible:</p><p>
</p><p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>CU_STATUSINFO_INDEX (Index integer, vehicle integer)</strong></span></p>
<p>(Integer)</p>
</td><td align="left">
<p>Control module status information byte.</p>
<p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0000: OK, communication OK</p>
</li><li>
<p>11xx: cannot be reached, static communication error</p>
</li><li>
<p>x010: DTC memory set, DTC memory in control module, possible error stored in the gateway due to sporadic communication error.</p>
</li><li>
<p>x0x1: not reported, control module is reported as not coded, possible error stored in the gateway due to sporadic communication error.</p>
</li></ul></div><p>
</p>
<p>The function does not return any usable result for UDS ECUs.</p>
<p><span class="bold"><strong>Parameter</strong></span> Index (Integer): the 0-based index of the control module in the list.</p><p>Vehicle (integer): vehicle type (optional) if not entered in LiveVehicle The following values are possible:</p><p>
</p><p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>CU_STATUSINFO_ADR (address integer, vehicle integer)</strong></span></p>
<p>(Integer)</p>
</td><td align="left">
<p>Control module status information byte.</p>
<p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0000: OK, communication OK</p>
</li><li>
<p>11xx: cannot be reached, static communication error</p>
</li><li>
<p>x010: DTC memory set, DTC memory in control module, possible error stored in the gateway due to sporadic communication error.</p>
</li><li>
<p>x0x1: not reported, control module is reported as not coded, possible error stored in the gateway due to sporadic communication error.</p>
</li></ul></div><p>
</p>
<p>The function does not return any usable result for UDS ECUs.</p>
<p><span class="bold"><strong>Parameter</strong></span> Address (Integer): the 5 baud address of the control module.</p><p>Vehicle (integer): vehicle type (optional) if not entered in LiveVehicle The following values are possible:</p><p>
</p><p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>CU_STATUSTEXT_INDEX (Index integer, vehicle integer)</strong></span></p>
<p>(Integer)</p>
</td><td align="left">
<p>Extracted status information.</p>
<p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>1: control module OK</p>
</li><li>
<p>2: control module cannot be reached by Bus</p>
</li><li>
<p>3: control module with error set</p>
</li><li>
<p>4: control module not registered (not coded)</p>
<p>
</p><div class="itemizedlist"><ul type="circle"><li>
<p>UNDEFINED(0)</p>
</li><li>
<p>OK(1)</p>
</li><li>
<p>NOTREACHABLE(2)</p>
</li><li>
<p>DEFECT(3)</p>
</li><li>
<p>NOTREGISTERED(4)</p>
</li></ul></div><p>
</p>
</li></ul></div><p>
</p>
<p>The function does not return any usable result for UDS ECUs.</p>
<p><span class="bold"><strong>Parameter</strong></span> Index (Integer): the 0-based index of the control module in the list.</p><p>Vehicle (integer): vehicle type (optional) if not entered in LiveVehicle The following values are possible:</p><p>
</p><p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>CU_STATUSTEXT_ADR (address integer, vehicle integer)</strong></span></p>
<p>(Integer)</p>
</td><td align="left">
<p>Extracted status information.</p>
<p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>1: control module OK</p>
</li><li>
<p>2: control module cannot be reached by Bus</p>
</li><li>
<p>3: control module with error set</p>
</li><li>
<p>4: control module not registered (not coded)</p>
<p>
</p><div class="itemizedlist"><ul type="circle"><li>
<p>UNDEFINED(0)</p>
</li><li>
<p>OK(1)</p>
</li><li>
<p>NOTREACHABLE(2)</p>
</li><li>
<p>DEFECT(3)</p>
</li><li>
<p>NOTREGISTERED(4)</p>
</li></ul></div><p>
</p>
</li></ul></div><p>
</p>
<p>The function does not return any usable result for UDS ECUs.</p>
<p><span class="bold"><strong>Parameter</strong></span> Address (Integer): the 5 baud address of the control module.</p><p>Vehicle (integer): vehicle type (optional) if not entered in LiveVehicle The following values are possible:</p><p>
</p><p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>CU_CODED_INDEX (Index integer, vehicle integer)</strong></span></p>
<p>(Integer)</p>
</td><td align="left">
<p>Indicated if coding results (coding table number, coding data) exist for the affected control module. A coding table describes the control module-specific coding bits and their meaning and any possible subsequent tables. Coding tables can be edited in DES-VW and published as an XML file. They are used in OBD in the coding function for filling the selection screens.</p>
<p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: no coding results available</p>
</li><li>
<p>1: coding results available</p>
</li></ul></div><p>
</p>
<p>The function does not return any usable result for UDS ECUs.</p>
<p><span class="bold"><strong>Parameter</strong></span> Index (Integer): the 0-based index of the control module in the list.</p><p>Vehicle (integer): vehicle type (optional) if not entered in LiveVehicle The following values are possible:</p><p>
</p><p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>CU_CODED_ADR (address integer, vehicle integer)</strong></span></p>
<p>(Integer)</p>
</td><td align="left">
<p>Indicated if coding results (coding table number, coding data) exist for the affected control module. A coding table describes the control module-specific coding bits and their meaning and any possible subsequent tables. Coding tables can be edited in DES-VW and published as an XML file. They are used in OBD in the coding function for filling the selection screens.</p>
<p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: no coding results available</p>
</li><li>
<p>1: coding results available</p>
</li></ul></div><p>
</p>
<p>The function does not return any usable result for UDS ECUs.</p>
<p><span class="bold"><strong>Parameter</strong></span> Address (Integer): the 5 baud address of the control module.</p><p>Vehicle (integer): vehicle type (optional) if not entered in LiveVehicle The following values are possible:</p><p>
</p><p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>CU_CODINGTABLE_INDEX (Index integer, vehicle integer)</strong></span></p>
<p>(Integer)</p>
</td><td align="left">
<p>Number of the first coding table (original table) for the corresponding control module. The original table can refer in turn to subsequent tables.</p>
<p><span class="bold"><strong>Parameter</strong></span> Index (Integer): the 0-based index of the control module in the list.</p><p>Vehicle (integer): vehicle type (optional) if not entered in LiveVehicle The following values are possible:</p><p>
</p><p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>CU_CODINGTABLE_ADR (address integer, vehicle integer)</strong></span></p>
<p>(Integer)</p>
</td><td align="left">
<p>Number of the first coding table (original table) for the corresponding control module. The original table can refer in turn to subsequent tables.</p>
<p><span class="bold"><strong>Parameter</strong></span> Address (Integer): the 5 baud address of the control module.</p><p>Vehicle (integer): vehicle type (optional) if not entered in LiveVehicle The following values are possible:</p><p>
</p><p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>CU_HARDWARE_NUMBER (Ecu string, vehicle integer)</strong></span></p>
<p>(Integer)</p>
</td><td align="left">
<p>The control module hardware number is provided.</p>
<p><span class="bold"><strong>Parameter</strong></span> Ecu (String): a control module identifier, such as group name such as 'mot_01', control module variant (for KWP protocols) such as: 'mot6000', Shortname z. B. 'EnginContrModul1', Logical Link, UDS variant name (BV or EV)</p><p>Vehicle (integer): vehicle type (optional) if not entered in LiveVehicle The following values are possible:</p><p>
</p><p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>CU_SOFTWARE_NUMBER (Ecu string, vehicle integer)</strong></span></p>
<p>(Integer)</p>
</td><td align="left">
<p>The control module software number is read out. This data can be used to supply the Ecukom "FlashName" command.</p>
<p><span class="bold"><strong>Parameter</strong></span> Ecu (String): a control module identifier, such as group name such as 'mot_01', control module variant (for KWP protocols) such as: 'mot6000', Shortname z. B. 'EnginContrModul1', Logical Link, UDS variant name (BV or EV)</p><p>Vehicle (integer): vehicle type (optional) if not entered in LiveVehicle The following values are possible:</p><p>
</p><p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>CU_SOFTWARE_VERSION (Ecu string, vehicle integer)</strong></span></p>
<p>(Integer)</p>
</td><td align="left">
<p>The control module software version is read out. This data can be used to supply the Ecukom "FlashName" command.</p>
<p><span class="bold"><strong>Parameter</strong></span> Ecu (String): a control module identifier, such as group name such as 'mot_01', control module variant (for KWP protocols) such as: 'mot6000', Shortname z. B. 'EnginContrModul1', Logical Link, UDS variant name (BV or EV)</p><p>Vehicle (integer): vehicle type (optional) if not entered in LiveVehicle The following values are possible:</p><p>
</p><p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>CU_SERIAL_NUMBER (Ecu string, vehicle integer)</strong></span></p>
<p>(Integer)</p>
</td><td align="left">
<p>The control module serial number is read out.</p>
<p><span class="bold"><strong>Parameter</strong></span> Ecu (String): a control module identifier, such as group name such as 'mot_01', control module variant (for KWP protocols) such as: 'mot6000', Shortname z. B. 'EnginContrModul1', Logical Link, UDS variant name (BV or EV)</p><p>Vehicle (integer): vehicle type (optional) if not entered in LiveVehicle The following values are possible:</p><p>
</p><p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>CU_CODING_STATE (Ecu string, vehicle integer)</strong></span></p>
<p>(Integer)</p>
</td><td align="left">
<p>The control module coding status (coding value) is read out.</p>
<p><span class="bold"><strong>Parameter</strong></span> Ecu (String): a control module identifier, such as group name such as 'mot_01', control module variant (for KWP protocols) such as: 'mot6000', Shortname z. B. 'EnginContrModul1', Logical Link, UDS variant name (BV or EV)</p><p>Vehicle (integer): vehicle type (optional) if not entered in LiveVehicle The following values are possible:</p><p>
</p><p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>CU_FLASHABLE (Ecu string, vehicle integer)</strong></span></p>
<p>(Integer)</p>
</td><td align="left">
<p>Indication if the control module can be flashed. 0: cannot be flashed 1: can be flashed -1: no information</p>
<p><span class="bold"><strong>Parameter</strong></span> Ecu (String): a control module identifier, such as group name such as 'mot_01', control module variant (for KWP protocols) such as: 'mot6000', Shortname z. B. 'EnginContrModul1', Logical Link, UDS variant name (BV or EV)</p><p>Vehicle (integer): vehicle type (optional) if not entered in LiveVehicle The following values are possible:</p><p>
</p><p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>CU_TIME_STAMP (Ecu string, vehicle integer)</strong></span></p>
<p>(String)</p>
</td><td align="left">
<p>The function argument is the error code path from the DTC memory model. The return value is the date-time string in the format DD.MM.YYYY|HH:MM:SS from the original error in the log book. Error codes with no timestamp have the value 0.</p>
<p><span class="bold"><strong>Parameter</strong></span> Ecu (String): error code path from the DTC memory model</p><p>Vehicle (integer): vehicle type (optional) if not entered in LiveVehicle The following values are possible:</p><p>
</p><p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>MAX_SPECLIST (vehicle integer)</strong></span></p>
<p>(Integer)</p>
</td><td align="left">
<p><span class="bold"><strong>Parameter</strong></span> Vehicle (integer): vehicle type (optional) if not entered in LiveVehicle The following values are possible:</p>
<p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>CU_REGULATIONIDENTIFICATION (Integer Vehicle)</strong></span></p>
<p>(String[])</p>
</td><td align="left">
<p>The function returns the values of the regulation identification from the RxSWIN. A one-dimensional array from the type string is returned so that the target variable in the expression must be specified without square brackets. Using an optional parameter, you can specify if the current status or the status at diagnostic entry should be checked.</p>
<p>Example: CU_REGULATIONIDENTIFICATION = {'R079', 'GB/T36047'}</p>
<p><span class="bold"><strong>Parameter</strong></span> Vehicle (Integer): condition/vehicle type (optional) if not entered then LiveVehicle. The following values are possible:</p>
<p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>CU_SOFTWAREIDENTIFICATION (Integer Vehicle)</strong></span></p>
<p>(String[])</p>
</td><td align="left">
<p>The function returns the values of the software identification from the RxSWIN. A one-dimensional array from the type string is returned so that the target variable in the expression must be specified without square brackets. Using an optional parameter, you can specify if the current status or the status at diagnostic entry should be checked.</p>
<p>Example: CU_SOFTWAREIDENTIFICATION = {'v05741753a', 'v04369852'}</p>
<p><span class="bold"><strong>Parameter</strong></span> Vehicle (Integer): condition/vehicle type (optional) if not entered then LiveVehicle. The following values are possible:</p>
<p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p>
</td></tr></tbody></table>

**Table 84. Log book data**

###### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Zuordnung_Messtechnik"></a>7.14.12.3.6. Measuring Equipment

<a id="d4e19565"></a>

<table border="1" summary="Measuring Equipment"><colgroup><col align="left"/><col align="left"/></colgroup><thead><tr bgcolor="#EEEEEE"><th align="left">Function</th><th align="left">Description</th></tr></thead><tbody><tr><td align="left">
<p><span class="bold"><strong>HVMT_FMVERSION_EXPECTED</strong></span></p>
<p>(String)</p>
</td><td align="left">
<p>Returns the device status information and the device information. The function attempts to connect with the device. The function does not change the device's current mode or status. The version numbers (Type String) are provided in the format 'aaabbbcccdddd' (a = Master, b = Major, c = Minor, d = Build). Example: '001002004019'.</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>HVMT_FMVERSION_AVAILABLE</strong></span></p>
<p>(String)</p>
</td><td align="left">
<p>Returns the device status information and the device information. The function attempts to connect with the device. The function does not change the device's current mode or status. The version numbers (Type String) are provided in the format 'aaabbbcccdddd' (a = Master, b = Major, c = Minor, d = Build). Example: '001002004019'.</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>HVMT_GDIDDVERSION_EXPECTED</strong></span></p>
<p>(String)</p>
</td><td align="left">
<p>Returns the device status information and the device information. The function attempts to connect with the device. The function does not change the device's current mode or status. The version numbers (Type String) are provided in the format 'aaabbbcccdddd' (a = Master, b = Major, c = Minor, d = Build). Example: '001002004019'.</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>HVMT_GDIDDVERSION_AVAILABLE</strong></span></p>
<p>(String)</p>
</td><td align="left">
<p>Returns the device status information and the device information. The function attempts to connect with the device. The function does not change the device's current mode or status. The version numbers (Type String) are provided in the format 'aaabbbcccdddd' (a = Master, b = Major, c = Minor, d = Build). Example: '001002004019'.</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>HVMT_DEVICE_IDENTIFICATION</strong></span></p>
<p>(String)</p>
</td><td align="left">
<p>Returns the device status information and the device information. The function attempts to connect with the device. The function does not change the device's current mode or status.</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>STDMT_DEVICE_IDENTIFICATION</strong></span></p>
<p>(String)</p>
</td><td align="left">
<p>Delivers information about the connected measuring equipment hardware and about the connected sensors. The return value consists of a nine-digit string. An example for the response is "110130001", whereby each position of a number has the following meaning:</p>
<p>Position 1: connected device (0=no device connected, 1=VAS6356)</p>
<p>Position 2: URDI (0=not connected, 1=connected)</p>
<p>Position 3: DSO1 (0=not connected, 1=connected)</p>
<p>Position 4: DSO2 (0=not connected, 1=connected)</p>
<p>Position 5: current probe (0=not connected, 1=50A, 2=500A, 3=100A, 4=1800A)</p>
<p>Position 6: TDI (0=not connected, 1=4bar, 2=16bar, 3=60bar, 4=400bar, 5=temperature sensor, 6=50mbar)</p>
<p>Position 7: TDI (0=not connected, 1=4bar, 2=16bar, 3=60bar, 4=400bar, 5=temperature sensor, 6=50mbar)</p>
<p>Position 8: kV (0=not connected, 1=connected)</p>
<p>Position 9: TZ (0=not connected, 1=connected)</p>
<p>Position 10: reserved for other sensors</p>
</td></tr></tbody></table>

**Table 85. Measuring Equipment**

###### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Zuordnung_Steuergeraeteidentifikation"></a>7.14.12.3.7. Control Module Identification

<a id="d4e19630"></a>

<table border="1" summary="Control Module Identification"><colgroup><col align="left"/><col align="left"/></colgroup><thead><tr bgcolor="#EEEEEE"><th align="left">Function</th><th align="left">Description</th></tr></thead><tbody><tr><td align="left">
<p><span class="bold"><strong>CU_MSP_KW1281_on_ISO_9141_2 (Ecu string, vehicle integer)</strong></span></p>
<p>(Bool)</p>
</td><td align="left">
<p>Provides the value '1' if the control module uses the corresponding diagnostic protocol with the transport protocol for communication.</p>
<p><span class="bold"><strong>Parameter</strong></span> Ecu (String): a control module identifier, such as group name such as 'mot_01', control module variant (for KWP protocols) such as: 'mot6000', Shortname z. B. 'EnginContrModul1', Logical Link, UDS variant name (BV or EV)</p><p>Vehicle (integer): vehicle type (optional) if not entered in LiveVehicle The following values are possible:</p><p>
</p><p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>CU_MSP_KW1281_on_TP16 (Ecu string, vehicle integer)</strong></span></p>
<p>(Bool)</p>
</td><td align="left">
<p>Provides the value '1' if the control module uses the corresponding diagnostic protocol with the transport protocol for communication.</p>
<p><span class="bold"><strong>Parameter</strong></span> Ecu (String): a control module identifier, such as group name such as 'mot_01', control module variant (for KWP protocols) such as: 'mot6000', Shortname z. B. 'EnginContrModul1', Logical Link, UDS variant name (BV or EV)</p><p>Vehicle (integer): vehicle type (optional) if not entered in LiveVehicle The following values are possible:</p><p>
</p><p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>CU_MSP_VW2000LP_on_ISO_14230_2 (Ecu string, vehicle integer)</strong></span></p>
<p>(Bool)</p>
</td><td align="left">
<p>Provides the value '1' if the control module uses the corresponding diagnostic protocol with the transport protocol for communication.</p>
<p><span class="bold"><strong>Parameter</strong></span> Ecu (String): a control module identifier, such as group name such as 'mot_01', control module variant (for KWP protocols) such as: 'mot6000', Shortname z. B. 'EnginContrModul1', Logical Link, UDS variant name (BV or EV)</p><p>Vehicle (integer): vehicle type (optional) if not entered in LiveVehicle The following values are possible:</p><p>
</p><p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>CU_MSP_VW2000LP_on_TP16 (Ecu string, vehicle integer)</strong></span></p>
<p>(Bool)</p>
</td><td align="left">
<p>Provides the value '1' if the control module uses the corresponding diagnostic protocol with the transport protocol for communication.</p>
<p><span class="bold"><strong>Parameter</strong></span> Ecu (String): a control module identifier, such as group name such as 'mot_01', control module variant (for KWP protocols) such as: 'mot6000', Shortname z. B. 'EnginContrModul1', Logical Link, UDS variant name (BV or EV)</p><p>Vehicle (integer): vehicle type (optional) if not entered in LiveVehicle The following values are possible:</p><p>
</p><p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>CU_MSP_VW2000LP_on_TP20 (Ecu string, vehicle integer)</strong></span></p>
<p>(Bool)</p>
</td><td align="left">
<p>Provides the value '1' if the control module uses the corresponding diagnostic protocol with the transport protocol for communication.</p>
<p><span class="bold"><strong>Parameter</strong></span> Ecu (String): a control module identifier, such as group name such as 'mot_01', control module variant (for KWP protocols) such as: 'mot6000', Shortname z. B. 'EnginContrModul1', Logical Link, UDS variant name (BV or EV)</p><p>Vehicle (integer): vehicle type (optional) if not entered in LiveVehicle The following values are possible:</p><p>
</p><p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>CU_ISO_14230_3_on_ISO_15765_2 (Ecu string, vehicle integer)</strong></span></p>
<p>(Bool)</p>
</td><td align="left">
<p>Provides the value '1' if the control module uses the corresponding diagnostic protocol with the transport protocol for communication.</p>
<p><span class="bold"><strong>Parameter</strong></span> Ecu (String): a control module identifier, such as group name such as 'mot_01', control module variant (for KWP protocols) such as: 'mot6000', Shortname z. B. 'EnginContrModul1', Logical Link, UDS variant name (BV or EV)</p><p>Vehicle (integer): vehicle type (optional) if not entered in LiveVehicle The following values are possible:</p><p>
</p><p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>CU_ISO_15765_3_on_ISO_15765_2 (Ecu string, vehicle integer)</strong></span></p>
<p>(Bool)</p>
</td><td align="left">
<p>Provides the value '1' if the control module uses the corresponding diagnostic protocol with the transport protocol for communication.</p>
<p><span class="bold"><strong>Parameter</strong></span> Ecu (String): a control module identifier, such as group name such as 'mot_01', control module variant (for KWP protocols) such as: 'mot6000', Shortname z. B. 'EnginContrModul1', Logical Link, UDS variant name (BV or EV)</p><p>Vehicle (integer): vehicle type (optional) if not entered in LiveVehicle The following values are possible:</p><p>
</p><p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>CU_ISO_13400_on_IEEE_802_3 (Ecu string, vehicle integer)</strong></span></p>
<p>(Bool)</p>
</td><td align="left">
<p>Provides the value '1' if the control module uses the corresponding diagnostic protocol with the transport protocol for communication.</p>
<p><span class="bold"><strong>Parameter</strong></span> Ecu (String): a control module identifier, such as group name such as 'mot_01', control module variant (for KWP protocols) such as: 'mot6000', Shortname z. B. 'EnginContrModul1', Logical Link, UDS variant name (BV or EV)</p><p>Vehicle (integer): vehicle type (optional) if not entered in LiveVehicle The following values are possible:</p><p>
</p><p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>CU_PROTOCOL (Ecu string, vehicle integer)</strong></span></p>
<p>(String)</p>
<p><span class="bold"><strong>Example:</strong></span> 'KWP2000 on ISOTP'.</p>
</td><td align="left">
<p>A string that contains the diagnostic protocol and the transport protocol is created. The following responses are possible as a result: UNKNOWN KWP1281_TPKLINE KWP1281_TP16 KWP2000_TPKLINE KWP2000_TP16 KWP2000_TP20 KWP2000_ISOTP UDS_ISOTP UDS_ETHERNET</p>
<p><span class="bold"><strong>Parameter</strong></span> Ecu (String): a control module identifier, such as group name such as 'mot_01', control module variant (for KWP protocols) such as: 'mot6000', Shortname z. B. 'EnginContrModul1', Logical Link, UDS variant name (BV or EV)</p><p>Vehicle (integer): vehicle type (optional) if not entered in LiveVehicle The following values are possible:</p><p>
</p><p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>CU_IDENT_MASTER (String Ecu, String Longname, Integer Vehicle)</strong></span></p>
<p>(String)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>CU_Ident_Master ('mot_01','$F1AD') = '01' (with raw value configuration)</p>
<p>CU_Ident_Master ('mot_01','ECU_Programming Information') = 'No Program available' (without raw value configuration)</p>
</td><td align="left">
<p>The master identification is read out. The following responses are possible as a result: hex raw value or interpreted value.</p>
<p>If the ID of the master identification value to be read by the DiagnServi_ReadDataByIdentGenerServi service is specified in the ODIS parameters, the RDID will be expected in the parameter long name. In this case, only the RAW type is permitted in the parameters.</p>
<p>Ecu (string) <span class="bold"><strong>Parameter</strong></span>: a control module identifier, such as group name such as 'mot_01', control module variant (for KWP protocols) such as: 'mot6000', Short name e.g. 'EnginContrModul1', Logical Link, UDS variant name (BV or EV) long name (string): record data identifier or long name</p><p>Vehicle (integer): vehicle type (optional) if not entered in LiveVehicle The following values are possible:</p><p>
</p><p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>CU_IDENT_SLAVE (String Ecu, String Longname, Integer Vehicle)</strong></span></p>
<p>(String)</p>
<p><span class="bold"><strong>Example:</strong></span> CU_Ident_Slave ('mot_01','003F','subsystem_coded') = 'Yes'.</p>
</td><td align="left">
<p>The slave identification is read out.</p>
<p><span class="bold"><strong>Parameter</strong></span> Ecu (String): a control module identifier, such as group name such as 'mot_01', control module variant (for KWP protocols) such as: 'mot6000', short name e.g. 'EnginContrModul1', Logical Link, UDS variant name (BV or EV) SlaveID (string): e.g. ‘003F’ (hex) or ‘63’ (dez) long name (string): e.g. ‘subsystem_coded’</p><p>Vehicle (integer): vehicle type (optional) if not entered in LiveVehicle The following values are possible:</p><p>
</p><p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>CU_SlaveIDs (Ecu string, vehicle integer)</strong></span></p>
<p>(String[])</p>
<p><span class="bold"><strong>Example:</strong></span> CU_SlaveIDs ('mot_01') = '63','25','299' (dec).</p>
</td><td align="left">
<p>The SlaveIDs are read out.</p>
<p><span class="bold"><strong>Parameter</strong></span> Ecu (String): a control module identifier, such as group name such as 'mot_01', control module variant (for KWP protocols) such as: 'mot6000', Shortname z. B. 'EnginContrModul1', Logical Link, UDS variant name (BV or EV)</p><p>Vehicle (integer): vehicle type (optional) if not entered in LiveVehicle The following values are possible:</p><p>
</p><p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>CU_UDS_ID_KWP_Dienst_22 (Ecu string, vehicle integer)</strong></span></p>
<p>(Bool)</p>
</td><td align="left">
<p>There will be a check to see if Service 1A is involved.</p>
<p><span class="bold"><strong>Parameter</strong></span> Ecu (String): a control module identifier, such as group name such as 'mot_01', control module variant (for KWP protocols) such as: 'mot6000', Shortname z. B. 'EnginContrModul1', Logical Link, UDS variant name (BV or EV)</p><p><span class="bold"><strong>Parameter</strong></span> Vehicle (integer): vehicle type (optional) if not entered in LiveVehicle The following values are possible:</p><p>
</p><p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>CU_Gatewayverbauliste (vehicle integer)</strong></span></p>
<p>(String)</p>
<p><span class="bold"><strong>Example:</strong></span> sample string entry: '03, 0' (ID = 03, not coded = 0)</p>
</td><td align="left">
<p>A list of gateway components is generated. The list contains an entry for each component with the ECU ID and the information of whether it is coded or not. Provides the entries for the gateway components list as a list separated by commas.</p>
<p>Vehicle (integer): vehicle type (optional) if not entered in LiveVehicle The following values are possible:</p>
<p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>CU_VW_ECU_HardwareVersionNumber (Ecu string, vehicle integer)</strong></span></p>
<p>(String)</p>
</td><td align="left">
<p>The control module hardware version is provided.</p>
<p><span class="bold"><strong>Parameter</strong></span> Ecu (String): a control module identifier, such as group name such as 'mot_01', control module variant (for KWP protocols) such as: 'mot6000', Shortname z. B. 'EnginContrModul1', Logical Link, UDS variant name (BV or EV)</p><p>Vehicle (integer): vehicle type (optional) if not entered in LiveVehicle The following values are possible:</p><p>
</p><p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>CU_VW_Coding_Value (Ecu string, vehicle integer)</strong></span></p>
<p>(String)</p>
</td><td align="left">
<p></p>
<p><span class="bold"><strong>Parameter</strong></span> Ecu (String): a control module identifier, such as group name such as 'mot_01', control module variant (for KWP protocols) such as: 'mot6000', Shortname z. B. 'EnginContrModul1', Logical Link, UDS variant name (BV or EV)</p><p>Vehicle (integer): vehicle type (optional) if not entered in LiveVehicle The following values are possible:</p><p>
</p><p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>CU_VW_DataSetNumberOrECUData­ContainerNumber (Ecu string, vehicle integer)</strong></span></p>
<p>(String)</p>
</td><td align="left">
<p></p>
<p><span class="bold"><strong>Parameter</strong></span> Ecu (String): a control module identifier, such as group name such as 'mot_01', control module variant (for KWP protocols) such as: 'mot6000', Shortname z. B. 'EnginContrModul1', Logical Link, UDS variant name (BV or EV)</p><p>Vehicle (integer): vehicle type (optional) if not entered in LiveVehicle The following values are possible:</p><p>
</p><p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>CU_VW_DataSetVersionNumber (Ecu string, vehicle integer)</strong></span></p>
<p>(String)</p>
</td><td align="left">
<p>A data set version number is read out.</p>
<p><span class="bold"><strong>Parameter</strong></span> Ecu (String): a control module identifier, such as group name such as 'mot_01', control module variant (for KWP protocols) such as: 'mot6000', Shortname z. B. 'EnginContrModul1', Logical Link, UDS variant name (BV or EV)</p><p>Vehicle (integer): vehicle type (optional) if not entered in LiveVehicle The following values are possible:</p><p>
</p><p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>CU_VehicleEquipmentCodeAndPRNumber­Combination (Ecu string, vehicle integer)</strong></span></p>
<p>(String)</p>
</td><td align="left">
<p>The vehicle equipment code and PR number combination are read out.</p>
<p><span class="bold"><strong>Parameter</strong></span> Ecu (String): a control module identifier, such as group name such as 'mot_01', control module variant (for KWP protocols) such as: 'mot6000', Shortname z. B. 'EnginContrModul1', Logical Link, UDS variant name (BV or EV)</p><p>Vehicle (integer): vehicle type (optional) if not entered in LiveVehicle The following values are possible:</p><p>
</p><p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>CU_VW_FAZITIdentification (Ecu string, vehicle integer)</strong></span></p>
<p>(String)</p>
</td><td align="left">
<p>The FAZIT identification is read out.</p>
<p><span class="bold"><strong>Parameter</strong></span> Ecu (String): a control module identifier, such as group name such as 'mot_01', control module variant (for KWP protocols) such as: 'mot6000', Shortname z. B. 'EnginContrModul1', Logical Link, UDS variant name (BV or EV)</p><p>Vehicle (integer): vehicle type (optional) if not entered in LiveVehicle The following values are possible:</p><p>
</p><p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>CU_Anzahl_Slave (Ecu string, vehicle integer)</strong></span></p>
<p>(Integer)</p>
</td><td align="left">
<p>The number of slaves is read out.</p>
<p><span class="bold"><strong>Parameter</strong></span> Ecu (String): a control module identifier, such as group name such as 'mot_01', control module variant (for KWP protocols) such as: 'mot6000', Shortname z. B. 'EnginContrModul1', Logical Link, UDS variant name (BV or EV)</p><p>Vehicle (integer): vehicle type (optional) if not entered in LiveVehicle The following values are possible:</p><p>
</p><p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>CU_MCD_VEHICLE_INFO (Ecu string, vehicle integer)</strong></span></p>
<p>(String)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>CU_MCD_VEHICLE_INFO = 'VI_MLBEVO_CAN'</p>
<p>CU_MCD_VEHICLE_INFO = 'VI_MLBEVO_DoIP'</p>
</td><td align="left">
<p>The CU_MCD_VEHICLE_INFO system variable is used to determine information about the current physical bus or the current communication medium.</p>
<p><span class="bold"><strong>Parameter</strong></span> Vehicle (integer): vehicle type (optional) if not entered in LiveVehicle The following values are possible:</p>
<p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p>
<p><span class="bold"><strong>Return value</strong></span> short name of the VEHICLE_INFO that is used</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>CU_ASAM_ODX_File_Identifier (Ecu string, vehicle integer)</strong></span></p>
<p>(String)</p>
<p><span class="bold"><strong>Examples:</strong></span></p>
<p>CU_ASAM_ODX_File_Identifier ('mot_01') = '123'</p>
<p>CU_ASAM_ODX_File_Identifier ('00FF') = '123'</p>
</td><td align="left">
<p>With this function, it is possible to retrieve the ASAM 2D/ODX data set name for the control module that is provided by the operating system after diagnostic entry.</p>
<p><span class="bold"><strong>Parameter</strong></span> Ecu (String): a control module identifier, such as group name such as 'mot_01', control module variant (for KWP protocols) such as: 'mot6000', Shortname z. B. 'EnginContrModul1', Logical Link, UDS variant name (BV or EV), control module address as 2-byte hex string.</p><p>Vehicle (integer): vehicle type (optional) if not entered in LiveVehicle The following values are possible:</p><p>
</p><p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p><p>
</p>
<p><span class="bold"><strong>Return value</strong></span> data set label (string)</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>CU_ASAM_ODX_File_Version (Ecu string, vehicle integer)</strong></span></p>
<p>(String)</p>
<p><span class="bold"><strong>Examples:</strong></span></p>
<p>CU_ASAM_ODX_File_Version ('mot_01') = '12.1'</p>
<p>CU_ASAM_ODX_File_Version ('00FF') = '12.1'</p>
</td><td align="left">
<p>With this function, it is possible to retrieve the ASAM 2D/ODX data set version for the control module, which is provided by the operating system after diagnostic entry.</p>
<p><span class="bold"><strong>Parameter</strong></span> Ecu (String): a control module identifier, such as group name such as 'mot_01', control module variant (for KWP protocols) such as: 'mot6000', Shortname z. B. 'EnginContrModul1', Logical Link, UDS variant name (BV or EV), control module address as 2-byte hex string.</p><p>Vehicle (integer): vehicle type (optional) if not entered in LiveVehicle The following values are possible:</p><p>
</p><p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p>
<p><span class="bold"><strong>Return value</strong></span> data set version (string)</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>CU_SystemNameOrEngineType (Ecu string, vehicle integer)</strong></span></p>
<p>(String)</p>
<p><span class="bold"><strong>Examples:</strong></span></p>
<p>CU_SystemNameOrEngineType ('mot_01') = 'EnginContrModul1'</p>
<p>CU_SystemNameOrEngineType ('00BA') = 'AssemMount'</p>
</td><td align="left">
<p>With this function it is possible to retrieve the system name for the control module that is provided by the operating system after diagnostic entry.</p>
<p><span class="bold"><strong>Parameter</strong></span> Ecu (String): a control module identifier, such as group name such as 'mot_01', control module variant (for KWP protocols) such as: 'mot6000', Shortname z. B. 'EnginContrModul1', Logical Link, UDS variant name (BV or EV), control module address as 2-byte hex string.</p><p>Vehicle (integer): vehicle type (optional) if not entered in LiveVehicle The following values are possible:</p><p>
</p><p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p>
<p><span class="bold"><strong>Return value</strong></span> control module system name (string)</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>CU_ASAM_ODX_Variante (Ecu string, vehicle integer)</strong></span></p>
<p>(String)</p>
<p><span class="bold"><strong>Examples:</strong></span></p>
<p>CU_ASAM_ODX_Variants ('get_02') = 'EV_TCMDQ500021_A01'</p>
<p>CU_ASAM_ODX_Variants ('0620') = 'EV_SunRoof_001'</p>
<p>CU_ASAM_ODX_Variants ('00BA') = 'EV_AEMLearAU64X_002'</p>
</td><td align="left">
<p>With this function, it is possible to check the ODX variant used when starting the tester.</p>
<p><span class="bold"><strong>Parameter</strong></span> Ecu (String): a control module identifier, such as group name such as 'mot_01', control module variant (for KWP protocols) such as: 'mot6000', Shortname z. B. 'EnginContrModul1', Logical Link, UDS variant name (BV or EV), control module address as 2-byte hex string.</p><p>Vehicle (integer): vehicle type (optional) if not entered in LiveVehicle The following values are possible:</p><p>
</p><p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p>
<p><span class="bold"><strong>Return value</strong></span> OCX variants (string)</p>
</td></tr></tbody></table>

**Table 86. Control Module Identification**

###### <a id="d4e20098"></a>7.14.12.3.8. Control module references

<a id="d4e20101"></a>

<table border="1" summary="Control module references"><colgroup><col align="left"/><col align="left"/></colgroup><thead><tr bgcolor="#EEEEEE"><th align="left">Function</th><th align="left">Description</th></tr></thead><tbody><tr><td align="left">
<p><span class="bold"><strong>SGRef_ControlModuleName (String Address)</strong></span></p>
<p>(String)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>SGRef_ControlModuleName('01') = 'engine electronics'</p>
<p>SGRef_ControlModuleName(0x01) = 'engine electronics'</p>
<p>SGRef_ControlModuleName(intVar) = 'engine electronics'</p>
<p>SGRef_ControlModuleName(strVar) = 'engine electronics'</p>
</td><td align="left">
<p>With this function, the attribute content for "Control module name" is read from the "System_5Baud_LL_table_T.xml" file. If the parameter '5 baud address' is not found in the file, then " (empty string) is returned.</p>
<p><span class="bold"><strong>Parameter</strong></span> Address (string): 5 baud-address</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>SGRef_5Baud (String Address)</strong></span></p>
<p>(String)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>SGRef_5-Baud('01') = ‘1‘</p>
<p>SGRef_5-Baud(0x01) = ‘1‘</p>
<p>SGRef_5-Baud(intVar) = ‘1‘</p>
<p>SGRef_5-Baud(strVar) = ‘1‘</p>
</td><td align="left">
<p>With this function, the attribute content for "5 baud" is read from the "System_5Baud_LL_table_S.xml" file. If the parameter '5 baud address' is not found in the file, then " (empty string) is returned.</p>
<p><span class="bold"><strong>Parameter</strong></span> Address (string): 5 baud address in the service reference table</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>SGRef_Longname (String Address)</strong></span></p>
<p>(String)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>SGRef_Longname('01') = ‘Engine Control Module 1‘</p>
<p>SGRef_Longname(0x01) = 'Engine Control Module 1'</p>
<p>SGRef_Longname(intVar) = 'Engine Control Module 1'</p>
<p>SGRef_Longname(strVar) = 'Engine Control Module 1'</p>
</td><td align="left">
<p>With this function, the attribute content for "Long name" is read from the "System_5Baud_LL_table_S.xml" file. If the parameter '5 baud address' is not found in the file, then " (empty string) is returned.</p>
<p><span class="bold"><strong>Parameter</strong></span> Address (string): 5 baud address in the service reference table</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>SGRef_Shortname (String Address)</strong></span></p>
<p>(String)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>SGRef_Shortname('01') = ‘EnginContrModul1‘</p>
<p>SGRef_Shortname(0x01) = 'EnginContrModul1'</p>
<p>SGRef_Shortname(intVar) = 'EnginContrModul1'</p>
<p>SGRef_Shortname(strVar) = 'EnginContrModul1'</p>
</td><td align="left">
<p>With this function, the attribute content for "Short name" is read from the "System_5Baud_LL_table_S.xml" file. If the parameter 5 baud address is not found in the file, then " (empty string) is returned.</p>
<p><span class="bold"><strong>Parameter</strong></span> Address (string): 5 baud address in the service reference table</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>SGRef_Symbol (String Address)</strong></span></p>
<p>(String)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>SGRef_Symbol('01') = ‘MOT_01‘</p>
<p>SGRef_Symbol(0x01) = 'MOT_01'</p>
<p>SGRef_Symbol(intVar) = 'MOT_01'</p>
<p>SGRef_Symbol(strVar) = 'MOT_01'</p>
</td><td align="left">
<p>With this function, the attribute content for "Symbol" is read from the "System_5Baud_LL_table_S.xml" file. If the parameter '5 baud address' is not found in the file, then " (empty string) is returned.</p>
<p><span class="bold"><strong>Parameter</strong></span> Address (string): 5 baud address in the service reference table</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>SGRef_KWP_available (String Address)</strong></span></p>
<p>(String)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>SGRef_KWP_available('01') = ‘true‘</p>
<p>SGRef_KWP_available(0x01) = 'false'</p>
<p>SGRef_KWP_available(intVar) = 'false'</p>
<p>SGRef_KWP_available(strVar) = 'false'</p>
</td><td align="left">
<p>With this function, the attribute content for "KWP_available" is read from the "System_5Baud_LL_table_S.xml" file. If the parameter '5 baud address' is not found in the file, then " (empty string) is returned.</p>
<p><span class="bold"><strong>Parameter</strong></span> Address (string): 5 baud address in the service reference table</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>SGRef_KWP_no_variants (String Address)</strong></span></p>
<p>(String)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>SGRef_KWP_no_variants('01') = ‘false‘</p>
<p>SGRef_KWP_no_variants(0x01) = 'false'</p>
<p>SGRef_KWP_no_variants(intVar) = 'false'</p>
<p>SGRef_KWP_no_variants(strVar) = 'false'</p>
</td><td align="left">
<p>With this function, the attribute content for "KWP_no_variants" is read from the "System_5Baud_LL_table_S.xml" file. If the parameter '5 baud address' is not found in the file, then " (empty string) is returned.</p>
<p><span class="bold"><strong>Parameter</strong></span> Address (string): 5 baud address in the service reference table</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>SGRef_LL_UDS (String Address)</strong></span></p>
<p>(String)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>SGRef_LL_UDS('01') = ‘LL_EnginContrModul1UDS‘</p>
<p>SGRef_LL_UDS(0x01) = 'LL_EnginContrModul1UDS'</p>
<p>SGRef_LL_UDS(intVar) = 'LL_EnginContrModul1UDS'</p>
<p>SGRef_LL_UDS(strVar) = 'LL_EnginContrModul1UDS'</p>
</td><td align="left">
<p>With this function, the attribute content for "LL_UDS" is read from the "System_5Baud_LL_table_S.xml" file. If the parameter '5 baud address' is not found in the file, then " (empty string) is returned.</p>
<p><span class="bold"><strong>Parameter</strong></span> Address (string): 5 baud address in the service reference table</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>SGRef_LL_KWP1281KLINE (String Address)</strong></span></p>
<p>(String)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>SGRef_LL_KWP1281KLINE('01') = ‘LL_EnginContrModul1KWP1281KLINE‘</p>
<p>SGRef_LL_KWP1281KLINE(0x01) = 'LL_EnginContrModul1KWP1281KLINE'</p>
<p>SGRef_LL_KWP1281KLINE(intVar) = 'LL_EnginContrModul1KWP1281KLINE'</p>
<p>SGRef_LL_KWP1281KLINE(strVar) = 'LL_EnginContrModul1KWP1281KLINE'</p>
</td><td align="left">
<p>With this function, the attribute content for "LL_KWP1281KLINE" is read from the "System_5Baud_LL_table_S.xml" file. If the parameter '5 baud address' is not found in the file, then " (empty string) is returned.</p>
<p><span class="bold"><strong>Parameter</strong></span> Address (string): 5 baud address in the service reference table</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>SGRef_LL_KWP1281CAN16 (String Address)</strong></span></p>
<p>(String)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>SGRef_LL_KWP1281CAN16('01') = ‘LL_EnginContrModul1KWP1281CAN16‘</p>
<p>SGRef_LL_KWP1281CAN16(0x01) = 'LL_EnginContrModul1KWP1281CAN16'</p>
<p>SGRef_LL_KWP1281CAN16(intVar) = 'LL_EnginContrModul1KWP1281CAN16'</p>
<p>SGRef_LL_KWP1281CAN16(strVar) = 'LL_EnginContrModul1KWP1281CAN16'</p>
</td><td align="left">
<p>With this function, the attribute content for "LL_KWP1281CAN16" is read from the "System_5Baud_LL_table_S.xml" file. If the parameter '5 baud address' is not found in the file, then " (empty string) is returned.</p>
<p><span class="bold"><strong>Parameter</strong></span> Address (string): 5 baud address in the service reference table</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>SGRef_LL_KWP2000KLINE (String Address)</strong></span></p>
<p>(String)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>SGRef_LL_KWP2000KLINE('01') = ‘LL_EnginContrModul1KWP2000KLINE‘</p>
<p>SGRef_LL_KWP2000KLINE(0x01) = 'LL_EnginContrModul1KWP2000KLINE'</p>
<p>SGRef_LL_KWP2000KLINE(intVar) = 'LL_EnginContrModul1KWP2000KLINE'</p>
<p>SGRef_LL_KWP2000KLINE(strVar) = 'LL_EnginContrModul1KWP2000KLINE'</p>
</td><td align="left">
<p>With this function, the attribute content for "LL_KWP2000KLINE" is read from the "System_5Baud_LL_table_S.xml" file. If the parameter '5 baud address' is not found in the file, then " (empty string) is returned.</p>
<p><span class="bold"><strong>Parameter</strong></span> Address (string): 5 baud address in the service reference table</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>SGRef_LL_KWP2000CAN16 (String Address)</strong></span></p>
<p>(String)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>SGRef_LL_KWP2000CAN16('01') = ‘LL_EnginContrModul1KWP2000CAN16‘</p>
<p>SGRef_LL_KWP2000CAN16(0x01) = 'LL_EnginContrModul1KWP2000CAN16'</p>
<p>SGRef_LL_KWP2000CAN16(intVar) = 'LL_EnginContrModul1KWP2000CAN16'</p>
<p>SGRef_LL_KWP2000CAN16(strVar) = 'LL_EnginContrModul1KWP2000CAN16'</p>
</td><td align="left">
<p>With this function, the attribute content for "LL_KWP2000CAN16" is read from the "System_5Baud_LL_table_S.xml" file. If the parameter '5 baud address' is not found in the file, then " (empty string) is returned.</p>
<p><span class="bold"><strong>Parameter</strong></span> Address (string): 5 baud address in the service reference table</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>SGRef_LL_KWP2000CAN20 (String Address)</strong></span></p>
<p>(String)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>SGRef_LL_KWP2000CAN20('01') = ‘LL_EnginContrModul1KWP1281CAN20‘</p>
<p>SGRef_LL_KWP2000CAN20(0x01) = 'LL_EnginContrModul1KWP1281CAN20'</p>
<p>SGRef_LL_KWP2000CAN20(intVar) = 'LL_EnginContrModul1KWP1281CAN20'</p>
<p>SGRef_LL_KWP2000CAN20(strVar) = 'LL_EnginContrModul1KWP1281CAN20'</p>
</td><td align="left">
<p>With this function, the attribute content for "LL_KWP2000CAN20" is read from the "System_5Baud_LL_table_S.xml" file. If the parameter '5 baud address' is not found in the file, then " (empty string) is returned.</p>
<p><span class="bold"><strong>Parameter</strong></span> Address (string): 5 baud address in the service reference table</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>SGRef_LL_KWP2000CANISO (String Address)</strong></span></p>
<p>(String)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>SGRef_LL_KWP2000CANISO('01') = ‘LL_EnginContrModul1KWP2000CANISO‘</p>
<p>SGRef_LL_KWP2000CANISO(0x01) = 'LL_EnginContrModul1KWP2000CANISO'</p>
<p>SGRef_LL_KWP2000CANISO(intVar) = 'LL_EnginContrModul1KWP2000CANISO'</p>
<p>SGRef_LL_KWP2000CANISO(strVar) = 'LL_EnginContrModul1KWP2000CANISO'</p>
</td><td align="left">
<p>With this function, the attribute content for "KWP2000CANISO" is read from the "System_5Baud_LL_table_S.xml" file. If the parameter '5 baud address' is not found in the file, then " (empty string) is returned.</p>
<p><span class="bold"><strong>Parameter</strong></span> Address (string): 5 baud address in the service reference table</p>
</td></tr></tbody></table>

**Table 87. Control module references**

###### <a id="d4e20321"></a>7.14.12.3.9. DTC memory references

<a id="d4e20324"></a>

<table border="1" summary="DTC memory references"><colgroup><col align="left"/><col align="left"/></colgroup><thead><tr bgcolor="#EEEEEE"><th align="left">Function</th><th align="left">Description</th></tr></thead><tbody><tr><td align="left">
<p><span class="bold"><strong>Text_DTC_VAG (String DtcVagHex)</strong></span></p>
<p>(String)</p>
<p><span class="bold"><strong>Example:</strong></span> Text_DTC_VAG('4C51') = ‘engine temperature too low‘</p>
</td><td align="left">
<p>The function returns the "Text" for the specified access parameter from "DTC_Table_S.xml" and "DTC_Table_T.xml".</p>
<p><span class="bold"><strong>Parameter</strong></span> DtcVagHex (String): DTC-VAG Code Hex in the service reference table</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>Text_DTC_SAE (Integer DtcSaeCode)</strong></span></p>
<p>(String)</p>
<p><span class="bold"><strong>Example:</strong></span> Text_DTC_SAE(3178752) = ‘engine temperature too low‘</p>
</td><td align="left">
<p>The function returns the "Text" for the specified access parameter from "DTC_Table_S.xml" and "DTC_Table_T.xml".</p>
<p><span class="bold"><strong>Parameter</strong></span> DtcSaeCode (Integer): DTC SAE code in the service reference table</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>Text_PUBC_Code (String PubcCode)</strong></span></p>
<p>(String)</p>
<p><span class="bold"><strong>Example:</strong></span> Text_PUBC_Code('P3081') = ‘engine temperature too low‘</p>
</td><td align="left">
<p>The function returns the "Text" for the specified access parameter from "DTC_Table_S.xml" and "DTC_Table_T.xml".</p>
<p><span class="bold"><strong>Parameter</strong></span> PubcCode (String): Text_PUBC_Code in the service reference table</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>PUBC_Code_aus_VAG_Code (String DtcVagHex)</strong></span></p>
<p>(String)</p>
<p><span class="bold"><strong>Example:</strong></span> PUBC_Code_aus_VAG_Code('4C51') = 'P3081'</p>
</td><td align="left">
<p>The function returns the PUBC code for the specified access parameter from "DTC_Table_S.xml".</p>
<p><span class="bold"><strong>Parameter</strong></span> DtcVagHex (String): DTC-VAG Code Hex in the service reference table</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>PUBC_Code_aus_SAE_Code (Integer DtcSaeCode)</strong></span></p>
<p>(String)</p>
<p><span class="bold"><strong>Example:</strong></span> PUBC_Code_aus_SAE_Code(3178752) = 'P3081'</p>
</td><td align="left">
<p>The function returns the PUBC code for the specified access parameter from "DTC_Table_S.xml".</p>
<p><span class="bold"><strong>Parameter</strong></span> DtcSaeCode (Integer): DTC SAE code in the service reference table</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>Text_Fehlerart_KWP1281 (String SymptomNumberHex)</strong></span></p>
<p>(String)</p>
<p><span class="bold"><strong>Example:</strong></span> Text_Fehlerart_KWP1281('0A') = ‘Adaptation threshold exceeded‘</p>
</td><td align="left">
<p>The function returns the "Text" for the specified access parameter from "DTC_fault_symptoms_KWP_1281_S.xml" and "DTC_fault_symptoms_KWP_1281_T.xml".</p>
<p><span class="bold"><strong>Parameter</strong></span> SymptomNumberHex (String): symptom number hex in the service reference table</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>Text_Fehlerart_KWP2000 (String SymptomNumberHex)</strong></span></p>
<p>(String)</p>
<p><span class="bold"><strong>Example:</strong></span> Text_Fehlerart_KWP2000('0B') = ‘Interruption‘</p>
</td><td align="left">
<p>The function returns the "Text" for the specified access parameter from "DTC_fault_symptoms_KWP_2000_S.xml" and "DTC_fault_symptoms_KWP_2000_T.xml".</p>
<p><span class="bold"><strong>Parameter</strong></span> SymptomNumberHex (String): symptom number hex in the service reference table</p>
</td></tr></tbody></table>

**Table 88. DTC memory references**

###### <a id="d4e20411"></a>7.14.12.3.10. DTC memory information

<a id="d4e20414"></a>

<table border="1" summary="DTC memory information"><colgroup><col align="left"/><col align="left"/></colgroup><thead><tr bgcolor="#EEEEEE"><th align="left">Function</th><th align="left">Description</th></tr></thead><tbody><tr><td align="left">
<p><span class="bold"><strong>Number_DTC_sporadic (AdditionalDTCs integer)</strong></span></p>
<p>(Integer)</p>
<p><span class="bold"><strong>Example:</strong></span> the diagnostic object on which the function test depends contains a suspicion rule with DTC P067000 from the engine control module and DTC U112300 from the airbag control module, both with Error 2 = Any (sporadic or static). The DTC P067000 was entered sporadically in the engine control module during diagnostic entry. The DTC P060200 in the engine control module and DTC U112300 in the airbag control module are also entered sporadically. The log book is updated.</p>
<p>Number_DTC_sporadic = 2</p>
<p>Number_DTC_sporadic(0)= 2</p>
<p>Number_DTC_sporadic(1)= 1</p>
<p>The DTC P060200 is not taken into consideration here because it is not contained in the suspicion rule.</p>
</td><td align="left">
<p>The function delivers the number of sporadic DTCs from the amount of DTCs that are contained in the suspicion rule for the diagnostic object associated with the function test. When calling up the function, there is no vehicle communication that determines information from the log book. Two time points can be selected using an option parameter: the status at diagnostic entry and the current log book status. The number determined corresponds to the length of the array, which returns the associated functions DTC_sporadic and Diagnosticaddress_DTC_sporadic.</p>
<p><span class="bold"><strong>Parameter</strong></span> AdditionalDTCs (integer): evaluates current DTCs or DTCs from entry. The following values are possible:</p>
<p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0 or no instruction: current DTCs</p>
</li><li>
<p>1: DTCs from entry</p>
</li></ul></div><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>Anzahl_DTC_statisch (AdditionalDTCs integer)</strong></span></p>
<p>(Integer)</p>
<p><span class="bold"><strong>Example:</strong></span> the diagnostic object on which the function test depends contains a suspicion rule with DTC P067000 from the engine control module and DTC U112300 from the airbag control module, both with Error 2 = Any (sporadic or static). The DTC P067000 was entered as static in the engine control module during diagnostic entry. The DTC P060200 in the engine control module and DTC U112300 in the airbag control module are also entered as sporadic. The log book is updated.</p>
<p>Number_DTC_static = 2</p>
<p>Number_DTC_static(0)= 2</p>
<p>Number_DTC_static(1) = 1</p>
<p>The DTC P060200 is not taken into consideration here because it is not contained in the suspicion rule.</p>
</td><td align="left">
<p>The function delivers the number of static DTCs from the amount of DTCs that are contained in the suspicion rule for the diagnostic object associated with the function test. When calling up the function, there is no vehicle communication that determines information from the log book. Two time points can be selected using an option parameter: the status at diagnostic entry and the current log book status. The number determined corresponds to the length of the array, which returns the associated functions DTC_static and Diagnosticaddress_DTC_static.</p>
<p><span class="bold"><strong>Parameter</strong></span> AdditionalDTCs (integer): evaluates current DTCs or DTCs from entry. The following values are possible:</p>
<p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0 or no instruction: current DTCs</p>
</li><li>
<p>1: DTCs from entry</p>
</li></ul></div><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>DTC_sporadisch(Integer AddtionalDTCs)</strong></span></p>
<p>(String[])</p>
<p><span class="bold"><strong>Example:</strong></span> the diagnostic object on which the function test depends contains a suspicion rule with DTC P067000 from the engine control module and DTC U112300 from the airbag control module, both with Error 2 = Any (sporadic or static). The DTC P067000 was entered sporadically in the engine control module during diagnostic entry. The DTC P060200 in the engine control module and DTC U112300 in the airbag control module are also entered sporadically. The log book is updated.</p>
<p>DTC_sporadic= {'P067000', 'U112300'}</p>
<p>DTC_sporadic(0) = {'P067000', 'U112300'}</p>
<p>DTC_sporadic(1) = {'P067000'}</p>
<p>The DTC P060200 is not taken into consideration here because it is not contained in the suspicion rule.</p>
</td><td align="left">
<p>The function delivers sporadic DTCs from those that are contained in the suspicion rule for the diagnostic object associated with the function test. A one-dimensional array from the type string is returned so that the target variable in the expression must be specified without square brackets. When calling up the function, there is no vehicle communication that determines information from the log book. Two time points can be selected using an option parameter: the status at diagnostic entry and the current log book status.</p>
<p>Note: the corresponding diagnostic addresses of the control modules and the number of DTCs present (and therefore the length of the array) can be determined using the associated functions Diagnosticaddress_DTC_sporadic and Number_DTC_sporadic.</p>
<p><span class="bold"><strong>Parameter</strong></span> AdditionalDTCs (integer): evaluates current DTCs or DTCs from entry. The following values are possible:</p>
<p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0 or no instruction: current DTCs</p>
</li><li>
<p>1: DTCs from entry</p>
</li></ul></div><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>DTC_statisch(Integer AdditionalDTCs)</strong></span></p>
<p>(String[])</p>
<p><span class="bold"><strong>Example:</strong></span> the diagnostic object on which the function test depends contains a suspicion rule with DTC P067000 from the engine control module and DTC U112300 from the airbag control module, both with Error 2 = Any (sporadic or static). The DTC P067000 was entered as static in the engine control module during diagnostic entry. The DTC P060200 in the engine control module and DTC U112300 in the airbag control module are also entered as sporadic. The log book is updated.</p>
<p>DTC_static = {'P067000', 'U112300'}</p>
<p>DTC_statisch(0) = {'P067000', 'U112300'}</p>
<p>DTC_statisch(1) = {'P067000'}</p>
<p>The DTC P060200 is not taken into consideration here because it is not contained in the suspicion rule.</p>
</td><td align="left">
<p>The function delivers static DTCs from those that are contained in the suspicion rule for the diagnostic object associated with the function test. A one-dimensional array from the type string is returned so that the target variable in the expression must be specified without square brackets. When calling up the function, there is no vehicle communication that determines information from the log book. Two time points can be selected using an option parameter: the status at diagnostic entry and the current log book status.</p>
<p>Note: the corresponding diagnostic addresses of the control modules and the number of DTCs present (and therefore the length of the array) can be determined using the associated functions Diagnosticaddress_DTC_static and Number_DTC_static.</p>
<p><span class="bold"><strong>Parameter</strong></span> AdditionalDTCs (integer): evaluates current DTCs or DTCs from entry. The following values are possible:</p>
<p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0 or no instruction: current DTCs</p>
</li><li>
<p>1: DTCs from entry</p>
</li></ul></div><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>Diagnoseadresse_DTC_sporadic( Integer AdditionalDTCs)</strong></span></p>
<p>(String[])</p>
<p><span class="bold"><strong>Example:</strong></span> the diagnostic object on which the function test depends contains a suspicion rule with DTC P067000 from the engine control module and DTC U112300 from the airbag control module, both with Error 2 = Any (sporadic or static). The DTC P067000 was entered sporadically in the engine control module during diagnostic entry. The DTC P060200 in the engine control module and DTC U112300 in the airbag control module are also entered sporadically. The log book is updated.</p>
<p>Diagnosticaddress_DTC_sporadic = {'0001', '0015'}</p>
<p>Diagnosticaddress_DTC_sporadic(0) = {'0001', '0015'}</p>
<p>Diagnosticaddress_DTC_sporadic(1) = {'0001'}</p>
<p>The DTC P060200 is not taken into consideration here because it is not contained in the suspicion rule.</p>
</td><td align="left">
<p>The function delivers the corresponding diagnostic addresses for the DTC that are determined by the DTC_sporadic function. A one-dimensional array from the type string is returned so that the target variable in the expression must be specified without square brackets. The diagnostic address in field position 0 corresponds to the DTC in field position 0 of the array, which is returned by the DTC_sporadic function. When calling up the function, there is no vehicle communication that determines information from the log book. Two time points can be selected using an option parameter: the status at diagnostic entry and the current log book status.</p>
<p>Note: the number of DTCs present (and therefore, the length of the array) can be determined using the associated Number_DTC_sporadic function.</p>
<p><span class="bold"><strong>Parameter</strong></span> AdditionalDTCs (integer): evaluates current DTCs or DTCs from entry. The following values are possible:</p>
<p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0 or no instruction: current DTCs</p>
</li><li>
<p>1: DTCs from entry</p>
</li></ul></div><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>Diagnoseadresse_DTC_statisch(Integer AdditionalDTCs)</strong></span></p>
<p>(String[])</p>
<p><span class="bold"><strong>Example:</strong></span> the diagnostic object on which the function test depends contains a suspicion rule with DTC P067000 from the engine control module and DTC U112300 from the airbag control module, both with Error 2 = Any (sporadic or static). The DTC P067000 was entered as static in the engine control module during diagnostic entry. The DTC P060200 in the engine control module and DTC U112300 in the airbag control module are also entered as sporadic. The log book is updated.</p>
<p>Diagnosticaddress_DTC_static = {'0001', '0015'}</p>
<p>Diagnosticaddress_DTC_statich(0) = {'0001', '0015'}</p>
<p>Diagnosticaddress_DTC_static(1) = {'0001'}</p>
<p>The DTC P060200 is not taken into consideration here because it is not contained in the suspicion rule.</p>
</td><td align="left">
<p>The function delivers the corresponding diagnostic addresses for the DTC that are determined by the DTC_staticfunction. A one-dimensional array from the type string is returned so that the target variable in the expression must be specified without square brackets. The diagnostic address in field position 0 corresponds to the DTC in field position 0 of the array, which is returned by the DTC_static function. When calling up the function, there is no vehicle communication that determines information from the log book. Two time points can be selected using an option parameter: the status at diagnostic entry and the current log book status.</p>
<p>Note: the number of DTCs present (and therefore, the length of the array) can be determined using the associated Number_DTC_static function.</p>
<p><span class="bold"><strong>Parameter</strong></span> AdditionalDTCs (integer): evaluates current DTCs or DTCs from entry. The following values are possible:</p>
<p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0 or no instruction: current DTCs</p>
</li><li>
<p>1: DTCs from entry</p>
</li></ul></div><p>
</p>
</td></tr></tbody></table>

**Table 89. DTC memory information**

###### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Ablauf.Ausdruck.Funktionen.SymptomVAG"></a>7.14.12.3.11. VAG Symptom

<a id="d4e20557"></a>

<table border="1" summary="VAG Symptom"><colgroup><col align="left"/><col align="left"/></colgroup><thead><tr bgcolor="#EEEEEE"><th align="left">Function</th><th align="left">Description</th></tr></thead><tbody><tr><td align="left">
<p><span class="bold"><strong>Symptom_Status_VAG (Integer Ecu, Integer VAG, Long DtcSymptom, Integer Vehicle)</strong></span></p>
<p>(Long)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>Symptom_Status_VAG(0x01, 123, 0x507E54) = 10001001</p>
</td><td align="left">
<p>This function allows you to check the status of a DTC memory entry that is provided by the operating system after diagnostic entry. The status can only be read for UDS DTC memory entries.</p>
<p>If the 'DtcSymptom' parameter is set, then the DTC memory code will be ignored. With VAG/SAE, the runtime for the available DTC memory type must always be selected.</p>
<p>The function returns the result from diagnostic entry. Runtime changes made afterward to DTC memory entries in the vehicle are ignored.</p>
<p>Hexadecimal numbers are automatically converted to decimal numbers if the hexadecimal number has "0x" at the beginning.</p>
<p>If the environmental conditions cannot be determined, the default value of 0 is returned.</p>
<p><span class="bold"><strong>Parameter</strong></span> Ecu (Integer): 5 baud control module address, such as 0x01</p>
<p><span class="bold"><strong>Parameter</strong></span> VAG (Integer): DTC memory VAG code</p>
<p><span class="bold"><strong>Parameter</strong></span> DtcSymptom (optional, Long): DTC symptom</p>
<p><span class="bold"><strong>Parameter</strong></span> Vehicle (integer): vehicle type (optional) if not entered in FrozenVehicle The following values are possible:</p>
<p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>Symptom_Datum_Zeit_VAG (Integer Ecu, Integer VAG, Long DtcSymptom, Integer Vehicle)</strong></span></p>
<p>(Long)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>Symptom_ Datum_Zeit_VAG(0x01, 123, 0x507E54) = 203958743</p>
</td><td align="left">
<p>This function allows you to check the "Date/time" environmental condition for a symptom that is provided by the operating system after diagnostic entry.</p>
<p>If the 'DtcSymptom' parameter is set, then the DTC memory code will be ignored. With VAG/SAE, the runtime for the available DTC memory type must always be selected.</p>
<p>The function returns the result from diagnostic entry. Runtime changes made afterward to DTC memory entries in the vehicle are ignored.</p>
<p>Hexadecimal numbers are automatically converted to decimal numbers if the hexadecimal number has "0x" at the beginning.</p>
<p>If the environmental conditions cannot be determined, the default value of 0 is returned.</p>
<p><span class="bold"><strong>Parameter</strong></span> Ecu (Integer): 5 baud control module address, such as 0x01</p>
<p><span class="bold"><strong>Parameter</strong></span> VAG (Integer): DTC memory VAG code</p>
<p><span class="bold"><strong>Parameter</strong></span> DtcSymptom (optional, Long): DTC symptom</p>
<p><span class="bold"><strong>Parameter</strong></span> Vehicle (integer): vehicle type (optional) if not entered in FrozenVehicle The following values are possible:</p>
<p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>Symptom_km_Stand_DTC_VAG (Integer Ecu, Integer VAG, Long DtcSymptom, Integer Vehicle)</strong></span></p>
<p>(Integer)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>Symptom_km_Stand_DTC_VAG(0x01, 123, 0x507E54) = 62</p>
</td><td align="left">
<p>This function allows you to check the "Mileage DTC" environmental condition for a symptom that is provided by the operating system after diagnostic entry.</p>
<p>If the 'DtcSymptom' parameter is set, then the DTC memory code will be ignored. With VAG/SAE, the runtime for the available DTC memory type must always be selected.</p>
<p>The function returns the result from diagnostic entry. Runtime changes made afterward to DTC memory entries in the vehicle are ignored.</p>
<p>Hexadecimal numbers are automatically converted to decimal numbers if the hexadecimal number has "0x" at the beginning.</p>
<p>If the environmental conditions cannot be determined, the default value of 0 is returned.</p>
<p><span class="bold"><strong>Parameter</strong></span> Ecu (Integer): 5 baud control module address, such as 0x01</p>
<p><span class="bold"><strong>Parameter</strong></span> VAG (Integer): DTC memory VAG code</p>
<p><span class="bold"><strong>Parameter</strong></span> DtcSymptom (optional, Long): DTC symptom</p>
<p><span class="bold"><strong>Parameter</strong></span> Vehicle (integer): vehicle type (optional) if not entered in FrozenVehicle The following values are possible:</p>
<p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>Symptom_Prioritaet_VAG (Integer Ecu, Integer VAG, Long DtcSymptom, Integer Vehicle)</strong></span></p>
<p>(Integer)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>Symptom_Priority_VAG (0x01, 123, 0x507E54) = 1</p>
</td><td align="left">
<p>This function allows you to check the "Priority" environmental condition for a symptom that is provided by the operating system after diagnostic entry.</p>
<p>If the 'DtcSymptom' parameter is set, then the DTC memory code will be ignored. With VAG/SAE, the runtime for the available DTC memory type must always be selected.</p>
<p>The function returns the result from diagnostic entry. Runtime changes made afterward to DTC memory entries in the vehicle are ignored.</p>
<p>Hexadecimal numbers are automatically converted to decimal numbers if the hexadecimal number has "0x" at the beginning.</p>
<p>If the environmental conditions cannot be determined, the default value of 0 is returned.</p>
<p><span class="bold"><strong>Parameter</strong></span> Ecu (Integer): 5 baud control module address, such as 0x01</p>
<p><span class="bold"><strong>Parameter</strong></span> VAG (Integer): DTC memory VAG code</p>
<p><span class="bold"><strong>Parameter</strong></span> DtcSymptom (optional, Long): DTC symptom</p>
<p><span class="bold"><strong>Parameter</strong></span> Vehicle (integer): vehicle type (optional) if not entered in FrozenVehicle The following values are possible:</p>
<p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>Symptom_Haeufigkeitszaehler_VAG (Integer Ecu, Integer VAG, Long DtcSymptom, Integer Vehicle)</strong></span></p>
<p>(Integer)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>Symptom_Frequencycounter_VAG (0x01, 123, 0x507E54) = 1</p>
</td><td align="left">
<p>This function allows you to check the "Frequency counter" environmental condition for a symptom that is provided by the operating system after diagnostic entry.</p>
<p>If the 'DtcSymptom' parameter is set, then the DTC memory code will be ignored. With VAG/SAE, the runtime for the available DTC memory type must always be selected.</p>
<p>The function returns the result from diagnostic entry. Runtime changes made afterward to DTC memory entries in the vehicle are ignored.</p>
<p>Hexadecimal numbers are automatically converted to decimal numbers if the hexadecimal number has "0x" at the beginning.</p>
<p>If the environmental conditions cannot be determined, the default value of 0 is returned.</p>
<p><span class="bold"><strong>Parameter</strong></span> Ecu (Integer): 5 baud control module address, such as 0x01</p>
<p><span class="bold"><strong>Parameter</strong></span> VAG (Integer): DTC memory VAG code</p>
<p><span class="bold"><strong>Parameter</strong></span> DtcSymptom (optional, Long): DTC symptom</p>
<p><span class="bold"><strong>Parameter</strong></span> Vehicle (integer): vehicle type (optional) if not entered in FrozenVehicle The following values are possible:</p>
<p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>Symptom_Verlernzaehler_VAG (Integer Ecu, Integer VAG, Long DtcSymptom, Integer Vehicle)</strong></span></p>
<p>(Integer)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>Symptom_Unlearning counter_VAG(0x01, 123, 0x507E54) = 26</p>
</td><td align="left">
<p>This function allows you to check the "Programming counter" environmental condition for a symptom that is provided by the operating system after diagnostic entry.</p>
<p>If the 'DtcSymptom' parameter is set, then the DTC memory code will be ignored. With VAG/SAE, the runtime for the available DTC memory type must always be selected.</p>
<p>The function returns the result from diagnostic entry. Runtime changes made afterward to DTC memory entries in the vehicle are ignored.</p>
<p>Hexadecimal numbers are automatically converted to decimal numbers if the hexadecimal number has "0x" at the beginning.</p>
<p>If the environmental conditions cannot be determined, the default value of 0 is returned.</p>
<p><span class="bold"><strong>Parameter</strong></span> Ecu (Integer): 5 baud control module address, such as 0x01</p>
<p><span class="bold"><strong>Parameter</strong></span> VAG (Integer): DTC memory VAG code</p>
<p><span class="bold"><strong>Parameter</strong></span> DtcSymptom (optional, Long): DTC symptom</p>
<p><span class="bold"><strong>Parameter</strong></span> Vehicle (integer): vehicle type (optional) if not entered in FrozenVehicle The following values are possible:</p>
<p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p>
</td></tr></tbody></table>

**Table 90. VAG Symptom**

###### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Ablauf.Ausdruck.Funktionen.SymptomSAE"></a>7.14.12.3.12. SAE Symptom

<a id="d4e20738"></a>

<table border="1" summary="SAE Symptom"><colgroup><col align="left"/><col align="left"/></colgroup><thead><tr bgcolor="#EEEEEE"><th align="left">Function</th><th align="left">Description</th></tr></thead><tbody><tr><td align="left">
<p><span class="bold"><strong>Symptom_Status_SAE (Integer Ecu, Integer SAE, Long DtcSymptom, Integer Vehicle)</strong></span></p>
<p>(Long)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>Symptom_Status_SAE(0x01, 5275220,0x507E54) = 10001001</p>
</td><td align="left">
<p>This function allows you to check the status of a DTC memory entry that is provided by the operating system after diagnostic entry. The status can only be read for UDS DTC memory entries.</p>
<p>If the 'DtcSymptom' parameter is set, then the DTC memory code will be ignored. With VAG/SAE, the runtime for the available DTC memory type must always be selected.</p>
<p>The function returns the result from diagnostic entry. Runtime changes made afterward to DTC memory entries in the vehicle are ignored.</p>
<p>Hexadecimal numbers are automatically converted to decimal numbers if the hexadecimal number has "0x" at the beginning.</p>
<p>If the environmental conditions cannot be determined, the default value of 0 is returned.</p>
<p><span class="bold"><strong>Parameter</strong></span> Ecu (Integer): 5 baud control module address, such as 0x01</p>
<p><span class="bold"><strong>Parameter</strong></span> SAE (Integer): DTC memory SAE code</p>
<p><span class="bold"><strong>Parameter</strong></span> DtcSymptom (optional, Long): DTC symptom</p>
<p><span class="bold"><strong>Parameter</strong></span> Vehicle (integer): vehicle type (optional) if not entered in FrozenVehicle The following values are possible:</p>
<p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>Symptom_Datum_Zeit_SAE (Integer Ecu, Integer SAE, Long DtcSymptom, Integer Vehicle)</strong></span></p>
<p>(Long)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>Symptom_ Date_Time_SAE(0x01, 5275220, 0x507E54) = 203958743</p>
</td><td align="left">
<p>This function allows you to check the "Date/time" environmental condition for a symptom that is provided by the operating system after diagnostic entry.</p>
<p>If the 'DtcSymptom' parameter is set, then the DTC memory code will be ignored. With VAG/SAE, the runtime for the available DTC memory type must always be selected.</p>
<p>The function returns the result from diagnostic entry. Runtime changes made afterward to DTC memory entries in the vehicle are ignored.</p>
<p>Hexadecimal numbers are automatically converted to decimal numbers if the hexadecimal number has "0x" at the beginning.</p>
<p>If the environmental conditions cannot be determined, the default value of 0 is returned.</p>
<p><span class="bold"><strong>Parameter</strong></span> Ecu (Integer): 5 baud control module address, such as 0x01</p>
<p><span class="bold"><strong>Parameter</strong></span> SAE (Integer): DTC memory SAE code</p>
<p><span class="bold"><strong>Parameter</strong></span> DtcSymptom (optional, Long): DTC symptom</p>
<p><span class="bold"><strong>Parameter</strong></span> Vehicle (integer): vehicle type (optional) if not entered in FrozenVehicle The following values are possible:</p>
<p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>Symptom_km_Stand_DTC_SAE (Integer Ecu, Integer SAE, Long DtcSymptom, Integer Vehicle)</strong></span></p>
<p>(Integer)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>Symptom_km_Status_DTC_SAE(0x01, 5275220, 0x507E54) = 62</p>
</td><td align="left">
<p>This function allows you to check the "Mileage DTC" environmental condition for a symptom that is provided by the operating system after diagnostic entry.</p>
<p>If the 'DtcSymptom' parameter is set, then the DTC memory code will be ignored. With VAG/SAE, the runtime for the available DTC memory type must always be selected.</p>
<p>The function returns the result from diagnostic entry. Runtime changes made afterward to DTC memory entries in the vehicle are ignored.</p>
<p>Hexadecimal numbers are automatically converted to decimal numbers if the hexadecimal number has "0x" at the beginning.</p>
<p>If the environmental conditions cannot be determined, the default value of 0 is returned.</p>
<p><span class="bold"><strong>Parameter</strong></span> Ecu (Integer): 5 baud control module address, such as 0x01</p>
<p><span class="bold"><strong>Parameter</strong></span> SAE (Integer): DTC memory VAG code</p>
<p><span class="bold"><strong>Parameter</strong></span> DtcSymptom (optional, Long): DTC symptom</p>
<p><span class="bold"><strong>Parameter</strong></span> Vehicle (integer): vehicle type (optional) if not entered in FrozenVehicle The following values are possible:</p>
<p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>Symptom_Prioritaet_SAE (Integer Ecu, Integer SAE, Long DtcSymptom, Integer Vehicle)</strong></span></p>
<p>(Integer)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>Symptom_Priority_SAE(0x01, 5275220, 0x507E54) = 1</p>
</td><td align="left">
<p>This function allows you to check the "Priority" environmental condition for a symptom that is provided by the operating system after diagnostic entry.</p>
<p>If the 'DtcSymptom' parameter is set, then the DTC memory code will be ignored. With VAG/SAE, the runtime for the available DTC memory type must always be selected.</p>
<p>The function returns the result from diagnostic entry. Runtime changes made afterward to DTC memory entries in the vehicle are ignored.</p>
<p>Hexadecimal numbers are automatically converted to decimal numbers if the hexadecimal number has "0x" at the beginning.</p>
<p>If the environmental conditions cannot be determined, the default value of 0 is returned.</p>
<p><span class="bold"><strong>Parameter</strong></span> Ecu (Integer): 5 baud control module address, such as 0x01</p>
<p><span class="bold"><strong>Parameter</strong></span> SAE (Integer): DTC memory SAE code</p>
<p><span class="bold"><strong>Parameter</strong></span> DtcSymptom (optional, Long): DTC symptom</p>
<p><span class="bold"><strong>Parameter</strong></span> Vehicle (integer): vehicle type (optional) if not entered in FrozenVehicle The following values are possible:</p>
<p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>Symptom_Haeufigkeitszaehler_SAE (Integer Ecu, Integer SAE, Long DtcSymptom, Integer Vehicle)</strong></span></p>
<p>(Integer)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>Symptom_Frequency counter_SAE (0x01, 5275220, 0x507E54) = 1</p>
</td><td align="left">
<p>This function allows you to check the "Frequency counter" environmental condition for a symptom that is provided by the operating system after diagnostic entry.</p>
<p>If the 'DtcSymptom' parameter is set, then the DTC memory code will be ignored. With VAG/SAE, the runtime for the available DTC memory type must always be selected.</p>
<p>The function returns the result from diagnostic entry. Runtime changes made afterward to DTC memory entries in the vehicle are ignored.</p>
<p>Hexadecimal numbers are automatically converted to decimal numbers if the hexadecimal number has "0x" at the beginning.</p>
<p>If the environmental conditions cannot be determined, the default value of 0 is returned.</p>
<p><span class="bold"><strong>Parameter</strong></span> Ecu (Integer): 5 baud control module address, such as 0x01</p>
<p><span class="bold"><strong>Parameter</strong></span> SAE (Integer): DTC memory SAE code</p>
<p><span class="bold"><strong>Parameter</strong></span> DtcSymptom (optional, Long): DTC symptom</p>
<p><span class="bold"><strong>Parameter</strong></span> Vehicle (integer): vehicle type (optional) if not entered in FrozenVehicle The following values are possible:</p>
<p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>Symptom_Verlernzaehler_SAE (Integer Ecu, Integer SAE, Long DtcSymptom, Integer Vehicle)</strong></span></p>
<p>(Integer)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>Symptom_Unlearning counter_SAE(0x01, 5275220, 0x507E54) = 26</p>
</td><td align="left">
<p>This function allows you to check the "Programming counter" environmental condition for a symptom that is provided by the operating system after diagnostic entry.</p>
<p>If the 'DtcSymptom' parameter is set, then the DTC memory code will be ignored. With VAG/SAE, the runtime for the available DTC memory type must always be selected.</p>
<p>The function returns the result from diagnostic entry. Runtime changes made afterward to DTC memory entries in the vehicle are ignored.</p>
<p>Hexadecimal numbers are automatically converted to decimal numbers if the hexadecimal number has "0x" at the beginning.</p>
<p>If the environmental conditions cannot be determined, the default value of 0 is returned.</p>
<p><span class="bold"><strong>Parameter</strong></span> Ecu (Integer): 5 baud control module address, such as 0x01</p>
<p><span class="bold"><strong>Parameter</strong></span> SAE (Integer): DTC memory SAE code</p>
<p><span class="bold"><strong>Parameter</strong></span> DtcSymptom (optional, Long): DTC symptom</p>
<p><span class="bold"><strong>Parameter</strong></span> Vehicle (integer): vehicle type (optional) if not entered in FrozenVehicle The following values are possible:</p>
<p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p>
</td></tr></tbody></table>

**Table 91. SAE Symptom**

###### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Ablauf.Ausdruck.Funktionen.SymptomPUBC"></a>7.14.12.3.13. PUBC Symptom

<a id="d4e20919"></a>

<table border="1" summary="PUBC Symptom"><colgroup><col align="left"/><col align="left"/></colgroup><thead><tr bgcolor="#EEEEEE"><th align="left">Function</th><th align="left">Description</th></tr></thead><tbody><tr><td align="left">
<p><span class="bold"><strong>Symptom_Status_PUBC (Integer Ecu, String PUBC, Long DtcSymptom, Integer Vehicle)</strong></span></p>
<p>(Long)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>Symptom_Status_PUBC(0x01, 'C107E54',0x507E54) = 10001001</p>
</td><td align="left">
<p>This function allows you to check the status of a DTC memory entry that is provided by the operating system after diagnostic entry. The status can only be read for UDS DTC memory entries.</p>
<p>If the 'DtcSymptom' parameter is set, then the 'PUBC' parameter will be ignored.</p>
<p>The function returns the result from diagnostic entry. Runtime changes made afterward to DTC memory entries in the vehicle are ignored.</p>
<p>Hexadecimal numbers are automatically converted to decimal numbers if the hexadecimal number has "0x" at the beginning.</p>
<p>If the environmental conditions cannot be determined, the default value of 0 is returned.</p>
<p><span class="bold"><strong>Parameter</strong></span> Ecu (Integer): 5 baud control module address, such as 0x01</p>
<p><span class="bold"><strong>Parameter</strong></span> PUBC (String): DTC memory PUBC code</p>
<p><span class="bold"><strong>Parameter</strong></span> DtcSymptom (optional, Long): DTC symptom</p>
<p><span class="bold"><strong>Parameter</strong></span> Vehicle (integer): vehicle type (optional) if not entered in FrozenVehicle The following values are possible:</p>
<p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>Symptom_Datum_Zeit_PUBC (Integer Ecu, String PUBC, Long DtcSymptom, Integer Vehicle)</strong></span></p>
<p>(Long)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>Symptom_Date_Time_PUBC(0x01, 'C107E54', 0x507E54) = 203958743</p>
</td><td align="left">
<p>This function allows you to check the "Date/time" environmental condition for a symptom that is provided by the operating system after diagnostic entry.</p>
<p>If the 'DtcSymptom' parameter is set, then the 'PUBC' parameter will be ignored.</p>
<p>The function returns the result from diagnostic entry. Runtime changes made afterward to DTC memory entries in the vehicle are ignored.</p>
<p>Hexadecimal numbers are automatically converted to decimal numbers if the hexadecimal number has "0x" at the beginning.</p>
<p>If the environmental conditions cannot be determined, the default value of 0 is returned.</p>
<p><span class="bold"><strong>Parameter</strong></span> Ecu (Integer): 5 baud control module address, such as 0x01</p>
<p><span class="bold"><strong>Parameter</strong></span> PUBC (String): DTC memory PUBC code</p>
<p><span class="bold"><strong>Parameter</strong></span> DtcSymptom (optional, Long): DTC symptom</p>
<p><span class="bold"><strong>Parameter</strong></span> Vehicle (integer): vehicle type (optional) if not entered in FrozenVehicle The following values are possible:</p>
<p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>Symptom_km_Stand_DTC_PUBC (Integer Ecu, String PUBC, Long DtcSymptom, Integer Vehicle)</strong></span></p>
<p>(Integer)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>Symptom_km_status_DTC_PUBC(0x01, 'C107E54', 0x507E54) = 62</p>
</td><td align="left">
<p>This function allows you to check the "Mileage DTC" environmental condition for a symptom that is provided by the operating system after diagnostic entry.</p>
<p>If the 'DtcSymptom' parameter is set, then the 'PUBC' parameter will be ignored.</p>
<p>The function returns the result from diagnostic entry. Runtime changes made afterward to DTC memory entries in the vehicle are ignored.</p>
<p>Hexadecimal numbers are automatically converted to decimal numbers if the hexadecimal number has "0x" at the beginning.</p>
<p>If the environmental conditions cannot be determined, the default value of 0 is returned.</p>
<p><span class="bold"><strong>Parameter</strong></span> Ecu (Integer): 5 baud control module address, such as 0x01</p>
<p><span class="bold"><strong>Parameter</strong></span> PUBC (String): DTC memory PUBC code</p>
<p><span class="bold"><strong>Parameter</strong></span> DtcSymptom (optional, Long): DTC symptom</p>
<p><span class="bold"><strong>Parameter</strong></span> Vehicle (integer): vehicle type (optional) if not entered in FrozenVehicle The following values are possible:</p>
<p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>Symptom_Prioritaet_PUBC (Integer Ecu, String PUBC, Long DtcSymptom, Integer Vehicle)</strong></span></p>
<p>(Integer)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>Symptom_priority_PUBC(0x01, 'C107E54', 0x507E54) = 1</p>
</td><td align="left">
<p>This function allows you to check the "Priority" environmental condition for a symptom that is provided by the operating system after diagnostic entry.</p>
<p>If the 'DtcSymptom' parameter is set, then the 'PUBC' parameter will be ignored.</p>
<p>The function returns the result from diagnostic entry. Runtime changes made afterward to DTC memory entries in the vehicle are ignored.</p>
<p>Hexadecimal numbers are automatically converted to decimal numbers if the hexadecimal number has "0x" at the beginning.</p>
<p>If the environmental conditions cannot be determined, the default value of 0 is returned.</p>
<p><span class="bold"><strong>Parameter</strong></span> Ecu (Integer): 5 baud control module address, such as 0x01</p>
<p><span class="bold"><strong>Parameter</strong></span> PUBC (String): DTC memory PUBC code</p>
<p><span class="bold"><strong>Parameter</strong></span> DtcSymptom (optional, Long): DTC symptom</p>
<p><span class="bold"><strong>Parameter</strong></span> Vehicle (integer): vehicle type (optional) if not entered in FrozenVehicle The following values are possible:</p>
<p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>Symptom_Haeufigkeitszaehler_PUBC (Integer Ecu, String PUBC, Long DtcSymptom, Integer Vehicle)</strong></span></p>
<p>(Integer)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>Symptom_Frequencycounter_PUBC (0x01, 'C107E54', 0x507E54) = 1</p>
</td><td align="left">
<p>This function allows you to check the "Frequency counter" environmental condition for a symptom that is provided by the operating system after diagnostic entry.</p>
<p>If the 'DtcSymptom' parameter is set, then the 'PUBC' parameter will be ignored.</p>
<p>The function returns the result from diagnostic entry. Runtime changes made afterward to DTC memory entries in the vehicle are ignored.</p>
<p>Hexadecimal numbers are automatically converted to decimal numbers if the hexadecimal number has "0x" at the beginning.</p>
<p>If the environmental conditions cannot be determined, the default value of 0 is returned.</p>
<p><span class="bold"><strong>Parameter</strong></span> Ecu (Integer): 5 baud control module address, such as 0x01</p>
<p><span class="bold"><strong>Parameter</strong></span> PUBC (String): DTC memory PUBC code</p>
<p><span class="bold"><strong>Parameter</strong></span> DtcSymptom (optional, Long): DTC symptom</p>
<p><span class="bold"><strong>Parameter</strong></span> Vehicle (integer): vehicle type (optional) if not entered in FrozenVehicle The following values are possible:</p>
<p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>Symptom_Verlernzaehler_PUBC (Integer Ecu, String PUBC, Long DtcSymptom, Integer Vehicle)</strong></span></p>
<p>(Integer)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>Symptom_Unlearning counter_PUBC(0x01, 'C107E54', 0x507E54) = 26</p>
</td><td align="left">
<p>This function allows you to check the "Programming counter" environmental condition for a symptom that is provided by the operating system after diagnostic entry.</p>
<p>If the 'DtcSymptom' parameter is set, then the 'PUBC' parameter will be ignored.</p>
<p>The function returns the result from diagnostic entry. Runtime changes made afterward to DTC memory entries in the vehicle are ignored.</p>
<p>Hexadecimal numbers are automatically converted to decimal numbers if the hexadecimal number has "0x" at the beginning.</p>
<p>If the environmental conditions cannot be determined, the default value of 0 is returned.</p>
<p><span class="bold"><strong>Parameter</strong></span> Ecu (Integer): 5 baud control module address, such as 0x01</p>
<p><span class="bold"><strong>Parameter</strong></span> PUBC (String): DTC memory PUBC code</p>
<p><span class="bold"><strong>Parameter</strong></span> DtcSymptom (optional, Long): DTC symptom</p>
<p><span class="bold"><strong>Parameter</strong></span> Vehicle (integer): vehicle type (optional) if not entered in FrozenVehicle The following values are possible:</p>
<p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>0: LiveVehicle</p>
</li><li>
<p>1: FrozenVehicle</p>
</li></ul></div><p>
</p>
</td></tr></tbody></table>

**Table 92. PUBC Symptom**

###### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Ablauf.Ausdruck.Funktionen.Backendsysteme"></a>7.14.12.3.14. Backend systems

<a id="d4e21100"></a>

<table border="1" summary="Backend systems"><colgroup><col align="left"/><col align="left"/></colgroup><thead><tr bgcolor="#EEEEEE"><th align="left">Function</th><th align="left">Description</th></tr></thead><tbody><tr><td align="left">
<p><span class="bold"><strong>In-service date</strong></span></p>
<p>(String)</p>
<p><span class="bold"><strong>Example:</strong></span> DATE = '2002-12-15'</p>
</td><td align="left">
<p>The function provides the in-service date noted in Carport for every vehicle.</p>
</td></tr><tr><td align="left">
<p><span class="bold"><strong>OrMa_Data(String ApprovalType)</strong></span></p>
<p>(String)</p>
<p><span class="bold"><strong>Example:</strong></span></p>
<p>OrMa_Data('customerConsentStatement') = Yes/No</p>
<p>OrMa_Data('OBFCM') = approved/notApproved</p>
<p>OrMa_Data('invalid value') = noEntry</p>
</td><td align="left">
<p>The function delivers the status of the order management customer objection (declaration of consent for the collection of data) based on parameters.</p>
</td></tr></tbody></table>

**Table 93. Backend systems**

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-14-11-category-definition.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="7-14-function-test-editor.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="7-14-13-category-process.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">7.14.11. Category - Definition </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 7.14.13. Category - Process</td></tr></table>
