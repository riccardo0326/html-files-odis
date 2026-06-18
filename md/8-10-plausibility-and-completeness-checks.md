[ODIS Creator Help](odis-creator-help.md) > [8. ODIS Creator Preparation Process](8-odis-creator-preparation-process.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">8.10. Plausibility and Completeness Checks</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="8-9-3-eu5-export-editor.md">Prev</a> </td><th align="center" width="60%">8. ODIS Creator Preparation Process</th><td align="right" width="20%"> <a accesskey="n" href="8-10-1-performing-the-plausibility-and-completeness-check-automatically.md">Next</a></td></tr></table>

---

### <a id="prozess.bereitstellung.pruefung"></a>8.10. Plausibility and Completeness Checks

In ODIS Creator, it is possible to perform a plausibility and completeness check for a deployment. This should identify errors that occur during a deployment to eliminate them in time. A series of plausibility checks are done by the system for this. It can be manually checked, however it occurs automatically after a baseline is created or when the deadline has been reached. After the test has ended, the log can be downloaded in an Excel file format. The "test" navigator is located in the deployment view. All brands, for which the logged in location administrator is authorized, are displayed at the top level in the navigator (see [Figure 617, “Test Navigator”](8-10-plausibility-and-completeness-checks.md#figure.bereitstellung.pruefung.navigator "Figure 617. Test Navigator")).

<a id="figure.bereitstellung.pruefung.navigator"></a>

![Test Navigator](images/bereitstellung_pruefung_navigator.png)

**Figure 617. Test Navigator**

The navigator structure is designed similar to the deployment navigator. All brands, for which the current location administrator is authorized, are displayed at the top level. The processing types are displayed at the second level: manual or automatic.

Under the "automatic" node, the automatic checks are broken up into the following types:

- Complete production baseline
- Incremental production baseline
- Test Baseline
- Rollout Baseline

Under the "manual" node, the manual checks are broken up into the following types:

- Complete production baseline
- Incremental production baseline
- Test Baseline

Year nodes are displayed on the other level. If a year node does not exist for the current year yet, then it will automatically be created by the system and displayed under the test object. Otherwise, the new check is added at the end of the existing structure. The name given by the user is displayed as the name, while the respective values are set for the entered placeholders when saving.

The name of the check is also used as the name for the log file. However, umlauts and spaces cause problems for file names. Therefore, the English term is used when replacing the placeholder. You can find a placeholder description in [Table 143, “Placeholder description”](8-10-3-placeholder.md#table.bereitstellung.pruefung.platzhalter "Table 143. Placeholder description").

The plausibility and completeness checks cover the following:

- Each object is checked for errors and if it can be deployed
- Completeness of the referenced objects
- Usage of ECU variants
- Content of the used MOVE objects
- Use of editorial objects from other brands

You can reference the exact descriptions of the checks in [Section 8.10.4, “Performing the Plausibility and Completeness Checks”](8-10-4-performing-the-plausibility-and-completeness-checks.md "8.10.4. Performing the Plausibility and Completeness Checks").

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="8-9-3-eu5-export-editor.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="8-odis-creator-preparation-process.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="8-10-1-performing-the-plausibility-and-completeness-check-automatically.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">8.9.3. EU5 Export Editor </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 8.10.1. Performing the Plausibility and Completeness Check Automatically</td></tr></table>
