[ODIS Creator Help](odis-creator-help.md) > [8. ODIS Creator Preparation Process](8-odis-creator-preparation-process.md) > [8.11. Cooperation export](8-11-cooperation-export.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">8.11.5. Change Tracking</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="8-11-4-using-an-export-template.md">Prev</a> </td><th align="center" width="60%">8.11. Cooperation export</th><td align="right" width="20%"> <a accesskey="n" href="8-11-6-managing-a-global-exclusion-list.md">Next</a></td></tr></table>

---

#### <a id="coopexport.editor.changespy"></a>8.11.5. Change Tracking

The “Track changes” checkbox enables tracking of changed editorial objects (auxiliary documents and function codes) and deleted editorial objects (auxiliary documents, function codes, and diagnostic objects) in the collaboration export. All changed and deleted objects are listed in a separate structure node. The objects are sorted alphabetically within the structure node and are marked with an icon (see [Figure 633, “Collaboration Export Tree View”](8-11-5-change-tracking.md#figure.coopexport.baumansicht "Figure 633. Collaboration Export Tree View")). The comparison will only happen for exports that were created from an export template. There is no comparison when data (knowledge base and equipment network) from the template is changed. It is checked off by default after selecting the template.

<a id="figure.coopexport.baumansicht"></a>

![Image: collaboration export tree view](images/coopexport_baumansicht.png)

**Figure 633. Collaboration Export Tree View**

For deleted objects that are still in the recycle bin, only the display name is shown within the tree structure. Objects that have been permanently deleted (deleted from the recycle bin) will not be displayed.

The following changes will cause an object to be marked as changed:

- New version of an object
- Newly created objects
- If an object has reached its market introduction date and was not previously contained in a collaboration export

##### <a id="coopexport.editor.changespy.flag"></a>8.11.5.1. Identifying the Differences between Test Steps and Action Elements in an SVG Export

Changes of test steps and action elements compared to the previous version will be marked in color so that the author can identify the changes. The following changes will be identified and marked in color:

- New test steps that are added: the frame is displayed with a “bold” green border. All action elements within the test step will also be marked in green.
- New action elements that are added: the frame is displayed with a “bold” green border. If a parent node (such as Loop, If, etc.) is added, the parent node will be marked in green along with all child nodes.
- Changed test steps of all types and action elements: the frame is displayed with a “bold” red border. All changes to content are identified. If an action element with a branch (such as an IF command) was changed, only this will be marked and not the entire branch.
- Moved test steps and action elements: the frame is displayed with a “bold” yellow border. Added and deleted instructions do not have any effect on the marking. All instructions that are affected by the move are marked.
- Moved and changed test steps: the frame is displayed with a “bold” orange border.
- Change or addition of an action element in a test step: the test step is displayed with a red background. The lettering of the test step name is shown in red on the instruction side.

The differences in subprograms (test procedure, general tests, and function tests) are also identified and marked accordingly.

<a id="figure.coopexport.markierung"></a>

![Image: collaboration export marking of differences](images/coopexport_markierung.png)

**Figure 634. Collaboration Export Marking of Differences**

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="8-11-4-using-an-export-template.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="8-11-cooperation-export.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="8-11-6-managing-a-global-exclusion-list.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">8.11.4. Using an Export Template </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 8.11.6. Managing a Global Exclusion List</td></tr></table>
