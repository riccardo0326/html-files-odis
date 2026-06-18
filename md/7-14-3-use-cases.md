[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md) > [7.14. Function Test Editor](7-14-function-test-editor.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.14.3. Use cases</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-14-2-menus-and-tool-bars.md">Prev</a> </td><th align="center" width="60%">7.14. Function Test Editor</th><td align="right" width="20%"> <a accesskey="n" href="7-14-4-drag-and-drop.md">Next</a></td></tr></table>

---

#### <a id="Funktionstesteditor.Allgemeine_Funktionalitaet2"></a>7.14.3. Use cases

##### <a id="Funktionstesteditor.Allgemeine_Funktionalitaet.Oeffnen_eines_Funktionstests"></a>7.14.3.1. Opening a Function Test

Function tests can be opened as follows.

###### <a id="Funktionstesteditor.Allgemeine_Funktionalitaet.Oeffnen_eines_Funktionstests.OEE"></a>7.14.3.1.1. Opening with an Object Properties Editor

If a function code is opened in the object properties editor, the associated function test can be opened in the function test editor using the "Test sequence" function. This function is available in the context menu, in the global menu under Extras -> Editor menu, and in the tool bar. It then appears on the desktop. Multiple function tests can be opened, and can then be selected using the tabs above the desktop.

###### <a id="Funktionstesteditor.Allgemeine_Funktionalitaet.Oeffnen_eines_Funktionstests.Validierung"></a>7.14.3.1.2. Validation

The function test is validated when opened. If a function test does not contain a valid XML, it cannot be opened. A corresponding error message appears. See [Figure 337, “Validation Error”](7-14-3-use-cases.md#figure.Funktionstesteditor.Allgemeine_Funktionalitaet.Oeffnen_eines_Funktionstests "Figure 337. Validation Error").

<a id="figure.Funktionstesteditor.Allgemeine_Funktionalitaet.Oeffnen_eines_Funktionstests"></a>

![Image: validation error](images/fte_Validierungsfehler.png)

**Figure 337. Validation Error**

##### <a id="Funktionstesteditor.Allgemeine_Funktionalitaet.Speichern"></a>7.14.3.2. Save

Changes that were made in the function test can be saved. Clicking on the disk symbol in the tool bar saves the active editor. Saving the prepared function test by exporting it is recommended. Changes can then be made with the current version and also saved. The changes are saved in the open function test. There is no prompt to ask for a different file name to save under.

A function test cannot be saved if action elements were created but not edited. See [Section 7.14.9.3, “Create Action Element”](7-14-9-desktop.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Anlegen "7.14.9.3. Create Action Element").

The XML that was created is validated when saving and entered into the test language. The code that results is displayed in the **Java code** view<a id="d4e15225"></a>, see [Section 7.14.23, “XML View”](7-14-23-xml-view.md "7.14.23. XML View") or [Section 7.14.24, “Java Code (View)”](7-14-24-java-code-view.md "7.14.24. Java Code (View)"), and compiled. Errors that occur are displayed in the **Problems** view. See [Section 7.14.25, “Problems (View)”](7-14-25-problems-view.md "7.14.25. Problems (View)").

When saving an edited function code in read-only mode, it is possible to save the content locally or on the server. Pressing the “No” button saves the function code locally. Pressing the “Yes” button performs the following actions:

- The function code and object are checked out (same functionality as “Placing Function Test in Editing Status,” see [Section 7.15.11.5, “Placing Function Test in Editing Status”](7-15-11-additional-debug-functions.md#Funktionstesteditor.Debugger.FunktionstestInBearbeitung_setzen "7.15.11.5. Placing Function Test in Editing Status"))
- The function code is saved
- The function code is also checked in after saving if a function, including check-in, was performed.

<a id="figure.Funktionstesteditor.Allgemeine_Funktionalitaet.Speichern_eines_Funktionstests_Readonly"></a>

![Image: Checking out a read-only function code](images/fte_readonly_funktionscode_auschecken.png)

**Figure 338. Checking Out a Read-Only Function Code**

##### <a id="Funktionstesteditor.Allgemeine_Funktionalitaet.KombiniertesSpeichern"></a>7.14.3.3. Combined Save

This function is similar to the Save function (see [Section 7.14.3.2, “Save”](7-14-3-use-cases.md#Funktionstesteditor.Allgemeine_Funktionalitaet.Speichern "7.14.3.2. Save")), except the linked object properties editor is also saved. By saving the object properties editor, the function test is saved on the ODIS Creator server. You can continue working directly after the combined save: the function test remains open and in the "In editing" status.

To be able to save a function test and its test sequence together, all required fields in the function test must be filled out and there must be at least one change made in the test sequence. You can save the test sequence and the associated file in the test sequence function test editor using the menu **File -> Combined save**.

If a non-modal dialog for the focused function test is opened during a combined save, a yes/now prompt appears which offers the option to automatically accept the dialog.

##### <a id="Funktionstesteditor.Allgemeine_Funktionalitaet.Drucken"></a>7.14.3.4. Print

The current function test can be printed using this function. After activating the function, you can select the area to be printed. See [Figure 339, “Area Selection”](7-14-3-use-cases.md#figure.Funktionstesteditor.Allgemeine_Funktionalitaet.Drucken.Bereichsauswahl "Figure 339. Area Selection"). The default setting is to print the commands.

<a id="figure.Funktionstesteditor.Allgemeine_Funktionalitaet.Drucken.Bereichsauswahl"></a>

![Image: area selection](images/fte_Druck_Export_Bereichsauswahl_Dialog.png)

**Figure 339. Area Selection**

Depending on the area selection, the corresponding section or the complete content of the function test may be sent to the printer. The test steps are always placed above the commands. A selection in the function test editor does not affect the print scope.

A sample printout is shown in [Figure 340, “Print”](7-14-3-use-cases.md#figure.Funktionstesteditor.Allgemeine_Funktionalitaet.Drucken "Figure 340. Print").

<a id="figure.Funktionstesteditor.Allgemeine_Funktionalitaet.Drucken"></a>

![Image: printing commands](images/fte_Drucken.png)

**Figure 340. Print**

##### <a id="Funktionstesteditor.Allgemeine_Funktionalitaet.SVG_Export"></a>7.14.3.5. SVG Export

This function exports the currently-selected function test in SVG format. See [Figure 341, “SVG Export”](7-14-3-use-cases.md#figure.Funktionstesteditor.Allgemeine_Funktionalitaet.SVG_Export "Figure 341. SVG Export"). The content can be viewed with [Adobe SVG Viewer](http://www.adobe.com/svg/viewer/install), for example.

When exporting SVG, you can select the area you would like to export (commands, test steps, all). See [Figure 339, “Area Selection”](7-14-3-use-cases.md#figure.Funktionstesteditor.Allgemeine_Funktionalitaet.Drucken.Bereichsauswahl "Figure 339. Area Selection"). Test steps are always placed above commands.

The icons and the JavaScript<a id="d4e15286"></a>for the display and the tool tip are copied into the 'Palette' folder related to the SVG file to be exported.

The following image shows an example display of the SVG export in a browser.

<a id="figure.Funktionstesteditor.Allgemeine_Funktionalitaet.SVG_Export"></a>

![Image: SVG export](images/fte_SVG.png)

**Figure 341. SVG Export**

##### <a id="Funktionstesteditor.Allgemeine_Funktionalitaet.Perspektive_Zuruecksetzen"></a>7.14.3.6. Reset View

The individual views can be hidden. You can undo this using the **Reset view** function. All views are shown again. The selected zoom factor is not reset.

##### <a id="Funktionstesteditor.Allgemeine_Funktionalitaet.Funktionstestanzeige_Aktualisieren"></a>7.14.3.7. Update Local Function Test Display

When this function is activated, the function test display in the right view is updated.

##### <a id="Funktionstesteditor.Allgemeine_Funktionalitaet.Javacode_Aktualisieren"></a>7.14.3.8. Update Java Code

This function is used to update the<a id="d4e15307"></a>code displayed in the Java code view. See [Section 7.14.24, “Java Code (View)”](7-14-24-java-code-view.md "7.14.24. Java Code (View)"). Otherwise, the Java code is only updated when the function test is opened.

##### <a id="Funktionstesteditor.Allgemeine_Funktionalitaet.Javacode_Kompilieren"></a>7.14.3.9. Compiling Java code

There are three compilation options available in the ODIS Creator client. These can be called up either via the menu, via buttons in the Java code tab (see also [Section 7.14.24, “Java Code (View)”](7-14-24-java-code-view.md "7.14.24. Java Code (View)")) or via keyboard shortcuts.

The three compilation options are described below.

###### <a id="Funktionstesteditor.Allgemeine_Funktionalitaet.Javacode_Kompilieren_normal"></a>7.14.3.9.1. Compile

This function includes the general activities for compiling a function test:

- The Java code is recreated and temporarily saved (update Java code).
- The Java file is compiled with all check language jars and debug jars in the class path.
- Compilation errors are listed in the Problems tab. The Problems tab is activated if errors have been entered, see also [Section 7.14.25, “Problems (View)”](7-14-25-problems-view.md "7.14.25. Problems (View)").

It runs locally on the computer. Saving the test sequence beforehand is not absolutely necessary to execute the function. Errors found are highlighted in the test sequence and can be accessed via the entries in the Problems tab.

###### <a id="Funktionstesteditor.Allgemeine_Funktionalitaet.Javacode_Kompilieren_server"></a>7.14.3.9.2. Compile on server

This function has the same scope as compilation, but runs on the server. The same compilation is carried out that is also carried out with the completion message. If a test sequence has been edited, it must be saved beforehand (see also [Section 7.14.3.2, “Save”](7-14-3-use-cases.md#Funktionstesteditor.Allgemeine_Funktionalitaet.Speichern "7.14.3.2. Save")), otherwise this function is not executed. The compilation takes place asynchronously on the server. When the function is finished, the user receives a dialog message indicating whether the compilation was successful or not. Several compilations can be started simultaneously; these are then processed one after the other. The dialog message contains the name of the relevant function test. Errors found are not highlighted in the test sequence and cannot be accessed via the entry in the Problems tab. The message in the Problems tab matches the compiler’s feedback and is not filtered. This function can be used to check whether a “code too large” problem would occur before the completion message appears. The function supplements the existing “Compile function test” function, as the client and server use different compilers, which can lead to different results. This function allows the author to check at an early stage whether server-side checks (e.g. consistency checks) are run without errors. This increases the likelihood that the deployment will complete successfully.

###### <a id="Funktionstesteditor.Allgemeine_Funktionalitaet.Javacode_Kompilieren_Debug"></a>7.14.3.9.3. Compile for debugging

This function has the same scope as compilation when the debugger is called up. It can be used to find problems during compilation before the debugger is started. If a test sequence has been edited, it must be saved beforehand (see also [Section 7.14.3.2, “Save”](7-14-3-use-cases.md#Funktionstesteditor.Allgemeine_Funktionalitaet.Speichern "7.14.3.2. Save")), otherwise this function is not executed. If there is already a syntax error, the debug compilation is aborted and a dialog message is output. The compilation takes place asynchronously on the local computer. After the function has been completed, the user receives a dialog message indicating whether the compilation was successful or not. Several compilations can be started simultaneously; these are then processed one after the other. The dialog message contains the name of the relevant function test. This function can be used to check whether a “code too large” problem would occur before starting the debugger. This function is similar to the debug function, but focuses exclusively on generating and validating functional tests for Java code. It is not necessary to open or close the debug window.

##### <a id="Funktionstesteditor.Allgemeine_Funktionalitaet.Problemansicht_Aktualisieren"></a>7.14.3.10. Update Problems View

The problems view can be updated with this function. See [Section 7.14.25, “Problems (View)”](7-14-25-problems-view.md "7.14.25. Problems (View)").

##### <a id="Funktionstesteditor.Allgemeine_Funktionalitaet.Details_Anzeigen"></a>7.14.3.11. Show Details

This function is used to display details about entries in the problems view. See [Section 7.14.25, “Problems (View)”](7-14-25-problems-view.md "7.14.25. Problems (View)").

##### <a id="Funktionstesteditor.Allgemeine_Funktionalitaet.Standardtexte"></a>7.14.3.12. Default Texts

This function is reached using a button labeled "Default" in the dialog for the action elements 'Question', 'Message', 'Test module title', 'Input', 'Help', 'Vehicle test point dialog' (for example, reached using the oscilloscope, DSOx cable selection). If you click this button, a dialog where you can select a default text appears. See [Figure 342, “Default Texts”](7-14-3-use-cases.md#figure.Funktionstesteditor.Allgemeine_Funktionalitaet.Standardtexte "Figure 342. Default Texts").

<a id="figure.Funktionstesteditor.Allgemeine_Funktionalitaet.Standardtexte"></a>

![Image: default texts](images/fte_Standardtext.png)

**Figure 342. Default Texts**

The selection is made by:

- selecting the text group
- selecting a default text.

If the dialog is confirmed with the OK button, a reference to the selected default text is automatically entered in the text field at the current cursor location (for example, '@[std]myStdTextID'). Nothing is entered after pressing the Cancel button. Default texts can only be created by a text administrator (see [Section 5.5, “Default Texts”](5-5-default-texts.md "5.5. Default Texts")).

##### <a id="Funktionstesteditor.Allgemeine_Funktionalitaet.URL-Liste"></a>7.14.3.13. URL List

The URL list is used in the action elements: 'Send online', 'Receive online', 'Send log'. The selection field shown there is filled with the corresponding values from the server.

##### <a id="Funktionstesteditor.Allgemeine_Funktionalitaet.XML-Templates"></a>7.14.3.14. XML Templates

XML templates are used in the five action elements from the category. The selection dialog is filled with corresponding values from the server.

##### <a id="Funktionstesteditor.Debugger.FunktionstestUebersetzungsinformation_anzeigen"></a>7.14.3.15. Change Display of Translation-Relevant Texts

This function allows you to visualize changes to translation-relevant texts. Using this display, you can determine early on if a change was made to translation-relevant texts. The display itself does not affect the translation of the texts for the function test. It is used only for visualization purposes for the author to see what types of changes have been made. Therefore, the change display may differ from the translation result. Depending on which status is the standard for your brand at the start of translation (Completed or Released), the change indicator may need to be interpreted differently.

Each change to a translation-relevant field in a command or a test step results in the need to translate the function test. Translation-relevant fields include one-line and multi-line texts fields (rich text editor) and expression fields, if they contain translation-relevant literal text.

The change indicator for translation-relevant texts indicates the change information for brands with "Release” translation trigger in three stages, as follows:

- Gray and deactivated: indicates that no translation-relevant text changes were made in the function test.
- Blue: indicates that the current version cycle of the function test contains translation-relevant text changes.
- Red: indicates that the user has made translation-relevant text changes after opening the function test.

The change indicator for translation-relevant texts indicates the change information for brands with "Completed” translation trigger in three stages, as follows:

- Gray and deactivated: indicates that no translation-relevant text changes have been made to the function test since the last relevance point (Completion or Release, whichever occurred last).
- Blue: indicates that the function test contains translation-relevant text changes in the current version cycle since the last relevance point (Completion or Release, whichever occurred last).
- Red: indicates that the user has made translation-relevant text changes after opening the function test.

In ODIS Creator, the change display for translation-relevant texts is displayed in the tool bar when opening a function test. It is grayed out as long as no translation-relevant changes were made to the function test in the version cycle.

<a id="figure.Funktionstesteditor.Allgemeine_Funktionalitaet.Uebersetzungsanzeige.Grau"></a>

![Image: change display for translation-relevant texts: gray](images/fte_allgemein_aenderungsanzeige_uebtexte_grau.png)

**Figure 343. Change Display for Translation-Relevant Texts: Gray**

If translation-relevant texts were changed or added in the version cycle for a function test (without a temporary change after opening), then the change status is initially shown as a blue icon in the tool bar.

<a id="figure.Funktionstesteditor.Allgemeine_Funktionalitaet.Uebersetzungsanzeige.Blau"></a>

![Image: change display for translation-relevant texts: blue](images/fte_allgemein_aenderungsanzeige_uebtexte_blau.png)

**Figure 344. Change Display for Translation-Relevant Texts: Blue**

If translation-relevant texts were changed or added in the function test editor after opening, then change status will be displayed as a red icon in the tool bar.

<a id="figure.Funktionstesteditor.Allgemeine_Funktionalitaet.Uebersetzungsanzeige.Rot"></a>

![Image: change display for translation-relevant texts: red](images/fte_allgemein_aenderungsanzeige_uebtexte_rot.png)

**Figure 345. Change Display for Translation-Relevant Texts: Red**

No functions can be triggered using the button for the change display of translatable texts. It is only for visualizing the combined change status.

If the function test is closed and then opened again in the function test editor, then the change display will be reset or it will no longer be red, and it will show that no texts were changed after opening. The button is blue initially if there was a translation-relevant change in the version cycle. Otherwise, it will be gray.

###### <a id="d4e15418"></a>7.14.3.15.1. Effect on Translation

The change display does not affect the translation logic. It only applies to content changes to texts within the function test. The translation logic is based on comparisons of text content with previous versions, regardless of the change display. Additional translations may also be needed due to translation-relevant triggers ("Reuse function test", "Add a new language to a market", or "Add a new market in the equipment network"). The latter do not have any effect on the change display.

###### <a id="d4e15421"></a>7.14.3.15.2. Recognizing Translation-Relevant Text Changes

The function test editor has optimized recognition of translation-relevant text changes. There is a "Touched" flag in order to recognize changes in the text control elements and to reduce text changes. Retroactive change recognition also performs a comparison of the content of texts for a command.

Texts that only contain text that is not translation-relevant are considered. If these are changed, there is no effect on the change display. A text that only contains content that is not relevant for translation may only consist of any number of the following elements:

- Tabs
- Default Texts
- Texts from the text library
- System texts
- Set characters
- Spaces
- Variables (such as %str\_component)
- Keywords (such as $str\_PW)
- Special characters (such as ellipsis, attention, information, warning)
- Line Breaks
- Formatting with content that is not translation-relevant
- Tables with content that is not translation-relevant
- Vehicle status texts
- ANSI special characters (information, note, warning, attention, caution) with content that is not translation-relevant

###### <a id="d4e15455"></a>7.14.3.15.3. Overview of Translation-Relevant Change Operations

The following table provides an overview for the authors of which change operations can be expected to be relevant for translation.

<a id="d4e15458"></a>

<table border="1" summary="List of Translation-Relevant Change Operations"><colgroup><col align="left"/><col align="left"/></colgroup><thead><tr bgcolor="#EEEEEE"><th align="left">Change operations</th><th align="left">Relevance for translation</th></tr></thead><tbody><tr><td align="left">Adding new nodes (commands)</td><td align="left">-</td></tr><tr><td align="left">Adding new nodes (steps)</td><td align="left">Yes, if translatable text was edited or changed.</td></tr><tr><td align="left">Editing nodes</td><td align="left">Yes, if translatable text was edited or changed.</td></tr><tr><td align="left">Editing nodes (steps)</td><td align="left">Yes, if translatable text was edited or changed.</td></tr><tr><td align="left">Copying nodes</td><td align="left">-</td></tr><tr><td align="left">Cutting nodes</td><td align="left">No, text change marking is not reset</td></tr><tr><td align="left">Inserting nodes</td><td align="left">Yes, if nodes with translation-relevant content were inserted from other function tests.</td></tr><tr><td align="left">Deleting nodes</td><td align="left">No, text change marking is not reset</td></tr><tr><td align="left">Moving nodes</td><td align="left">Yes, if nodes with translation-relevant content were inserted from other function tests.</td></tr><tr><td align="left">Editing test module settings (steps)</td><td align="left">Yes, if translatable text was edited or changed.</td></tr><tr><td align="left">Editing post-run</td><td align="left">Yes, if translatable text was edited or changed.</td></tr><tr><td align="left">Editing output step</td><td align="left">-</td></tr><tr><td align="left">Setting output step</td><td align="left">-</td></tr><tr><td align="left">Changing step type</td><td align="left">-</td></tr><tr><td align="left">Adding default case in switch</td><td align="left">-</td></tr><tr><td align="left">Executing Ecukom QuickFix</td><td align="left">-</td></tr><tr><td align="left">Merging declares</td><td align="left">Yes, if nodes with translation-relevant content from other function tests were merged.</td></tr><tr><td align="left">New keywords using keyword button</td><td align="left">Yes, if translatable text is contained.</td></tr><tr><td align="left">New variables using variable button</td><td align="left">Yes, if translatable text is contained.</td></tr></tbody></table>

**Table 69. List of Translation-Relevant Change Operations**

  

Change recognition for translation-relevant texts is done by default with all change operations. A change to language-dependent content is triggered as follows, among other ways:

- Confirm the dialog with the language-dependent content
- Create a command that contains a language-dependent section
- Insert a command that was copied from other function test editor

Changes made to language-dependent content using the undo/redo function are considered.

##### <a id="Funktionstesteditor.Allgemeine_Funktionalitaet.Textneutralit%C3%A4t_pr%C3%BCfen"></a>7.14.3.16. Check text neutrality

This function can be used to check the function test editor at any time to see which action elements contain texts relevant to translation. The user does not necessarily have to save their changes separately via the function [Section 7.14.3.2, “Save”](7-14-3-use-cases.md#Funktionstesteditor.Allgemeine_Funktionalitaet.Speichern "7.14.3.2. Save"). The function detects the user changes and saves them automatically. It then checks nodes for translation-relevant texts. The check always applies to the currently active function test and can be performed via the menu bar, ![](images/textneutralitaet_schwarz.png)using the key combination **Ctrl+N**, in the selection menu **Extras >> Check text neutrality** or by calling it up via the context menu.

The status of the text neutrality check is displayed in three stages as follows:

- Black(![](images/textneutralitaet_schwarz.png)): Indicates that text neutrality has not yet been calculated.
- Red(![](images/textneutralitaet_rot.png)): Indicates that translation-relevant texts are available in the function test
- Green(![](images/textneutralitaet_gruen.png)): Indicates that translation-relevant texts are not available in the function test

In the user settings in the “Function test editor” area, you can specify whether the **text neutrality** function should be executed when the test sequence of the function test is opened (see [Figure 346, “Change Display for Translation-Relevant Texts: Red”](7-14-3-use-cases.md#figure.Funktionstesteditor.Allgemeine_Funktionalitaet.Textneutralit%C3%A4t_pr%C3%BCfen "Figure 346. Change Display for Translation-Relevant Texts: Red")). The **Execute text neutrality** checkbox is deactivated by default, which means that the function is not executed.

When the function test editor is opened, the status is loaded from the database and displayed in the properties window of the editor.

- Not calculated: If the checkbox is deactivated, the text neutrality icon is displayed in black after the test sequence is opened. If the “**Execute text neutrality**” checkbox is activated, the text neutrality check will be performed. The “Text neutrality” tab will open and the symbol will be displayed in either red or green, depending on the test result.
- Yes: The function test is text-neutral and the icon is displayed in green after the test sequence is opened. The Text neutrality tab is only displayed if the checkbox is activated.
- No: The function test is not text-neutral and the icon is displayed in red after the test sequence is opened. The Text neutrality tab is only displayed if the checkbox is activated.

<a id="figure.Funktionstesteditor.Allgemeine_Funktionalitaet.Textneutralit%C3%A4t_pr%C3%BCfen"></a>

![Image: change display for translation-relevant texts: red](images/fte_benutzereinstellungen_textneutraltaet.png)

**Figure 346. Change Display for Translation-Relevant Texts: Red**

The action elements that are not text-neutral in terms of content are displayed in the text neutrality view in the order in which they are used [Section 7.14.27, “Text Neutrality (View)”](7-14-27-text-neutrality-view.md "7.14.27. Text Neutrality (View)").

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-14-2-menus-and-tool-bars.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="7-14-function-test-editor.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="7-14-4-drag-and-drop.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">7.14.2. Menus and Tool Bars </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 7.14.4. Drag and Drop</td></tr></table>
