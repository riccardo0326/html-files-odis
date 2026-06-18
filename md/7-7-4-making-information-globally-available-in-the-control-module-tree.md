[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md) > [7.7. Control Module Tree](7-7-control-module-tree.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.7.4. Making Information Globally Available in the Control Module Tree</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-7-3-object-editor-in-control-module-tree.md">Prev</a> </td><th align="center" width="60%">7.7. Control Module Tree</th><td align="right" width="20%"> <a accesskey="n" href="7-7-5-detailed-view-of-operations.md">Next</a></td></tr></table>

---

#### <a id="sgbaum.globalisieren"></a>7.7.4. Making Information Globally Available in the Control Module Tree

Operations can be "globalized" from a control module version. This allows variant-specific operations to be assigned to the base control module and are then available in all logs. This function must be performed to be able to retrieve operations later in an Ecukom at a base control module, similar to the old system at the base control module description.

Select the **Globalize** context menu entry in the base control module object editor. See [Figure 272, “Globalize Function”](7-7-4-making-information-globally-available-in-the-control-module-tree.md#figure.sg-baum.globalisieren "Figure 272. Globalize Function"). A supplemental editor will open with the list of all available operations from the control module versions of the base control module. The operations are sorted by log variants in the supplemental editor.

<a id="figure.sg-baum.globalisieren"></a>

![Image: opening the "Globalize" function](images/globalisieren.png)

**Figure 272. Globalize Function**

Select one or more desired options in the supplemental editor and set the value in the selection list to **yes** in the **global** column.

This makes the operations of a function test now available in Ecukom when selecting a base control module.

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-7-3-object-editor-in-control-module-tree.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="7-7-control-module-tree.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="7-7-5-detailed-view-of-operations.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">7.7.3. Object Editor in Control Module Tree </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 7.7.5. Detailed View of Operations</td></tr></table>
