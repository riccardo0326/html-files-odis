[ODIS Creator Help](odis-creator-help.md) > [5. ODIS Creator Administration Process](5-odis-creator-administration-process.md) > [5.4. Importing Control Module Descriptions](5-4-importing-control-module-descriptions.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">5.4.1. Initiating the Import of Control Module Descriptions</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="5-4-importing-control-module-descriptions.md">Prev</a> </td><th align="center" width="60%">5.4. Importing Control Module Descriptions</th><td align="right" width="20%"> <a accesskey="n" href="5-4-2-control-module-import-phases.md">Next</a></td></tr></table>

---

#### <a id="sgbimport.start"></a>5.4.1. Initiating the Import of Control Module Descriptions

The control module import element is in the administration view. You will see the view there as in [Figure 65, “Control module import view”](5-4-importing-control-module-descriptions.md#figure.sgbimport.navigator "Figure 65. Control module import view"). In the control module import navigator, you can initiate a new order for a control module description import via the entry **"New control module import"**. This entry is also in the global menu under **"Insert"**.

The import configuration editor opens like in [Figure 66, “Control Module Import Editor”](5-4-1-initiating-the-import-of-control-module-descriptions.md#figure.sgbimport.editor "Figure 66. Control Module Import Editor"). There you can assign a name to your import. This is set with the variables **<Brand>\_<Date>\_<Time>** by default, as it is also used in the allocation (see [Section 8.2, “Production Settings”](8-2-production-settings.md "8.2. Production Settings")). You can however also adjust the names to your needs. In the comments text field, you must insert additional information for the import.

<a id="figure.sgbimport.editor"></a>

![Control Module Import Editor](images/sgbimporteditor.png)

**Figure 66. Control Module Import Editor**

If you are the location administrator for more than one brand, then you have the option to select one of the brands assigned to you in the brand selection field. Select in the **"Import type"** selection field, if the import is importing objects that have the "approved" status or the "in processing" status. The effects of these types of imports are described under [Section 7.7.8, “Using Control Module Descriptions”](7-7-8-using-control-module-descriptions.md "7.7.8. Using Control Module Descriptions").

The site administrator can only import VRT/VPT files by activating the “Import exclusively for VRT/VPT” checkbox. The import can be carried out simultaneously with other ongoing control module imports, provided that no other import is running for the selected brand. First, the integrity of the VRT/VPT files to be imported is checked. The checksum from the VRTVPT.properties file, which can be found alongside the other import files, is used for this. If the import is successful, the VRT/VPT files and the VRTVPT.properties file are deleted from the import directory. If the verification fails, the import is canceled with an error message and registered in the log file (phase\_check\_error.log). The control module import is still carried out up until this point if the checkbox is not activated.

You also have the option to switch off either the relationship processing phase or the check in the relationship processing by selecting the “Deactivate relationship processing phase” or “Deactivate relationship processing check” checkbox. The checkboxes are mutually exclusive, so only one can be selected. When the “Deactivate relationship processing check” checkbox is selected, the properties "DISABLE\_ECU\_CHECK\_AT\_EQN\_FOR\_BRANDS", "DISABLE\_ECU\_CHECK\_AT\_DGO\_FOR\_BRANDS" and "DISABLE\_ECU\_CHECK\_AT\_FKC\_FOR\_BRANDS" from the vaudes\_server.properties are overridden and all relevant relationships are rewritten to new control module versions after the import. When the “Deactivate relationship processing phase” checkbox is selected, existing relationships to old control module versions will be kept after the import.

A vehicle description file (input baseline) is required for the control module import. If it is not available when the import starts, the import will be canceled.

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="5-4-importing-control-module-descriptions.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="5-4-importing-control-module-descriptions.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="5-4-2-control-module-import-phases.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">5.4. Importing Control Module Descriptions </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 5.4.2. Control Module Import Phases</td></tr></table>
