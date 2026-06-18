[ODIS Creator Help](odis-creator-help.md) > [8. ODIS Creator Preparation Process](8-odis-creator-preparation-process.md) > [8.10. Plausibility and Completeness Checks](8-10-plausibility-and-completeness-checks.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">8.10.1. Performing the Plausibility and Completeness Check Automatically</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="8-10-plausibility-and-completeness-checks.md">Prev</a> </td><th align="center" width="60%">8.10. Plausibility and Completeness Checks</th><td align="right" width="20%"> <a accesskey="n" href="8-10-2-performing-the-plausibility-and-completeness-check-manually.md">Next</a></td></tr></table>

---

#### <a id="prozess.bereitstellung.pruefung.automatische.durchfuehrung"></a>8.10.1. Performing the Plausibility and Completeness Check Automatically

If you confirm the "automatic" sub-item of a brand node by double clicking, then the editor opens for the configuration of performing the plausibility and completeness check automatically for the previously selected brand. In the "When a Baseline is Created" tab, you must specify a name for the test. There is a placeholder available for this, which you can select and insert. The following placeholders are available and are included in the default name:

- Brand
- Test date
- Test time
- Baseline version
- Baseline market name
- Baseline date
- Baseline time
- Test type
- Test trigger
- Test sort

<a id="table.hinweis.platzhalter1"></a>

<table border="1" summary="Note for Placeholders"><colgroup><col align="center"/><col align="left"/></colgroup><tbody valign="top"><tr><td align="center" valign="top"><span class="inlinemediaobject"><img alt="Note symbol" src="images/info.png"/></span></td><td align="left" valign="top"><span class="bold"><strong>Note:</strong></span> The previously selected placeholders are given in the name field in English.</td></tr></tbody></table>

**Table 139. Note for Placeholders**

You can also select for which baseline types a test should be performed and which checks should be performed (see [Figure 618, “Automatic Test Editor - When a Baseline is Created Tab”](8-10-1-performing-the-plausibility-and-completeness-check-automatically.md#figure.bereitstellung.pruefung.editor.automatisch.baseline "Figure 618. Automatic Test Editor - When a Baseline is Created Tab")). The test can be performed automatically for the following baselines:

- Complete production baseline
- Incremental production baseline
- Test Baseline
- Rollout Baseline

<a id="figure.bereitstellung.pruefung.editor.automatisch.baseline"></a>

![Automatic Test Editor - When a Baseline is Created Tab](images/bereitstellung_pruefung_editor_auto_1.png)

**Figure 618. Automatic Test Editor - When a Baseline is Created Tab**

No types are selected as a default. If one or more types are selected, the plausibility and completeness check is also performed when the respective baseline is created, that runs during the deployment or briefly thereafter. The editorial objects considered during the test correspond to the editorial objects (or the versions of the editorial objects) of the respective baseline.

Several deviations are possible for the test baselines. Since the test baselines also consider the working versions of the editorial objects, it is possible that some working versions of the considered editorial objects are different at the time of deployment and the time the tests are done. The user is informed of this status in the test log.

For each baseline type, you can also select if a notification should be created at the end of the respective test.

In the "When a deadline is reached" tab, you must specify a name for the test. Placeholders are also available here. The following placeholders are available and preset:

- Brand
- Test date
- Test time
- Test type
- Test trigger
- Test sort
- Test sort
- Number of days

<a id="table.hinweis.platzhalter2"></a>

<table border="1" summary="Note for Placeholders"><colgroup><col align="center"/><col align="left"/></colgroup><tbody valign="top"><tr><td align="center" valign="top"><span class="inlinemediaobject"><img alt="Note symbol" src="images/info.png"/></span></td><td align="left" valign="top"><span class="bold"><strong>Note:</strong></span> The previously selected placeholders are given in the name field in English.</td></tr></tbody></table>

**Table 140. Note for Placeholders**

If you activate the option, you must specify the time interval in days, the time (UTC) for the processing as well as the baseline type. The following can be selected:

- Complete production baseline for the time limit
- Incremental production baseline for the time limit

You can also determine which types of tests should be performed (see [Figure 619, “Automatic Test Editor - When a Deadline is Reached Tab”](8-10-1-performing-the-plausibility-and-completeness-check-automatically.md#figure.bereitstellung.pruefung.editor.automatisch.endtermin "Figure 619. Automatic Test Editor - When a Deadline is Reached Tab")). This option is not enabled by default. If the option is enabled, the number of days is 1 by default. The time is set to 00:00 by default. The option is set for the incremental productive baseline by default. If the option is enabled, all deadlines in the order steps of all scheduled orders for the selected brand are checked in a daily background process. If the specified time interval in days has been reached for a deadline, the automatic test for the specified baseline type for the selected brand will start at the specified time.

During the test, objects are considered that are at least risk-released, which have reached the specified deadline for the verification and are explicitly still used within the brand (the brand relation has not set an end date or the end date is not within the selected deadline). If an incremental baseline was selected for the test, then the last baseline before the applied deadlined is used as a reference.

You can also select here, if a notification should be created at the end of the test.

<a id="table.hinweis.inkrementelleBaseline"></a>

<table border="1" summary="Incremental Baseline Note"><colgroup><col align="center"/><col align="left"/></colgroup><tbody valign="top"><tr><td align="center" valign="top"><span class="inlinemediaobject"><img alt="Note symbol" src="images/info.png"/></span></td><td align="left" valign="top"><span class="bold"><strong>Note:</strong></span> For the incremental baseline, only objects for testing are selected where the scheduled completion date matches the calculated deadline (test day - configured days). The calculated deadline date can be seen in the editor under the "Order step deadline" entry.</td></tr></tbody></table>

**Table 141. Incremental Baseline Note**

<a id="figure.bereitstellung.pruefung.editor.automatisch.endtermin"></a>

![Automatic Test Editor - When a Deadline is Reached Tab](images/bereitstellung_pruefung_editor_auto_2.png)

**Figure 619. Automatic Test Editor - When a Deadline is Reached Tab**

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="8-10-plausibility-and-completeness-checks.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="8-10-plausibility-and-completeness-checks.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="8-10-2-performing-the-plausibility-and-completeness-check-manually.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">8.10. Plausibility and Completeness Checks </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 8.10.2. Performing the Plausibility and Completeness Check Manually</td></tr></table>
