[ODIS Creator Help](odis-creator-help.md) > [8. ODIS Creator Preparation Process](8-odis-creator-preparation-process.md) > [8.11. Cooperation export](8-11-cooperation-export.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">8.11.3. Collaboration export editor</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="8-11-2-collaboration-export-properties-view.md">Prev</a> </td><th align="center" width="60%">8.11. Cooperation export</th><td align="right" width="20%"> <a accesskey="n" href="8-11-4-using-an-export-template.md">Next</a></td></tr></table>

---

#### <a id="coopexport.editor"></a>8.11.3. Collaboration export editor

The editor serves to define new collaboration exports as well as to view collaboration exports that have already been exported. In addition to the name of the collaboration export and the comment field, the editor also shows configuration options for an export. These include the option to select export templates, knowledge bases, and equipment network objects, as well as a checkbox for selecting the “German” or “English” language, use of an exclusion list, and a “Test baseline” checkbox for selecting the processing status that should be taken into consideration during the export. The configuration options will be described in more detail now. The [Figure 625, “Cooperation export”](8-11-3-collaboration-export-editor.md#figure.coopexport.editor "Figure 625. Cooperation export") shows the complete editor in read mode. The individual components and selection options are described in more detail. The logs for exports can be viewed and downloaded as the logs for orders are (see [Section 8.7, “Logs for Baselines”](8-7-logs-for-baselines.md "8.7. Logs for Baselines")).

<a id="figure.coopexport.editor"></a>

![Image: cooperation export editor](images/coopexport_editor.png)

**Figure 625. Cooperation export**

  

##### <a id="coopexport.editor.knowledgebaseAndEquipment"></a>8.11.3.1. Selecting a Knowledge Base and Equipment Network Objects

The selected knowledge base will be listed in the “Knowledge base” field. The knowledge base is selected in the “Editorial objects selection dialog” [Figure 626, “Knowledge base selection dialog for collaboration export”](8-11-3-collaboration-export-editor.md#figure.coopexport.dialog.knowledgebase "Figure 626. Knowledge base selection dialog for collaboration export"), which can be opened by clicking on the “Select” button next to the “Knowledge base” field.

<a id="figure.coopexport.dialog.knowledgebase"></a>

![Image: knowledge base selection dialog for collaboration export](images/coopexport_knowledgebase_dialog.png)

**Figure 626. Knowledge base selection dialog for collaboration export**

  

This dialog displays the knowledge bases that can be selected with their subordinate diagnostic objects. An entire knowledge base or one or more diagnostic objects can be selected, but all of the diagnostic objects must be from one knowledge base. Then one or more equipment network objects must selected in the associated equipment network for filtering the variant rules. The selected equipment network objects must be allocated to a vehicle type, which is assigned to the selected knowledge base. The selection is made in the “Editorial objects selection dialog” [Figure 627, “Equipment network selection dialog for collaboration export”](8-11-3-collaboration-export-editor.md#figure.coopexport.dialog.equipment "Figure 627. Equipment network selection dialog for collaboration export"), which can be opened by clicking on the “Select” button next to the “Equipment network” field. If the knowledge base selection is changed, any equipment network objects already selected will be discarded.

<a id="figure.coopexport.dialog.equipment"></a>

![Image: equipment network selection dialog for collaboration export](images/coopexport_equipment_dialog.png)

**Figure 627. Equipment network selection dialog for collaboration export**

  

Only the last risk-released status will be displayed in both selection dialogs so that only the production data can ever be used.

##### <a id="coopexport.editor.language"></a>8.11.3.2. Language Selection

The selection of the “German” or “English” language defines in which language the collaboration exports should be created. No language is selected by default. At least one language must be selected. If both languages are selected, a collaboration export package will be created for each language.

##### <a id="coopexport.exclusionlist"></a>8.11.3.3. Using an Exclusion List

The editor also gives the option of using a local or global exclusion list [Figure 628, “Global exclusion list”](8-11-3-collaboration-export-editor.md#figure.coopexport.globalexclusions "Figure 628. Global exclusion list"), which are both simple text files consisting of regular expressions. When creating a configured collaboration export, the system will reference this exclusion list. Based on these, the values for the variables listed and the keywords for the collaboration export [Figure 629, “Example collaboration export”](8-11-3-collaboration-export-editor.md#figure.coopexport.example "Figure 629. Example collaboration export") will be made unrecognizable. For example, the value of the “test1” variable in the collaboration export will be displayed in a way that cannot be identified because the “test1” variable is contained in the exclusion list.

<a id="figure.coopexport.globalexclusions"></a>

![Image: global exclusion list](images/coopexport_globalexclusionlist.png)

**Figure 628. Global exclusion list**

  

<a id="figure.coopexport.example"></a>

![Image: example cooperation export Example](images/coopexport_example_without_wildcard.png)

**Figure 629. Example collaboration export**

  

The following example [Figure 630, “Global Exclusion List with Wildcard”](8-11-3-collaboration-export-editor.md#figure.coopexport.globalexclusions.wildcard "Figure 630. Global Exclusion List with Wildcard") shows a regular expression with a wildcard in the exclusion list:

<a id="figure.coopexport.globalexclusions.wildcard"></a>

![Image: global exclusion list with wildcard](images/coopexport_globalexclusionlist_wildcard.png)

**Figure 630. Global Exclusion List with Wildcard**

  

In the associated collaboration export, the values for the test1, test2, and test3 variables will be made unrecognizable.

<a id="figure.coopexport.example.wildcard"></a>

![Image: example collaboration export with wildcard](images/coopexport_example_with_wildcard.png)

**Figure 631. Example collaboration export with wildcard**

  

Exclusion lists can be used as follows:

- no exclusion list
- local exclusion list only
- global exclusion list only
- local and global exclusion lists (contents will be combined)

If a local exclusion list is used, it must be imported using the import dialog. A list that has already been imported can be exported.

If using a global exclusion list, it must be imported first if that has not already been done. A global exclusion list that has already been imported in the editor is preselected by default.

##### <a id="coopexport.editor.testbaseline"></a>8.11.3.4. Selecting the Processing Status

Selecting the “Test baseline” checkbox specifies that the most current versions of the editorial objects (regardless of status, logic such as test baseline) should be exported if applicable so that a co-op export will also reflect the current processing status. The objects that are in the “In Processing" status will also be taken into account during the export.

If the checkbox is deactivated, a production export will take place.

If the checkbox is activated:

- The processing status of the editorial objects will be exported
- The “Comment” action element and the content from the “Global Start” will be exported
- The data classification will be set to “Confidential” (data classification cannot be configured)
- The local and global exclusion lists (contents) will be combined

Change tracking will only happen for exports that were created from an export template. When changing the data (knowledge base, equipment network, and “Test baseline” checkbox) from the template, there is no comparison and the “Test baseline” checkbox will be deactivated.

To track changes better, they will be indicated with a changed icon directly on an object.

The following changes will cause an object to be marked:

- New version of an object (also a working version)
- Newly created objects
- If an object has reached its market introduction date and was not previously contained in a co-op export
- The “Last change” date is greater than in the last export
- The “Last change” date is greater than in the last export

Objects that are in processing will also be marked by a change in icon

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="8-11-2-collaboration-export-properties-view.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="8-11-cooperation-export.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="8-11-4-using-an-export-template.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">8.11.2. Collaboration export properties view </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 8.11.4. Using an Export Template</td></tr></table>
