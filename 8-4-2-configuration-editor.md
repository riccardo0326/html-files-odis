[ODIS Creator Help](odis-creator-help.md) > [8. ODIS Creator Preparation Process](8-odis-creator-preparation-process.md) > [8.4. Test Settings](8-4-test-settings.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">8.4.2. Configuration Editor</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="8-4-1-brand-navigator.md">Prev</a> </td><th align="center" width="60%">8.4. Test Settings</th><td align="right" width="20%"> <a accesskey="n" href="8-5-rollout-baseline.md">Next</a></td></tr></table>

---

#### <a id="konfigurationseditor.test"></a>8.4.2. Configuration Editor

Within the editor, the settings are structured by theme as follows and compiled in individual tabs:

1. Creation interval for test baselines
2. Parameters for the automatic creation of the test baseline descriptions.
3. Specifications for the saved location of the created test baselines.

The location administrator enters the times or conditions for the regular provision in the **Creation** tab in the configuration dialog (see [Figure 607, “Test Settings Editor - Creation Tab”](8-4-2-configuration-editor.md#figure.test.baseline.konfig.build "Figure 607. Test Settings Editor - Creation Tab")).

<a id="figure.test.baseline.konfig.build"></a>

![Image: test settings editor - Creation tab](images/testbaseline_konfig_build.png)

**Figure 607. Test Settings Editor - Creation Tab**

The production base baseline used for the test baseline is the most recent, complete and explicitly released production baseline.

The location administrator can set a period in days of the week for how often a test baseline is automatically created and can select a time that the creation occurs. At least one day of the week must be selected. Changes from the automatic test baseline creation have immediate effect, even on test baselines from the same day.

The following configurations are possible for complete test baselines:

- Checkbox for activating/deactivating automatic creation of the test baseline
- Time (UTC) can be set collectively for all days of the week
- Checkboxes for each day of the week from Monday through Sunday

The location administrator enters the specifications for the automatically created names for full test baselines and any comments in the **Description** tab in the configuration dialog (see [Figure 608, “Test Settings Editor - Description Tab”](8-4-2-configuration-editor.md#figure.test.baseline.konfig.description "Figure 608. Test Settings Editor - Description Tab")).

<a id="figure.test.baseline.konfig.description"></a>

![Image: test settings editor - Description tab](images/testbaseline_konfig_description.png)

**Figure 608. Test Settings Editor - Description Tab**

The location administrator enters the specifications for the target folder of the rebuilt test baseline in the **save location** tab in the configuration dialog (see [Figure 609, “Test Settings Editor - Save Location Tab”](8-4-2-configuration-editor.md#figure.test.baseline.konfig.path "Figure 609. Test Settings Editor - Save Location Tab")). Specifying the save location is mandatory!

<a id="figure.test.baseline.konfig.path"></a>

![Image: test settings editor - Save location tab](images/testbaseline_konfig_path.png)

**Figure 609. Test Settings Editor - Save Location Tab**

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="8-4-1-brand-navigator.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="8-4-test-settings.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="8-5-rollout-baseline.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">8.4.1. Brand Navigator </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 8.5. Rollout Baseline</td></tr></table>
