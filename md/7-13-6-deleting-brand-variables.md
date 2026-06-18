[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md) > [7.13. Brand Variables](7-13-brand-variables.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.13.6. Deleting Brand Variables</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-13-5-deactivating-activating-brand-variables.md">Prev</a> </td><th align="center" width="60%">7.13. Brand Variables</th><td align="right" width="20%"> <a accesskey="n" href="7-13-7-usage-locations-dialog.md">Next</a></td></tr></table>

---

#### <a id="markenvariable.loeschen"></a>7.13.6. Deleting Brand Variables

Brand variables can be deleted if they have the "deactivated" status and currently (meaning under consideration of all current working versions and all currently valid released versions) cannot be used by a function code object

##### <a id="markenvariable.loeschen.manuell"></a>7.13.6.1. Deleting Brand Variables Manually

Select one or more unused, deactivated brand variables and select the "Delete brand variable" entry in the context menu. After a confirmation prompt is confirmed, the brand variables will be permanently deleted.

##### <a id="markenvariable.loeschen.job"></a>7.13.6.2. Brand Variables Deletion Job

The management of the brand variable deletion jobs is controlled by the location administrator through the "brand variables job configuration editor" in the brand nodes of the brand variables navigator.

<a id="figure.markenvariable.loeschen.job"></a>

![Brand variable job configuration editor](images/markenvariablen_konfigurationseditor.png)

**Figure 332. Brand variable job configuration editor**

In the "brand variable job configuration editor", you can configure the job with author and location administrator rights. The job can be configured for each brand. If you deselect the "Deactivate job" checkbox, the job will be activated and will run at the times defined in the table. All unused, deactivated brand variables are permanently deleted at that time.

Up to five tuples of weekdays and times can be applied for the job start in the configuration. Individual tuples can be activated or deactivated. The order of tuples does not play a role, because it will use the chronological order of the activated entries for determining the next start time for the job.

Users, that only have the author role, can open the "brand variable job configuration editor" as read-only. This allows you to see the current configuration.

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-13-5-deactivating-activating-brand-variables.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="7-13-brand-variables.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="7-13-7-usage-locations-dialog.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">7.13.5. Deactivating/Activating Brand Variables </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 7.13.7. Usage Locations Dialog</td></tr></table>
