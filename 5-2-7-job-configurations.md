[ODIS Creator Help](odis-creator-help.md) > [5. ODIS Creator Administration Process](5-odis-creator-administration-process.md) > [5.2. Managing Master Data](5-2-managing-master-data.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">5.2.7. Job Configurations</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="5-2-6-location-data.md">Prev</a> </td><th align="center" width="60%">5.2. Managing Master Data</th><td align="right" width="20%"> <a accesskey="n" href="5-2-8-server-configuration.md">Next</a></td></tr></table>

---

#### <a id="administration.jobkonfig"></a>5.2.7. Job Configurations

The **job configuration** entry in the master data navigator ([2](5-2-managing-master-data.md#figure.stammdatennavigator "Figure 47. Master Data Navigator")) is managed by the administrators.

<a id="table.administration.jobkonfig"></a>

<table border="1" summary="Job Configuration"><colgroup><col align="left"/><col align="left"/></colgroup><thead><tr bgcolor="#EEEEEE"><th align="left"><span class="bold"><strong>Data</strong></span></th><th align="left"><span class="bold"><strong>Description</strong></span></th></tr></thead><tbody valign="top"><tr><td align="left" valign="top">Job monitor<a class="indexterm" name="d4e1906"></a></td><td align="left" valign="top">In this editor the administrator can see which jobs are currently running from ODIS Creator on the server and how much time is potentially needed until the end of the process. Only the information for the editing and import of control module descriptions are currently displayed.</td></tr><tr><td align="left" valign="top">P-Differ Export<a class="indexterm" name="d4e1912"></a></td><td align="left" valign="top">The administrator can configure the parameters for a P-differ export in this editor.</td></tr><tr><td align="left" valign="top">Mass Data Translation Job<a class="indexterm" name="d4e1918"></a></td><td align="left" valign="top">The group administrator can configure the mass data translation job in this editor (see <a class="xref" href="6-4-6-translation-jobs.md#massendaten_job" title="6.4.6.2. Mass Data Translation Job">Section 6.4.6.2, “Mass Data Translation Job”</a>).</td></tr><tr><td align="left" valign="top">Editorial Translation Job<a class="indexterm" name="d4e1925"></a></td><td align="left" valign="top">The group administrator can configure the company-wide editorial translation job in this editor (see <a class="xref" href="6-4-6-translation-jobs.md#redaktioneller_job_standortuebergreifend" title="6.4.6.1.1. Cross-Location Editorial Translation Job">Section 6.4.6.1.1, “Cross-Location Editorial Translation Job”</a>).</td></tr><tr><td align="left" valign="top">GOCAT inquiry interval<a class="indexterm" name="d4e1932"></a></td><td align="left" valign="top">In this editor, the interval for the GOCAT inquiry can be set per location. The default value is one hour and it must be at least 10 minutes.</td></tr><tr><td align="left" valign="top">Tool Lists Export<a class="indexterm" name="d4e1938"></a></td><td align="left" valign="top">The automated tool list export can be configured in this editor.</td></tr></tbody></table>

**Table 18. Job Configuration**

  

##### <a id="p.differ"></a>5.2.7.1. P-Differ Export

In the administrator view, the **P-differ editor** ([Figure 52, “P-Differ Editor”](5-2-7-job-configurations.md#p.differ.export "Figure 52. P-Differ Editor")) can be opened through an entry in the **master data navigator** ([2](5-2-managing-master-data.md#figure.stammdatennavigator "Figure 47. Master Data Navigator")) for the configuration of automatic P-differ exports [to be edited](3-2-5-editor.md "3.2.5. Editor").

<a id="p.differ.export"></a>

![Image: P-differ editor](images/p-differ-export.png)

**Figure 52. P-Differ Editor**

The **location** is selected in the upper [selection field](2-2-general-definitions-and-glossaries.md#auswahlfeld) in the P-differ editor. All locations are offered to the group administrator for selection. The location administrator is only offered the locations they are responsible for. If an export job has already been previously configured for a selected location, then the corresponding values are displayed in the editor.

So that the export can be started automatically with the displayed configuration, the [checkbox](2-2-general-definitions-and-glossaries.md#kontrollfeld) in front of "automatic export" must be activated. If the checkbox is deactivated, then the displayed export job is deactivated.

To control the time of the export, the days of the week and the time for the automatic creation can be selected. The P-Differ export is then started every week on each of the selected days at the specified time. If no day of the week is selected, the automatic P-Differ export will be deactivated when saving.

Which object status should be exported is determined by enabling the corresponding [checkboxes](2-2-general-definitions-and-glossaries.md#kontrollfeld).

Changes to the configuration will only be saved for the location that is currently selected.

##### <a id="gocat-abfrage"></a>5.2.7.2. GOCAT inquiry interval

In the administrator view, the **GOCAT inquiry interval editor** ([Figure 53, “GOCAT Inquiry Interval Editor”](5-2-7-job-configurations.md#gocat-abfrage.editor "Figure 53. GOCAT Inquiry Interval Editor")) to configure the interval at which information from GOCAT is accessed, can be opened [for editing](3-2-5-editor.md "3.2.5. Editor") through an entry in the **master data navigator** ([2](5-2-managing-master-data.md#figure.stammdatennavigator "Figure 47. Master Data Navigator")).

<a id="gocat-abfrage.editor"></a>

![Image: GOCAT inquiry interval editor](images/gocat_abfrage_editor.png)

**Figure 53. GOCAT Inquiry Interval Editor**

The **location** is selected in the upper [selection field](2-2-general-definitions-and-glossaries.md#auswahlfeld) in the GOCAT inquiry interval editor. All locations are offered to the group administrator for selection. The location administrator is only offered the locations they are responsible for.

The interval will be given underneath in hours (from 0 to 23) and minutes (from 0 to 59).

##### <a id="werkzeugliste"></a>5.2.7.3. Tool Lists Export

In the administrator view, the **tool lists export editor** ([Figure 54, “Tool Lists Export Editor”](5-2-7-job-configurations.md#werkzeuglisten.export "Figure 54. Tool Lists Export Editor")) can be opened through an entry in the **master data navigator** ([2](5-2-managing-master-data.md#figure.stammdatennavigator "Figure 47. Master Data Navigator")) to configure the automatic tool lists export [for editing](3-2-5-editor.md "3.2.5. Editor").

<a id="werkzeuglisten.export"></a>

![Image: tool lists export editor](images/werkzeuglisten-export.png)

**Figure 54. Tool Lists Export Editor**

The following settings can be applied by the group administrator:

- Storage folder
- Schedule settings

A valid path to a folder on the server must be specified for the storage folder, in which the files created during the automatic and manual tool lists export process are stored. While saving the configuration, it checks if the input field has been populated and if the specified folder exists on the server.

Because the storage folder is also required for the manual implementation of jobs, the configuration must be edited before the first request for manual implementation. Automatic implementation can be blocked with the "Disable automatic tool list creation" [checkbox](2-2-general-definitions-and-glossaries.md#kontrollfeld).

If the "Disable automatic tool list creation" checkbox has not been selected, the "used tools analysis" job will start according to the specifications in the schedule.

The batch jobs implementation process is displayed on the server in the job monitor.

Notifications are not generated after the automatic implementation of the "used tools analysis" job is complete. Exception: if this type of job is already running during an automatic start, the start is canceled and a notification is generated.

###### <a id="werkzeugliste.manuell"></a>5.2.7.3.1. Manual Tool Lists Export

Group administrators or location administrators have the option to start the tool lists export manually. There is a button in the tool bar for this and also a menu item in the menu **File > Used tools analysis**.

When the function is selected, a new "used tools analysis job" is created without further confirmation; it is then started in the server asynchronously by the batch job scheduler within the next several minutes. This will be indicated with a corresponding message. Before creating a new job, ODIS Creator checks if this type of job is already running. If this is the case, a message will appear and a new job will not be created. A new job can start only when the currently running job has finished.

The user can work without limitations in the ODIS Creator system while the job is being performed. The user can monitor the progress of the asynchronous execution of the batch job on the server in the job monitor.

After the batch job is complete, a notification is created in the "order" structure node with the final status (successful or unsuccessful) of the running job. The notification is sent to all teams with the "group administrator" or "location administrator" roles, where the user, who initiated the job, belongs.

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="5-2-6-location-data.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="5-2-managing-master-data.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="5-2-8-server-configuration.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">5.2.6. Location Data </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 5.2.8. Server Configuration</td></tr></table>
