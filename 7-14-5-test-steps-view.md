[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md) > [7.14. Function Test Editor](7-14-function-test-editor.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.14.5. Test Steps (View)</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-14-4-drag-and-drop.md">Prev</a> </td><th align="center" width="60%">7.14. Function Test Editor</th><td align="right" width="20%"> <a accesskey="n" href="7-14-6-using-variables.md">Next</a></td></tr></table>

---

#### <a id="Funktionstesteditor.Testschritte_View"></a>7.14.5. Test Steps (View)

The basic structure for a test module consists of:

- **Global Start** and
- **Global End**
- Between the two elements **Global Start** and **Global End**, you can add "Step", "Select", and "Sub-program" test steps.
- You can add a test step interruption after the **Global End** element. This test step is only executed in the operating system if the operating system executes the "Cancel test" function.

A test module can consist of any number of test steps. You can detail a test step in the desktop with any number of commands. Generally, there are 3 to 10 commands per test step.

##### <a id="Funktionstesteditor.Testschritte_View.Spezielle_Testschritte"></a>7.14.5.1. Test Steps and Sub-Programs

###### <a id="Funktionstesteditor.Testschritte_View.Spezielle_Testschritte.Global_Start"></a>7.14.5.1.1. Global Start Test Step

This test step contains the global command part 1 for specification of variables ("Declare") and keywords ("Definition") and is always run by the program. Other global commands can be defined here, such as a document command.

The command part 1 runs at the start of the test module before the manually created test steps. Its commands apply initially for all test steps that follow. However, you can override individual test steps using local commands.

Double-clicking on a test step opens the test module settings dialog. See [Figure 348, “Test Module Settings”](7-14-5-test-steps-view.md#figure.Funktionstesteditor.Testschritte_View.Spezielle_Testschritte.Global_Start "Figure 348. Test Module Settings").

The dialog contains three tabs:

- Function test: this tab has an input field that can be used to change the title of the function test, and the test ID is displayed.
- Tester description: here you can add information about the function test in formatted text that will display on the tester.
- Engineering description: for comments from the authors that are not displayed on the tester.

<a id="figure.Funktionstesteditor.Testschritte_View.Spezielle_Testschritte.Global_Start"></a>

![Image: test module settings](images/fte_Global_Start.png)

**Figure 348. Test Module Settings**

###### <a id="Funktionstesteditor.Testschritte_View.Spezielle_Testschritte.Global_End"></a>7.14.5.1.2. Global End Test Step

This test step represents the "Static suspicion list" and "OK" list status indicators that are returned after the program on the tester operating system ends.

When you double-click on the test step, the dialog explained below appears. See [Figure 349, “End Dialog Test Module”](7-14-5-test-steps-view.md#figure.Funktionstesteditor.Testschritte_View.Spezielle_Testschritte.Global_End "Figure 349. End Dialog Test Module").

Diagnostic objects that have been added are displayed here in a list. Use the button labeled "..." (available at the end of each line in the table) if you have defined diagnostic objects as variables.

This makes it possible to run so-called "rough tests" whose results are instant but not 100% informative. If no fault was found in the vehicle by the end of the diagnostic session, the search can continue in any child nodes that may be present. This saves the technician from having to go through all tests systemically if the probability of a fault in a particular location is relatively low.

**Suspicion list**

Static suspicion list: if you enter an object here, it will always be entered in the test plan regardless of the test sequence (statically). The suspicion list is also available in the "Set status" command. Because this action element can be located at any place in the function test, meaning after an If command, this is referred to as a "dynamic suspicion list".

**OK list**

Static OK list: if you enter an object here, the object status will always be "OK" regardless of the function test sequence (static). Diagnostic objects that indicate suspicion relations cannot be set to "OK" with this function. Therefore, this function is only suitable for objects in the equipment network. The OK list is also available in the "Set status" command. This allows a more flexible usage at each location in the function test and is called a "dynamic OK list".

<a id="figure.Funktionstesteditor.Testschritte_View.Spezielle_Testschritte.Global_End"></a>

![Image: end dialog test module](images/fte_Global_End.png)

**Figure 349. End Dialog Test Module**

  

Elements can be added, removed, or moved using the plus/minus/arrow buttons. See [Figure 350, “Controls Settings”](7-14-5-test-steps-view.md#figure.Funktionstesteditor.Testschritte_View.Spezielle_Testschritte.Steuerfelder "Figure 350. Controls Settings").

<a id="figure.Funktionstesteditor.Testschritte_View.Spezielle_Testschritte.Steuerfelder"></a>

![Image: controls settings](images/fte_pmpf.png)

**Figure 350. Controls Settings**

##### <a id="Funktionstesteditor.Testschritte_View.Testschritte_Titelzeile"></a>7.14.5.2. Test Step View

The test step view is displayed on the left side by default. The buttons for adding new test steps and sub-programs are located above the test step view. There is a separating line between the test step view and the command page that can be moved horizontally using the mouse. The following [Figure 351, “Test Step View in Function Test Editor”](7-14-5-test-steps-view.md#figure.Funktionstesteditor.Testschritte_View.Testschritte_Ansicht_Integriert "Figure 351. Test Step View in Function Test Editor") shows an example for the resulting function test editor with arranged views.

<a id="figure.Funktionstesteditor.Testschritte_View.Testschritte_Ansicht_Integriert"></a>

![Image: test step view in function test editor](images/fte_testschritte_testschrittanzeige_integriert.png)

**Figure 351. Test Step View in Function Test Editor**

The following [Figure 352, “Side-By-Side Function Tests”](7-14-5-test-steps-view.md#figure.Funktionstesteditor.Testschritte_View.Testschritte_Ansicht_Nebeneinander "Figure 352. Side-By-Side Function Tests") shows an example of two function tests open at the same time with their test step views.

<a id="figure.Funktionstesteditor.Testschritte_View.Testschritte_Ansicht_Nebeneinander"></a>

![Image: side-by-side function tests](images/fte_testschritte_testschrittanzeige_nebeneinander.png)

**Figure 352. Side-By-Side Function Tests**

Some functions depend on the area that is currently active, either test step view or editor. For example, the editing functions are based on the element currently selected in the active area. The test step view gives a response about the graphic view where the user is currently located. The background color of the button tool bar changes depending on the selected area (see [Figure 353, “Test Step View Focus Change”](7-14-5-test-steps-view.md#figure.Funktionstesteditor.Testschritte_View.Testschritte_Ansicht_Fokuswechsel "Figure 353. Test Step View Focus Change")).

<a id="figure.Funktionstesteditor.Testschritte_View.Testschritte_Ansicht_Fokuswechsel"></a>

![Image: test step focus change](images/fte_testschritte_testschrittanzeige_fokuswechsel.png)

**Figure 353. Test Step View Focus Change**

In addition to clicking on the test step view with the mouse, the user can change the focus to the test step area by clicking on an empty area of the button toolbar.

##### <a id="Funktionstesteditor.Testschritte_View.Testschritte_Erzeugen"></a>7.14.5.3. Adding Test Steps, Selections, Sub-programs and Sub-program Selections

Test steps/selections or sub-program/function alls can be created in the left working window using the "Test step", "Test selection", "Sub-program" and "Sub-program selection" functions. See [Figure 354, “Creating Test Steps”](7-14-5-test-steps-view.md#figure.Funktionstesteditor.Testschritte_View.Testschritte_Erzeugen.Steuerfelder "Figure 354. Creating Test Steps").

- "Test step" generates an element with two outputs (OK/NOT OK). Commands for self-contained procedures can be compiled in them. The connections between them organize the test steps into a functional context.
- "Test selection" generates an element with any number of outputs (multiple branches). The connections between them organize the test steps into a functional context.
- "Sub-program" generates an element with two outputs (OK/NOT OK) that calls up a sub-program or another function test. See also [Section 7.14.5.3.1, “Sub-Program”](7-14-5-test-steps-view.md#Funktionstesteditor.Testschritte_View.Testschritte_Erzeugen.Aufruf "7.14.5.3.1. Sub-Program").
- "Sub-program selection" generates an element with any number of outputs (multiple branches) that calls up a sub-program or another function test. See also [Section 7.14.5.3.1, “Sub-Program”](7-14-5-test-steps-view.md#Funktionstesteditor.Testschritte_View.Testschritte_Erzeugen.Aufruf "7.14.5.3.1. Sub-Program").

The individual elements can be added using the buttons in the upper area of the views, the context menu, or the **Add** menu item.

<a id="figure.Funktionstesteditor.Testschritte_View.Testschritte_Erzeugen.Steuerfelder"></a>

![Image: buttons for creating test step elements](images/fte_Testschritte_Steuerfelder.png)

**Figure 354. Creating Test Steps**

Click one of the buttons. The mouse cursor changes to an arrow that is pointing up (the sensitive area is at the point of the arrow).

Place the mouse cursor in the test steps view and click the left mouse button. The new test step is added.

When a new test step is added, you will see the **Edit test steps** dialog. See [Figure 355, “Edit Test Step”](7-14-5-test-steps-view.md#figure.Funktionstesteditor.Testschritte_View.Testschritte_Erzeugen "Figure 355. Edit Test Step"). The test step title field is a mandatory field. Variables and keywords can also be used in the title.

Enter an informative title that is up to 50 characters long for the test step here. The function test is displayed in the information window on the test with each command.

The decision between an OK/NOT OK test step and a SELEKT can be revised again in this dialog.

<a id="figure.Funktionstesteditor.Testschritte_View.Testschritte_Erzeugen"></a>

![Image: edit test step](images/fte_Testschritt_Bearbeiten.png)

**Figure 355. Edit Test Step**

A test step with multiple branches (SELECT) can have an unlimited number of outputs, as described previously. The outputs can be specified in the test step itself using the **Set status** or **Query** commands. This specification always applies only to the current test step, but it can also be evaluated using the "While", "If" or "Switch/Case" control structures.

###### <a id="Funktionstesteditor.Testschritte_View.Testschritte_Erzeugen.Aufruf"></a>7.14.5.3.1. Sub-Program

The "sub-program" button represents a test step from which you can call up a sub-program ("general" type) or another function test ("function test" type). The nesting depth is theoretically unlimited, meaning it is only limited by the natural limits of the programming language that is used. The "sub-program" test step has the logical outputs OK and NOT OK. "Sub-program selection" has multiple branches (SELECT) and has an unlimited number of outputs.

If the sub-program has transfer parameters, then the transfer values (values of variables, keywords, arrays, or literal) can be transferred using the Interface variables and Interface keywords tables, as well as have returns on variables in the main program assigned. The selection options depend on the transfer type for the sub-program variables / the sub-program keyword.

The [Figure 356, “Edit Sub-Program”](7-14-5-test-steps-view.md#figure.Funktionstesteditor.Testschritte_View.Testschritte_Unterprogramm "Figure 356. Edit Sub-Program") shows the example of a sub-program with interface variables and interface keywords. The individual entires can be sorted using the table header and the context menu.

<a id="figure.Funktionstesteditor.Testschritte_View.Testschritte_Unterprogramm"></a>

![Image: edit sub-program](images/fte_Unterprogramm_Bearbeiten.png)

**Figure 356. Edit Sub-Program**

If a sub-program is added, a special dialog opens. Compare to [Figure 535, “Sub-Program Action Element”](7-14-20-category-miscellaneous.md#figure.Funktionstesteditor.Testschritte_View.Testschritte_Erzeugen.Aufruf2 "Figure 535. Sub-Program Action Element").

**Sub-Program**

Enter the name for the program to be called up here, or select it using access to the function test management ("Selection" button) If you click the "Edit" button, you can display the sub-program entered in a second function test editor and edit it if necessary.

Not every type of function code can be used in every function code. The following table shows which function codes can be selected on the test step side for a sub-program.

<a id="d4e15837"></a>

<table border="1" summary="Sub-Program Calls in Function Codes"><colgroup><col align="left"/><col align="left"/></colgroup><thead><tr bgcolor="#EEEEEE"><th align="left">Source</th><th align="left">Objective</th></tr></thead><tbody><tr><td align="left">Function test</td><td align="left">Function test, general test</td></tr><tr><td align="left">Traversal test</td><td align="left">General test</td></tr><tr><td align="left">General test</td><td align="left">Function test, general test</td></tr></tbody></table>

**Table 72. Sub-Program Calls in Function Codes**

When using an incorrect function test, a fatal error will be displayed in the problems view. It is then not possible to close the sub-program dialog or save the function code.

**Interface variables**

The contents of the global variables listed here is adopted and returned by the sub-program if the content is declared correctly there.

- "Main program" column: specification of a variable from the main program. A new variable can also be created in the main program using the field. It is also possible to specify direct TextIDs for variables with “Transfer” call-up type.
- "Sub-program" column: contains the variable from the sub-program with specification of the data type of the variable.
- "Sub-program preconfiguration": if the variable from the sub-program has a preconfiguration, it will be displayed here.
- "Sub-program comments" column: if the variable in the sub-program has comments, they will be displayed here.

**Interface keywords**

The contents of the global keywords listed here is adopted by the sub-program if the content is declared correctly there.

- "Main program" column: specification of a keyword from the main program. A new keyword can also be created in the main program using the field. It is also possible to specify a TextID directly.
- "Sub-program" column: contains the keyword from the sub-program with specification of the data type of the keyword.
- "Sub-program preconfiguration": if the keyword from the sub-program has a preconfiguration, it will be displayed here.
- "Sub-program comments" column: if the keyword in the sub-program has comments, they will be displayed here.

**OK**

Use this button to transfer the input into the command and close the dialog.

**Cancel**

Use this button to close the diesel without transferring the input into the command.

**Sub-program on the command page**

A sub-program (including sub-program selection) in the test step view is also displayed on the command page (see [Section 7.14.20.4, “Action Element - Sub-Program”](7-14-20-category-miscellaneous.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Sonstige.Aufruf_Testprozedur "7.14.20.4. Action Element - Sub-Program")). A start node (round circle) in the sequence display indicates the location of the sub-program integrated between the processes for test step, pre-run, post-run and other sub-programs. The circle symbol is overwritten with the system name (without location code) and contains no functions to be expanded or collapsed. The [Figure 357, “Sub-program on the command page”](7-14-5-test-steps-view.md#Funktionstesteditor.Testschritte_View.Testschritte_Erzeugen.UP-Anweisungsseite "Figure 357. Sub-program on the command page") shows the sub-program display on the command page.

<a id="Funktionstesteditor.Testschritte_View.Testschritte_Erzeugen.UP-Anweisungsseite"></a>

![Image: sub-program](images/fte_Unterprogramm_Anweisungsseite.png)

**Figure 357. Sub-program on the command page**

The symbol serves exclusively as the display. It has the following properties:

- If you click on the node, the sub-program will be selected in the test step view.
- A tool tip with the sub-program properties is displayed above the node.

The printout and SVG export for the function test also contain this symbol with the symbol title.

###### <a id="d4e15907"></a>7.14.5.3.1.1. Adding and Modifying Sub-Program Calls Using Drag and Drop

In the test step view, existing sub-program calls can be modified or replaced by dragging and dropping the function tests or general tests to the sub-program call. To do this, select an object from the navigation tree function library and drag and drop it to the sub-program that you wish to modify. The sub-program dialog is opened automatically. The existing interface table is compared and updated with the new interface table:

- Identical variables/key words will remail as they were.
- Old variables/key words that are not in the new sub-program will be deleted.
- New variables/key words that are not in the old sub-program are added.

The type of sub-program call is retained (IO/NIO or Select)

By dragging and dropping the function tests or general tests to a test step connection, the sub-program call is inserted below the test step connection source and the output of the newly inserted sub-program is set to “Next”. In this case, the sub-program dialog is also opened automatically.

Drag and drop is not possible if a sub-program editor is already open.

##### <a id="Funktionstesteditor.Testschritte_View.AbbruchTestschritt_erstellen"></a>7.14.5.4. Adding a Test Step Interruption

A special test step is added in the left working window using the "Test Step Interruption" function. You can use this test step to create a secure status, for example, if the "Cancel test" function is activated in the operating system. This may make sense if there is a basic setting running or during an actuator test, for example.

**Warning: if the "Cancel' test" function is activated in the operating system, it will not jump to Global 2.**

The [Figure 358, “Cancel Test Step”](7-14-5-test-steps-view.md#figure.Funktionstesteditor.Testschritte_View.Testschritte_Erzeugen.AbbruchTS "Figure 358. Cancel Test Step") shows the cancel test step in the test step view.

<a id="figure.Funktionstesteditor.Testschritte_View.Testschritte_Erzeugen.AbbruchTS"></a>

![Image: cancel test step](images/fte_Testschritte_abbruchtestschritt.png)

**Figure 358. Cancel Test Step**

The cancel test step can be added using the buttons in the upper area of the views, the context menu, or the **Add** menu item. The location where the cancel test step is added cannot be selected using the mouse, as with other commands. The cancel test step is always added below "Global 2".

<a id="figure.Funktionstesteditor.Testschritte_View.Testschritte_Erzeugen.SteuerfelderAbbruchTS"></a>

![Image: button for creating a cancel test step](images/fte_Testschritte_Steuerfelder.AbbruchTS.png)

**Figure 359. Creating a Cancel Test Step**

A function test can only have one cancel test step. The function test editor ensures this. The cancel test step is located below Global 2 and can neither be moved to another location in the function test nor be linked with a connection.

The cancel test step can be edited using the "Cut", "Add", "Copy" and "Delete" functions. For details on pasting from the clipboard, see [Section 7.14.5.4.1, “Adding from the Clipboard”](7-14-5-test-steps-view.md#Funktionstesteditor.Testschritte_View.Testschritte_Erzeugen.BearbeitenAbbruchTS "7.14.5.4.1. Adding from the Clipboard").

The cancel test step can contain all commands that can also be used within test step and selections. The cancel test step does not have any other parameters and no dialog screen.

The cancel test step always initially has the test step status OK and selection: -1 for runtime. Changes to the test step status do not affect the surrounding function test. In contrast to Global 2 (post-run), the status of the function test remains unchanged.

###### <a id="Funktionstesteditor.Testschritte_View.Testschritte_Erzeugen.BearbeitenAbbruchTS"></a>7.14.5.4.1. Adding from the Clipboard

Test steps can be added mainly from the clipboard. The function test editor ensures that only one cancel test step is present in each function test. There is a differentiation between a single cancel test step and a multiple selection with cancel test step in the clipboard.

**Exclusive adding**

The function for adding from the clipboard is inactive if there is already a cancel test step in the function test. Otherwise, the function is active. In this case, the add function can be used with any element in the test step view. The cancel test step is always added after Global 2.

**Adding from a multiple selection**

If the content of the clipboard is a mixture of elements from the test step view and a cancel test step, then it may not be possible to add all of the elements. The following information is shown to the user.

<a id="figure.Funktionstesteditor.Testschritte_View.Testschritte_Erzeugen.AbbruchTSeinfuegen"></a>

![Image: cancel test cannot be added](images/fte_Testschritte_AbbruchTS_meldungbereitsvorhanden.png)

**Figure 360. Cancel Test Cannot Be Added**

In this case, the entire content of the clipboard is added except the cancel test step.

##### <a id="Funktionstesteditor.Testschritte_View.Verbindungen_herstellen"></a>7.14.5.5. Establishing Connections

Test step connections are created by selecting a selection in a test step and dragging it to another test step while holding the mouse button.

The behavior of test steps with two outputs (OK/NOT OKAY) takes place accordingly.

**Detailed description:**

The connection is always drawn from an output to an input. The drawing of connections is always the same in principle.

1. Click on the OK or NOT OK field for the test step from where the connection should begin (output). The activated test step is highlight and its output filed is marked in blue.
2. Open the "Connection" function using the context menu. Move the mouse to the target test step. Once you move the cursor onto the upper part of a test step, its input field will be highlighted in blue. The blue connection between both test steps is displayed dynamically. The cursor displays the add symbol while this is happening.
3. When the desired connection is displayed, click on the left mouse button to create the connection statically. The cursor returns to its normal form.

**Note**

If there is already a connection to an output, it will be replaced with the new connection that was drawn.

##### <a id="Funktionstesteditor.Testschritte_View.Verbindungen_aufloesen"></a>7.14.5.6. Deleting Connections

A connection is deleted by selecting the arrow that is display and then clicking the delete button or using the context menu. The selection from which the connection begins is set to BREAK.

Or, each selection can be set to NEXT, BREAK, or STEP using the context menu, which also serves to remove the connection. See [Figure 361, “Context Menu - Deleting Connections”](7-14-5-test-steps-view.md#figure.Funktionstesteditor.Testschritte_View.Verbindungen_aufloesen "Figure 361. Context Menu - Deleting Connections").

The behavior of test steps with two outputs (OK/NOT OKAY) takes place accordingly.

<a id="figure.Funktionstesteditor.Testschritte_View.Verbindungen_aufloesen"></a>

![Image: context menu - deleting connections](images/fte_Kontext_Verbindung_Loesen.png)

**Figure 361. Context Menu - Deleting Connections**

##### <a id="Funktionstesteditor.Testschritte_View.Testschritttyp_aendern"></a>7.14.5.7. Changing Test Step Type

The type of the test step can be changed between test selection and test step using the context menu or the menu bar.

##### <a id="Funktionstesteditor.Testschritte_View.VerbundenerTestschritt"></a>7.14.5.8. Connected Test Step

If there is a connection selected between test steps, the action "Connected test step" can be activated. The action is located in the menu bar (edit) and in the context menu for connections. The target test step for the selected connection is marked.

##### <a id="Funktionstesteditor.Testschritte_View.UnterprogrammOeffnen"></a>7.14.5.9. Opening a Sub-Program

The function can be triggered using the context menu and the global menu. It is visible or active when an individual sub-program command is selected. The function is available for sub-program commands on both the test step page as well as the command page. It is opened without checking out and the function test editor tab of the sub-program is automatically activated and brought to the front. The main program remains open.

<a id="figure.Funktionstesteditor.Testschritte_View.UnterprogrammOeffnen"></a>

![Image: context menu - opening a sub-program](images/fte_Testschritte_UPOeffnen.png)

**Figure 362. Context Menu - Opening a Sub-Program**

##### <a id="Funktionstesteditor.Testschritte_View.Testschritte_selektieren"></a>7.14.5.10. Selecting Test Steps

Test steps can be selected by clicking in the title area but not by selecting the area.

If a test step is selected, the window will move to the beginning of the test step.

##### <a id="Funktionstesteditor.Testschritte_View.Testschritte_loeschen"></a>7.14.5.11. Deleting Test Steps

Test steps can be selected by clicking in the title area but not by selecting the area.

The deleting can be done using the menu bar, the delete button, or the context menu.

##### <a id="Funktionstesteditor.Testschritte_View.Testschritte_Kopieren"></a>7.14.5.12. Copying Test Steps

Test steps can be selected by clicking in the title area but not by selecting the area.

The copying is done using the menu bar, the keyboard shortcut CTRL+C, the context menu, or by dragging and dropping.

When dragging and dropping, the selected element is moved into the area between two test step while the mouse button is pressed and held.

##### <a id="Funktionstesteditor.Testschritte_View.Testschritte_Ausschneiden"></a>7.14.5.13. Cutting Test Steps

Test steps can be selected by clicking in the title area but not by selecting the area.

The cutting is done using the menu bar, the keyboard shortcut CTRL + X, or the context menu.

##### <a id="Funktionstesteditor.Testschritte_View.Testschritte_Einfuegen"></a>7.14.5.14. Adding Test Steps

To add test steps, the arrow between the two test steps must be selected. This is indicated by a thicker line.

The adding is done using the menu bar, the keyboard shortcut CTRL + V, or the context menu.

##### <a id="Funktionstesteditor.Testschritte_View.Bearbeitungshistorie"></a>7.14.5.15. Undoing/Repeating Test Steps

In the test step graphic display, user actions can be undone or repeated by right-clicking the mouse on a context menu.

The keyboard shortcuts CTRL+Z, CTRL+Y, and the corresponding functions in the menu bar and the buttons can also be used. See [Figure 363, “Editing History”](7-14-5-test-steps-view.md#figure.Funktionstesteditor.Testschritte_View.Bearbeitungshistorie "Figure 363. Editing History").

<a id="figure.Funktionstesteditor.Testschritte_View.Bearbeitungshistorie"></a>

![Image: undo/repeat editing history](images/fte_Bearbeitungshistorie.png)

**Figure 363. Editing History**

##### <a id="Funktionstesteditor.Allgemeine_Funktionalitaet.Testschrittfilter"></a>7.14.5.16. Test Step Filter

In larger function tests, similar test step content may occur in multiple test steps. For this reason, there is a "test step" display that filters the function test to the selected test step. Only test step content for the selected test step is shown. The filter can be adjusted so that you can switch between the complete view or the filtered view.

The buttons for activating/deactivating the test step filter are available in the toolbar (see [Figure 364, “Test Step Filter in the Toolbar”](7-14-5-test-steps-view.md#figure.Funktionstesteditor.Testschritte_View.Testschrittfilter.Toolleiste "Figure 364. Test Step Filter in the Toolbar")). The menu under view also has a "Test step filter" menu item (see [Figure 365, “Test Step Filter in the Menu”](7-14-5-test-steps-view.md#figure.Funktionstesteditor.Testschritte_View.Testschrittfilter.Menu "Figure 365. Test Step Filter in the Menu")).

<a id="figure.Funktionstesteditor.Testschritte_View.Testschrittfilter.Toolleiste"></a>

![Image: test step filter in the toolbar](images/fte_testschritte_testschrittfilter_toolleiste.png)

**Figure 364. Test Step Filter in the Toolbar**

<a id="figure.Funktionstesteditor.Testschritte_View.Testschrittfilter.Menu"></a>

![Image: test step filter in the menu](images/fte_testschritte_testschrittfilter_menu.png)

**Figure 365. Test Step Filter in the Menu**

Depending on the test step filter selection, either all function test commands are displayed in the editor or only the commands for the selected test step. Both versions can be seen in [Figure 366, “Test Step Filter Deactivated”](7-14-5-test-steps-view.md#figure.Funktionstesteditor.Testschritte_View.Testschrittfilter.Anzeige.deaktiv "Figure 366. Test Step Filter Deactivated") and [Figure 367, “Test Step Filter Activated”](7-14-5-test-steps-view.md#figure.Funktionstesteditor.Testschritte_View.Testschrittfilter.Anzeige.aktiv "Figure 367. Test Step Filter Activated").

<a id="figure.Funktionstesteditor.Testschritte_View.Testschrittfilter.Anzeige.deaktiv"></a>

![Image: test step filter deactivated](images/fte_testschritte_testschrittfilter_anzeige_deaktiv.png)

**Figure 366. Test Step Filter Deactivated**

<a id="figure.Funktionstesteditor.Testschritte_View.Testschrittfilter.Anzeige.aktiv"></a>

![Image: test step filter activated](images/fte_testschritte_testschrittfilter_anzeige_aktiv.png)

**Figure 367. Test Step Filter Activated**

The test step filter is a filter for the function test editor command page. The filter is always used when a node is selected in the test step view. When the test step filter is activated, the function test editor shows the following properties:

- Initially after opening the function test, all commands are displayed on the function test editor command page.
- When multiple test steps are selected, only the content of the first test step marked is displayed.
- If a previously selected test step has been erased, then all commands are shown on the function test command page.
- For display-specific functions (print, SVG export), only the visible nodes are printed or exported. Structure nodes hidden on the command page remain hidden. To print or export everything, the test step filter must be deactivated first.
- The command can also switch automatically between the test steps (for example, when selecting problem navigation, search object navigation, debugging). In these cases, the command page is also filtered when the test step filter is active.
- Clicking on the empty area in the test step view resets the selection. All commands are shown again.

The setting for the "test step filter" is stored locally for the Windows user that is currently logged into the workspace, and it will be restored the next time ODIS Creator starts. The initial default setting for the test step filter is deactivated.

When the test step filter is activated using the menu or the toolbar, the test step filter is applied to all open function tests. If a test step is selected, it will be used to filter the command page. If multiple test steps are selected, only the first will be used for filtering. When the test step filter is deactivated, the hidden steps in all open function tests are made visible again on the command page.

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-14-4-drag-and-drop.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="7-14-function-test-editor.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="7-14-6-using-variables.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">7.14.4. Drag and Drop </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 7.14.6. Using Variables</td></tr></table>
