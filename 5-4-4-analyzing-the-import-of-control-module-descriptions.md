[ODIS Creator Help](odis-creator-help.md) > [5. ODIS Creator Administration Process](5-odis-creator-administration-process.md) > [5.4. Importing Control Module Descriptions](5-4-importing-control-module-descriptions.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">5.4.4. Analyzing the Import of Control Module Descriptions</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="5-4-3-observing-the-import-of-control-module-descriptions.md">Prev</a> </td><th align="center" width="60%">5.4. Importing Control Module Descriptions</th><td align="right" width="20%"> <a accesskey="n" href="5-4-5-checking-the-input-baseline-for-the-control-module-import.md">Next</a></td></tr></table>

---

#### <a id="sgbimport.analyse"></a>5.4.4. Analyzing the Import of Control Module Descriptions

When the control module import ends, the location administrator team, the group administrator team, and the user who started the import will receive a notification about the end of the import in the order management.

If the import is canceled with an error message, the vehicle project subfolders and the vehicle description file will not be deleted.

Various log files generate when importing control module descriptions. After the import has completed (see [Figure 65, “Control module import view”](5-4-importing-control-module-descriptions.md#figure.sgbimport.navigator "Figure 65. Control module import view")), these can be examined through the "Log" interface in the editor or saved in a user-defined folder through the "Download log" interface. The log files are located in the selected folder within the "ecuimportlog.zip" file.

There are the following types of log files:

- ecuimport\_error\_log: contains any errors that occurred during the import.
- ecuimport\_phase\_check\_error\_log: Contains errors that occurred during the import while verifying the checksum.
- ecuimport\_phase\_vpt\_vrt\_error\_log: Contains errors that occurred during the import while importing the VRT/ VPT.
- ecuimport\_phase\_import\_vehicle\_project\_error\_log: Contains the errors that occurred while importing control module extracts.
- ecuimport\_phase\_import\_vehicle\_project\_general\_log: Contains the progress information that occurred during the import of control module extracts.
- phase\_relation\_obj\_error\_log: Contains the errors that occurred while importing control module extracts.
- ecuimport\_phase\_relation\_obj\_error\_log: Contains the progress information that applies during relationship processes of editorial objects.
- ecuimport\_general\_log: contains the progress information that occurred during the import.
- ecuimport\_statistics\_log: contains the time and quantity information that accrued during the import.
- ecuimport\_ecuupdate\_warnings\_log: contains any accrued problems during the update of usage locations for control module descriptions. All editorial objects are listed which contain incompatibilities to the control module extracts.

If an automatic update is not possible due to incompatibilities, then a notification regarding the entry in the log file ecuimport\_ecuupdate\_warnings\_log will also be sent to the team responsible for the respective editorial object. New entries are also created in the consistency check log and in the problems tab for function code entries, as well as for the version being edited (if existing) and for the last risk-released version.

The following exceptions apply to editorial objects, which do not have the migration protection flag:

- No notifications are created.
- No new entries are created in the consistency check logs.
- No new entries in the Problems tab are created for function codes.

The following rules apply to editorial objects, for which the control module description could be replaced by the new imported version of the control module description:

- There is no notification.
- No new entries are added to the consistency check log.
- No new entries are added to the Problems tab for function codes.
- The object version does not change including the version comments. It is merely the usage relationship that is converted to the new version of the control module description.

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="5-4-3-observing-the-import-of-control-module-descriptions.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="5-4-importing-control-module-descriptions.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="5-4-5-checking-the-input-baseline-for-the-control-module-import.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">5.4.3. Observing the Import of Control Module Descriptions </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 5.4.5. Checking the Input Baseline for the Control Module Import</td></tr></table>
