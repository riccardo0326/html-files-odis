[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md) > [7.15. Debugger (Integrated Operating System)](7-15-debugger-integrated-operating-system.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.15.4. Actions in Debug Mode</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-15-3-creating-break-points.md">Prev</a> </td><th align="center" width="60%">7.15. Debugger (Integrated Operating System)</th><td align="right" width="20%"> <a accesskey="n" href="7-15-5-running-the-debugger.md">Next</a></td></tr></table>

---

#### <a id="Funktionstesteditor.Debugger.Ablauf"></a>7.15.4. Actions in Debug Mode

The same buttons (see [Figure 553, “Debugger Button”](7-15-4-actions-in-debug-mode.md#figure.Funktionstesteditor.Debugger.Breakpoint_Ablauf "Figure 553. Debugger Button")) in the debugger panel are displayed in all views. They have the following functions:

<a id="figure.Funktionstesteditor.Debugger.Breakpoint_Ablauf"></a>

![Illustration; break point view](images/fte_Debuggerleiste.png)

**Figure 553. Debugger Button**

- Deactivate all break points (but does not delete them)
- Continue in single step mode, meaning it moves to the next command
- Skip the next command, meaning the command to access a test procedure or another test module is not following (unless it contains break points)
- Continue running to the next break point or to the end
- Interrupt the running in progress, meaning single step mode is activated and the interruption takes place at the next request to the debugger (for example, not during prolonged vehicle communication or when running a Java box) [Note: the button is not shown in the illustrations]
- Cancel the current loop, continue running after the loop
- Cancel the current test step: an input dialog for the test step result appears; running continues with the further test steps either based on the result that was entered or without changes as long as the input dialog was not confirmed. Same when using test procedures: cancels the test procedure, continues running after the test procedure access point with the result entered.
- Cancel current test module. May continue running in a test module that is opened, but otherwise the debugger ends
- End debugger

The individual functions can be controlled using the Extras men in the main menu. See [Figure 335, “Menu Bar”](7-14-2-menus-and-tool-bars.md#figure.Funktionstesteditor.Allgemeine_Funktionalitaet.Menueleiste "Figure 335. Menu Bar").

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-15-3-creating-break-points.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="7-15-debugger-integrated-operating-system.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="7-15-5-running-the-debugger.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">7.15.3. Creating Break Points </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 7.15.5. Running the Debugger</td></tr></table>
