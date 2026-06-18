[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md) > [7.14. Function Test Editor](7-14-function-test-editor.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.14.4. Drag and Drop</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-14-3-use-cases.md">Prev</a> </td><th align="center" width="60%">7.14. Function Test Editor</th><td align="right" width="20%"> <a accesskey="n" href="7-14-5-test-steps-view.md">Next</a></td></tr></table>

---

#### <a id="Funktionstesteditor.Allgemein.DragUndDrop"></a>7.14.4. Drag and Drop

In the test step view, new sub-program calls can be inserted or linked using the drag-and-drop function or existing sub-program calls can be modified. In the If, Case and Set status dialogs, it is possible to insert or link editorial objects to tables. The following entries can be dragged and dropped from the editing navigators to a table or within the test step view:

<a id="d4e15589"></a>

<table border="1" summary="List of Possible Drag and Drop Operations"><colgroup><col align="left"/><col align="left"/><col align="left"/></colgroup><thead><tr bgcolor="#EEEEEE"><th align="left">Source</th><th align="left">Objective</th><th align="left">Description</th></tr></thead><tbody><tr><td align="left">Function library navigator: functional tests, general tests</td><td align="left">Test step view: sub-program, test step connections</td><td align="left">For test step connections, the sub-program call is entered below the test step connection source. For existing sub-program calls, the existing one is modified or replaced. The sub-program dialog is opened automatically in both cases.</td></tr><tr><td align="left">Function library navigator: functional tests, general tests, test procedures</td><td align="left">Instruction page: sub-program, instruction connections</td><td align="left">For instruction connections, the sub-program call is entered below the test step connection source. For existing sub-program calls, the existing one is modified or replaced. The sub-program dialog is opened automatically in both cases.</td></tr><tr><td align="left">Equipment network navigator: equipment</td><td align="left">In the set status dialog: equipment list</td><td align="left">If the system names of equipment and the type are inserted at the applicable place in the table or overwrites an existing row upon request. The new/changed row is then marked.</td></tr><tr><td align="left">Knowledge base navigator: diagnostic object</td><td align="left">In Set status dialog: suspicion list, OK list</td><td align="left">If the system names of editorial objects are inserted at the applicable place in the table or overwrites an existing row upon request. The new/changed row is then marked.</td></tr><tr><td align="left">Control module tree, vehicle project navigator: fault location</td><td align="left">In the IF dialog, Case dialog: symptom rule</td><td align="left">The insertion replaces the fault location in the existing row or inserts a new row at the end of the table, if no target row was marked. It is not inserted between rows. The logical operator „Or“ is set for new rows.</td></tr><tr><td align="left">Equipment network navigator: equipment</td><td align="left">In the IF dialog, Case dialog: equipment rule</td><td align="left">There must be at least one row. Inserting replaces the equipment in the present row.</td></tr></tbody></table>

**Table 70. List of Possible Drag and Drop Operations**

  

The following image shows the process of the drag and drop operation. If the instruction dialog is in front of the ODIS Creator desktop, then click on an object in the navigator to move it to the background. If you use the mouse to move the selected object over the windows task bar, then the dialog will come back to the front. Now the object can be stored in the table or table row.

<a id="figure.Funktionstesteditor.Allgemeine_Funktionalitaet.DragUndDrop"></a>

![Image: link with drag and drop](images/fte_arbeitsflaeche_allgemein_dragunddrop.png)

**Figure 347. Link with Drag and Drop**

The following table lists the individual steps on how to link editorial objects using drag and drop.

<a id="d4e15635"></a>

<table border="1" summary="Steps to Link Objects"><colgroup><col align="left"/><col align="left"/></colgroup><thead><tr bgcolor="#EEEEEE"><th align="left">Steps</th><th align="left">Description</th></tr></thead><tbody><tr><td align="left">
<p>Double click to open the target dialog for the instructions.</p>
<p>(If necessary, bring the tab with the target table to the front in the instruction dialog.)</p>
</td><td align="left">
<p>The instruction dialog appears in the foreground.</p>
</td></tr><tr><td align="left">
<p>Insert a new row using the „+“ button.</p>
</td><td align="left">
<p>A new empty row is inserted in the target table.</p>
</td></tr><tr><td align="left">
<p>Click on the view bar to open the navigator.</p>
<p>Then search for and mark the editorial object to be linked in the navigator.</p>
<p>(If necessary, cancel a prompt dialog to save the dialog entries.)</p>
</td><td align="left">
<p>The instruction dialog disappears into the background.</p>
</td></tr><tr><td align="left">
<p>Pull the editorial object out of the navigator using drag and drop. Without releasing the mouse button, move over the entry for ODIS Creator on the task bar.</p>
<p>Wait a moment, until the preview of the application window appears. Then hover over to the instruction dialog. Then wait until the instruction dialog appears in the foreground.</p>
<p>Then continue to drag the editorial object to the new line in the instruction dialog, and finally release the mouse button.</p>
</td><td align="left">
<p>The rows in the table are linked to the editorial object.</p>
</td></tr></tbody></table>

**Table 71. Steps to Link Objects**

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-14-3-use-cases.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="7-14-function-test-editor.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="7-14-5-test-steps-view.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">7.14.3. Use cases </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 7.14.5. Test Steps (View)</td></tr></table>
