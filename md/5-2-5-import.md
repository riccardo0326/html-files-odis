[ODIS Creator Help](odis-creator-help.md) > [5. ODIS Creator Administration Process](5-odis-creator-administration-process.md) > [5.2. Managing Master Data](5-2-managing-master-data.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">5.2.5. Import</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="5-2-4-creating-a-brand.md">Prev</a> </td><th align="center" width="60%">5.2. Managing Master Data</th><td align="right" width="20%"> <a accesskey="n" href="5-2-6-location-data.md">Next</a></td></tr></table>

---

#### <a id="administration.import"></a>5.2.5. Import

The **Import** entry in the master data navigator ([2](5-2-managing-master-data.md#figure.stammdatennavigator "Figure 47. Master Data Navigator")) is used for the import of **master component lists**, **reference tables**, , **VWG reference tables**, **LT3 text tables**, the **measured value standard display**, **tool lists**, **control module parameter mapping**, **TimeMeasurementExclusion**, **DSGVO match word list**, **Cyclone text tables**, **VFA reference tables**, **HV module characteristic curves** and **config.ini (operating system).** The group administrator manages the import.

In addition to the data type, the current version of the imported database, the timestamp for the last import, and the user who performed the import are displayed in the [editor](3-2-5-editor.md "3.2.5. Editor") (for example, for a reference table import). Furthermore, there is the option to display an **import log**.

<a id="figure.referenztabellen.importieren"></a>

![Image: "Reference table” import editor](images/administration_referenztabellen_importieren.png)

**Figure 49. "Reference Table” Import Editor**

The **Import new...** [button](2-2-general-definitions-and-glossaries.md#schaltflaeche) starts the import of the selected data. It will open a dialog to select an import file. By selecting an import file, the import of the contained data will start.

##### <a id="administration.mutterlistenimport"></a>5.2.5.1. Master Components List Import

When importing master components lists, the length and language of the master component terms are checked. If the master component term is too long, the group administrator receives a notification for each master component term that was shortened during the import. The maximum length for a master component term is 330 bytes.

If a language code is in the master components list, that is not included in the ODIS Creator, then the group administrator will also receive a notification with the unknown language code.

##### <a id="administration.lt3texttabellen"></a>5.2.5.2. LT3 text tables

The import of LT3 text tables for the Crafter runs separately from the group data. There are no correlations or dependencies between the imports. The fault location objects generated from the LT3 table are listed under the "Crafter" structure node.

The version of the structure file and the associated text file will be verified during the import. If they match, then the import can be performed. If they do not match, then a corresponding message will be given in the import log and the import will be canceled.

Another test will check if only files with the DTC\_Table\_S\_Crafter format are included in the TableConfig.xml. If these conditions are not met, the import will be canceled correspondingly.

##### <a id="administration.cyclonetexttabellen"></a>5.2.5.3. Cyclone text tables

The import of Cyclone text tables for Cyclone runs separately from the group data. There are no correlations or dependencies between the imports. The fault location objects generated from the Cyclone table are listed under the "Cyclone" structure node. Fault location objects that cannot be allocated in the corresponding subfolders in the “Cyclone” structure nodes according to the P/U/B/C codes will be assigned to the separate “PUBC” collective folder in the “Cyclone” structure nodes.

The version of the structure file and the associated text file will be verified during the import. If they match, then the import can be performed. If they do not match, then a corresponding message will be given in the import log and the import will be canceled.

Another test will check if only files with the DTC\_Table\_S\_Cyclone format are included in the TableConfig.xml. If these conditions are not met, the import will be canceled correspondingly.

##### <a id="administration.referencetabellen.vfa"></a>5.2.5.4. VFA Reference Tables

The import of VFA reference tables runs separately from group data. There are no correlations or dependencies between the imports. The fault location objects generated from the VFA reference tables are listed under the "Cyclone" structure node. Fault location objects that cannot be allocated in the corresponding subfolders in the “Cyclone” structure nodes according to the P/U/B/C codes will be assigned to the separate “PUBC” collective folder in the “Cyclone” structure nodes.

The version of the structure file and the associated text file will be verified during the import. If they match, then the import can be performed. If they do not match, then a corresponding message will be given in the import log and the import will be canceled.

Another test will check if only files with the DTC\_VFA format are included in the TableConfig.xml. If these conditions are not met, the import will be canceled correspondingly.

##### <a id="administration.messwertnormanzeige"></a>5.2.5.5. Measured value default display

When importing the **measured value default display**, each user is responsible for making sure that the file to be imported matches the schema. ODIS Creator does not perform a schema check.

##### <a id="administration.werkzeugliste"></a>5.2.5.6. Tool list

The tool lists import is performed in the following order:

- Consistency check

  If inconsistencies are detected when checking the XML file for conformity to the XML schema werkzeugliste.xsd, an error message will appear and the import will be canceled.
- Tool list import

  The import is done asynchronously in the server. The user can continue to work with the ODIS Creator system without limitations.
- Logging

  The import is logged in the import log the same as the usual group data imports. The import log of the last completed tool lists import can be displayed with the "Display import log" button.

The data processing is displayed in the status bar with a status message and a progress indicator. After the import is complete, a notification in the "order" structure node with the status of the running job is displayed.

If the tool lists contains a language that is not available in ODIS Creator, this will not be imported and the group administrator will receive a notification about the issue.

The tool list version, which was used during the last import, will also be displayed in the editor for the tool list import.

##### <a id="administration.dsgvoimport"></a>5.2.5.7. DSGVO match word list

The match word list can be edited in OC. When saving, an import for the DSGVO consistency check is executed asynchronously in the server. The user can continue to work with the ODIS Creator system without limitations.

The match words must be separated in the editor by line breaks and/or semi-colons.

##### <a id="administration.sgparametermappingimport"></a>5.2.5.8. Control Module Parameter Mapping

The Control Module Parameter Mapping import is performed in the following order:

- Consistency check

  If inconsistencies are detected when checking the XML file (MapUDSReqRespParameter.xml) for conformity to the XML schema MapUDSReqRespParameter.xsd, an error message and the result from the check will appear and the import process will be canceled.
- Import of Control Module Parameter Mapping

  The import is done asynchronously in the server. The user can continue to work with the ODIS Creator system without limitations.
- Logging

  The import is logged in the import log the same as the usual group data imports. The import log of the last completed Control Module Parameter Mapping list import can be displayed with the "Display import log" button.

In addition to the import function, there is also an export function here. The export process exports the Control Module Parameter Mapping that was last imported to a desired location as an XML file. The default name for the XML file is MapUDSReqRespParameter.xml.

##### <a id="administration.timemeasurementexclusion"></a>5.2.5.9. TimeMeasurementExclusion

The TimeMeasurementExclusion import is performed in the following order:

- Consistency check

  If inconsistencies are detected when checking the XML file for conformity to the TimeMeasurementExclusion.xsd XML schema, an error message and the result from the check will be displayed temporarily in the log window (until the editor is closed) and the import process will be canceled.
- Content check

  The import process for the “TimeMeasurementExclusion” will be canceled, an error message will be displayed, and the result will be logged temporarily in the import log if

  - The function code is not present in the OC database

  - The brand allocation of the function code in the OC does not match the brand allocation of the function code in the “TimeMeasurementExclusion” XML file

  - The brand is not present in the OC database
- Import of TimeMeasurementExclusion

  The import is done asynchronously in the server. The user can continue to work with the ODIS Creator system without limitations.
- Logging

  The import is logged in the import log the same as the usual group data imports. The import log of the last completed TimeMeasurementExclusion import can be displayed with the "Display import log" button.

The data processing is displayed in the status bar with a status message and a progress indicator.

##### <a id="administration.hvmodulkennlinien"></a>5.2.5.10. HV module characteristic curves

When importing the HV module characteristic curves, a synchronous REST-API request is made to the Bitbucket repository set up in the server configuration. All commits and their version information (tag version and commit date) of the XML file for HV modules are read out and displayed in the dialog "Adopt version number of HV module characteristic curves” (see [Figure 50, “Dialog - Adopt the version number of the HV module characteristic curves”](5-2-5-import.md#figure.hv.modul "Figure 50. Dialog - Adopt the version number of the HV module characteristic curves")).

<a id="figure.hv.modul"></a>

![Figure: Dialog - Adopt the version number of the HV module characteristic curves](images/administration_hv_modul_kennlinien.png)

**Figure 50. Dialog - Adopt the version number of the HV module characteristic curves**

The user can select a tag version so that this is played out for provisions (production [complete and incremental], rollout, correction of the production or rollout baseline) in the order file.

##### <a id="administration.osconfigini"></a>5.2.5.11. config.ini (Operating System)

When importing the config.ini (operating system) file, a synchronous REST-API request is made to the Bitbucket repository set up in the server configuration. All commits and their version information (tag version and commit date) of the file for config.ini (operating system) are read out and displayed in the dialog "Tag (version) name” (see [Figure 51, “Tag (Version) Name Dialog”](5-2-5-import.md#figure.os.configini "Figure 51. Tag (Version) Name Dialog")).

<a id="figure.os.configini"></a>

![Image: Tag (Version) Name Dialog](images/administration_os_config_ini.png)

**Figure 51. Tag (Version) Name Dialog**

The user can select a tag version so that this is played out for provisions (production [complete and incremental], rollout, correction of the production or rollout baseline) in the order file.

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="5-2-4-creating-a-brand.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="5-2-managing-master-data.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="5-2-6-location-data.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">5.2.4. Creating a Brand </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 5.2.6. Location Data</td></tr></table>
