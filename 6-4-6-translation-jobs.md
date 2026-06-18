[ODIS Creator Help](odis-creator-help.md) > [6. ODIS Creator Order Management Process](6-odis-creator-order-management-process.md) > [6.4. Translation](6-4-translation.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">6.4.6. Translation Jobs</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="6-4-5-commissioning-translations-manually.md">Prev</a> </td><th align="center" width="60%">6.4. Translation</th><td align="right" width="20%"> <a accesskey="n" href="6-4-7-translation-packages.md">Next</a></td></tr></table>

---

#### <a id="uebersetzungsjobs"></a>6.4.6. Translation Jobs

The translation package includes two jobs, the **Editorial** and the **Mass data translation job**.

The editorial translation job includes the normal translation, that is triggered by the risk release or a link between editorial objects.

The mass data translation job is triggered by the link from new markets or new languages to markets on the equipment network. It is important here that the translation requirements for the mass data cannot be viewed on the interface.

The translation jobs can be individually deactivated and activated for every configuration. If all day-time entries are marked as inactive for a configuration, then the affiliated translation job is automatically deactivated. The visible job status in the configuration remains unaffected by this.

##### <a id="redaktioneller_job"></a>6.4.6.1. Editorial Translation Job

The management of the editorial translation job is controlled by the [translation coordinator](3-3-1-description-of-roles.md "3.3.1. Description of Roles"). In the translation view, the editorial translation job can be set in the translation parameters. There is an extra tab in the editor for this (see [Figure 158, “Managing Location-Specific Editorial Translation Jobs”](6-4-6-translation-jobs.md#figure.auftragsverwaltung.uebersetzung.redaktionellerJob "Figure 158. Managing Location-Specific Editorial Translation Jobs")). You have the option to use the cross-location configuration or the location-specific configuration.

<a id="figure.auftragsverwaltung.uebersetzung.redaktionellerJob"></a>

![Image: managing location-specific editorial translation jobs](images/uebersetzungsparameter_redaktionellerJob.jpg)

**Figure 158. Managing Location-Specific Editorial Translation Jobs**

As the translation coordinator, you will see the status for the editorial translation job. The status can assume one of the following values:

- Active: used default configuration
- Active: used location configuration
- Active: job is being performed
- Inactive: editorial translation job is discontinued

Up to five tuples of weekdays and times can be applied for the job start in the configuration. Every tuple can be activated or deactivated. When calculating the next start time of the editorial translation job, only the active configurations are considered.

In addition to the configuration, the translation coordinator can also manually start the editorial translation job. This function can be started through the global menu or the button. After confirming the action, you can select the desired location where the job should start, if multiple locations are assigned.

###### <a id="redaktioneller_job_standortuebergreifend"></a>6.4.6.1.1. Cross-Location Editorial Translation Job

The cross-location configuration (see [Figure 159, “Managing Cross-Location Editorial Translation Jobs”](6-4-6-translation-jobs.md#figure.auftragsverwaltung.uebersetzung.redaktionellerJob_admin "Figure 159. Managing Cross-Location Editorial Translation Jobs")) is done by the group administrator in the administration. For the configuration, there are likewise five tuples available to the group administrator of week days and times to execute the job. All adaptations are made across locations, as long as no location uses their own configurations.

<a id="figure.auftragsverwaltung.uebersetzung.redaktionellerJob_admin"></a>

![Image: managing cross-location editorial translation jobs](images/administration_redaktionellerJob.jpg)

**Figure 159. Managing Cross-Location Editorial Translation Jobs**

You also have the option in the editor to see the job status for every location. The status can assume one of the following values:

- Active: used default configuration
- Active: used location configuration
- Active: job is being performed
- Inactive: editorial translation job is discontinued

The status is not automatically updated when there are changes in the dialog. The update only occurs when the dialog opens.

Deactivating the editorial translation job can also be done here. However, this is then valid system-wide, thus for all locations. Jobs already started will be finished and not canceled.

##### <a id="massendaten_job"></a>6.4.6.2. Mass Data Translation Job

The mass data translation job is managed by the [group administrator](3-3-1-description-of-roles.md "3.3.1. Description of Roles") in the administration (see [Figure 160, “Managing the Mass Data Translation Job”](6-4-6-translation-jobs.md#figure.auftragsverwaltung.uebersetzung.massendatenJob "Figure 160. Managing the Mass Data Translation Job")).

<a id="figure.auftragsverwaltung.uebersetzung.massendatenJob"></a>

![Image: managing mass data translation job](images/administration_massendatenJob.jpg)

**Figure 160. Managing the Mass Data Translation Job**

As the group administrator, you can apply the mass data translation job configuration across locations as well as to individual locations. You have the option in the editor to select the location through a selection field. For every location, you can then select one of the following options.

- Deactivate job for this location
- Use cross-location configuration
- Use location-specific configuration

Up to five tuples of weekdays and times can be applied for the job start in the configuration. Individual tuples can be activated or deactivated. The order of tuples does not play a role, because it will use the chronological order of the activated entries for determining the next start time for the mass data translation job.

It can also be seen in the editor, what the status of the mass data translation job is for each location. The status can be one of the following values:

- Active: used default configuration
- Active: used location configuration
- Active: job is being performed
- Inactive: mass data translation job is discontinued

Deactivating the mass data translation job can also be done here. However, this is then valid system-wide, thus for all locations.

To be able to respond flexibly to requests, there is the option to manually start the mass data translation job for a location. This can be done using the global menu or through a button. After confirming the action, you can select the desired location where the job should start, if multiple locations are assigned.

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="6-4-5-commissioning-translations-manually.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="6-4-translation.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="6-4-7-translation-packages.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">6.4.5. Commissioning Translations Manually </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 6.4.7. Translation Packages</td></tr></table>
