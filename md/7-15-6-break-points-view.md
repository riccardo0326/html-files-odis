[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md) > [7.15. Debugger (Integrated Operating System)](7-15-debugger-integrated-operating-system.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.15.6. Break Points View</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-15-5-running-the-debugger.md">Prev</a> </td><th align="center" width="60%">7.15. Debugger (Integrated Operating System)</th><td align="right" width="20%"> <a accesskey="n" href="7-15-7-variables-view.md">Next</a></td></tr></table>

---

#### <a id="Funktionstesteditor.Debugger.Breakpoint_View"></a>7.15.6. Break Points View

The break points view is always available and it lists all break points above all break points that were set locally. A break point can be activated or deactivated in the "Active" column. The Environment column shows information about the location of the break point.

Double-clicking on a break point selects the associated nodes in the function test editor.

The display can be sorted in all views in either ascending or descending order (done by double-clicking on the column header). If running was stopped at one of the break points shown, the corresponding line will be highlighted in yellow.

You can delete a break point by clicking a line and pressing the Remove button (or: using the context menu).

To deactivate all break points, you can use the "Deactivate all break points" menu item in the "Extras" menu or the corresponding action in the break points view. See also [Figure 565, “Break Point View”](7-15-6-break-points-view.md#figure.Funktionstesteditor.Debugger.Breakpoint_View "Figure 565. Break Point View").

<a id="figure.Funktionstesteditor.Debugger.Breakpoint_View"></a>

![Illustration; break point view](images/fte_breakpoint_ansicht.png)

**Figure 565. Break Point View**

Double-clicking on one of the lines displayed opens the test module/test step that is referenced in the FTE (a new window opens, if necessary), marks the referenced command there, and moves it into the visible area of the window, if necessary (the block where it is located in collapsed, it will be expanded).

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-15-5-running-the-debugger.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="7-15-debugger-integrated-operating-system.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="7-15-7-variables-view.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">7.15.5. Running the Debugger </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 7.15.7. Variables View</td></tr></table>
