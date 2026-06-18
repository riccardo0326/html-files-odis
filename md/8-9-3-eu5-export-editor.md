[ODIS Creator Help](odis-creator-help.md) > [8. ODIS Creator Preparation Process](8-odis-creator-preparation-process.md) > [8.9. EU5 Export](8-9-eu5-export.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">8.9.3. EU5 Export Editor</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="8-9-2-eu5-export-properties-display.md">Prev</a> </td><th align="center" width="60%">8.9. EU5 Export</th><td align="right" width="20%"> <a accesskey="n" href="8-10-plausibility-and-completeness-checks.md">Next</a></td></tr></table>

---

#### <a id="eu5export.editor"></a>8.9.3. EU5 Export Editor

The editor serves to define new EU5 exports as well as to view EU5 exports that have already been exported. The editor shows the selected brands as well as the defined filter criteria for the EU5 export. The [Figure 613, “EU5 Export Editor”](8-9-3-eu5-export-editor.md#figure.eu5export.editor "Figure 613. EU5 Export Editor") shows the complete editor in read mode. The individual components and selection options are described in more detail. The logs for exports can be viewed and downloaded as the logs for orders are (see [Section 8.7, “Logs for Baselines”](8-7-logs-for-baselines.md "8.7. Logs for Baselines")).

<a id="figure.eu5export.editor"></a>

![Image: EU5 export editor](images/eu5export_editor.png)

**Figure 613. EU5 Export Editor**

  

##### <a id="eu5export.editor.brand"></a>8.9.3.1. Brand Selection

The EU5 export is not brand-dependent. For this reason, you must select at least one brand in the editor for which the EU5 export should be performed. You can select all brands or a random subset of brands given in the system.

By pressing the ![](images/Plus01.png)button above the list of brands, a selection dialog opens (see [Figure 614, “Brand Selection”](8-9-3-eu5-export-editor.md#figure.eu5export.brandselect "Figure 614. Brand Selection")) in which you can select all brands that exist in the system.

By pressing the ![](images/minus.png)-button, previously selected brands can also be deleted.

The base of the EU5 export is the last completed production baseline of the selected brands that was exported. So that an editorial object is recorded in the EU5 export, it must have been previously included in a production baseline.

If a production baseline does not exist yet for one of the specified brands, then the entire EU5 export will be canceled and set to the [Error](8-6-4-error.md "8.6.4. Error") status.

<a id="figure.eu5export.brandselect"></a>

![Image: brand selection](images/eu5export_brandselection.png)

**Figure 614. Brand Selection**

##### <a id="eu5export.editor.filter"></a>8.9.3.2. Filter Definition

In addition to the brand selection (and thus the selection of base production baselines), you can still also specify special filter criteria in order to limit the amount of exported objects. With the **Apply filter** button, you can apply a filter definition of a past EU5 export in the current editor. Other adjustments/changes can then be made to the applied filter criteria. There are three different filter options for this:

- **Filter by UMB flag:**

  If this checkbox is enabled, only the knowledge base of the selected brands will be exported which have at least one UMB flag set to an assigned vehicle model.
- **Filter by system names**

  When filtering by system names, you can specify any list of XML template system names or any list of strings that should act as the filter. All XML templates and function codes which use this XML template are then excluded from the export. It is important to note that upper-case and lower-case letters are not considered when filtering by system names.

  To make input easier, the dialog from [Figure 615, “System Names Selection”](8-9-3-eu5-export-editor.md#figure.eu5export.namefilter "Figure 615. System Names Selection") appears after pressing the ![](images/Plus01.png)-button.

  By double-clicking on an existing filter criteria, it can be revised again. The dialog appears here similar to how it is pre-filled for a new creation with the string to be revised.

  By pressing the ![](images/minus.png)-button, previously selected filter settings can also be deleted.

  <a id="figure.eu5export.namefilter"></a>

  ![Image: system names selection](images/eu5export_namefilter.png)

  **Figure 615. System Names Selection**
- **Filter by FTE node types**

  When filtering by FTE node types, you can specify which node types are not allowed to appear in the exported function tests. If a function test contains a matching node type, then it will be excluded from the EU5 export. The node types **Login** and **Write XML/XML IA** are initially preset. To make the selection easier, the dialog from [Figure 616, “FTE Node Filter”](8-9-3-eu5-export-editor.md#figure.eu5export.ftefilter "Figure 616. FTE Node Filter") appears after pressing the ![](images/Plus01.png)-button.

  By pressing the ![](images/minus.png)-button, previously selected filter settings can also be deleted. This also applies to the entries initially given.

  <a id="figure.eu5export.ftefilter"></a>

  ![Image: FTE node filter](images/eu5export_ftefilter.png)

  **Figure 616. FTE Node Filter**

As an example, the [Table 138, “Filter Example”](8-9-3-eu5-export-editor.md#table.eu5.filter "Table 138. Filter Example") shows how the above mentioned filter criteria will be analyzed. The sequence of the filter analysis is:

- First, the volume given by the base production baseline will be limited based on the UMB flag filter.
- Then all Guided Functions of the remaining knowledge base will be determined.
- The amount of Guided Functions, including their child objects used, are now limited based on the specified XML template system names filter and the FTE node type filter.
- The quantity resulting from this will then be prepared.

<a id="table.eu5.filter"></a>

<table border="1" summary="Filter Example"><colgroup><col align="left"/><col align="left"/><col align="left"/><col align="left"/></colgroup><thead><tr><th align="left"><span class="bold"><strong>Objects</strong></span></th><th align="left"><span class="bold"><strong>UMB flag set</strong></span></th><th align="left"><span class="bold"><strong>XML template system names filter list:</strong></span> "service42"</th><th align="left"><span class="bold"><strong>FTE node filter list:</strong></span> "Login", "Write_XML/XML_IA", "Logout"</th></tr></thead><tbody valign="top"><tr><td align="left" bgcolor="#00BF00" valign="top"> <span class="bold"><strong>WBS</strong></span> with reference to vehicle model with UMB</td><td align="left" valign="top">Will be exported</td><td align="left" valign="top">----</td><td align="left" valign="top">----</td></tr><tr><td align="left" valign="top"><span class="bold"><strong>WBS</strong></span> with reference to vehicle model without UMB</td><td align="left" valign="top">Will not be exported</td><td align="left" valign="top">----</td><td align="left" valign="top">----</td></tr><tr><td align="left" valign="top"><span class="bold"><strong>FKC</strong></span> "Kn_12_32_mnb_read" with "Login" and "Read_XML" (reference to XML template "Response_LineIn")</td><td align="left" valign="top">----</td><td align="left" valign="top">Will be exported</td><td align="left" valign="top">Will not be exported</td></tr><tr><td align="left" valign="top"><span class="bold"><strong>FKC</strong></span> "XT_2_drb_read" with "Read_XML" (reference to XML template "Request_service42")</td><td align="left" valign="top">----</td><td align="left" valign="top">Will not be exported</td><td align="left" valign="top">----</td></tr><tr><td align="left" bgcolor="#00BF00" valign="top"> <span class="bold"><strong>FKC</strong></span> "drm_5_x_calculate" with "Read_XML" (reference to XML template "Response_LineIn")</td><td align="left" valign="top">----</td><td align="left" valign="top">Will be exported</td><td align="left" valign="top">Will be exported</td></tr><tr><td align="left" valign="top"><span class="bold"><strong>FKC</strong></span> "Lah_3_11_wfs_write" with "Write_XML/XML_IA" (reference to XML template "Response_LineIn")</td><td align="left" valign="top">----</td><td align="left" valign="top">Will be exported</td><td align="left" valign="top">Will not be exported</td></tr><tr><td align="left" bgcolor="#00BF00" valign="top"> <span class="bold"><strong>FKC</strong></span> "dfn_3_95_read" with "ASAM result"</td><td align="left" valign="top">----</td><td align="left" valign="top">----</td><td align="left" valign="top">Will be exported</td></tr></tbody></table>

**Table 138. Filter Example**

  

The filtering of system names matches a filtering of objects. If "Service42" is specified as filter criteria for system names, then all function code objects will then by excluded from the export, that refer to XML templates that have this string in the name.

##### <a id="eu5export.editor.pruefsumme"></a>8.9.3.3. Checksum

After a successful export, the checksum for the export file will be displayed in the editor. The logic and purpose of using the checksum is to validate the data integrity of the exports, similar to the cooperation export (see [Section 8.11.7, “Export Check Sum”](8-11-7-export-check-sum.md "8.11.7. Export Check Sum")).

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="8-9-2-eu5-export-properties-display.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="8-9-eu5-export.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="8-10-plausibility-and-completeness-checks.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">8.9.2. EU5 Export Properties Display </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 8.10. Plausibility and Completeness Checks</td></tr></table>
