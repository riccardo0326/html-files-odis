[ODIS Creator Help](odis-creator-help.md) > [8. ODIS Creator Preparation Process](8-odis-creator-preparation-process.md) > [8.1. Production Baselines](8-1-production-baselines.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">8.1.4. Create and Edit a Production Baseline</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="8-1-3-production-baseline-editor.md">Prev</a> </td><th align="center" width="60%">8.1. Production Baselines</th><td align="right" width="20%"> <a accesskey="n" href="8-2-production-settings.md">Next</a></td></tr></table>

---

#### <a id="baseline.produktiv.erstellen"></a>8.1.4. Create and Edit a Production Baseline

Create a new production baseline in the production baseline browser context menu using the menu item **Create baseline** or **Insert > Baseline** in the selection menu. You have the option in the production baseline editor to enter an optional comment, and to select the respective brand and the type of production baseline. If the full type is selected, the base production baseline input field remains empty; for incremental baselines, the base baseline will be automatically set to the most recent production baseline and will not be able to be changed (full or incremental). The default type is **incremental**.

The **comments** field in the saved production baselines can be changed later.

The name of the production baseline is automatically determined by the system. If available, the specifications for the automatic generation of the production baseline descriptions for this brand will be used here (see [Figure 606, “Specifications for Automatic Creation”](8-2-2-configuration-editor.md#figure.produktiv.baseline.konfig.editor2 "Figure 606. Specifications for Automatic Creation")). If no corresponding specifications are set, then the baseline version number and its name will be automatically applied.

The other fields will be applied from the configuration, if available. The data can be edited from the following fields: market name, TFD (tool-supported vehicle database) baseline, exclusion list, unauthorized DTC memory entries and evaluation factors for verification calculation.

##### <a id="baseline.erstellen.inkrement"></a>8.1.4.1. Characteristics of Incremental Production Baselines

- The current condition of rebuilt data for a brand can be obtained by using the base production baseline (1.0.0) and all of the incremental production baselines following it. Therefore it is irrelevant whether additional full production baselines are given in the meantime.
- When rebuilding a full production baseline, an incremental production baselines is always automatically rebuilt as well. This incremental production baseline contains all changes between the full production baseline just rebuilt and the last successfully rebuilt production baseline (incremental or full) prior to that. This is important to ensure the continuity of the incremental production baselines in relation to the entire database of a brand.
- When rebuilding incremental production baselines, it is possible that no changes occurred in the database for a brand since the last successfully rebuilt production baseline. If this is the case, then the production baseline has the ['**Empty**'](8-6-5-an-incremental-baseline-is-not-required.md "8.6.5. An incremental baseline is not required") status.

##### <a id="baseline.auftragsdatei"></a>8.1.4.2. Order File

The update creator tool documents the data preparation progress in a status file while processing an order file created by ODIS Creator. The status file is located in the same folder as the applicable order file. The update creator tool logs the data preparation progress in one or more log files while processing an order file created by ODIS Creator. These log files are located in a sub-folder with the name 'log' of the folder of the applicable order file. To allocated the log files to the respective order, they will be stored in a sub-folder of the 'log' folder. This sub-folder has the name of the order as the folder name.

If you open or update the baseline view, the status of the data preparation (based on the generated status file) is requested through the update creator tool for all production baselines which already have an order file for the update creator tool. The determined status is displayed in the baseline browser through the icons. This is differentiated based on the icons if the baseline is just processed in ODIS Creator or in the update creator tool.

##### <a id="baseline.korrektur"></a>8.1.4.3. Revised Baseline

A revised baseline references a full or incremental production baseline. The database of the prepared diagnostic data from ODIS Creator does not change. Only updated vehicle data and/or an updated exclusion list are prepared. You can select a more current version for a TFD baseline for the generation of the baseline. The selection of an updated exclusion list is optional. As long as no new exclusion list was selected for the file selection dialog, the file name of the exclusion list of the referenced production baseline is displayed by default. The version number of a revised baseline is identical to the version number of the referenced full or incremental production baseline.

When creating the revised baseline, the market name is filled with the value that was entered when creating the production baseline. Similar to the release of production baselines, this value is displayed as read-only and cannot be changed. The market name field is also displayed as read only when the revised baseline is released.

No new data will be exported for the preparation of a revised baseline. Only one new order file for the update creation tool is created with the new updated component versions. The order file is stored in the folder, in which the data of the referenced production baseline is already located. The order files have the date and time in the file names similar to the example instances in the materials. With this, the order file of the referenced production baseline will remain the same and will not be overwritten. If a new exclusion list was selected for the revised baseline; this will be rebuilt when preparing the baseline in the "Exclusion\_List" subfolder of the folder, in which the order file for the update creator tool is saved. The sub-folder "Exclusion\_List" already contains a file with the name of the updated exclusion list, the old file is renamed (old name plus more up-to-date time stamp). The same applies if a new list is selected for "Unauthorized DTC memory entries" or "evaluation factors for verification calculation" for the revised baseline. The new list is archived in the folder "DTC\_Exclusion" or "DTC\_Factors" in a folder with the current time stamp.

For a baseline that has the status **externally canceled** or **external error** (see [Section 8.6, “Baseline Status”](8-6-baseline-status.md "8.6. Baseline Status")), the external preparation can be initiated again by creating a revised baseline. The creation of revised baselines is offered for the production baseline currently released in the market as well as for all production baselines which a market release can still be issued for.

##### <a id="baseline.freigabe.baseline"></a>8.1.4.4. Releasing a Production Baseline

After the tests of one of the production baselines deployed on the pre-release platform have been successfully completed, the production baseline will be released for the market on MirrorServer/2. This market release occurs through the update creator tool. The order file for this market release is generated by ODIS Creator, if you open the release function for the applicable baseline. The release function of a production baseline is available for the following types:

- Full production
- Incremental production
- Vehicle data production

The function can be accessed either through the menu or context menu of the baseline browser. To do this, select the desired production baseline and select **Release**. When released, the market name is given the value that was entered when it was created. The value is displayed as read-only and cannot be changed.

The following conditions apply for the release of a production baseline:

- The user can release full and incremental production baselines only then on the mirror server/2, if they have a higher version number than the last released production baseline in the respective brand.
- The user can release revised baselines only then on the mirror server/2, if they have a higher or the same version number as the last released production baseline in the respective brand.
- For the same version numbers of revised baselines, the user can only release the newest revised baseline to the mirror server/2 based on the date.

When preparing a full production baseline, ODIS Creator also creates an incremental baseline automatically in addition to the full production baseline. The following additional conditions apply relating to the release for the automatically generated incremental production baselines:

- The user cannot release incremental baselines, that were automatically created for a full baseline.
- If the user releases a full baseline, then the ODIS Creator system may not release the increment for this full baseline.

##### <a id="baseline.sperren.baseline"></a>8.1.4.5. Locking a Production Baseline

In addition to the release of a production baseline, you also have the option to lock a baseline. This is necessary to ensure that false data does not enter the market. A disabled baseline can no longer be released. To lock a production baseline, select the desired production baseline and select the **Lock** menu item.

The criteria for locking a production baseline are the following:

- The baseline must have one of the following statuses (see [Section 8.6, “Baseline Status”](8-6-baseline-status.md "8.6. Baseline Status")) in order to be disabled.

  - Externally Created
  - In external processing
  - Externally Canceled
  - External Error
  - Externally Completed
- The user can disable all baselines that have not yet been released.
- The user cannot disable incremental baselines, that were created automatically for a full baseline.
- If the user locks a full baseline, then the incremental production baseline automatically created will not be locked.

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="8-1-3-production-baseline-editor.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="8-1-production-baselines.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="8-2-production-settings.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">8.1.3. Production Baseline Editor </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 8.2. Production Settings</td></tr></table>
