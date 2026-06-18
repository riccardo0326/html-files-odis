[ODIS Creator Help](odis-creator-help.md) > [8. ODIS Creator Preparation Process](8-odis-creator-preparation-process.md) > [8.5. Rollout Baseline](8-5-rollout-baseline.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">8.5.4. Creating and Editing a Rollout Baseline</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="8-5-3-rollout-baseline-editor.md">Prev</a> </td><th align="center" width="60%">8.5. Rollout Baseline</th><td align="right" width="20%"> <a accesskey="n" href="8-6-baseline-status.md">Next</a></td></tr></table>

---

#### <a id="baseline.rollout.erstellen"></a>8.5.4. Creating and Editing a Rollout Baseline

The creation of a new rollout baseline is done the same as the [creation of a production baseline](8-1-4-create-and-edit-a-production-baseline.md "8.1.4. Create and Edit a Production Baseline"), also only via the [rollout baseline browser](8-5-1-rollout-baseline-browser.md "8.5.1. Rollout Baseline Browser"). As with production baselines, the name of the rollout baseline is automatically generated from the defined specifications. To determine the volume of data, you must specify the market introduction date that limits the scope of the rollout baseline. This can be seen in [Figure 610, “Rollout Baseline Editor”](8-5-4-creating-and-editing-a-rollout-baseline.md#figure.rollout.baseline.editor "Figure 610. Rollout Baseline Editor").

<a id="figure.rollout.baseline.editor"></a>

![Image: rollout baseline editor](images/rolloutbaseline.png)

**Figure 610. Rollout Baseline Editor**

Using **Delete baseline** in the context menu, already generated rollout baselines can be removed from the ODIS Creator system again. This only applies to rollout baselines with [Canceled](8-6-3-canceled.md "8.6.3. Canceled"), [Error](8-6-4-error.md "8.6.4. Error"), [Completed (externally)](8-6-8-completed-externally.md "8.6.8. Completed (Externally)"), [Error externally](8-6-9-external-error.md "8.6.9. External Error"), or [Canceled externally](8-6-10-externally-canceled.md "8.6.10. Externally Canceled") status.

If you stop the rebuilding of data for a baseline with the [processing](8-6-2-in-progress.md "8.6.2. In progress") status, the job will be canceled and not completed. Since this job is performed in a separate process, there is a time lapse between when the cancellation is interrupt and when the operation is complete. The baseline status is set to [Error](8-6-4-error.md "8.6.4. Error") and the information about the cancellation is entered in the log by a user.

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="8-5-3-rollout-baseline-editor.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="8-5-rollout-baseline.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="8-6-baseline-status.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">8.5.3. Rollout Baseline Editor </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 8.6. Baseline Status</td></tr></table>
