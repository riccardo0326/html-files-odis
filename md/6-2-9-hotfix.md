[ODIS Creator Help](odis-creator-help.md) > [6. ODIS Creator Order Management Process](6-odis-creator-order-management-process.md) > [6.2. Orders](6-2-orders.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">6.2.9. Hotfix</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="6-2-8-determining-the-market-supply.md">Prev</a> </td><th align="center" width="60%">6.2. Orders</th><td align="right" width="20%"> <a accesskey="n" href="6-3-text-request.md">Next</a></td></tr></table>

---

#### <a id="prozess.hotfix"></a>6.2.9. Hotfix

A hotfix is a supply of individual editorial objects that are connected to the equipment network. Some editorial objects, such as measured value tables and XML templates, must be used by a function code in order to be supplied. The author can select if only the selected or all of the referenced objects should be included in a hotfix. Editorial objects from different teams and with different statuses can be provided in a hotfix.

The creation may take a very long time when exporting with reference objects and because of this, occurs asynchronously in the background. The author can continue to work on editing while the hotfix exports.

The editor for creating a hotfix can be seen in [Figure 133, “Hotfix Editor”](6-2-9-hotfix.md#figure.hotfix.overview "Figure 133. Hotfix Editor"). The objects from the desired order are displayed in the upper section. Objects are listed in the lower table, which are provided with the hotfix. In the column **Already referenced objects**, it can be decided which option (see [Table 31, “Options for the Incorporation of Referenced Objects”](6-2-9-hotfix.md#table.hotfix.objekte "Table 31. Options for the Incorporation of Referenced Objects")) should be selected for each object.

<a id="figure.hotfix.overview"></a>

![Editor for creating a hotfix](images/Hotfix_Editor.jpg)

**Figure 133. Hotfix Editor**

##### <a id="hotfix.aufgaben"></a>6.2.9.1. Create Hotfix

To create a hotfix, you must be in the author role. Click on the **Insert** and **Hotfix** [buttons](2-2-general-definitions-and-glossaries.md#schaltflaeche) in the [menu bar](2-2-general-definitions-and-glossaries.md#menuleiste) or use the corresponding buttons from the [context menu](2-2-general-definitions-and-glossaries.md#kontextmenu) in the order navigator to access an order header or order step. Select the desired authoring team in the [selection field](2-2-general-definitions-and-glossaries.md#auswahlfeld) in the following dialog.

The editor for defining hotfixes will open. Using the [selection field](2-2-general-definitions-and-glossaries.md#auswahlfeld) in the upper left side, you can select the order header, order step and team. The editorial objects from the currently selected order step will always be displayed. Alternatively, you can also select the entry used across teams for a location (for example "00021 - all locations"). Then all editorial objects can be selected, which belong to an order step from an authoring team at the selected location. In addition to this, the editorial objects in the order step must have been marked with the flag "hotfix". See [Figure 134, “Editor for Hotfix with Cross-Location Selection”](6-2-9-hotfix.md#figure.hotfix.overview.team.location "Figure 134. Editor for Hotfix with Cross-Location Selection").

<a id="figure.hotfix.overview.team.location"></a>

![Editor for creating a hotfix with all locations selection](images/Hotfix_Editor_Standort.png)

**Figure 134. Editor for Hotfix with Cross-Location Selection**

The user pulls the desired editorial objects into the hotfix table via drag and drop. As soon as the desired editorial objects are placed together from the desired orders, then the author must still specify a name, a dealer code and a base line. Furthermore, a production baseline or a test baseline can be selected for the hotfix. After setting the baseline type, the baseline for creating the hotfix can be selected from the last baseline of the selected type.

By saving and checking in, the hotfix will be created and the author receives a notification, that the creation (see [Figure 135, “Hotfix Information”](6-2-9-hotfix.md#figure.hotfix.info "Figure 135. Hotfix Information")) was started.

<a id="figure.hotfix.info"></a>

![Information for creating a hotfix](images/Hotfix_Info.jpg)

**Figure 135. Hotfix Information**

After confirming the information, the author can continue to work editorially and they will received an additional message only when the hotfix preparation ends.

If the hotfix preparation was not successful, the user receives a message with a table in which the objects and the associated errors are listed (see [Figure 136, “Hotfix error”](6-2-9-hotfix.md#figure.hotfix.fehler "Figure 136. Hotfix error")).

<a id="figure.hotfix.fehler"></a>

![Hotfix error](images/HotfixTabelle.jpg)

**Figure 136. Hotfix error**

The user now has the option to double click in order to switch directly from the system names to the object in ODIS Creator. This will close all opened editors. If one or more editors or open in edit mode, then the user will be asked if they would like to save before closing. Excluded from this are hotfix editors that are open in edit mode; these will be closed without confirming and saving. Only if all editors could be successfully closed, then the editor will open to the editorial object.

The hotfix error table remains open when jumping to an editorial object. With the button "Open hotfix editor", the user goes back to the hotfix definition, for which the error has occurred. All open editors are closed when jumping to the editorial object.

The warning will be closed without additional actions using the button "Close".

If the hotfix is exported successfully, the user receives the information displayed in [Figure 137, “Hotfix successful”](6-2-9-hotfix.md#figure.hotfix.erfolgreich "Figure 137. Hotfix successful").

<a id="figure.hotfix.erfolgreich"></a>

![Hotfix successful](images/Hotfix_erfolgreich.png)

**Figure 137. Hotfix successful**

If available, the translations for all exported editorial objects are exported in the hotfix. In an additional language package, the translation-relevant texts of the respective editorial object is exported in the source language for each editorial object contained in the hotfix, in which the applicable editorial object was created. With this, texts that are not translated are displayed in their original language in the processing system.

Depending on which baseline type was selected for a hotfix, the translation-relevant texts of the transferred objects are also exported. For hotfixes with production baselines, all available translations are always exported with the transferred objects. For hotfixes based on a text baseline, only the source language of the objects under the concatenated source language ISO code "OD-OD" is exported.

##### <a id="hotfix.javaboxe"></a>6.2.9.2. Creating a Hotfix with a Function Code with the **In Processing** Status

When a hotfix is exported, in the case of a production baseline, it is also checked for function code objects to see whether Java box(es) are included in the test sequence. If all existing Java boxes have the status  **Accepted**, the hotfix is successfully exported.

The export cannot be created if:

- The function code has the “In Processing” status and at least one Java box is present within the test sequence.
- The function code has the “In testing” status and at least one unverified or rejected Java box is present within the test sequence.

An error message will inform the author of this (see [Figure 138, “Hotfix Java Box”](6-2-9-hotfix.md#figure.hotfix.javabox "Figure 138. Hotfix Java Box")).

<a id="figure.hotfix.javabox"></a>

![Hotfix Java Box](images/Hotfix_Javabox.jpg)

**Figure 138. Hotfix Java Box**

When a hotfix is exported, in the case of a test baseline, no checks are carried out on the function code objects, whether they contain Java boxes in test sequences and the status of the java boxes. The hotfix is successfully exported in any case.

##### <a id="hotfix.objekte"></a>6.2.9.3. Incorporation of Referenced Objects

Editorial objects can be prepared in a hotfix. The author can select which objects are included in a hotfix. There are four different options for how referenced objects can be included (see [Table 31, “Options for the Incorporation of Referenced Objects”](6-2-9-hotfix.md#table.hotfix.objekte "Table 31. Options for the Incorporation of Referenced Objects")).

<a id="table.hotfix.objekte"></a>

<table border="1" summary="Options for the Incorporation of Referenced Objects"><colgroup><col align="left"/><col align="left"/></colgroup><thead><tr bgcolor="#EEEEEE"><th align="left"><span class="bold"><strong>Option</strong></span></th><th align="left"><span class="bold"><strong>Description</strong></span></th></tr></thead><tbody valign="top"><tr><td align="left" valign="top">No referenced objects</td><td align="left" valign="top">Only the selected object itself can be applied to the hotfix. The object is however <span class="bold"><strong>only</strong></span> then applied to the hotfix, if the selected version of this object is <span class="bold"><strong>not included in the selected base line</strong></span>.</td></tr><tr><td align="left" valign="top">No parent objects</td><td align="left" valign="top">
<p>The selected object is applied to the hotfix, if the selected version of this object is <span class="bold"><strong>not included in the selected base line</strong></span>.</p>
<p>If the selected object is applied to the hotfix and there is <span class="bold"><strong>no diagnostic object</strong></span>, all of its <span class="bold"><strong>subordinate objects from the function library</strong></span> are applied to the hotfix. Only subordinate objects with the confirmed completed or released status are exported into the hotfix.</p>
<p>The search for subordinate objects is recursive. The recursion ends at a subordinate object, that is already in either the selected baseline itself or its version in the list of the primarily selected objects, that are applied to the hotfix. The object at which the recursion ends, is <span class="bold"><strong>not applied</strong></span> to the hotfix.</p>
<p><span class="bold"><strong>Note:</strong></span> All referenced objects (supplemental documents, function codes, other diagnostic objects as child objects) from the diagnostic object must be explicitly added by the authors.</p>
</td></tr><tr><td align="left" valign="top">No sub-objects</td><td align="left" valign="top">
<p>The selected object is applied to the hotfix, if the selected version of this object is <span class="bold"><strong>not included in the selected base line</strong></span>.</p>
<p>If the selected object itself is applied to the hotfix, all of its direct superordinate objects (parent objects) are considered. It checks if the version of the <span class="bold"><strong>direct</strong></span> parent object is included in the list of primary selected objects that are already applied to the hotfix. If not, then the parent object will be applied to the hotfix. This ensures that the access points of new objects are also included in the hotfix package and are included in the export for the ODIS Service.</p>
<p>The superordinate objects that are completely new or have newly released versions (relating to the hotfix) are added recursively. The recursion ends at a superordinate object:</p>
<div class="itemizedlist"><ul type="disc"><li>
<p>that is already included in the selected baseline. The object at which the recursion ends, is <span class="bold"><strong>applied</strong></span> to the hotfix.</p>
</li><li>
<p>its version is already included in the list of primary selected objects that are applied to the hotfix. The object at which the recursion ends, is <span class="bold"><strong>not</strong></span> <span class="bold"><strong>applied</strong></span> to the hotfix.</p>
</li></ul></div>
</td></tr><tr><td align="left" valign="top">All referenced objects</td><td align="left" valign="top">
<p><span class="bold"><strong>Default:</strong></span> The object itself and its superordinate and subordinate objects are applied to the hotfix. This selection is preallocated.</p>
<p>The selection of superordinate objects matches the selection of superordinate objects for the "No subobjects" option. The selection of subordinate objects matches the selection of subordinate objects for the "No parent objects" option.</p>
</td></tr></tbody></table>

**Table 31. Options for the Incorporation of Referenced Objects**

  

<a id="figure.hotfix.objekte"></a>

![Selection Menu for Incorporating Referenced Objects](images/ReferenzierteObjekte.png)

**Figure 139. Selection Menu for Incorporating Referenced Objects**

The option for an individual or multiple editorial objects can be placed in ODIS Creator. [Figure 139, “Selection Menu for Incorporating Referenced Objects”](6-2-9-hotfix.md#figure.hotfix.objekte "Figure 139. Selection Menu for Incorporating Referenced Objects") shows the selection menu for the object options.

To set the same option for multiple editorial objects, the editorial objects will be marked and then the desired option is selected via the context menu. (see [Figure 140, “Context menu for including referenced objects”](6-2-9-hotfix.md#figure.hotfix.kontextmenu "Figure 140. Context menu for including referenced objects"))

<a id="figure.hotfix.kontextmenu"></a>

![Context menu for including referenced objects](images/KontextmenuReferenzierteObjekte.png)

**Figure 140. Context menu for including referenced objects**

##### <a id="hotfix.redobjekte.markieren"></a>6.2.9.4. Mark Editorial Objects for Hotfix

So that an editorial object is available in the "all location" selection, it must be marked for this by the author. For this, you must open the order step, to which the editorial object is assigned, in the order management view for editing. Then you can activate the checkbox in the "hotfix" column from the editorial objects list or mark multiple editorial objects and select the entry **Mark for hotfix** in the context menu (see [Figure 141, “Order step with the editorial object selection for a hotfix”](6-2-9-hotfix.md#figure.hotfix.objekte.aktivieren "Figure 141. Order step with the editorial object selection for a hotfix")). With the entry **Delete hotfix flag** in the context menu, you can revert the selection.

<a id="figure.hotfix.objekte.aktivieren"></a>

![Order step with the editorial object selection for a hotfix](images/Auftragsschritt_Hotfix.png)

**Figure 141. Order step with the editorial object selection for a hotfix**

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="6-2-8-determining-the-market-supply.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="6-2-orders.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="6-3-text-request.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">6.2.8. Determining the Market Supply </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 6.3. Text request</td></tr></table>
