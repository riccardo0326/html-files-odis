[ODIS Creator Help](odis-creator-help.md) > [8. ODIS Creator Preparation Process](8-odis-creator-preparation-process.md) > [8.10. Plausibility and Completeness Checks](8-10-plausibility-and-completeness-checks.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">8.10.6. Test Object Editor</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="8-10-5-test-status.md">Prev</a> </td><th align="center" width="60%">8.10. Plausibility and Completeness Checks</th><td align="right" width="20%"> <a accesskey="n" href="8-10-7-plausibility-and-completeness-check-log.md">Next</a></td></tr></table>

---

#### <a id="prozess.bereitstellung.pruefung.pruefobjekt"></a>8.10.6. Test Object Editor

By selecting a test object in the navigator, the editor opens as read-only with the previously selected values (see [Figure 621, “Test Object Editor for an Automatic Test”](8-10-6-test-object-editor.md#figure.bereitstellung.pruefung.pruefobjekt.automatisch "Figure 621. Test Object Editor for an Automatic Test") and [Figure 622, “Test Object Editor for a Manual Test”](8-10-6-test-object-editor.md#figure.bereitstellung.pruefung.pruefobjekt.manuell "Figure 622. Test Object Editor for a Manual Test")). The additional attributes, that are automatically filled in by the system, are displayed in [Table 144, “Test Object Editor Attribute”](8-10-6-test-object-editor.md#table.bereitstellung.pruefung.pruefobjekt "Table 144. Test Object Editor Attribute").

<a id="figure.bereitstellung.pruefung.pruefobjekt.automatisch"></a>

![Test Object Editor for an Automatic Test](images/bereitstellung_pruefung_pruefobjekt_automatisch.png)

**Figure 621. Test Object Editor for an Automatic Test**

<a id="figure.bereitstellung.pruefung.pruefobjekt.manuell"></a>

![Test Object Editor for a Manual Test](images/bereitstellung_pruefung_pruefobjekt_manuell.png)

**Figure 622. Test Object Editor for a Manual Test**

A data revision is not possible. The button „Download log“ remains deactivated, as long as no log file exists. A correlating properties window will also open for the editor. See [Section 8.10.12, “Properties”](8-10-12-properties.md "8.10.12. Properties").

<a id="table.bereitstellung.pruefung.pruefobjekt"></a>

<table border="1" summary="Test Object Editor Attribute"><colgroup><col align="left"/><col align="left"/></colgroup><thead><tr bgcolor="#EEEEEE"><th align="left">Name</th><th align="left">Value</th></tr></thead><tbody valign="top"><tr><td align="left" valign="top">Baseline version</td><td align="left" valign="top">
<p>The baseline version used for the test.</p>
<p>Is only filled in for the tests that are started after a baseline is created.</p>
</td></tr><tr><td align="left" valign="top">Baseline creation date</td><td align="left" valign="top">
<p>The creation date (with the time) of the baseline used for the test.</p>
<p>Is only filled in for the tests that are started after a baseline is created.</p>
</td></tr><tr><td align="left" valign="top">Test type</td><td align="left" valign="top">
<div class="itemizedlist"><ul type="disc"><li>
<p>Complete production baseline</p>
</li><li>
<p>Incremental production baseline</p>
</li><li>
<p>Test Baseline</p>
</li><li>
<p>Rollout Baseline</p>
</li><li>
<p>Full production baseline with end date</p>
</li><li>
<p>Incremental production baseline with end date</p>
</li></ul></div>
</td></tr><tr><td align="left" valign="top">Test trigger</td><td align="left" valign="top">
<div class="itemizedlist"><ul type="disc"><li>
<p>"manual" for manual tests</p>
</li><li>
<p>"automatic" for automatic tests</p>
</li></ul></div>
</td></tr><tr><td align="left" valign="top">Test sort</td><td align="left" valign="top">
<p>The following tests simulate a baseline creation:</p>
<p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>Complete production baseline</p>
</li><li>
<p>Incremental production baseline</p>
</li><li>
<p>Test Baseline</p>
</li><li>
<p>End date complete</p>
</li><li>
<p>End date incremental</p>
</li></ul></div><p>
</p>
<p>The "simulated" value is entered in this case.</p>
<p>For tests that are started after a baseline is created, the "real" value is entered here.</p>
</td></tr></tbody></table>

**Table 144. Test Object Editor Attribute**

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="8-10-5-test-status.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="8-10-plausibility-and-completeness-checks.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="8-10-7-plausibility-and-completeness-check-log.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">8.10.5. Test Status </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 8.10.7. Plausibility and Completeness Check Log</td></tr></table>
