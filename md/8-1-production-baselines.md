[ODIS Creator Help](odis-creator-help.md) > [8. ODIS Creator Preparation Process](8-odis-creator-preparation-process.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">8.1. Production Baselines</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="8-odis-creator-preparation-process.md">Prev</a> </td><th align="center" width="60%">8. ODIS Creator Preparation Process</th><td align="right" width="20%"> <a accesskey="n" href="8-1-1-production-baseline-browser.md">Next</a></td></tr></table>

---

### <a id="baselines.produktiv"></a>8.1. Production Baselines

A production baseline includes the editorial objects of a brand in their most recent released version at the selected time. A complete production baseline contains all released editorial objects and the editorial objects used by a brand up to the selected date. For an incremental production baseline, only those editorial objects are included that were released with the previous production baseline. In general, a production baseline corresponds to a delivery condition in the format of an installation package.

If available, the translations in the production baseline are exported for all exported editorial objects. In an additional language package, the translation-relevant texts of the respective editorial object is exported in the source language for each editorial object contained in the preparation, in which the applicable editorial object was created. With this, texts that are not translated are displayed in their original language in the processing system.

The version numbers of the correctly exported production baselines (complete and incremental) create a continuous row without spaces. Production baselines that were canceled due to an error as well as 'empty' incremental production baselines do not interrupt this row. If, for example, there are one or more incremental baselines that contain no objects (they are empty) after a complete production baseline with version number **1.3.0**, then the following incremental production baseline that contains objects will have the version number **1.3.1** regardless.

An order file is created for each production baseline. These order files are automatically created for the update creator tool in ODIS Creator after exporting the data for a production baseline. Starting the update creator tool then occurs manually. The progress of the data preparation by the update creator tool is logged in an OUT status file. These OUT status files are read out by the ‘SplExportBaselinesToDIDB’ job when exporting a baseline for DIDB creation and by ODIS Creator when calling and updating the display of the baselines in the deployment view. The current status is displayed in the application interface. This checks the integrity of the OUT status file. If this check fails, the OUT status file is not read out and the author is notified via a warning dialog (see [Figure 600, “Problems with the OUT Status File”](8-1-production-baselines.md#figure.produktiv.baseline.integritiydialog "Figure 600. Problems with the OUT Status File")) about which baselines could not be verified in the OUT status files. This allows the data preparation step of the update creator tool to be monitored through the ODIS Creator user interface. The order files for the update creator tool contain the versions of all components necessary for the creation and application of the prepared data.

<a id="figure.produktiv.baseline.integritiydialog"></a>

![Image: problems with the OUT status file](images/dialog_Probleme_mit_der_OUT_Status_Datei.jpg)

**Figure 600. Problems with the OUT Status File**

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="8-odis-creator-preparation-process.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="8-odis-creator-preparation-process.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="8-1-1-production-baseline-browser.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">8. ODIS Creator Preparation Process </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 8.1.1. Production Baseline Browser</td></tr></table>
