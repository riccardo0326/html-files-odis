[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md) > [7.14. Function Test Editor](7-14-function-test-editor.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.14.25. Problems (View)</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-14-24-java-code-view.md">Prev</a> </td><th align="center" width="60%">7.14. Function Test Editor</th><td align="right" width="20%"> <a accesskey="n" href="7-14-26-search-view.md">Next</a></td></tr></table>

---

#### <a id="Funktionstesteditor.Zusaetzliche_Views.Probleme_View"></a>7.14.25. Problems (View)

The errors that occurred during function test validation and compilation are displayed in this view. See [Figure 543, “Problems View”](7-14-25-problems-view.md#figure.Funktionstesteditor.Zusaetzliche_Views.Probleme_View "Figure 543. Problems View").

Events with different weights (information, warning, error) and origin are displayed in table form in the problems view. The events are based on commands (column: Location). A detailed text about the event is given in the Description column.

The origin of a problem can be:

- Compile: compilation of the GFF Java code
- Syntax: syntax check in GFF
- Empty: empty instructions in GFF
- Migration: migration of data into ODIS Creator
- EcuUsageUpdate: import of control modules into ODIS Creator
- Transformation: removal of redundant format instructions in XML
- Replace: replace function in the function test editor
- TextIdUsage: usage of text IDs
- Parameter: parameter assignment of sub-programs
- Import: import function of ODIS Creator

The problems view is updated after opening a function test and after performing a test (called up by saving, among other things). The problems are sorted in descending order based on weight (error, warning, information) and, within the weight, based on the vertical location of the node. The Problems view is also updated when an instruction dialog is confirmed and when instructions are pasted in from the clipboard, but this does not move the view into the front.

<a id="figure.Funktionstesteditor.Zusaetzliche_Views.Probleme_View"></a>

![Image: function test editor - additional views - problems](images/fte_Probleme_View.png)

**Figure 543. Problems View**

The default sorting can be replaced by alphabetical sorting of the columns in three stages (natural, ascending, descending). Click on the column headers for the columns that you would like to sort.

The two buttons in the upper right corner trigger the following functions from left to right:

- Check and display errors again
- Detail view

In addition to these two functions, you can also double-click on the entries. The corresponding dialog is then opened where the described error exists.

##### <a id="Funktionstesteditor.Zusaetzliche_Views.Probleme_View.SGB_Import"></a>7.14.25.1. Messages in the View based on Control Module Description Imports

Importing control module descriptions can lead to various conflicts in existing function code objects. If these systems cannot be resolved automatically by the system, they will be displayed in the list and also listed in a control module import log file. This will allow you to make the necessary modifications to function code objects for the changed control module descriptions. As with other error messages, you can open the corresponding ASAM dialog where the error is located by double-clicking on an entry. After the corrections have been made, the changes must be confirmed by clicking OK in the dialog. The problem entries are cleared from the list when a new compilation process is run.

All error messages that may occurring during an import of control module descriptions are listed in [Table 128, “Possible Warnings after Control Module Import”](7-14-25-problems-view.md#table.Probleme_View.Problembeschreibung "Table 128. Possible Warnings after Control Module Import"). The table also contains a brief description (second column) about the meaning of the error message and how the error can be corrected (third column).

<a id="table.Probleme_View.Problembeschreibung"></a>

<table border="1" summary="Possible Warnings after Control Module Import"><colgroup><col align="left"/><col align="left"/><col align="left"/></colgroup><thead><tr bgcolor="#EEEEEE"><th align="left">Warning in problem view for the FTE</th><th align="left">Explanation</th><th align="left">Correction instructions</th></tr></thead><tbody valign="top"><tr><td align="left" valign="top">The value for parameter 'X' in operation 'Y' is no longer compatible with the new version of the control module description.</td><td align="left" valign="top">The current version of the control module description contains other Enum values for the parameter 'X' from the function 'Y'.</td><td align="left" valign="top">Select the current version of the control module description in the system in the "Control module variant" input field. Set the operation parameter to another value that is present.</td></tr><tr><td align="left" valign="top">The type for parameter 'X' in operation 'Y' is no longer compatible with the new version of the control module description.</td><td align="left" valign="top">The type of parameter 'X' for the operation 'Y' has changed with the current version of the control module description.</td><td align="left" valign="top">Select the current version of the control module description in the system in the "Control module variant" input field. The type and value of the operation parameters change accordingly.</td></tr><tr><td align="left" valign="top">The check parameter 'X' for operation 'Y' is no longer contained in the new version of the control module description.</td><td align="left" valign="top">The current version of the control module description no longer contains the check parameter 'X' for the operation 'Y'.</td><td align="left" valign="top">Select the current version of the control module description in the system in the "Control module variant" input field. Set a different check parameter for the corresponding operation.</td></tr><tr><td align="left" valign="top">The response parameter 'X' for operation 'Y' is no longer contained in the new version of the control module description.</td><td align="left" valign="top">The current version of the control module description no longer contains the response parameter 'X' for the operation 'Y'.</td><td align="left" valign="top">Select the current version of the control module description in the system in the "Control module variant" input field. Set a different response parameter for the corresponding operation.</td></tr><tr><td align="left" valign="top">Operation 'X' is no longer contained in the new version of the control module description.</td><td align="left" valign="top">The logical link for the current version of the control module description no longer contains operation 'X'.</td><td align="left" valign="top">Select the current version of the control module description in the system in the "Control module variant" input field. Select another operation in the "Diagnostic service" field.</td></tr><tr><td align="left" valign="top">Logical link 'X' is no longer contained in the new version of the control module description.</td><td align="left" valign="top">The logical link for the current version of the control module description is not compatible with the value in the 'Logical link' field for the ASAM Ecukom dialog.</td><td align="left" valign="top">Select the current version of the control module description in the system in the "Control module variant" input field. Set parameters for the corresponding operation. This automatically adapts the values in the 'Logical link' selection field so you can then select a new suitable value.</td></tr><tr><td align="left" valign="top">Logical links are no longer compatible with the new version of the control module description.</td><td align="left" valign="top">The logical link for the current version of the control module description is not compatible with the values in the 'Logical link' selection field for the ASAM Ecukom dialog.</td><td align="left" valign="top">Select the current version of the control module description in the system in the "Control module variant" input field. Set parameters for the corresponding operation. This adapts the values in the 'Logical link' selection field automatically.</td></tr><tr><td align="left" valign="top">There is no current version for the control module description; the old version will be used.</td><td align="left" valign="top">The ASAM Ecukom element uses an old version of the control module description that was not updated during the last control module import.</td><td align="left" valign="top">Select a control module description that exists in the system with corresponding operation and parameters.</td></tr><tr><td align="left" valign="top">The control module description is ambiguous (ID missing). A check for the new version of the control module description is not possible.</td><td align="left" valign="top">The ASAM Ecukom element (in the XML file) does not contain an ID for the control module description that is used. It may not have been possible to set this during the data migration.</td><td align="left" valign="top">Select a control module description that exists in the system with a corresponding operation and parameters so that the ID can be set.</td></tr><tr><td align="left" valign="top">The reference for the control module description was replaced by the current version.</td><td align="left" valign="top">Information that the control module description was successfully replaced by the system.</td><td align="left" valign="top">No need for action.</td></tr></tbody></table>

**Table 128. Possible Warnings after Control Module Import**

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-14-24-java-code-view.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="7-14-function-test-editor.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="7-14-26-search-view.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">7.14.24. Java Code (View) </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 7.14.26. Search (View)</td></tr></table>
