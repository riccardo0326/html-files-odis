[ODIS Creator Help](odis-creator-help.md) > [5. ODIS Creator Administration Process](5-odis-creator-administration-process.md) > [5.7. Remote diagnosis export](5-7-remote-diagnosis-export.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">5.7.2. Editors for Remote Diagnosis Exports</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="5-7-1-remote-diagnosis-export-navigation-tree.md">Prev</a> </td><th align="center" width="60%">5.7. Remote diagnosis export</th><td align="right" width="20%"> <a accesskey="n" href="5-8-java-box-test.md">Next</a></td></tr></table>

---

#### <a id="ocs.editor"></a>5.7.2. Editors for Remote Diagnosis Exports

##### <a id="ocs.editor.conf"></a>5.7.2.1. Settings Editor

The preparation methods that should be used for the export are configured in the respective brand nodes. Any preparation method can be selected.

The exports for the test baseline are created based on the number of days that are set. The basis for calculation is the time of the last test baseline at which a remote diagnosis export was performed. If the number of days between the last test baseline with remote diagnosis export and the current test baseline is less than the set number of days, then no further remote diagnosis export will be performed.

<a id="figure.ocs.editor.conf"></a>

![Image: configuration editor for remote diagnosis export](images/ocs_editor_conf.png)

**Figure 104. Settings Editor**

##### <a id="ocs.editor.export"></a>5.7.2.2. Editor for Remote Diagnosis Export

The name of the editor for an export corresponds to the name of the export in the navigation tree. The log files for the remote diagnosis export that is currently displayed can be viewed and downloaded in the Editor.

The name of the export in the save folder will also be displayed in the Editor. This name can be copied into the clipboard using a button.

After a successful export, the checksum for the export file will be displayed in the editor. The logic and purpose of using the checksum is to validate the data integrity of the exports, similar to the cooperation export (see [Section 8.11.7, “Export Check Sum”](8-11-7-export-check-sum.md "8.11.7. Export Check Sum")).

<a id="figure.ocs.editor.export"></a>

![Image: remote diagnosis export editor](images/ocs_editor_export.png)

**Figure 105. Remote Diagnosis Export Editor**

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="5-7-1-remote-diagnosis-export-navigation-tree.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="5-7-remote-diagnosis-export.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="5-8-java-box-test.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">5.7.1. Remote Diagnosis Export Navigation Tree </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 5.8. Java Box Test</td></tr></table>
