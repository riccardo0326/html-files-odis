[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md) > [7.14. Function Test Editor](7-14-function-test-editor.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.14.13. Category - Process</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-14-12-category-mapping.md">Prev</a> </td><th align="center" width="60%">7.14. Function Test Editor</th><td align="right" width="20%"> <a accesskey="n" href="7-14-14-category-measurement.md">Next</a></td></tr></table>

---

#### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Ablauf"></a>7.14.13. Category - Process

The **Process** category contains the following elements:

- [Section 7.14.13.1, “Action Element - IF Command”](7-14-13-category-process.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Ablauf.IF-Anweisung "7.14.13.1. Action Element - IF Command")
- [Section 7.14.13.2, “Action Element - Loop”](7-14-13-category-process.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Ablauf.Loop "7.14.13.2. Action Element - Loop")
- [Section 7.14.13.3, “Action Element - Break Loop”](7-14-13-category-process.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Ablauf.Break_Loop "7.14.13.3. Action Element - Break Loop")
- [Section 7.14.13.4, “Action Element - While”](7-14-13-category-process.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Ablauf.While "7.14.13.4. Action Element - While")
- [Section 7.14.13.5, “Action Element - While Not”](7-14-13-category-process.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Ablauf.While_Not "7.14.13.5. Action Element - While Not")
- [Section 7.14.13.6, “Action Element - Break While”](7-14-13-category-process.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Ablauf.Break_While "7.14.13.6. Action Element - Break While")
- [Section 7.14.13.7, “Action Element - Wait”](7-14-13-category-process.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Ablauf.Wait "7.14.13.7. Action Element - Wait")
- [Section 7.14.13.8, “Action Element - Switch”](7-14-13-category-process.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Ablauf.Switch_Case "7.14.13.8. Action Element - Switch")

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Ablauf.IF-Anweisung"></a>7.14.13.1. Action Element - IF Command

The "IF" action element can be seen in [Figure 415, “IF Command Action Element”](7-14-13-category-process.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Ablauf.IF-Anweisung "Figure 415. IF Command Action Element").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Ablauf.IF-Anweisung"></a>

![Image: IF command action element](images/fte_arbeitsflaeche_dialog_if.png)

**Figure 415. IF Command Action Element**

The display of the IF command changes based on the request criteria in the command. The following requests are available for selection: tester status, comparison, vehicle status, symptom, equipment.

Compare "If" request if certain conditions are met. Depending on the result of this, the program will branch to only one of two possibilities.

###### <a id="d4e21174"></a>7.14.13.1.1. Tester Status

Check test status. If the condition is met, the program sequence branches to the Then output. Otherwise, it branches to the Else output.

- OK, NOT OK, unknown, diagnosis created and component repaired: same as the "Case" command. Goes to the Then branch if the result is "true".
- End: command in a loop followed by "Break Loop" or "Break While". The construction allows an interruption in the loop using the "Next" button on the tester.
- Verification: goes to the Then branch if Guided Fault Finding starts the function test in verification mode. This mode is always given, either if a function test ends with "Diagnosis created, component repaired" and then subsequent question "Should the repair be checked" is answered with "yes", or if a function test is called up from the test plan again and the "Test" option is selected in the subsequent question (means: check verification or repair).
- Select: check the system variable "Select" that is preset in the "Question" and "Set status" commands.

###### <a id="d4e21186"></a>7.14.13.1.2. Comparison

Arithmetical and logical comparison operations, see the "Expression" command ([Section 7.14.12.1, “Action Element - Expression”](7-14-12-category-mapping.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Zuordnung.Ausdruck "7.14.12.1. Action Element - Expression")) and the "While" command ([Section 7.14.13.4.2, “Comparison”](7-14-13-category-process.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Ablauf.IF-Vergleich "7.14.13.4.2. Comparison")).

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Ablauf.IF-Vergleich"></a>

![Image: IF command with comparison action element](images/fte_arbeitsflaeche_dialog_if_vergleich.png)

**Figure 416. IF Command with Comparison Action Element**

To record the time when a fault occurs, you can use the following functions:

- Existence check timestamp:

  IF CU\_TIME\_STAMP(fault code path x) = 0
- Comparison check timestamp:

  IF CU\_TIME\_STAMP(fault code path x) > CU\_TIME\_STAMP(fault code path y)

Copy the fault code path ("Fault location" object) from the DTC memory model into the clipboard using the "Copy path" function and add it to the "IF" command. Fault codes with no timestamp have the value "0".

###### <a id="d4e21208"></a>7.14.13.1.3. Vehicle Status

Checks the vehicle status (ignition on/off, etc.). If you press the "Plus" button, you will enter a dialog similar to the one for the "Vehicle status" command. See [Section 7.14.10.8, “Action Element - Vehicle Status”](7-14-10-category-dialog.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Dialog.Fahrzeugzustand "7.14.10.8. Action Element - Vehicle Status").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Ablauf.IF-Fahrzeugzustand"></a>

![Image: IF command with vehicle status action element](images/fte_arbeitsflaeche_dialog_if_fzgzustaende.png)

**Figure 417. IF Command with Vehicle Statuses Action Element**

The statuses that are programmed using the "Vehicle status" command are entered into the tester log book when the command is executed. The "If" refers to the status entered in the log book. The vehicle statuses are linked in runtime with AND so that all vehicle statuses must be set in order to meet the requirement. If a vehicle status is not set, no other vehicle statuses can be checked from the log book.

###### <a id="fte.if.symptome"></a>7.14.13.1.4. Symptoms

Check for perceived symptoms, DTC memory entries, empirical rules.

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Ablauf.IF-Symptome"></a>

![Image: IF command with symptoms action element](images/fte_arbeitsflaeche_dialog_if_symptome.png)

**Figure 418. IF Command with Symptoms Action Element**

Add symptoms using the "Plus" button. Use the "Minus" button if a symptom should be removed. The "Fault location" and "Fault type" are necessary when entering specifications about the "Type".

The DFCC for the DTC can be entered in the "DTC Symptom" column. When specifying the DTC symptom, the VAG and/or SAE codes selected for the fault location are ignored and only this value is checked on the DTC.

If more rules/symptoms are needed, they can be linked together using the logical operators OR/AND. Single-level brackets are possible within logical expressions.

The symptoms referenced here are not checked to see if they are actually present at the time of publication. This means a reference is not automatically triggered from the "If" command if the corresponding symptom is removed from its structure.

The fault symptoms and equipment in the function test editor (IF and Switch case commands) can be sorted alphanumerically. The sorting affects only the viewing and does not change the order of any data. If the table view is sorted by a column, the dialog cannot be edited further.

###### <a id="d4e21237"></a>7.14.13.1.5. Equipment

Check for vehicle basic features and control module equipment.

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Ablauf.IF-Ausstattungen"></a>

![Image: IF command with equipment action element](images/fte_arbeitsflaeche_dialog_if_ausstattungen.png)

**Figure 419. IF Command with Equipment Action Element**

If you press the "Plus" button, a new variant rule is added. If there is a previous selection of an existing variant rule, the new variant rule will be added under the selected variant rule. When selecting one or more variant rules in an associated block, they can be sorted or moved up or down using the ![](<images/Pfeil hoch.png>) ![](<images/Pfeil runter.png>)symbols. A list with possible type specifications appears during the selection in the "Type" input field. After the type has been selected, data can be selected from the editing object using the "Value" input field.

The fault symptoms and equipment in the function test editor (IF and Switch case commands) can be sorted alphanumerically. The sorting affects only the viewing and does not change the order of any data. If the table view is sorted by a column, the dialog cannot be edited further.

###### <a id="d4e21256"></a>7.14.13.1.6. VCI Comparison

Check of VCI types and VCI connection types.

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Ablauf.IF-Vci"></a>

![Image: IF command with VCI comparison action element](images/fte_arbeitsflaeche_dialog_if_vci.png)

**Figure 420. IF Command with VCI Comparison Action Element**

If you press the "Plus" button, a new VCI comparison is added. A list with possible "VCIType" and "ConnectionType" specifications appears during the selection in the "Type" input field. After the type has been selected, suitable comparison values can be selected from the editing object using the "Value" input field.

- AND, OR, EXOR: switches between the logical link types for further conditions.
- (: add an opening bracket in this column. You can use multiple bracket levels (multiple nesting levels).
- -, NOT: switches the negation of the condition on/off.
- Type: selection option between VCIType and ConnectionType.
- Value: selection option for the previously selected type. The default value of VCIType is 'VAS5054'. The default value of the ConnectionType is 'USB'.
- ): Add closing brackets in this column.

The table entries can be sorted alphanumerically. The sorting affects only the viewing and does not change the order of any data. If the table view is sorted by a column, the dialog cannot be edited further.

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Ablauf.Loop"></a>7.14.13.2. Action Element - Loop

The "Loop" action element can be seen in [Figure 421, “Loop Action Element”](7-14-13-category-process.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Ablauf.Loop "Figure 421. Loop Action Element").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Ablauf.Loop"></a>

![Image: action element categories -process.loop](images/fte_arbeitsflaeche_dialog_loop.png)

**Figure 421. Loop Action Element**

You can program a loop using this command. The following options are available as cancellation criteria for a loop: confirmation (by the user on the tester), number, timeout.

The "Number" or "Timeout" loop construction should be a manual interruption by the technician using the "Next" button. To do this, add an "IF - Quit" into the loop (the "IF" command with configured tester status/end), followed by the "Break Loop" command.

###### <a id="d4e21296"></a>7.14.13.2.1. Confirmation

The loop runs until the activated "Next" button is pressed ("IF - Quiet" (see [Section 7.14.13.2, “Action Element - Loop”](7-14-13-category-process.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Ablauf.Loop "7.14.13.2. Action Element - Loop")) is not required).

###### <a id="d4e21300"></a>7.14.13.2.2. Quantity

You can specify the exact number of cycles for the program loop or control it using a variable. The value of the variables is transferred to the command at the beginning of the loop. A dynamic change of the "Number" parameter is not possible while running the loop.

###### <a id="d4e21303"></a>7.14.13.2.3. Timeout

You can specify a time in seconds or minutes while the program loop is running. You can also specify the option "Bars" parameter. In this case, a time bar based on the side of the "Timeout" is displayed in the "Message" command that is placed before or after the "Loop", if the "Bars" option is set there.

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Ablauf.Break_Loop"></a>7.14.13.3. Action Element - Break Loop

The Break Loop action element interrupts a loop. There is no other dialog for configuration. The graphic nodes are the same color as the loop nodes. An interruption symbol on the lower edge also indicates that adding additional nodes within a loop is not permitted after a Break command.

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Ablauf.While"></a>7.14.13.4. Action Element - While

The "While" action element can be seen in [Figure 422, “While Action Element”](7-14-13-category-process.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Ablauf.While "Figure 422. While Action Element").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Ablauf.While"></a>

![Image: action element categories - while](images/fte_arbeitsflaeche_dialog_while.png)

**Figure 422. While Action Element**

You can program a loop with interruption condition using this command. The loop runs until the defined condition is met or the interruption occurs after a "Break While" command, such after an "IF" command.

###### <a id="d4e21322"></a>7.14.13.4.1. Tester Status

The interruption condition can check the tester status.

###### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Ablauf.IF-Vergleich"></a>7.14.13.4.2. Comparison

A comparison expression can be entered. The loop runs as long s the comparison condition is met. The function test editor grammar enables the entering of brackets for control the priority when comparison expressions are evaluated. The brackets (parentheses) can be nested in one another as desired.

<a id="d4e21329"></a>

<table border="1" summary="Comparison Operation Example"><colgroup><col align="left"/><col align="left"/><col align="left"/><col align="left"/></colgroup><thead><tr bgcolor="#EEEEEE"><th align="left">Mapping</th><th align="left">Example</th><th align="left">Result</th><th align="left">Explanations</th></tr></thead><tbody><tr><td align="left">a = 7</td><td align="left">a BIT_TEST 4</td><td align="left">not met</td><td align="left">0111, the bit is zero</td></tr><tr><td align="left">a = 4, b = 2</td><td align="left">a &gt; b</td><td align="left">met</td><td align="left">a is greater than b</td></tr><tr><td align="left">a = 4, b = 4</td><td align="left">a = b</td><td align="left">met</td><td align="left">a is equal to b</td></tr><tr><td align="left">a = 'ABC', b = 'CDE', c = 'ABC'</td><td align="left">a = b OR a = c</td><td align="left">met</td><td align="left">a = c</td></tr><tr><td align="left">a = 'AB' b = 'AB' c = 'BC' d = 'BC'</td><td align="left">a = b AND c = d</td><td align="left">met</td><td class="auto-generated"> </td></tr><tr><td align="left">a = 1, b = 1, c = 2, d = 2</td><td align="left">a = b AND c = d OR a = d</td><td align="left">met</td><td align="left">Evaluation from left to right, AND and OR are the same priority.</td></tr><tr><td align="left">a = 1, b = 1, c = 2, d = 2</td><td align="left">a = b AND (c = d OR a = d)</td><td align="left">met</td><td align="left">Evaluation with brackets</td></tr></tbody></table>

**Table 94. Comparison Operation Example**

###### <a id="d4e21377"></a>7.14.13.4.3. Vehicle Status

If you select the "vehicle status" option and press the "Plus" button, a new condition is created. The condition can be selected directly from the list using the "Vehicle status" option field.

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Ablauf.While_Not"></a>7.14.13.5. Action Element - While Not

Using this command, you can program a loop with a negated interruption condition, meaning the loop will run as long as the condition is not encountered. Otherwise, the behavior is identical to the While loop. See [Section 7.14.13.4, “Action Element - While”](7-14-13-category-process.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Ablauf.While "7.14.13.4. Action Element - While").

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Ablauf.Break_While"></a>7.14.13.6. Action Element - Break While

The Break While action element interrupts a While loop. There is no other dialog for configuration. The graphic nodes are the same color as the While nodes. An interruption symbol on the lower edge also indicates that adding additional nodes within a while loop is not permitted after a Break command.

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Ablauf.Wait"></a>7.14.13.7. Action Element - Wait

The "Wait" action element can be seen in [Figure 423, “Wait Action Element”](7-14-13-category-process.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Ablauf.Wait "Figure 423. Wait Action Element").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Ablauf.Wait"></a>

![Image: action element categories - wait](images/fte_arbeitsflaeche_dialog_wait.png)

**Figure 423. Wait Action Element**

You can program a wait time in milliseconds using this command. Wait times are needed for coordination tasks during real-time tests, for example. A typical example is waiting for a relay switching procedure. The test program stops for this and waits (CPU time runs) until the programmed wait time has ended.

###### <a id="d4e21400"></a>7.14.13.7.1. Time

The process on the tester is interrupted for the time period specified under **Time**. The input is done in milliseconds.

For longer times, the time can be controlled using the "Loop" command. See [Section 7.14.13.2, “Action Element - Loop”](7-14-13-category-process.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Ablauf.Loop "7.14.13.2. Action Element - Loop").

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Ablauf.Switch_Case"></a>7.14.13.8. Action Element - Switch

The "Switch" action element with configured expression can be seen in [Figure 424, “Switch Action Element”](7-14-13-category-process.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Ablauf.Switch_Case "Figure 424. Switch Action Element").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Ablauf.Switch_Case"></a>

![Image: switch action element](images/fte_arbeitsflaeche_dialog_switch.png)

**Figure 424. Switch Action Element**

With a switch/case multiple branching, you make a test step later in the procedure dependent on the result of a status check. Depending on the result of the selection, the program sequence branches out to one or the other of the subsequent "Case" commands and works through the remaining commands that are listed below it. Ideally, all results that may occur in the "Switch" command should be covered by the subsequent "Case" commands. After processing a "Case" branch, the switch/case structure ends in a common output.

The "Switch" command can be set to one of several types that specifies the character of the subsequent "Case" commands. Once a "Switch" is linked with a "Case" command, its type can no longer be changed (for example, from "Select" to "Constant"). In order to change it later, you must first delete all linked "Case" commands.

###### <a id="d4e21420"></a>7.14.13.8.1. Tester Status

For checking results statuses ("OK", "NOT OK", "unknown", "Diagnosis created and component repaired", as well as "Select 1" - "Select ...").

###### <a id="d4e21423"></a>7.14.13.8.2. Expression

For entering a constant or an arithmetical, logical, or mixed expression.

###### <a id="d4e21426"></a>7.14.13.8.3. Vehicle Status

For checking vehicle statuses.

###### <a id="d4e21429"></a>7.14.13.8.4. Symptoms

For checking perceived symptoms (log book). The look book is managed on the tester.

###### <a id="d4e21432"></a>7.14.13.8.5. Equipment

For checking vehicle equipment (log book). The look book is managed on the tester.

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Ablauf.Case_Anordnung"></a>7.14.13.9. Action Element - Case

The "Case" action element with configured tester status can be seen in [Figure 425, “Case - Tester Status Action Element”](7-14-13-category-process.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Ablauf.Case.Testerstate "Figure 425. Case - Tester Status Action Element").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Ablauf.Case.Testerstate"></a>

![Image: case - tester status](images/fte_arbeitsflaeche_dialog_case_testerstate.png)

**Figure 425. Case - Tester Status Action Element**

"Case" commands are located directly under a "Switch" command in the program sequence. All "Case" commands for a "Switch" command are arranged one below the other and at the same level. See also [Figure 426, “Case - Layout Action Element”](7-14-13-category-process.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Ablauf.Case_Anordnung "Figure 426. Case - Layout Action Element").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Ablauf.Case_Anordnung"></a>

![Image: case - layout](images/fte_arbeitsflaeche_case_anordnung.png)

**Figure 426. Case - Layout Action Element**

If none of the "Case" conditions listed are applicable, you should insert another "Case" command as a default specification that will then be run.

The "Case" command is then equipped with the "Default" control field as a default specification in the corresponding dialog. For "Case" commands where "Default" is set, parameter input is irrelevant and is therefore not active.

Another switch/case structure may be located under a "Case" command. An example of the Case command for selecting the Switch expression is shown in [Figure 427, “Case - Dialog Action Element”](7-14-13-category-process.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Ablauf.Case "Figure 427. Case - Dialog Action Element").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Ablauf.Case"></a>

![Image: case - dialog](images/fte_arbeitsflaeche_dialog_case.png)

**Figure 427. Case - Dialog Action Element**

The layout of the "Case" dialog that is called up depends on the type of the upstream "Switch" command.

###### <a id="d4e21470"></a>7.14.13.9.1. Tester Status

The following results checks are possible: "OK", "NOT OK", "unknown", "Diagnosis created and component repaired" as well as "Select 1" - "Select 8" or their combinations:

- OK: "Case" command process if the program status is "OK". It can be formulated from questions to the user ("Question" command), measurement results within the tolerances (measurement commands), or from vehicle data that is read (Ecukom command).
- NOT OK: "Case" command process if the program status is "NOT OK".
- unknown: "Case" command process if a "Question" command was answered with "unknown" or the test status was set explicitly with the "Set status" command.
- Diagnosis created and component repaired: "Case" command process if the test status was set explicitly with the "Set status" command.
- SELECT 1 ...: "Case" command process if the "Select" system variable that was preset in the "Question" and "Set status" commands has the specified status.

###### <a id="d4e21484"></a>7.14.13.9.2. Expression

List of comparison values that are entered as a table. Each of the values is compared with the expression in the Switch command one after another. If a comparison results in "true" then the commands in the Case block are executed.

An example of a Case command is shown in [Figure 428, “Case - Expression Action Element”](7-14-13-category-process.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Ablauf.Case.Ausdruck "Figure 428. Case - Expression Action Element"). The individual comparison values can be sorted using the table header and the context menu.

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Ablauf.Case.Ausdruck"></a>

![Image: case - expression](images/fte_arbeitsflaeche_dialog_case_ausdruck.png)

**Figure 428. Case - Expression Action Element**

###### <a id="d4e21497"></a>7.14.13.9.3. Vehicle Status

Checks the vehicle status (ignition on/off, etc.). If you press the "Plus" button, you will enter a dialog similar to the one for the "Vehicle status" command. See [Section 7.14.10.8, “Action Element - Vehicle Status”](7-14-10-category-dialog.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Dialog.Fahrzeugzustand "7.14.10.8. Action Element - Vehicle Status").

The statuses that are programmed using the "Vehicle status" command are entered into the tester log book when the command is executed. The "Case" refers to the status entered in the log book. The vehicle statuses are linked in runtime with OR so that at least one vehicle status must be set in order to meet the requirement. If a vehicle status is set, no other vehicle statuses can be checked from the log book.

An example of the Case command for selecting the Switch vehicle status selection is shown in [Figure 429, “Case - Vehicle Status Action Element”](7-14-13-category-process.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Ablauf.Case.Fahrzeugzustaende "Figure 429. Case - Vehicle Status Action Element"). The individual vehicle statuses can be sorted using the table header and the context menu.

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Ablauf.Case.Fahrzeugzustaende"></a>

![Image: case - vehicle status](images/fte_arbeitsflaeche_dialog_case_fahrzeugzustand.png)

**Figure 429. Case - Vehicle Status Action Element**

###### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Ablauf.Case.Symptome"></a>7.14.13.9.4. Symptoms

List of system strings of perceived symptoms.

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Ablauf.Case.Symptome"></a>

![Image: case - symptoms](images/fte_arbeitsflaeche_ablauf_case_symptome.png)

**Figure 430. Case - Symptoms Action Element**

Add symptoms using the "Plus" button. Use the "Minus" button if a symptom should be removed. The "Fault location" and "Fault type" are necessary when entering specifications about the "Type".

The DFCC for the DTC can be entered in the "DTC Symptom" column. When specifying the DTC symptom, the VAG and/or SAE codes selected for the fault location are ignored and only this value is checked on the DTC.

If more rules/symptoms are needed, they can be linked together using the logical operators OR/AND. Single-level brackets are possible within logical expressions.

The symptoms referenced here are not checked to see if they are actually present at the time of publication. This means a reference is not automatically triggered from the "Case" command if the corresponding symptom is removed from its structure.

The fault symptoms and equipment in the function test editor (IF and Switch case commands) can be sorted alphanumerically. The sorting affects only the viewing and does not change the order of any data. If the table view is sorted by a column, the dialog cannot be edited further.

###### <a id="d4e21528"></a>7.14.13.9.5. Equipment

List of basic features and equipment for input.

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Ablauf.Case.Ausstattung"></a>

![Image: case - equipment](images/fte_arbeitsflaeche_ablauf_case_ausstattung.png)

**Figure 431. Case - Equipment Action Element**

Select the correct version of the equipment network. The following buttons are available in the editing line:

- AND, OR, EXOR: switches between the logical link types for further conditions.
- (: add an opening bracket in this column. You can use multiple bracket levels (multiple nesting levels).
- -, NOT: switches the negation of the condition on/off.
- Type: selection option among the four basic features, the equipment, and the control module equipment.
- ): Add closing brackets in this column.

The templates from the structure editors are based on the current status of the selected version. There is no check to see if a node is actually present in other versions or if a change was made in the structure in the meantime.

The fault symptoms and equipment in the function test editor (IF and Switch case commands) can be sorted alphanumerically. The sorting affects only the viewing and does not change the order of any data. If the table view is sorted by a column, the dialog cannot be edited further.

###### <a id="d4e21553"></a>7.14.13.9.6. VCI Comparison

Check of VCI types and VCI connection types.

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Ablauf.Case.Vci"></a>

![Image: case - VCI comparison](images/fte_arbeitsflaeche_dialog_case_vci.png)

**Figure 432. Case - VCI Comparison Action Element**

If you press the "Plus" button, a new VCI comparison is added. A list with possible "VCIType" and "ConnectionType" specifications appears during the selection in the "Type" input field. After the type has been selected, suitable comparison values can be selected from the editing object using the "Value" input field.

- AND, OR, EXOR: switches between the logical link types for further conditions.
- (: add an opening bracket in this column. You can use multiple bracket levels (multiple nesting levels).
- -, NOT: switches the negation of the condition on/off.
- Type: selection option between VCIType and ConnectionType.
- Value: selection option for the previously selected type. The default value of VCIType is 'VAS5054'. The default value of the ConnectionType is 'USB'.
- ): Add closing brackets in this column.

The table entries can be sorted alphanumerically. The sorting affects only the viewing and does not change the order of any data. If the table view is sorted by a column, the dialog cannot be edited further.

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-14-12-category-mapping.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="7-14-function-test-editor.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="7-14-14-category-measurement.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">7.14.12. Category - Mapping </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 7.14.14. Category - Measurement</td></tr></table>
