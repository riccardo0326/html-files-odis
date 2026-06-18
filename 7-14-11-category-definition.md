[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md) > [7.14. Function Test Editor](7-14-function-test-editor.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.14.11. Category - Definition</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-14-10-category-dialog.md">Prev</a> </td><th align="center" width="60%">7.14. Function Test Editor</th><td align="right" width="20%"> <a accesskey="n" href="7-14-12-category-mapping.md">Next</a></td></tr></table>

---

#### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Definition"></a>7.14.11. Category - Definition

This category contains two action elements:

- [Section 7.14.11.1, “Action Element - Declare Variable”](7-14-11-category-definition.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Definition.Deklariere_Variablen "7.14.11.1. Action Element - Declare Variable")
- [Section 7.14.11.4, “Action Element - Define Keyword”](7-14-11-category-definition.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Definition.Definiere_Kennwort "7.14.11.4. Action Element - Define Keyword")

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Definition.Deklariere_Variablen"></a>7.14.11.1. Action Element - Declare Variable

The "Declare variable" action element can be seen in [Figure 401, “Action Element - Declare Variable”](7-14-11-category-definition.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Definition.Deklariere_Variablen "Figure 401. Action Element - Declare Variable").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Definition.Deklariere_Variablen"></a>

![Image: declare variable action element](images/fte_arbeitsflaeche_dialog_deklarierevariablen.png)

**Figure 401. Action Element - Declare Variable**

Using the "Declare variable", one or more variables can be declared and values can be specified for them.

The variables table shows the declared variables.

###### <a id="d4e17222"></a>7.14.11.1.1. Buttons above the table

- The plus creates a new variable.
- The double-plus duplicates the variable that is marked.
- The minus deletes the variable that was marked.
- Pressing the "Edit" button opens another editing menu for the variable.

###### <a id="d4e17233"></a>7.14.11.1.1.1. Variable

The name of the variable can be edited directly in the column.

###### <a id="d4e17236"></a>7.14.11.1.1.2. Type

The variable data type is described in [Section 7.14.11.3, “Examples for the Action Element - Declare Variable”](7-14-11-category-definition.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Definition.Deklariere_Variablen.Beispiele "7.14.11.3. Examples for the Action Element - Declare Variable") and it can be selected using a selection field.

###### <a id="d4e17240"></a>7.14.11.1.1.3. Constants

Variables declared as constant can no longer be changed in the program sequence that follows.

###### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Definition.Vorbelegung"></a>7.14.11.1.1.4. Defaults

The variables preconfiguration is in this field. No value is preconfigured if there is no explicit preconfiguration.

There is button with three dots in the preconfiguration field on the right edge of the variable. It appears once that is selected. This button displays a list of functions. This list of functions is also available as buttons in other action elements. The main groups are **Variable**, **Keyword**, **Functions**, **From Odx**, **Default text** and **Text library**

###### <a id="d4e17253"></a>7.14.11.1.1.4.1. Variable

The current variable is assigned as a preconfiguration when an existing variable is selected or a new one is created.

###### <a id="d4e17256"></a>7.14.11.1.1.4.2. Keyword

The current keyword is assigned as a preconfiguration when an existing keyword is selected or a new one is created.

###### <a id="d4e17259"></a>7.14.11.1.1.4.3. Functions

The desired function or operator can be selected from the list. The lists consists of the areas: mathematical, trigonometry, text and bit, tester data, log book data, measuring equipment, control module identification, control module references, DTC memory references, DTC memory information, symptom PUBC, symptom SAE, and symptom VAG. See also [Figure 410, “Function Selection List in Dialog”](7-14-12-category-mapping.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Zuordnung.Ausdruck_Auswahl "Figure 410. Function Selection List in Dialog").

###### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Definition.Asam_Mux_Auswahl"></a>7.14.11.1.1.4.4. From ODX

The button takes you to the "ASAM MUX Selection" dialog. An MUX case for a control module can be assigned using this dialog. For this case, the variables are provided with the "SwitchKey" data type.

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Definition.Asam_Mux_Auswahl"></a>

![Image: dialog - ASAM MUX Selection](images/fte_arbeitsflaeche_dialog_asam_mux_auswahl.png)

**Figure 402. Dialog - ASAM MUX Selection**

###### <a id="d4e17274"></a>7.14.11.1.1.4.5. Standard text

A default text can be assigned as a preselection. See also [Section 7.14.3.12, “Default Texts”](7-14-3-use-cases.md#Funktionstesteditor.Allgemeine_Funktionalitaet.Standardtexte "7.14.3.12. Default Texts").

###### <a id="d4e17278"></a>7.14.11.1.1.4.6. Text Library

A text from the text library can be assigned as a preselection. See also [Figure 209, “Text Selection in Table Cells”](7-1-17-using-text-ids-in-editing.md#figure.redaktion.text.tabellen "Figure 209. Text Selection in Table Cells").

###### <a id="d4e17282"></a>7.14.11.1.2. Visibility

The visibility of the variables can be specified here. There is a differentiation between internal program, transfer, and transfer/return. The visibility is based on the transfer of variables into the sub-program call-ups.

When "Transfer" is selected, a value or a variable is transferred from the main program into the sub-program. If "Transfer/return" is selected, the variable is not only transferred to the sub-program, but it also receives a value after the sub-program runs.

###### <a id="Funktionstesteditor.Declare.Protokollierung"></a>7.14.11.1.3. Logging

The variable output that is logged in the diagnostic log when using sub-programs can be suppressed in this column. The default for new variables and arrays is "Yes". If switched to "No", the main program must also be edited: the sub-program call-up dialog screen must be opened in a new instance and closed again. Background: The logging information must be known in the main program and is passed on to subprogram calls when the Java code is generated.

###### <a id="d4e17289"></a>7.14.11.1.4. Comment

A useful comment can be added to a variable in this location.

###### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Definition.Deklariere_Variablen.Bearbeiten"></a>7.14.11.1.5. Editing Variable Declaration

Pressing the “Edit” button opens another dialog (see [Figure 624, “Collaboration export display”](8-11-cooperation-export.md#figure.coopexport.overview "Figure 624. Collaboration export display")). The declaration of variables or an array can be modified in this dialog. Variable name, variable type, visibility of the variable, logging and comments can be modified here.

<a id="figure.edit.overview"></a>

![Image: Edit variable declaration dialog](images/fte_arbeitsflaeche_edit_deklariere.png)

**Figure 403. Editing Variable Declaration Dialog**

###### <a id="d4e17304"></a>7.14.11.1.5.1. Array Preselection

In the “Array” view, you can define a one-dimensional or two-dimensional array. The dialog also includes an “Apply” button, which is used to transfer values from the list copied from Excel to the “Preset” field and to convert these values automatically using an array format. The data is formatted according to certain rules to ensure that it is correctly transferred to the array.

###### <a id="d4e17307"></a>7.14.11.1.5.1.1. Converting the Values to an Array-Compatible Format

Values that span multiple lines (1D) or are separated by tabs (2D) are converted to corresponding one-dimensional or two-dimensional arrays.

The “Apply” button automatically detects the length of the array and sets this in the corresponding “Length” field.

###### <a id="d4e17311"></a>7.14.11.1.5.1.1.1. Line Breaks

Line breaks separate entries in the outer array. Each new line in the Excel list is interpreted as a new entry in the array.

For example, for five line breaks, the outer array length is six.

###### <a id="d4e17315"></a>7.14.11.1.5.1.1.2. Tabs and Spaces for Inner Arrays

Tabs and spaces serve as separators within the inner array to separate the values.

###### <a id="d4e17318"></a>7.14.11.1.5.1.1.3. Identification of Strings

String values must be marked with single quotation marks **‘ ’** and double quotation marks **“ ”**. If the string contains only one single or double quotation mark, the missing mark is automatically added during the transformation. However, if a value is already written between double quotation marks, it remains unchanged and is recognized as an array element. If string values are not written with any quotation marks, they are automatically enclosed in single quotation marks. Empty cells are recognized as empty strings and are automatically marked with **''**. See [Figure 405, “One-Dimensional Array Preselection”](7-14-11-category-definition.md#figure.edit.2dimensionalesliste "Figure 405. One-Dimensional Array Preselection").

###### <a id="d4e17325"></a>7.14.11.1.5.1.1.4. Number Formatting

Periods **.** and commas **,** are automatically interpreted as floating-point values. These do not affect the dimension of the array. Empty cells are marked as **0** (integer, short, byte data type) and **0.0** (double and floating). See [Figure 404, “One-Dimensional Array Preselection”](7-14-11-category-definition.md#figure.edit.einfacheliste "Figure 404. One-Dimensional Array Preselection").

###### <a id="d4e17333"></a>7.14.11.1.5.1.2. Application Examples

###### <a id="d4e17335"></a>7.14.11.1.5.1.2.1. Simple List

Input and output in the “Preset” field. (See [Figure 404, “One-Dimensional Array Preselection”](7-14-11-category-definition.md#figure.edit.einfacheliste "Figure 404. One-Dimensional Array Preselection")).

<a id="figure.edit.einfacheliste"></a>

![Image: one-dimensional array preselection](images/fte_arbeitsflaeche_edit_deklariere_1darray.png)

**Figure 404. One-Dimensional Array Preselection**

###### <a id="d4e17347"></a>7.14.11.1.5.1.2.2. Two-Dimensional List

Input and output in the “Preset” field. (See [Figure 405, “One-Dimensional Array Preselection”](7-14-11-category-definition.md#figure.edit.2dimensionalesliste "Figure 405. One-Dimensional Array Preselection")).

<a id="figure.edit.2dimensionalesliste"></a>

![Image: one-dimensional array preselection](images/fte_arbeitsflaeche_edit_deklariere_2darray.png)

**Figure 405. One-Dimensional Array Preselection**

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Definition.Deklariere_Variablen.Markenvariablen"></a>7.14.11.2. Using Brand Variables

Brand variables can be used to save and to use run-time values using a diagnostic session across all functions. Usually, the brand variables are set during the diagnostic entry, so that they can be evaluated later. The brand variables will remain available, until a new diagnostic entry has been started again.

With the new brand variables, it is possible to determine information from the control module communication only one time and to use them directly in other test programs, without having to repeat the control module communication. In a similar way, user entries made by the technician one time can also be recorded through a diagnostic session, without opening or entering them again. The use of brand variables improves the GFF creation process, the data processing security and increases the GFF quality. This will also save you time by avoiding additional control module communication.

The incorporation of brand variables in the function codes occurs through the "Declare variable" action element. After incorporating, the brand variables can be used within the function codes like normal variables.

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Definition.Deklariere_Variablen_Markenvariable_auswaehlen"></a>

![Image: selecting brand variables](images/fte_arbeitsflaeche_dialog_deklarierevariablen_markenvariablen_auswaehlen.png)

**Figure 406. Selecting Brand Variables**

Brand variables are selected with the „…“ button in the „Name“ column. Manual input is not possible. When brand variables are selected, a function test variable with the same type as the brand variable is declared at the same time and assigned to the brand variables.

The cell editor is active when clicking on the "Variable" cell. When clicking on the „…“ button, a pop-up menu opens which enables the selection of brand variables. The selection is entered in the "Variable" column. The properties of this menu structure are as follows:

- The menu structure matches the following hierarchy: brand / type / brand variable name
- All brand variables are listed for all brands.
- All brand variables are listed regardless of their status.
- All menu items are sorted alphanumerically.
- Deactivated brand variables are not displayed.
- Submenus without menu items are not displayed.
- Array names contain the field sizes, for example, V\_int\_Array[10,10].
- The tool tip for brand variables in the menu selection contains the properties of the brand variables (name, type, log, comments).

The variable receives the allocation to the brand variables after selecting the brand variables from the menu. The attributes are transferred for this and set at the function test variables:

- The "Name", the "Variable type", the "Log" and the "Comments" are transferred.
- The "Visibility" attribute is fixed to the value "Transfer/return"
- The other attributes "Constant" and "Preset" do not change.

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Definition.Deklariere_Variablen_Markenvariable_verwenden"></a>

![Image: using brand variables](images/fte_arbeitsflaeche_dialog_deklarierevariablen_markenvariablen_verwenden.png)

**Figure 407. Using Brand Variables**

The lines are grayed out after the transfer, which prevents changing all attributes with the following exceptions:

- Another brand variable under "Name" can be selected.
- The "Constant" attribute can be changed.

The function test variable with brand variable allocation behaves like all other function test variables when it is used. The allocation rules for brand variables are checked with the dialog validation in the "Declare variable" dialog. Here are the following rules for validation:

<a id="d4e17418"></a>

<table border="1" summary="Brand Variable Usage Validation"><colgroup><col/><col/><col/><col/></colgroup><thead><tr bgcolor="#EEEEEE"><th>Status of brand variables</th><th>Dialog validation</th><th>Function test validation</th><th>Consistency check</th></tr></thead><tbody><tr><td>Variable type of brand variable is different from the variable type in the function test.</td><td>Dialog transfer not possible.</td><td>Fatal level: the entry is listed in the problem view. Saving the function test is not possible.</td><td>-</td></tr><tr><td>Assigned brand variable is in the "in processing" status.</td><td>Dialog transfer possible.</td><td>Warning level: the entry is listed in the problem view. Saving the function test is possible.</td><td>Function test is inconsistent. An error is listed in the test log.</td></tr><tr><td>Assigned brand variable is deleted</td><td>Dialog transfer not possible.</td><td>Fatal level: the entry is listed in the problem view. Saving the function test is not possible.</td><td>-</td></tr><tr><td>Assigned brand variable is deactivated</td><td>Dialog transfer possible.</td><td>Warning level: the entry is listed in the problem view. Saving the function test is possible.</td><td>Function test consistent. A warning is listed in the test log.</td></tr></tbody></table>

**Table 75. Brand Variable Usage Validation**

If you use a brand variable for the first time without having been previously listed, then this brand variable receives the default value for its respective data type. The following table lists the various default values based on the respective data type.

<a id="d4e17454"></a>

<table border="1" summary="Default Values for Brand Variables"><colgroup><col/><col/></colgroup><thead><tr bgcolor="#EEEEEE"><th>Data type</th><th>Default value</th></tr></thead><tbody><tr><td>Bool</td><td>0</td></tr><tr><td>Byte</td><td>0</td></tr><tr><td>Double</td><td>0.0</td></tr><tr><td>Float</td><td>0.0</td></tr><tr><td>Integer</td><td>0</td></tr><tr><td>Long</td><td>0</td></tr><tr><td>Short</td><td>0</td></tr><tr><td>String</td><td>" or empty string</td></tr><tr><td>SwitchKey</td><td>" or empty string</td></tr></tbody></table>

**Table 76. Default Values for Brand Variables**

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Definition.Deklariere_Variablen.Beispiele"></a>7.14.11.3. Examples for the Action Element - Declare Variable

<a id="d4e17494"></a>

<table border="1" summary="Examples for Declare Variable Content Command"><colgroup><col align="left"/><col align="left"/><col align="left"/><col align="left"/></colgroup><thead><tr bgcolor="#EEEEEE"><th align="left">Variable</th><th align="left">Defaults</th><th align="left">Type</th><th align="left">Explanation</th></tr></thead><tbody><tr><td align="left">z</td><td align="left">100 or 0x64 or 10**2 or 1E+2</td><td align="left">Integer</td><td align="left">This variable type uses all positive or negative numbers. The value range depends on the PC system. If the preconfiguration is missing, the value zero is automatically assigned when running. Decimal, hexadecimal, or exponential forms are possible in the preconfiguration. The value range contains the numbers -2.147.483.648 through b+2.147.483.647 (32-bit word).</td></tr><tr><td align="left">error[11]</td><td align="left">5</td><td align="left">Integer</td><td align="left">Declaration for a field variable with 11 elements (error[0] through error[10]). The preset is 5 for all elements.</td></tr><tr><td align="left">error[5]</td><td align="left">1;2;3;4;99</td><td align="left">Integer</td><td align="left">Declaration for a field variable with 5 elements (error[0] through error[4]) with individual presets: error[0] = 1, error[1] = 2 .through error[4] = 99.</td></tr><tr><td align="left">field[2,3]</td><td align="left"> </td><td align="left">String</td><td align="left">Declaration of a two-dimensional field with 2 x 3 elements and a preset with the string "empty". Element addressing: field[0,0], field[1,0], field[0,1], field[1,1], field[0,2], field[1,2].</td></tr><tr><td align="left">k_temp_max</td><td align="left">80.0</td><td align="left">Float</td><td align="left">Declaration of a variable for natural numbers. Most frequent command: storing measured values. Presets are written with a decimal point.</td></tr><tr><td align="left">VIN</td><td align="left"> </td><td align="left">String</td><td align="left">rejected, because it's a reserved word in the test language</td></tr><tr><td align="left">status_specified</td><td align="left">'00000111'</td><td align="left">String</td><td align="left">System strings are not relevant for translation and are in single apostrophes.</td></tr><tr><td align="left">status_actual</td><td align="left">''</td><td align="left">String</td><td align="left">Empty system string</td></tr><tr><td align="left">text_01</td><td align="left">"Threshold reached"</td><td align="left">String</td><td align="left">Text strings are relevant for translation are in double apostrophes.</td></tr><tr><td align="left">textoutput</td><td align="left">""</td><td align="left">String</td><td align="left">Empty text string</td></tr><tr><td align="left">linew</td><td align="left">"\n" or '\n'</td><td align="left">String</td><td align="left">creates a line change</td></tr><tr><td align="left">tab</td><td align="left">"\t" or '\t'</td><td align="left">String</td><td align="left">jumps to the next tab location</td></tr><tr><td align="left">blue</td><td align="left">"\B"</td><td align="left">String</td><td align="left">switches to blue text (only for text strings)</td></tr><tr><td align="left">specialchar</td><td align="left">"\337"</td><td align="left">String</td><td align="left">creates a "ß" (only as a text string)</td></tr><tr><td align="left">one</td><td align="left">1</td><td align="left">Bool</td><td align="left">Only "1" or "0" can be used. This type is suitable for defining internal control variables for recording status, such as "On", "Off", or "Error", "No error".+</td></tr><tr><td align="left">counter</td><td align="left">1</td><td align="left">Byte</td><td align="left">This variable type uses all positive or negative numbers in the range from -128 through +127 (8-bit word) Typical usage: counter in a loop with a low number of cycles</td></tr><tr><td align="left">result[5]</td><td align="left">0</td><td align="left">Byte (as field)</td><td align="left">Declaration and initialization of a "result" byte field with a field size of 5. The elements result[0] through result[4] are generated. The individual value allocation is done in the "Expression" command. The preconfiguration applies to all elements.</td></tr><tr><td align="left">x</td><td align="left">125</td><td align="left">Long</td><td align="left">This variable type uses all positive or negative numbers in the range from -9.223.372.036.854.775.808 through 9.223.372.036.854.775.807 (64-bit word)</td></tr><tr><td align="left">pi</td><td align="left">3.1415927</td><td align="left">Double</td><td align="left">Declaration of the constant "pi" with assigned fixed value. The content can no longer be changed in the program. The constants are specified using an extra column. Constants can have any data type</td></tr><tr><td align="left">Number</td><td align="left">12</td><td align="left">Short</td><td align="left">This variable type uses all positive or negative numbers in the range from -32.768 through 32.767 (16-bit word)</td></tr><tr><td align="left">Engine</td><td align="left">'Case_MeasuValue VoltaScale'</td><td align="left">SwitchKey</td><td align="left">Using the "SwitchKey" data type, a parameter from an ASAM control module can be assigned in a variable.</td></tr></tbody></table>

**Table 77. Examples for Declare Variable Content Command**

###### <a id="d4e17614"></a>7.14.11.3.1. Multi-Dimensional Arrays

The number of cells results from the multiplication of the individual dimensions. For example, numbers[3,3,3] results in a total of 37 cells. The specified dimensions do not need to be identical. For example, numbers[2,3] will result in 6 cells.

The preconfiguration can be used for all cells with a declare command and a value such as numbers[4,4,4] or individually, such as numbers[2,2] = 1;2;3;4.

The individual dimensions can be controlled using variables, such as x=2, y=4, z=4 and numbers[x,y,z]=1. The addressing of individual cells can be done, for example, in an expression in a loop, such as cell=number[z,y,z]. The individual variables can run using nested While loops.

###### <a id="d4e17619"></a>7.14.11.3.2. Text String

A text string is enclosed in double quotes "<textstring>". ODIS Creator then recognizes that this text is relevant for translation. When gathering the text to be translated, texts marked in this way are automatically placed in the translation table. Only texts declared as text strings are converted into the formatted format for text output in output instructions (message, question, help).

Examples:

Declare, type "String":text\_output = ""text\_01 = "Hello"text\_02 = "World"tab = "\t"blue = "\B"

Expression:

text\_output = text\_01 CAT tab CAT blue CAT text\_02

###### <a id="d4e17626"></a>7.14.11.3.3. System String

A system string is enclosed in single quotes. ODIS Creator then recognizes that this text is not relevant for translation. Only the following control characters can be used:

- Line change
- Single quote output
- Tab
- Backslash output

###### <a id="d4e17638"></a>7.14.11.3.4. Special characters

There are restrictions for the characters "%", "$", and "@". The percent symbol introduces a variable, a dollar sign introduces the keyword, and the "at" symbol introduces default text. The characters may be used alone, such as 10 %. The direct use of single or double quotes in the text is forbidden. The backslash is used to identify control operations within texts (see above).

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Definition.Definiere_Kennwort"></a>7.14.11.4. Action Element - Define Keyword

The "Define keyword" action element can be seen in [Figure 408, “Action Element - Define Keyword”](7-14-11-category-definition.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Definition.Definiere_Kennwort "Figure 408. Action Element - Define Keyword").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Definition.Definiere_Kennwort"></a>

![Image: Define_keyword action element](images/fte_arbeitsflaeche_dialog_definierekennwort.png)

**Figure 408. Action Element - Define Keyword**

Keywords that can be used by the test steps that follow can be defined using the **Define keyword** action element.

The keyword table shows the defined keywords.

###### <a id="d4e17656"></a>7.14.11.4.1. Buttons above the table

- A new keyword is created using the plus.
- A keyword that is marked is duplicated using the double plus.
- The minus deletes the keyword that was marked.

###### <a id="d4e17665"></a>7.14.11.4.1.1. Keyword

The name of the keyword is entered in this column. It can be edited directly in the list. Keywords are differentiated from variables by the dollar sign character ($) at the beginning.

###### <a id="d4e17668"></a>7.14.11.4.1.2. Type

The keyword data type can be selected using a selection field.

###### <a id="d4e17671"></a>7.14.11.4.1.3. Substituent

The substituent depends on the selected type. The substituent is used during runtime. Globally-defined keywords behave like constants. You can define keywords and provide them with a substituent using this command.

###### <a id="d4e17674"></a>7.14.11.4.1.4. Visibility

The visibility setting matches the "Declare variable" setting, except for one difference. It is not possible to assign the visibility "Transfer/return" to a keyword.

###### <a id="d4e17677"></a>7.14.11.4.1.5. Logging

See [Section 7.14.11.1.3, “Logging”](7-14-11-category-definition.md#Funktionstesteditor.Declare.Protokollierung "7.14.11.1.3. Logging").

###### <a id="d4e17681"></a>7.14.11.4.1.6. Comment

A useful comment can be added to a variable in this location.

###### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Definition.Definiere_Kennwort.Beispiele"></a>7.14.11.4.2. Examples

<a id="d4e17687"></a>

<table border="1" summary="Example for Content of Definition Command"><colgroup><col align="left"/><col align="left"/><col align="left"/><col align="left"/><col align="left"/></colgroup><thead><tr bgcolor="#EEEEEE"><th align="left">Keyword</th><th align="left">Type</th><th align="left">Substituent</th><th align="left">Visibility</th><th align="left">Comment</th></tr></thead><tbody><tr><td align="left">$Location</td><td align="left">String</td><td align="left">'G28'</td><td align="left">Transfer</td><td align="left">For determining</td></tr><tr><td align="left">$Code</td><td align="left">String</td><td align="left">'Code according to ISO16949'</td><td align="left">Transfer</td><td align="left">Name of code</td></tr></tbody></table>

**Table 78. Example for Content of Definition Command**

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-14-10-category-dialog.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="7-14-function-test-editor.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="7-14-12-category-mapping.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">7.14.10. Category - Dialog </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 7.14.12. Category - Mapping</td></tr></table>
