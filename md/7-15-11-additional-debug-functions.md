[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md) > [7.15. Debugger (Integrated Operating System)](7-15-debugger-integrated-operating-system.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.15.11. Additional Debug Functions</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-15-10-additional-views.md">Prev</a> </td><th align="center" width="60%">7.15. Debugger (Integrated Operating System)</th><td align="right" width="20%"> <a accesskey="n" href="7-16-odis-service-debug.md">Next</a></td></tr></table>

---

#### <a id="d4e32228"></a>7.15.11. Additional Debug Functions

##### <a id="Funktionstesteditor.Debugger.DebugSitzung.Hintergrund"></a>7.15.11.1. Background: Debug Session

The timespan in which ODIS Debug is active is considered the debug session. A debug session can be started in two different ways.

- Using Start test module: the session lasts until the base data function test has run through completely (including all sub-programs). Concrete: the timespan between the Configure test execution and Simulation service dialogs. A runtime error ends the debug session early.
- Using Start GFF: timespan between diagnostic entry and diagnostic exit. Concrete: the timespan between the Configure diagnostic entry service dialog and successful diagnostic exit. Individual function tests can also be run using Start test module in the time period between performing diagnostic entry and diagnostic exit.

The debug session process including user interactions is shown in the following illustration.

<a id="figure.Funktionstesteditor.Debugger.WeitereFunktionen.ActivitySitzung"></a>

![Image: debug session cycle](images/fte_Debug_WeitereFunktionen_DebugSitzung.png)

**Figure 582. Debug Session Cycle**

In the illustration, the debug session begins using the Start GFF function. ODIS Creator contains a callback with Diagnostic entry canceled or Diagnostic entry performed. During entry, the editor has the option to cancel using the Stop GFF function. ODIS Creator receives a callback as soon as this function has canceled diagnostic entry. The debug session ends.

If entry was completed, the Start test module function can be run with no limit on the number (outside of diagnostic entry, this step is intended as its own debug session). Callbacks to ODIS Creator occur depending on the status (started, ended, canceled). The editor calls up the Stop GFF function in order to start diagnostic exit. If the exit is performed, ODIS Creator receives a callback and the debug session is considered ended.

The following table describes the activation status of the functions.

<a id="d4e32249"></a>

<table border="1" summary="Function Activation Status"><colgroup><col/><col/></colgroup><thead><tr bgcolor="#EEEEEE"><th>Function</th><th>Active if</th></tr></thead><tbody><tr><td>Start GFF</td><td>
<div class="itemizedlist"><ul type="disc"><li>
<p>no diagnostic entry is performed</p>
</li><li>
<p>no diagnostic exit is performed</p>
</li><li>
<p>the status of the debug session is diagnostic entry not performed</p>
</li></ul></div>
</td></tr><tr><td>Stop GFF</td><td>
<div class="itemizedlist"><ul type="disc"><li>
<p>while diagnostic entry is running (cancels entry)</p>
</li><li>
<p>Diagnostic entry performed (starts diagnostic exit)</p>
</li></ul></div>
</td></tr><tr><td>Start test module/start test module in single step mode</td><td>
<div class="itemizedlist"><ul type="disc"><li>
<p>no diagnostic entry is performed</p>
</li><li>
<p>no diagnostic exit is performed</p>
</li></ul></div>
</td></tr></tbody></table>

**Table 135. Function Activation Status**

##### <a id="d4e32285"></a>7.15.11.2. Background: Editing Variables

Variables and keywords are called names in the following information. There are different types of names in a function test.

- Super globals: Tester State and Select identify the status of the global tester. Their values cannot be edited manually, but only be affected by the program using the "Set status" command.
- Global name: they are declared/defined within pre-run and are therefore visible for the entire function test (visible until post-run ends).
- Local name: they are declared/defined within a test step or a process command. If the test step or process command ends (such as loop, while, etc.), these variables no longer exist.

The administrative structure of the names is typically in the form of a stack message (LIFO). The following illustration shows the stack with different names.

<a id="figure.Funktionstesteditor.Debugger.VariablenView.Background.Stack"></a>

![Image: stack](images/fte_Debug_VariableView_Background_Stack.png)

**Figure 583. Stack**

After a local command (such as a test step or loop) has ended, meaning the process has exited this area, the name is removed from the stack and destroyed. After the function test post-run has completed, the function test is considered ended and the global name is removed. The stack is displayed in the variables view. There are still filtered variables views that display the content of the stack, filtered based on various criteria.

ODIS Creator assembles and disassembles the stack depending on the procedure item. A **history** of the function tests that have run and the last name used including the values is saved. The values in the history can no longer be changed because the copy of the elements on the stack is not running.

<a id="figure.Funktionstesteditor.Debugger.VariablenView.Background.History"></a>

![Image: history](images/fte_Debug_VariableView_Background_History.png)

**Figure 584. History**

The history contains the names (including the last values that were set) that were available in the last function test when the process ended. There are reasons that could cause the process to end:

1. Because the post-run ended: the process reaches the post-run stage and ends.
2. Due to a runtime error: runtime errors can theoretically occur at any time. (Example: access to an array field that does not exist).
3. Because a function test was canceled using the "Cancel test module" function.
4. Due to ending the debugger using the "End debugger" function.

In all cases, the history is filled with names that are available at the time it ended. The global names are retained for all cases. Especially for cause 4, the local name that was available on the stack at the time of the cancellation. With cause 2, this is not possible because a runtime error occurs here in the operating system that ODIS Creator does not recognize, and this causes local variables to be removed from the stack.

##### <a id="Funktionstesteditor.Debugger.DebugSitzung.SitzungStoppen"></a>7.15.11.3. Stop Debug Session

A debug session can be stopped using the "Stop debug session" function. Executing this function causes the integrated operating system to stop the debug session at the next possible point. During diagnostic entry, the spacing of these points can increase. If the function is used during within diagnostic entry while a function test is being executed with "Start test module", the entire diagnostic session will stop.

##### <a id="Funktionstesteditor.Debugger.ODISDebugMenueeintraege"></a>7.15.11.4. ODIS Debug Menu Items

There are separate menu items for configuring and controlling ODIS Debug. The following menu items are added:

- **ODIS Debug status display**

  Displays the current status of ODIS Service Debug and the interface to the vehicle.
- **Load ODIS Debug test baseline**

  Loads the test baselines from a shared drive.
- **Remove ODIS Debug vehicle project**

  Removes the last vehicle project that was selected.
- **ODIS Debug configuration**

  Configure ODIS Debug and select test baselines or production baselines.
- **Close ODIS Debug measuring equipment view**

  Closes the measuring equipment view.
- **ODIS Debug VCI configuration**

  Configure the connected VCI.

The individual menu items can be seen in the following illustration.

<a id="figure.Funktionstesteditor.Debugger.ODISDebugMenueeintraege"></a>

![Image: ODIS Debug menu items](images/fte_Debug_ODISDebugMenueeintraege.png)

**Figure 585. ODIS Debug Menu Items**

<a id="Funktionstesteditor.Debugger.PruefungsausfuehrungKonfigurieren"></a>The configuration of the test execution can be applied using a separate menu item. To do this, the item "Configure test execution" must be selected. The following image shows the menu item.

<a id="figure.Funktionstesteditor.Debugger.ODISDebugMenueeintraegPruefungsausfuehrungKonfigurieren"></a>

![Image: menu item \\"Configure test execution\\"](images/fte_Debug_ODISDebugMenueeintragPruefAusfKonfig.png)

**Figure 586. "Configure test execution" in the Menu**

##### <a id="Funktionstesteditor.Debugger.FunktionstestInBearbeitung_setzen"></a>7.15.11.5. Placing Function Test in Editing Status

During a debug session, function tests loaded from the database are in read-only mode. Changes can also be made for the debug session and are also visible after being saved locally. In order to make changes that can be saved in the database directly during the debug session, the "Edit function test" function is used to set the status of the function test to "In editing".

The "Edit function test" function allows the author to change a function test during a debug session and then set it afterward to the status "In editing". Changes that were made in read-only mode are transferred into the editing status.

<a id="figure.Funktionstesteditor.Debugger.FunktionstestBearbeiten"></a>

![Image: edit function test](images/fte_Debug_FunktionstestBearbeiten.png)

**Figure 587. Edit Function Test**

An order context must be active in order to change the status. Also, no other users maybe editing the function test. Otherwise, there will be an error message. The text of the error message specifies the name of the user who is editing the function test. ODIS Debug must also be in single step mode in the context of ODIS Creator.

The function is available as a sub-item in the "Extras" menu and as a button in the toolbar. If no order context is set, the dialog screen for setting a context will be displayed, as in ODIS Creator. The function is active if:

- a debug session is running in ODIS Creator,
- the function test currently running in debug mode is in a read-only context,
- ODIS Debug is in single step mode.

The function is always executed in the function test that is currently running in debugger (regardless of the focus).

When the status changes, the associated object properties editor is updated to "In editing". This occurs in the background. The FTE file for the function test is changed from read-only context to order context. The local file is also copied when this happens, which involves closing the read-only version and opening the copy in the function test editor. The FTE file is copied, which may have already been changed locally during the debug session. The changes are retained so they can be saved in the database later (the changes are not visible for ODIS Debug).

The opening and closing occur almost simultaneously. The debug views (ODIS Creator and Service views) are not closed. Their content remains the same. The command counter (yellow arrow) is reset right after reopening.

##### <a id="Funktionstesteditor.Debugger.KonfigurationLogging"></a>7.15.11.6. Logging Mechanism Configuration

ODIS Creator gives the option of adapting the logging level at the time of execution for the application. Using this function, the logging level (scope, type of log entries) of the output in the log file can be controlled. Each time ODIS Creator starts, all output is logged at the "Information" level by default. The logging level can be adjusted in the settings. The settings affect the integrated ODIS Service debug.

<a id="figure.Funktionstesteditor.Benutzervorgaben"></a>

![Image: Settings](images/fte_Benutzervorgaben.png)

**Figure 588. Settings**

The user preferences can be selected using the menu item **Help >> Settings**. There is a “Logging” entry in the navigation tree in the settings. If it is selected, the page for configuring the log levels opens.

<a id="figure.Funktionstesteditor.Benutzervorgaben.LoggingLevel"></a>

![Image: Log-level settings](images/fte_Benutzervorgaben_LoggingLevel.png)

**Figure 589. Log-Level Settings**

The log file specifies the degree/scope of the logging mechanism. Possible levels are:

- Critical error
- Error
- Warning
- Information
- All (corresponds to debug)

The ranking of the log levels is: All (corresponds to debug) < Information < Warning < Error < Critical error (for example, if the level is set to warning, neither debugging nor information entries will be logged, but warnings, errors and critical errors will be logged).

If this dialog is confirmed, the program will set the log levels in the ODIS Logging framework. The level that is set is valid across ODIS, meaning the change in level applies to the root logger and is inherited by all specific loggers as long as they do not have a specified level defined.

The default setting is the "Information" level. The level that is currently active is selected when the dialog opens. If the "All" log level is selected, there may be performance restrictions when running the ODIS Creator application.

The log level change takes place immediately after confirming the dialog and remains in effect for the current ODIS Creator session. meaning this setting is not stored for all sessions that occur. The log level reverts to the default value the next time ODIS Creator is started.

###### <a id="d4e32438"></a>7.15.11.6.1. Configuration by File

In addition to changing the log level in the user interface, there is another configuration option. By supplying the Log4j configuration file by webstarter, the logging can be configured already before ODIS Creator actually starts. The configuration file can also affect more details of the logging functionality beyond just setting the log level.

Notes:

- Each time ODIS Creator starts, the webstarter delivers the default configuration file and overwrites any file that is available locally. If the file is modified manually, ODIS Creator must be restarted using odisc.exe.
- In the configuration file, separate loggers are linked with namespaces with the log level. If no log level is specified, the level of the entry defined as the root logger is used.

The Log4j configuration file consists of three components.

- Appender: specifies the output location for log files. Three appenders that can write log messages in files are currently defined (FileAppender).
- Logger: links a log level with an appender. If the logger name matches a Java package, then the logger only provides messages for the package.
- Root logger: the root logger specifies a log level and a number of appenders. All other loggers inherit the log level from the root logger as long as no specific level is specified. All other loggers inherit the appender from the root logger and can define their own appenders.

For additional information on Log4j, see [Apache Log4J](http://logging.apache.org/log4j/2.x/manual/index.html).

###### <a id="d4e32459"></a>7.15.11.6.2. Log Entries

The following table shows the actions that trigger log outputs in ODIS Creator. Work with ODIS Creator can be reproduced if necessary using these outputs.

<a id="d4e32463"></a>

<table border="1" summary="Log Entries for User Interactions"><colgroup><col/><col/><col/></colgroup><thead><tr bgcolor="#EEEEEE"><th>Topic</th><th>Logging implementation</th><th>Log level</th></tr></thead><tbody><tr><td>View change</td><td>Each time the view changes, a log entry with the name of the new view is written.</td><td>Debug</td></tr><tr><td>Editor displays</td><td>Each time an editor opens and closes, a log entry with the name of the editor (system name of the object) and the action (open or close) is written.</td><td>Debug</td></tr><tr><td>View displays</td><td>If a view is opened, closed or activated, a log entry with the name of the view will be written.</td><td>Debug</td></tr><tr><td>FTE command dialogs</td><td>When opening and closing an FTE command dialog, a log entry with the name of the dialog is written.</td><td>Debug</td></tr><tr><td>Commands</td><td>Each time a command is initiated using the menu, a log entry with information about the initiated command is written.</td><td>Debug</td></tr><tr><td>ODIS Creator Debug</td><td>Activities regarding status of the debug session, etc.</td><td>Debug</td></tr></tbody></table>

**Table 136. Log Entries for User Interactions**

##### <a id="Funktionstesteditor.Debugger.DebugSitzung.BekannteProbleme"></a>7.15.11.7. Messages in the Problems View

A special Java code must be generated from the function test in order to use ODIS Debug. The scope of the debug Java code is larger than the standard Java code that is playing during preparation. For this reason, the debug Java code can reach the limits of the Java Virtual Machine, which the standard Java code does not reach. This first occurs during debugging and is displayed in the problems view.

For example, if a compilation message that contains the text "Code too large" indicates this condition. The solution can consist of various actions:

- Reducing the scope of test steps
- Storing logic in sub-programs
- Reducing the commands in pre-run
- Splitting control module communication commands with many parameters
- Optimizing/splitting expensive array initializations
- Splitting case commands that check too many values

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-15-10-additional-views.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="7-15-debugger-integrated-operating-system.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="7-16-odis-service-debug.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">7.15.10. Additional Views </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 7.16. ODIS Service Debug</td></tr></table>
