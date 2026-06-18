[ODIS Creator Help](odis-creator-help.md) > [5. ODIS Creator Administration Process](5-odis-creator-administration-process.md) > [5.2. Managing Master Data](5-2-managing-master-data.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">5.2.10. Additional Functions</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="5-2-9-user-management.md">Prev</a> </td><th align="center" width="60%">5.2. Managing Master Data</th><td align="right" width="20%"> <a accesskey="n" href="5-3-rights.md">Next</a></td></tr></table>

---

#### <a id="administration.weitere.funktionen"></a>5.2.10. Additional Functions

##### <a id="administration.weitere.funktionen.neukompilieren"></a>5.2.10.1. Recompiling all Function Tests

You can initiate the recompilation of function tests in the administration view with the **Recompile all function tests** menu item. You must be simultaneously assigned both roles of "author" and "location administrator" by different teams. This process may be necessary if a new test language was imported. To perform the function, you must also define an order context, in which the recompilation will be performed. After calling up the function, you must then select the brand in the following dialog that the recompilation should be performed for. In addition to the brands available based on your rights, there is always the **Without brand** item in the selection field. This is for the function tests that do not have a brand allocation yet. After initiating it, the other tasks will be performed in a background job on the ODIS Creator server. You will receive a notification when the job is complete.

After recompiling all function tests, a deployment should be done immediately. This makes sure that the EU5 export runs smoothly.

##### <a id="administration.weitere.funktionen.xml-templates.import"></a>5.2.10.2. Import XML Templates

You can initiate the import of XML templates with the **Import XML templates** menu item in the administration view. Similar to the required authorization for the "Recompiling all function tests" functionality, you must also be simultaneously assigned both roles of "author" and "location administrator" here. You can find additional information under [Section 7.12.1, “Importing XML templates”](7-12-1-importing-xml-templates.md "7.12.1. Importing XML templates")

##### <a id="administration.weitere.funktionen.dissexport"></a>5.2.10.3. Perform DISS Export

You can perform the DISS export with the **DISS export** menu item (see [Figure 55, “Start DISS Export”](5-2-10-additional-functions.md#figure.dissexport.menu "Figure 55. Start DISS Export")).

<a id="figure.dissexport.menu"></a>

![Image: start DISS export](images/dissexport.png)

**Figure 55. Start DISS Export**

It is determined in the following dialog ([Figure 56, “DISS Export Dialog”](5-2-10-additional-functions.md#figure.dissexport.dialog "Figure 56. DISS Export Dialog")) if an incremental DISS export or a full DISS export is taking place. The date for the selection of the provisions to be included for the DISS export is also determined.

<a id="figure.dissexport.dialog"></a>

![Image: DISS export dialog](images/dissexport_dialog.png)

**Figure 56. DISS Export Dialog**

Since the export for the languages is done at the same time, the recommended default value for the maximum amount of simultaneously running processes must not be exceeded to ensure that everything runs smoothly.

The export folder and the pattern for the export package is specified in the server configuration by the group administrator.

##### <a id="administration.weitere.funktionen.sscaexport"></a>5.2.10.4. Performing SSCA Export

You can perform the SSCA export with the **SSCA export** menu item (see [Figure 57, “Starting SSCA Export”](5-2-10-additional-functions.md#figure.sscaexport.menu "Figure 57. Starting SSCA Export")). The SSCA export loads the most current version of all function tests (across brands), generates Java code from there, and zips the result. If a working version of a function test already exists, it will be used for the export.

A file with a checksum for the results sip will also be created. See [Section 8.11.7, “Export Check Sum”](8-11-7-export-check-sum.md#export.pruefsumme).

Note: working versions of function tests can have an invalid status, where a Java code cannot be generated. Function tests in this status will be skipped.

<a id="figure.sscaexport.menu"></a>

![Image: starting SSCA export](images/sscaexport.png)

**Figure 57. Starting SSCA Export**

The save path and file name can be modified in the server configuration.

In the parameters dialog for the SSCA export ([Figure 58, “SSCA export dialog”](5-2-10-additional-functions.md#figure.sscaexport.dialog "Figure 58. SSCA export dialog")), you can selected if an export of all function test Java codes should be performed, or only the Java code for function tests that contain the “Java box” command.

<a id="figure.sscaexport.dialog"></a>

![Image: SSCA export dialog](images/sscaexport_dialog.png)

**Figure 58. SSCA export dialog**

Group administrators will receive notification after the export is completed.

##### <a id="administration.weitere.funktionen.userexport"></a>5.2.10.5. Perform User Export

You can export the list of all active and inactive users into a CSV file using the**Export user information** menu item or the **Export user list** button (see [Figure 59, “Start User Export”](5-2-10-additional-functions.md#figure.userexport "Figure 59. Start User Export")).

This action can only be performed by users with a Group administrator role. All other users do not have this option and the menu item cannot be selected.

After starting the action, the group administrator will be asked for a target folder for the export. The export file will be saved there in CSV format with the name ‘userExport\_>Date>\_>Time>.csv’. The group administrator will be informed with a message when the export is completed successfully.

<a id="figure.userexport"></a>

![Image: starting user export](images/userexport.png)

**Figure 59. Start User Export**

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="5-2-9-user-management.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="5-2-managing-master-data.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="5-3-rights.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">5.2.9. User Management </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 5.3. Rights</td></tr></table>
