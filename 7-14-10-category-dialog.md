[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md) > [7.14. Function Test Editor](7-14-function-test-editor.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.14.10. Category - Dialog</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-14-9-desktop.md">Prev</a> </td><th align="center" width="60%">7.14. Function Test Editor</th><td align="right" width="20%"> <a accesskey="n" href="7-14-11-category-definition.md">Next</a></td></tr></table>

---

#### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Dialog"></a>7.14.10. Category - Dialog

The **Dialog** category contains the following action elements:

- [Section 7.14.10.1, “Action Element - Set Test Module Title”](7-14-10-category-dialog.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Dialog.Setze_Testmodultitel "7.14.10.1. Action Element - Set Test Module Title")
- [Section 7.14.10.2, “Action Element - Question”](7-14-10-category-dialog.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Dialog.Frage "7.14.10.2. Action Element - Question")
- [Section 7.14.10.3, “Action Element - Input”](7-14-10-category-dialog.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Dialog.Eingabe "7.14.10.3. Action Element - Input")
- [Section 7.14.10.4, “Action Element - Keyboard Input”](7-14-10-category-dialog.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Dialog.Tastatureingabe "7.14.10.4. Action Element - Keyboard Input")
- [Section 7.14.10.5, “Action Element - Help”](7-14-10-category-dialog.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Dialog.Hilfe "7.14.10.5. Action Element - Help")
- [Section 7.14.10.6, “Action Element - Message”](7-14-10-category-dialog.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Dialog.Meldung "7.14.10.6. Action Element - Message")
- [Section 7.14.10.8, “Action Element - Vehicle Status”](7-14-10-category-dialog.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Dialog.Fahrzeugzustand "7.14.10.8. Action Element - Vehicle Status")
- [Section 7.14.10.9, “Action Element - Lock Button”](7-14-10-category-dialog.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Dialog.Lock_Button "7.14.10.9. Action Element - Lock Button")
- [Section 7.14.10.10, “Action Element - Progress Bars”](7-14-10-category-dialog.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Dialog.Fortschrittsbalken "7.14.10.10. Action Element - Progress Bars")
- [Section 7.14.10.11, “Action Element - BZD”](7-14-10-category-dialog.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Dialog.BZD "7.14.10.11. Action Element - BZD")

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Dialog.Setze_Testmodultitel"></a>7.14.10.1. Action Element - Set Test Module Title

The "Set test module title" action element can be seen in [Figure 387, “Action Element - Set Test Module Title”](7-14-10-category-dialog.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Dialog.Setze_Testmodultitel "Figure 387. Action Element - Set Test Module Title").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Dialog.Setze_Testmodultitel"></a>

![Image: set test module title action element](images/fte_arbeitsflaeche_dialog_setzetestmodultitel.png)

**Figure 387. Action Element - Set Test Module Title**

This action element is used to change the content of the corresponding information window in ODIS Service. The "Set test module title" dialog controls the content of the left information window 3 (LIW 3) on the tester, which generally shows the title of the function test that was called up.

When using sub-programs, it may be necessary to adapt the title using this command. The main program can transfer the title to the sub-program using a variable.

The number of characters for a test module title is limited to 50. The title is shown in two lines on the tester. If more than 50 characters are given, the rest will be truncated. Manual line breaks are not possible.

###### <a id="d4e16900"></a>7.14.10.1.1. Test Module Title

The test module title is entered in the input field. The title can consist of a variable or a keyword, which can be added using the buttons alongside (see [Section 7.14.6, “Using Variables”](7-14-6-using-variables.md "7.14.6. Using Variables")).

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Dialog.Frage"></a>7.14.10.2. Action Element - Question

The "Question" action element can be seen in [Figure 388, “Action Element - Question”](7-14-10-category-dialog.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Dialog.Frage "Figure 388. Action Element - Question").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Dialog.Frage"></a>

![Image: question action element](images/fte_arbeitsflaeche_dialog_frage.png)

**Figure 388. Action Element - Question**

This action element is used to create a question to the user. Possible answers are yes/no/unknown or a selection.

Using the "Question" command, you can formulate a question that the user of the tester must answer. You can create and edit the question in the editing field.

The question is created in an editor and then saved in XML format.

Just as with the **Set status** command (see [Section 7.14.12.2, “Action Element - Set Status”](7-14-12-category-mapping.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Zuordnung.Setze_Zustand "7.14.12.2. Action Element - Set Status")), you can specify the test step outputs using this action element. See also [Section 7.14.5.3, “Adding Test Steps, Selections, Sub-programs and Sub-program Selections”](7-14-5-test-steps-view.md#Funktionstesteditor.Testschritte_View.Testschritte_Erzeugen "7.14.5.3. Adding Test Steps, Selections, Sub-programs and Sub-program Selections"). Various formats are possible, and a selection of symbols is available.

###### <a id="d4e16923"></a>7.14.10.2.1. Text Field

The text field contains the question text. Use of text fields is described in [Section 7.14.7, “Editing Text”](7-14-7-editing-text.md "7.14.7. Editing Text").

###### <a id="d4e16927"></a>7.14.10.2.2. Yes/no

If "Yes/No" is selected, then the Yes/No buttons appear on the tester. The (default" selection "OK = Yes" sets the test status to OK if the user answers with "Yes". If the user selects "No" instead, then the tester sets the NOT OK status. If the "OK = NO" selection is specified, then the logic is the opposite: "Yes" generates NOT OK, "No" generates OK.

The "Unknown" option can be marked with the scope of the Yes/No option. If you mark the "Unknown" option, the "Unknown" button will appear in addition to "Yes" and "No". If the user selects it, the test status will be set to "Unknown". If the results of the test step change this test status later, the test module will be ended with "Unknown" and a "?" appears to the left of the diagnostic object in the test plan to indicate the status.

###### <a id="d4e16931"></a>7.14.10.2.3. Select

A selection for control the "Select" system variables: enter the desired responses into the field and leave fields that are not needed blank. The entries are displayed on the tester as button names. Using only short texts as button names is recommended. Adjust longer texts in the text window and label them with index numbers that correspond to the button numbering.

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Dialog.Eingabe"></a>7.14.10.3. Action Element - Input

The "Input" action element can be seen in [Figure 389, “Action Element - Input”](7-14-10-category-dialog.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Dialog.Eingabe "Figure 389. Action Element - Input").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Dialog.Eingabe"></a>

![Image: input action element](images/fte_arbeitsflaeche_dialog_eingabe.png)

**Figure 389. Action Element - Input**

With the "Input" command, the user can enter characters using a virtual keyboard displayed on the tester in ODIS Service. The input is transferred into a variable (result) that you must enter in the "Result" field. The variables must be defined globally or locally in the current test step.

###### <a id="d4e16947"></a>7.14.10.3.1. Text Field

The text field contains the text that is displayed for an input on the tester. Use of text fields is described in [Section 7.14.7, “Editing Text”](7-14-7-editing-text.md "7.14.7. Editing Text").

###### <a id="d4e16951"></a>7.14.10.3.2. Result

A variable in which the result of the input will be saved must be entered in the results field. A variable can be entered using the button (see [Section 7.14.6, “Using Variables”](7-14-6-using-variables.md "7.14.6. Using Variables")).

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Dialog.Tastatureingabe"></a>7.14.10.4. Action Element - Keyboard Input

The "Keyboard input" action element can be seen in [Figure 390, “Action Element - Keyboard Input”](7-14-10-category-dialog.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Dialog.Tastatureingabe "Figure 390. Action Element - Keyboard Input").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Dialog.Tastatureingabe"></a>

![Image: keyboard input action element](images/fte_arbeitsflaeche_dialog_tastatureingabe.png)

**Figure 390. Action Element - Keyboard Input**

This action element generates a virtual ASCII, HEX or DEC keyboard for entering data. The length, defaults, and the results are expressed in variables.

In this way, you can program an ASCII, hexadecimal, or decimal virtual keyboard that the user can use to enter data. The value entered will be transferred to the variable entered in the "Results" field.

The user can position the cursor at any location on the keyboard displayed on the tester using the arrow buttons. It always works in insert mode. New characters are always added before the cursor. Extra characters at the end of the input field are automatically truncated.

The ASCII keyboard allows for upper case and lower case text as well as a range of special characters, including the underscore. The data is applied using the "Q" (Quittieren = confirm) button.

###### <a id="d4e16971"></a>7.14.10.4.1. Type

The format of the virtual keyboard can be specified here.

###### <a id="d4e16974"></a>7.14.10.4.2. Length

Using the "Length" field (integer), you can set a maximum limit for the number of characters entered. The highest value permitted is 255.

###### <a id="d4e16977"></a>7.14.10.4.3. Defaults

You can specify a default value using the "Default" field. This appears on the tester as a default for the virtual keyboard input field. A string variable can be used to specify.

###### <a id="d4e16980"></a>7.14.10.4.4. Result

A string variable can be specified for saving the results of the keyboard input (see [Section 7.14.6, “Using Variables”](7-14-6-using-variables.md "7.14.6. Using Variables")).

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Dialog.Hilfe"></a>7.14.10.5. Action Element - Help

The "Help" action element can be seen in [Figure 391, “Action Element - Help”](7-14-10-category-dialog.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Dialog.Hilfe "Figure 391. Action Element - Help").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Dialog.Hilfe"></a>

![Image: help action element](images/fte_arbeitsflaeche_dialog_hilfe.png)

**Figure 391. Action Element - Help**

The Help action element allows you to create a help text that the user can call up in ODIS Service.

The help text is displayed when the user presses the "Help" button on the tester while processing a function test in the navigation line. The user then finds the topic "Function test help" in the "Help overview" dialog that is displayed. If the user selects this topic, the text from the command defined here appears.

Use the "Help for test" function for a summarized description of the test step and for useful notes on it. The command should be at the beginning of a test step. The command is applicable locally unless it is inserted in the Global Start test step. See also [Section 7.14.5.1.1, “Global Start Test Step”](7-14-5-test-steps-view.md#Funktionstesteditor.Testschritte_View.Spezielle_Testschritte.Global_Start "7.14.5.1.1. Global Start Test Step").

###### <a id="d4e17000"></a>7.14.10.5.1. Text Field

The help text is inserted in the text field. Use of text fields is described in [Section 7.14.7, “Editing Text”](7-14-7-editing-text.md "7.14.7. Editing Text").

###### <a id="d4e17004"></a>7.14.10.5.2. Print

Printing information is described under [Section 7.14.10.7, “Printing in the Help and Message Action Elements”](7-14-10-category-dialog.md#Funktionstesteditor.Arbeitsflaeche.Drucken "7.14.10.7. Printing in the Help and Message Action Elements").

###### <a id="d4e17008"></a>7.14.10.5.3. Print preview

The print preview is described in [Section 7.14.10.7, “Printing in the Help and Message Action Elements”](7-14-10-category-dialog.md#Funktionstesteditor.Arbeitsflaeche.Drucken "7.14.10.7. Printing in the Help and Message Action Elements").

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Dialog.Meldung"></a>7.14.10.6. Action Element - Message

The "Message" action element can be seen in [Figure 392, “Action Element - Message”](7-14-10-category-dialog.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Dialog.Meldung "Figure 392. Action Element - Message").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Dialog.Meldung"></a>

![Image: message action element](images/fte_arbeitsflaeche_dialog_meldung.png)

**Figure 392. Action Element - Message**

The "Message" command is used for messages to the tester user. You can formulate free text and enter it directly in the work area, access status or default texts, and integrate variables or keywords in the text. You can also configure if user confirmation is required.

###### <a id="d4e17025"></a>7.14.10.6.1. Text Field

The message text is inserted in the text field. Editing the text is described under [Section 7.14.7, “Editing Text”](7-14-7-editing-text.md "7.14.7. Editing Text").

###### <a id="d4e17029"></a>7.14.10.6.2. Bars

No function.

###### <a id="d4e17032"></a>7.14.10.6.3. Confirmation

Using this function, you can control if the user must confirm the message text. A timeout can be defined for a message without a confirmation. The timeout specifies how long the message text should be displayed (in seconds).

###### <a id="d4e17035"></a>7.14.10.6.4. Print

Printing information is described under [Section 7.14.10.7, “Printing in the Help and Message Action Elements”](7-14-10-category-dialog.md#Funktionstesteditor.Arbeitsflaeche.Drucken "7.14.10.7. Printing in the Help and Message Action Elements").

###### <a id="d4e17039"></a>7.14.10.6.5. Print preview

The print function is described in [Section 7.14.10.7, “Printing in the Help and Message Action Elements”](7-14-10-category-dialog.md#Funktionstesteditor.Arbeitsflaeche.Drucken "7.14.10.7. Printing in the Help and Message Action Elements").

##### <a id="Funktionstesteditor.Arbeitsflaeche.Drucken"></a>7.14.10.7. Printing in the Help and Message Action Elements

There is the option to print the displayed message or help information in the process window. This function is used to print results from the control module communication (Ecukom) or results from system variables (such as DATE, VIN) or measuring equipment results in the documents. The Print option used for this is in the "Help" action element (see [Figure 391, “Action Element - Help”](7-14-10-category-dialog.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Dialog.Hilfe "Figure 391. Action Element - Help")) and the "Message" action element (see [Figure 392, “Action Element - Message”](7-14-10-category-dialog.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Dialog.Meldung "Figure 392. Action Element - Message")). In the "Message" action element, the Print option is only active for the messages to be confirmed. The Print option is deactivated for messages with a timeout.

<a id="figure.Funktionstesteditor.Arbeitsflaeche.beispiel.hilfe"></a>

![Image: help action element](images/fte_Arbeitsflaeche_Dialog_Hilfe_drucken.png)

**Figure 393. "Help" Action Element with Print Option**

If Print is selected, "Print" or "Require print" can be selected in the selection menu (see [Figure 394, “Print Menu”](7-14-10-category-dialog.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Hilfe.drucken "Figure 394. Print Menu")). "Require print" is only possible in the message. Printing cannot be required in the "Help" action element.

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Hilfe.drucken"></a>

![Print Menu](images/fte_Arbeitsflaeche_Dialog_drucken_menue.png)

**Figure 394. Print Menu**

A print preview can also be generated. The dialog print preview can be seen in [Figure 395, “Print Preview from the Help Action Element”](7-14-10-category-dialog.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Hilfe.druckvorschau "Figure 395. Print Preview from the Help Action Element"). If the "Print preview" button is pressed, then a print preview with the content of the action element that is currently open is displayed for the user. Any default texts or vehicle statuses that may be contained are removed. Variables and keywords are retained.

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Hilfe.druckvorschau"></a>

![Print Preview from the Help Action Element](images/fte_druckvorschau.png)

**Figure 395. Print Preview from the Help Action Element**

If the "Print" option is selected, it will be possible to print information in ODIS Service. An additional print button will be displayed in the process window near the message or under the help text.

With the "Require print" option, printing of information in ODIS Service will be required, meaning the user cannot continue the function test without starting to print. A Print button with a red border is displayed in the process window near the message. The Finish/Next button for the message remains deactivated until the user presses the Print button.

If the "Print" button is pressed, the current output (such as the message or help information that is currently displayed) is transmitted to the operating system as a print order. The function is carried out similarly to the "Documents -> Print" function.

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Dialog.Fahrzeugzustand"></a>7.14.10.8. Action Element - Vehicle Status

The "Vehicle status" action element can be seen in [Figure 396, “Action Element - Vehicle Status”](7-14-10-category-dialog.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Dialog.Fahrzeugzustand "Figure 396. Action Element - Vehicle Status").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Dialog.Fahrzeugzustand"></a>

![Image: vehicle status action element](images/fte_arbeitsflaeche_dialog_fahrzeugzustand.png)

**Figure 396. Action Element - Vehicle Status**

In ODIS Service, this action element should generate a system default text for recurring situations, such as "Ignition on". Each setting produces one corresponding status text, such as "-Connect the tester", and it must be confirmed by the user as with the "Message" command. The corresponding vehicle statuses are added and removed with the plus and minus buttons and the position is moved using the arrow buttons.

The sequence of the status texts in the output can be adjusted. Initially, the numbers appear in the order of the selection that was made. You can then change the order. In doing so, the content is adapted to the new order automatically when all other settings are changed.

The vehicle status can be checked using the commands "While", "If", or "Switch". See also [Section 7.14.13, “Category - Process”](7-14-13-category-process.md "7.14.13. Category - Process").

###### <a id="d4e17095"></a>7.14.10.8.1. Vehicle Status Table

Contains the individual vehicle statuses in table form. The optional "Check" selection (tester, ignition, battery) can be selected in order to verify the vehicle status using a measurement.

Elements can be added, removed, or moved using the plus/minus/arrow buttons. See [Figure 397, “Vehicle Status Controls”](7-14-10-category-dialog.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Dialog.Fahrzeugzustand.Steuerfelder "Figure 397. Vehicle Status Controls").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Dialog.Fahrzeugzustand.Steuerfelder"></a>

![Image: vehicle status controls](images/fte_Arbeitsflaeche_Dialog_Fahrzeugzustand_Steuerfelder.png)

**Figure 397. Vehicle Status Controls**

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Dialog.Lock_Button"></a>7.14.10.9. Action Element - Lock Button

The "Lock" action element can be seen in [Figure 398, “Action Element - Lock Button”](7-14-10-category-dialog.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Dialog.Lock_Button "Figure 398. Action Element - Lock Button").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Dialog.Lock_Button"></a>

![Image: lock button action element](images/fte_arbeitsflaeche_dialog_lock.png)

**Figure 398. Action Element - Lock Button**

With this command, you can hide all buttons in the screen that is shown using a first command with the setting "Lock buttons" and a second command with the setting "Do not lock buttons". When this is done, the tester can no longer be operated using the user interface until this function is disabled.

This function may be used, for example, during function tests for network flashing in order to prevent the user from interrupting the process.

The buttons on the tester can be locked or unlocked using the "Lock buttons" and "Do not lock buttons" option fields.

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Dialog.Fortschrittsbalken"></a>7.14.10.10. Action Element - Progress Bars

The "Progress bars" action element can be seen in [Figure 399, “Action Element - Progress Bars”](7-14-10-category-dialog.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Dialog.Fortschrittsbalken "Figure 399. Action Element - Progress Bars").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Dialog.Fortschrittsbalken"></a>

![Image: progress bars action element](images/fte_arbeitsflaeche_dialog_fortschrittsbalken.png)

**Figure 399. Action Element - Progress Bars**

**Ranges**, **loops** or a **position** can be specified for the progress bars. Variables (predefined) can be selected.

Using this command, you can display a progress bar or a communication display in a message. This is useful, for example, if there are long wait times for the user during online access or flashing. There are two use cases: "Area" (with "Set position") and "Loop".

###### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Dialog.Fortschrittsbalken.Konfiguration"></a>7.14.10.10.1. Area for Analog Bars

In the first command before a loop, set the "Area" option and define the left and right borders of the bars as well as the desired dimension. The specifications appear later as labeling on the analog bars.

In a second command in a loop, set the "Set position" option and assign the bar display to a variable. A message with the "Bars" option must also call up the bar display in the loop.

Command sequence (example):

- Progress bars, range (such as specified above)
- While Ecukom (temp) progress bars, Set position (temp), Message (without confirmation, output "temp", "bars" set)

**Loop for communication display**

There must be a message with the "Bars" option marked in the loop that is responsible for the display. The communication display is hidden again with another "Progress bar" command.

Command sequence (example):

- Progress bars, loop, start, while, any commands, message ("Bars" option set), progress bars, loop, stop

###### <a id="d4e17156"></a>7.14.10.10.2. Set Position

Can be used in conjunction with 'Area'. See [Section 7.14.10.10.1, “Area for Analog Bars”](7-14-10-category-dialog.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Dialog.Fortschrittsbalken.Konfiguration "7.14.10.10.1. Area for Analog Bars").

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Dialog.BZD"></a>7.14.10.11. Action Element - BZD

The "BZD" action element can be seen in [Figure 400, “Action Element - BZD”](7-14-10-category-dialog.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Dialog.BZD "Figure 400. Action Element - BZD").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Dialog.BZD"></a>

![Image: BZD action element](images/fte_arbeitsflaeche_dialog_bzd.png)

**Figure 400. Action Element - BZD**

The action element triggers the equipment status documentation. The goal is recording of components that are not diagnostic-capable by the worker.

The recorded build groups/serial numbers are stored in the **Build group** array variable. The array must be a ‘String’ data type. Please note that the entire array is described. For this reason, an array index cannot be specified. The input of an array variable for the build group is required.

The type of recording is stored in the **Method** array variable. The array must be a ‘String’ data type. Please note that the entire array is described. For this reason, an array index cannot be specified.

The recording method can be the following values:

- **A**: entry was scanned in automatically
- **M**: entry was recorded manually
- **E**: entry was scanned in and then edited

The result of the checksum calculation is saved in the **Checksum** array variable. The array must be a whole number data type. Please note that the entire array is described. For this reason, an array index cannot be specified.

The result of the checksum calculation a have the following values:

- **0**: checksum calculation not successful
- **1**: checksum calculation successful

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-14-9-desktop.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="7-14-function-test-editor.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="7-14-11-category-definition.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">7.14.9. Desktop </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 7.14.11. Category - Definition</td></tr></table>
