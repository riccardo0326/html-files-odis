[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md) > [7.7. Control Module Tree](7-7-control-module-tree.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.7.3. Object Editor in Control Module Tree</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-7-2-tree-view-in-the-control-module-tree.md">Prev</a> </td><th align="center" width="60%">7.7. Control Module Tree</th><td align="right" width="20%"> <a accesskey="n" href="7-7-4-making-information-globally-available-in-the-control-module-tree.md">Next</a></td></tr></table>

---

#### <a id="sgbaum.objekteditor"></a>7.7.3. Object Editor in Control Module Tree

The object editor in the control module tree displays a version for every marked control module object according to the ODX standard main version, secondary version. The logical links from the used vehicle projects are also listed in the **Logical Links** table.

The object editor also contains all operations of the selected control module and the associated parameters.

<a id="table.hinweis.sgbaum_operationen"></a>

<table border="1" summary="Operations"><colgroup><col align="center"/><col align="left"/></colgroup><tbody valign="top"><tr><td align="center" valign="top"><span class="inlinemediaobject"><img alt="Note symbol" src="images/info.png"/></span></td><td align="left" valign="top"><span class="bold"><strong>Note:</strong></span> For performance reasons, the operations are no longer displayed in the default view of the object editors. They can be reloaded for every control module, in which the context menu entry <span class="bold"><strong>Load operations</strong></span> is performed in the <span class="bold"><strong>Operations</strong></span> table.</td></tr></tbody></table>

**Table 62. Operations**

As usual, the object relationships to the used objects are also seen at the control module objects in the **used** table, here they are the DTC memory entries or DTC objects used by the control module object. Base control modules and base versions here also contain the respective child elements in the tree, such as ECU versions.

The object editor likewise contains the object relationships to the control module object in the **used by** table. There you will find all test programs, vehicle projects and basic control modules that are directly related to the object. These are subsequently loaded in the “Used” and “Used by” tables when the editor is opened for the first time. The relationship of test programs to control module objects is established, for example, via an Ecukom command.

<a id="table.hinweis.sgbaum_objekt_loeschen"></a>

<table border="1" summary="Deleting Control Module Objects"><colgroup><col align="center"/><col align="left"/></colgroup><tbody valign="top"><tr><td align="center" valign="top"><span class="inlinemediaobject"><img alt="Note symbol" src="images/info.png"/></span></td><td align="left" valign="top"><span class="bold"><strong>Note:</strong></span> Control module objects can be deleted! If the deletion of a control module object is initiated, all usage locations are automatically displayed by the system in a dialog window, in order to inform you of the effects of the deletion.</td></tr></tbody></table>

**Table 63. Deleting Control Module Objects**

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-7-2-tree-view-in-the-control-module-tree.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="7-7-control-module-tree.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="7-7-4-making-information-globally-available-in-the-control-module-tree.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">7.7.2. Tree View in the Control Module Tree </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 7.7.4. Making Information Globally Available in the Control Module Tree</td></tr></table>
