[ODIS Creator Help](odis-creator-help.md) > [5. ODIS Creator Administration Process](5-odis-creator-administration-process.md) > [5.4. Importing Control Module Descriptions](5-4-importing-control-module-descriptions.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">5.4.6. Display OC input baseline</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="5-4-5-checking-the-input-baseline-for-the-control-module-import.md">Prev</a> </td><th align="center" width="60%">5.4. Importing Control Module Descriptions</th><td align="right" width="20%"> <a accesskey="n" href="5-4-7-import-of-ecu-increments.md">Next</a></td></tr></table>

---

#### <a id="d4e2452"></a>5.4.6. Display OC input baseline

As soon as an input baseline is in the control module import folder, it can be checked with the menu item **File > Display OC input baseline**. The coding of the vehicle projects is also available there, so that you can see when the control module import can be started.

<a id="figure.sgbimport.ocinputbaseline.editor"></a>

![OC Input Baseline Editor](images/Inputbaseline_editor.png)

**Figure 68. OC Input Baseline Editor**

In the current OC input baseline editor (see [Figure 68, “OC Input Baseline Editor”](5-4-6-display-oc-input-baseline.md#figure.sgbimport.ocinputbaseline.editor "Figure 68. OC Input Baseline Editor")), you can also delete the content of the respective brand-specific import folder. To do this, press the **Clear input baseline folder** button. The following dialog will appear after that:

<a id="figure.sgbimport.ocinputbaseline.meldung1"></a>

![Clear Input Baseline Folder](images/Inputbaseline_verzeichnis_leeren.png)

**Figure 69. Clear Input Baseline Folder**

If you click the dialog, it will attempt to delete the respective import folder. It will check if an import is being currently done for this brand. If yes, the following message will appear and the deleting process will be canceled.

<a id="figure.sgbimport.ocinputbaseline.meldung2"></a>

![Clear Input Baseline Folder Not Possible](images/Inputbaseline_verzeichnis_leeren_Fehler.png)

**Figure 70. Clear Input Baseline Folder Not Possible**

Otherwise, the current import folder content will be deleted. If there is at least one folder or one file that cannot be deleted, then the following error message will appear.

<a id="figure.sgbimport.ocinputbaseline.meldung3"></a>

![Clear Input Baseline Folder Failed](images/Inputbaseline_verzeichnis_leeren_Fehler2.png)

**Figure 71. Clear Input Baseline Folder Failed**

A collision with a possible simultaneously running TFD deployment is not checked or blocked for this.

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="5-4-5-checking-the-input-baseline-for-the-control-module-import.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="5-4-importing-control-module-descriptions.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="5-4-7-import-of-ecu-increments.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">5.4.5. Checking the Input Baseline for the Control Module Import </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 5.4.7. Import of ECU Increments</td></tr></table>
