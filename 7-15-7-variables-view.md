[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md) > [7.15. Debugger (Integrated Operating System)](7-15-debugger-integrated-operating-system.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.15.7. Variables View</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-15-6-break-points-view.md">Prev</a> </td><th align="center" width="60%">7.15. Debugger (Integrated Operating System)</th><td align="right" width="20%"> <a accesskey="n" href="7-15-8-brand-variables-view.md">Next</a></td></tr></table>

---

#### <a id="Funktionstesteditor.Debugger.Variablen_View"></a>7.15.7. Variables View

The variables view (see [Figure 566, “Variables View”](7-15-7-variables-view.md#figure.Funktionstesteditor.Debugger.Variablen_View "Figure 566. Variables View")) shows all variables that are currently entered. If a filter is entered, only a portion of the variables is shown. The following information is shown in the columns for each variable:

1. Name: name of the variables, with index for array variables if necessary (for information only)
2. Value: current value of the variables. The display is red if the value was changed since the last update. The display is blue if the value was a new value added since the last update. For variables that are not set to "const", you can enter a new value here. The value is transferred into the variable as soon as you exit the field.
3. Type: value type for the variables (for information only)
4. Focus: you can change the "monitor" status of the variables interactively in order to monitor specific variables. For arrays, this column is used to specify the number of array variables to be displayed. ("Monitor" cannot be set for an entire array, only for individual variables.)
5. Environment: exact specification about the visibility, in which the variable is defined. The visibility is a list of valid entries separated by slashes, with the "innermost" specification (meaning the place where the variable is defined) first. (The innermost BLOCK environment is shown if it does not match a comprehensive LOOP environment ("voltage"), outer BLOCK environments are not shown.)

Double-clicking on one of the lines displayed opens the test module/test step that is referenced in the FTE (a new window opens, if necessary), marks the referenced command there, and moves it into the visible area of the window, if necessary (the block where it is located in collapsed, it will be expanded).

<a id="figure.Funktionstesteditor.Debugger.Variablen_View"></a>

![Image: variables view](images/fte_Variablen_View.png)

**Figure 566. Variables View**

##### <a id="Funktionstesteditor.Debugger.Variablen_View.Darstellungen"></a>7.15.7.1. Displays

The variable view in ODIS Creator shows all visible identifiers (the stack) for an execution point in a function test. The variables view shows the content of the function test that is running. Separate tabs are created in the variable view for each function test, which show the access sequence for each function test performed.

A function test running in the debugger automatically generates a new tab. If a new function test is added, whether by a sub-program request or a function test access by diagnostic entry, a new tab will be added to the right of the existing tabs. If the request sequence is empty and there is no function test running in the debugger, then there is no tab or the variables view is empty.

Mapping between the main and sub-programs is done based on the system name. Separate identification is not done because each main program can also be a sub-program at the same time.

An exception if when a function test is running that was already run through within the debug session, for which there is also a tab with the accessing sequence. The new process does not generate a new tab, but uses the one that is already present. Its content are removed and the name of the current stack is added. The location of the tab remains the same, meaning the tab is not moved to the right.

The variables view can display its content in two different forms.

1. Tabs above one another: in this format, one tab is created for each function test running. New tabs are added at the right of the tab list. The tabs are named according to the system name of the function test (without location code). The tab title display may be shortened based on the length of the system name. A horizontal scrollbar becomes active as the number of tabs increases.

   <a id="figure.Funktionstesteditor.Debugger.Variablen_View.Reiter.Uebereinander"></a>

   ![Image: stacked tabs](images/fte_Debug_VariablenView_Reiter_Uebereinander.png)

   **Figure 567. Stacked Tabs**
2. Side-by-side tabs (default): the tabs are shown next to each other if there is more than one tab. This shows an complete view of the debug session. The width of each tab is scaled automatically. The minimum width is restricted to approximately 380 pixels. If the minimal width of all tabs will not fit in this view, a scrollbar is displayed. The width of the tabs cannot be changed.

   <a id="figure.Funktionstesteditor.Debugger.Variablen_View.Reiter.Nebeneinander"></a>

   ![Image: side-by-side tabs](images/fte_Debug_VariablenView_Reiter_Nebeneinander.png)

   **Figure 568. Side-by-Side Tabs**

   In contrast to the stacked display, the columns of each individual tab are shown in a very compressed display. If a value is too large for a cell, it will be shortened (three dots at the end). The column width is not fixed. It can be modified at any time. Horizontal and vertical scrollbars may be added if necessary based on the restricted space (there are then vertical and horizontal scrollbars within each tab as well as horizontal scrollbars within the view).

The two different display types can be configured. A button in the variables view is used to switch between both display types. The button is right next to the debugger control buttons. The side-by-side view is the default display when opening the variables view (manually or automatically). If the display type is changed, it will remain in use for the tabs until it is manually or automatically closed.

<a id="figure.Funktionstesteditor.Debugger.Variablen_View.Buttons"></a>

![Image: buttons in the variables view](images/fte_Debug_VariablenView_Historie_Buttons.png)

**Figure 569. Buttons in the Variables View**

Each variables view has a button for switching the view that is only valid for the display type in this view. In this way, each variables view can have a different display type. If a variables view is closed and then reopened, the default settings are restored. The button for switching the display types is always active. They can be switched at any time. Note: the view does not contain any data if opened outside of a debug session. In this case, the displays in the empty variables view match the current usage.

All functions listed here are available in all (filtered) variables views. Each variables view has several independent configuration options regarding displays/closing of tabs. The configuration switch is located in the view (toolbar, toolbar menu and context menu).

The focus during each debugging step (with each debug call, meaning before executing each graphic command on the right editor side) is on the tab for the function test that is running in ODIS Debug. In the stacked view, this means: the tab is activated (and moved to the front). In the side-by-side view, the tab will be visible and it may be moved into the visible area to do this. Tabs are focused automatically regardless of whether the variables view is in focus or another view withing the views in the lower right of the function test editor.

##### <a id="Funktionstesteditor.Debugger.Variablen_View.Historie"></a>7.15.7.2. History/Automatic Tab Closing

The variables view saves old variables statuses for function tests. They can be displayed or hidden using the "Do not close tab" function.

1. Close tab (default): with this setting, the tab for a sub-program is closed when you return from the sub-program. Only the tabs for the current function test are shown.

   If a function test has completed its run during a debug session (or if it encounters a runtime error), the associated tab in the variables view will be closed. This happens regardless of the display type in the variables view. The closing applies to all function test tabs that display sub-programs that are run as well as for function tests that are started separately (for example, by diagnostic entry).

   <a id="figure.Funktionstesteditor.Debugger.Variablen_View.Reiter.Schliessen"></a>

   ![Image: close tabs](images/fte_Debug_VariablenView_Reiter_Schliessen.png)

   **Figure 570. Close Tabs**
2. Do not close tabs: the tab for a sub-program remains open after returning from the sub-program. The contents are grayed out and cannot be modified.

   <a id="figure.Funktionstesteditor.Debugger.Variablen_View.Reiter.NichtSchliessen"></a>

   ![Image: do not close tabs](images/fte_Debug_VariablenView_Reiter_NichtSchliessen.png)

   **Figure 571. Do Not Close Tabs**

The name stored in the history is displayed after the debug session ends. If you select "Do not close tabs", the history for the saved names is only displayed for the last function test that ended (main program).

<a id="figure.Funktionstesteditor.Debugger.Variablen_View.Reiter.NachBeenden"></a>

![Image: close tabs after ending debug session](images/fte_Debug_VariablenView_Reiter_NachBeenden.png)

**Figure 572. Close Tabs after Ending Debug Session**

There is a button in the variables view for controlling the closing function. The button offers two options:

1. Close tabs: tabs for function tests that have run are closed automatically
2. Do not close tabs: tabs for function tests that have run remain open

The default setting for the button after opening the view (manually or automatically) is "Close tabs". The button is always active as long as the variables view is visible. Changes take effect from the time the change is made:

- For "Do not close tabs": the tabs are not closed. Tabs that were already closed are not displayed again.
- For "Close tabs": the current tab is closed after running. Existing tabs are not closed.

The configuration switch is located in the variables view (toolbar, toolbar menu and context menu).

##### <a id="Funktionstesteditor.Debugger.Variablen_View.Markierung"></a>7.15.7.3. Marking changes

Identifier values for runtime and default value inputs for variables are changed manually in the variables view. The view assist the author by highlighting variables that have changed in color.

Variables can change for two reasons:

1. Programmatic variable assignment by GFF
2. Manual variable assignment by the editor using the variables view

Both causes result in visual marking of the affected variables lines in the variables view. The entire line (spanning the name, value, type, and environment columns) displays the text in red. The following illustration shows an array that is marked. The value 3.14159265 was assigned to the array field with the index [1.1].

<a id="figure.Funktionstesteditor.Debugger.Variable_View.Aenderungen.Array"></a>

![Image: marking an array field](images/fte_Debug_VariablenView_Aenderungen_Array.png)

**Figure 573. Marking an Array Field**

The following illustration shows the marking of a variable to which the value 1.4142135 was assigned.

<a id="figure.Funktionstesteditor.Debugger.Variable_View.Aenderungen.Variable"></a>

![Image: marking a variable](images/fte_Debug_VariablenView_Aenderungen_Variable.png)

**Figure 574. Marking a Variable**

If new variables are declared or new keywords are defined (new compared to the last command), the entire line will be marked (with blue text).

<a id="figure.Funktionstesteditor.Debugger.Variable_View.Aenderungen.Declarations"></a>

![Image: marking declarations/definitions](images/fte_Debug_VariablenView_Aenderungen_Declarations.png)

**Figure 575. Marking Declarations/Definitions**

Changing a value (programmatically or manually) removes the previous change marking. In this way, only one line at a time can be marked as changed in the variables view (in an array variable, the lines with the array names can also be marked). The text in the variables line is shown in black when the marking is removed.

The value of super-global variables (tester state, select) cannot be changed manually. Marking or unmarking programmatical changes functions the same as described here.

##### <a id="Funktionstesteditor.Debugger.Variablen_View.Feldvariablen"></a>7.15.7.4. Field Variables

For a better overview of array variables with a high number of fields, there is a function where you can restrict the maximum number of fields that are displayed.

<a id="figure.Funktionstesteditor.Debugger.Variable_View.Feldvariablen.Menu"></a>

![Image: "Filter..." selection for filtering variables displays](images/fte_Debug_VariablenView_Feldvariablen_Menu.png)

**Figure 576. "Filter..." Selection for Filtering Variables Displays**

There is a selection (see [Figure 577, “Filter Dialog with Default of Maximum 50 Array Fields Set”](7-15-7-variables-view.md#figure.Funktionstesteditor.Debugger.Variable_View.Feldvariablen.Dialog "Figure 577. Filter Dialog with Default of Maximum 50 Array Fields Set")) added to the variables view for displaying field variables that offers the following options:

1. All: shows all available array variables and array fields
2. None: shows the names of array variables (one line), but array fields are hidden
3. Maximum: allows you to enter a value that will serve as the maximum number of fields to display. Array variables are always displayed. The value you have entered is the maximum limit, meaning no fields with an index above this value are displayed. The default value is 50 array fields. You specify the maximum value in a text field that is only active if this option is selected.

<a id="figure.Funktionstesteditor.Debugger.Variable_View.Feldvariablen.Dialog"></a>

![Image: filter dialog with default of maximum 50 array fields set](images/fte_Debug_VariablenView_Feldvariablen_Dialog.png)

**Figure 577. Filter Dialog with Default of Maximum 50 Array Fields Set**

The option for adjusting the amount displayed is always active when the variables view is active and it remains valid until the view is closed (manually or programmatically). The default setting for the number of fields in option 3.

The variables view is updated immediately after the option is changed. Version 3 uses the default value unless a different value is specified. If the maximum value is entered, the update will occur after leaving the text field or pressing the "Enter" button on the keyboard. Entries in the text field must be whole numbers that are greater than 0. Otherwise, the value will not be transferred and the last valid value in the text field will remain.

<a id="figure.Funktionstesteditor.Debugger.Variable_View.Feldvariablen.FilterAnzahl"></a>

![Image: example of a filter with maximum field number = 3](images/fte_Debug_VariablenView_Feldvariablen_FilterAnzahl.png)

**Figure 578. Example of a Filter with Maximum Field Number = 3**

<a id="figure.Funktionstesteditor.Debugger.Variable_View.Feldvariablen.FilterKeine"></a>

![Image: example of "none" filter](images/fte_Debug_VariablenView_Feldvariablen_FilterKeine.png)

**Figure 579. Example of "None" Filter**

The setting for the maximum field values to display applies to each variables view. All filtered variables views can be configured separately in this way. Resetting the view is classified as closing the variables view.

##### <a id="Funktionstesteditor.Debugger.Variablen_View.VariablenaenderungenProtokollieren"></a>7.15.7.5. Logging Variables Changes

In order for it to be possible to track changes to variables at the time of debugging, there is a "Log variables changes" function that counts the number of variables changes during a debugging procedure in a separate file ("variable.log"). The log file with the entries remains after a debug procedure ends. The log file is only re-initialized (cleared) after restarting the debug procedure.

As long as the debug session is active, the variables changes are logged. If the debugger is ended manually or automatically (for example, by an error), no more variables changes will be logged.

<a id="d4e32102"></a>

<table border="1" summary="Use Case: Logging Variables Changes"><colgroup><col/><col/></colgroup><thead><tr bgcolor="#EEEEEE"><th>Name</th><th>Content</th></tr></thead><tbody><tr><td>Description</td><td>The value assignments are logged in a log file during a debug session. The log file is re-initialized each time the debugger restarts.</td></tr><tr><td>Actor</td><td>Author</td></tr><tr><td>Requirement</td><td>
<div class="itemizedlist"><ul type="disc"><li>
<p>ODIS Creator is started</p>
</li><li>
<p>A debug session was started (start test module, start GFF)</p>
</li><li>
<p>Function tests must be available in the compiled debug format.</p>
</li><li>
<p>The function test in debug format is located in the ODIS Debug version</p>
</li></ul></div>
</td></tr><tr><td>Result</td><td>Value assignments to arrays, variables, and keywords are logged in a log file during the debug session. The log file is written in the log directory.</td></tr><tr><td>Steps</td><td>
<div class="itemizedlist"><ul type="disc"><li>
<p>When starting the debug session: re-initialized the log file (erase)</p>
</li><li>
<p>With each debug call: log commands (type of commands)</p>
</li><li>
<p>With each variable assignment (including declaration): log value assignments</p>
</li></ul></div>
<p>The following information is recorded:</p>
<div class="itemizedlist"><ul type="disc"><li>
<p>Program name (function test system name)</p>
</li><li>
<p>Test step title</p>
</li><li>
<p>Type of command</p>
</li><li>
<p>Variable name and value assignment</p>
</li></ul></div>
</td></tr><tr><td>Relevant data</td><td>The relevant data for running a debug session must be available (MCD software (VW post including DTS or VW MCD, vehicle projects, DIDB, measuring equipment installation, etc.).</td></tr><tr><td>Exceptions</td><td>If the log file cannot be created or written, an error message will be written in the error log (engine.log). No additional error messages will be displayed.</td></tr></tbody></table>

**Table 134. Use Case: Logging Variables Changes**

The value assignments for the individual variables are written in a separate log file. The context information is also added so that the author has the option to localize the location of the change to the variables.

Initializing the log file:

- Any existing log file is deleted when a debug session starts (function test or diagnostic entry). The applicable log entries are then written into the file after that.

Content of the log file:

- The log file is a simple text file that can be opened with a text editor (such as Notepad).
- The log entries are logged with the date and time.
- Each command is logged (system name of the test program, title of the test step, type of command).
- Each variable assignment is logged with the name of the variables and value of the assignment to the runtime.

**Sample content of the "variable.log" log file**

```
20121108 17:40:34:849 : _FKC_UptDbg_Werte@00000 - Global 1 - Deklarieren 20121108 17:40:34:958 : DECLARE Integer integer = 1 20121108 17:40:34:958 : DECLARE String string = 2 20121108 20121108 17:40:34:958 : DECLARE Byte byte = 3 20121108 17:40:34:958 : DECLARE Double double = 4.0
```

Saving the log file:

- The log file is written in the "log" directory in the application directory. The required file system rights are needed in order to create and edit the applicable file.

Details about using the log file:

- The preparation components Log4J are used. A RollingFileAppender is automatically created when the application starts, which creates a "variable.log" file in the "log" directory. The maximum "RollSize" is set to 0. No log file history is saved.
- The log entries are written for the log name "DEBUG\_VARIABLE\_LOG". With this name, new log output can be written in the variables log in various locations in ODIS Creator.
- A menu item for displaying the log file using the default editor ("Notepad") is added in ODIS Creator.

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-15-6-break-points-view.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="7-15-debugger-integrated-operating-system.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="7-15-8-brand-variables-view.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">7.15.6. Break Points View </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 7.15.8. Brand Variables View</td></tr></table>
