[ODIS Creator Help](odis-creator-help.md) > [8. ODIS Creator Preparation Process](8-odis-creator-preparation-process.md) > [8.10. Plausibility and Completeness Checks](8-10-plausibility-and-completeness-checks.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">8.10.2. Performing the Plausibility and Completeness Check Manually</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="8-10-1-performing-the-plausibility-and-completeness-check-automatically.md">Prev</a> </td><th align="center" width="60%">8.10. Plausibility and Completeness Checks</th><td align="right" width="20%"> <a accesskey="n" href="8-10-3-placeholder.md">Next</a></td></tr></table>

---

#### <a id="prozess.bereitstellung.pruefung.manuelle.durchfuehrung"></a>8.10.2. Performing the Plausibility and Completeness Check Manually

You can open the editor for the manual plausibility and completeness check for the previously selected brand through the context menu at the "manual" subnode of a brand node (see [Figure 620, “Manual Test Editor”](8-10-2-performing-the-plausibility-and-completeness-check-manually.md#figure.bereitstellung.pruefung.editor.manuell "Figure 620. Manual Test Editor")).

<a id="figure.bereitstellung.pruefung.editor.manuell"></a>

![Manual Test Editor](images/bereitstellung_pruefung_editor_manuell.png)

**Figure 620. Manual Test Editor**

In the editor, you must give a name for the check. There is a placeholder available for this, which you can select and insert. The following placeholders are available and are included in the default name:

- Brand
- Test date
- Test time
- Test type
- Test trigger
- Test sort

As the next step, you can select the type of simulated baseline. For this, you can also select the following types:

- Complete production baseline
- Incremental production baseline
- Test Baseline

<a id="table.hinweis.platzhalter3"></a>

<table border="1" summary="Note for Placeholders"><colgroup><col align="center"/><col align="left"/></colgroup><tbody valign="top"><tr><td align="center" valign="top"><span class="inlinemediaobject"><img alt="Note symbol" src="images/info.png"/></span></td><td align="left" valign="top"><span class="bold"><strong>Note:</strong></span> The previously selected placeholders are given in the name field in English.</td></tr></tbody></table>

**Table 142. Note for Placeholders**

If a manual plausibility and completeness check for a simulated baseline considers all objects, they would be included in this simulated baseline. Thus only objects of the previously selected brand, that are at least risk-released and have a valid brand relation (end date is not set or is not within the deadline time frame), are considered when testing the simulated, complete production baseline and the simulated, incremental production baseline. When checking for the simulated test baseline, all objects for the previously selected brand are considered. For a simulated incremental production baseline, the production baseline with the highest version number is used as the reference baseline.

In the next step, you must enter a simulated deployment deadline. All objects are considered for the test, that are valid corresponding to their initial deployment deadline relating to the simulated deployment deadline. The current date is entered by default in the field for the simulated deployment deadline.

In the "Archive folder" field, specify the path to a folder on the replacement drive, the same as for the test baseline, from the server view where the logs of manual checks are stored. When saving the test object, it checks if the specified folder can be reached from the server.

The fields "Test sort" and "Test trigger" are preset by the system and cannot be changed. The value for the test sort is preset with "simulated" and the value for the test trigger is "manual".

After the user has saved the editor, a Documentum job is created for the test and an information message informs the user that the initialization was successful. There are two different scenarios for this:

- If currently no other test for the selected brand is performed, a message is given to the user saying that the test was initiated and will start within the next several minutes.
- If one or more tests already ran for the selected brand or are in the queue, a message will be given that a test has already ran and the likewise configured test will be started as soon as all jobs in progress have been completed. The job monitor will inform you of the status of the test in progress. There is not an overview of if and which other tests are in the queue.

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="8-10-1-performing-the-plausibility-and-completeness-check-automatically.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="8-10-plausibility-and-completeness-checks.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="8-10-3-placeholder.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">8.10.1. Performing the Plausibility and Completeness Check Automatically </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 8.10.3. Placeholder</td></tr></table>
