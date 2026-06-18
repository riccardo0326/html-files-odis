[ODIS Creator Help](odis-creator-help.md) > [8. ODIS Creator Preparation Process](8-odis-creator-preparation-process.md) > [8.3. Test Baseline](8-3-test-baseline.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">8.3.4. Creating and Editing a Test Baseline</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="8-3-3-test-baseline-editor.md">Prev</a> </td><th align="center" width="60%">8.3. Test Baseline</th><td align="right" width="20%"> <a accesskey="n" href="8-4-test-settings.md">Next</a></td></tr></table>

---

#### <a id="baseline.test.erstellen"></a>8.3.4. Creating and Editing a Test Baseline

The creation of a new test baseline is done the same as the [creation of a production baseline](8-1-4-create-and-edit-a-production-baseline.md "8.1.4. Create and Edit a Production Baseline"), via the [test baseline browser](8-3-1-test-baseline-browser.md "8.3.1. Test Baseline Browser"). The value **'Full test'** is automatically set as the type. As with production baselines, the name of the test baseline is automatically generated from the defined specifications.

Through **Delete baseline** in the context menu, already generated test baselines can be removed from the ODIS Creator system again. This only applies to test baselines with [Canceled](8-6-3-canceled.md "8.6.3. Canceled"), [Error](8-6-4-error.md "8.6.4. Error"), [DIDB creation ended with errors](8-6-15-didb-creation-ended-with-error.md "8.6.15. DIDB Creation Ended with Error"), or [Completed](8-6-8-completed-externally.md "8.6.8. Completed (Externally)") status.

If you stop the rebuilding of data for a baseline with the [processing](8-6-2-in-progress.md "8.6.2. In progress") status, the job will be canceled and not completed. Since this job is performed in a separate process, there is a time lapse between when the cancellation is interrupt and when the operation is complete. The baseline status is set to [Error](8-6-4-error.md "8.6.4. Error") and the information about the cancellation is entered in the log by a user.

<a id="table.hinweis.vorbelegungen2"></a>

<table border="1" summary="Note for Preset Fields"><colgroup><col align="center"/><col align="left"/></colgroup><tbody valign="top"><tr><td align="center" valign="top"><span class="inlinemediaobject"><img alt="Note symbol" src="images/info.png"/></span></td><td align="left" valign="top"><span class="bold"><strong>Note:</strong></span> These fields are pre-filled with the entries from the test settings.</td></tr></tbody></table>

**Table 137. Note for Preset Fields**

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="8-3-3-test-baseline-editor.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="8-3-test-baseline.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="8-4-test-settings.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">8.3.3. Test Baseline Editor </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 8.4. Test Settings</td></tr></table>
