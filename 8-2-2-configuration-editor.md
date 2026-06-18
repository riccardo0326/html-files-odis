[ODIS Creator Help](odis-creator-help.md) > [8. ODIS Creator Preparation Process](8-odis-creator-preparation-process.md) > [8.2. Production Settings](8-2-production-settings.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">8.2.2. Configuration Editor</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="8-2-1-brand-navigator.md">Prev</a> </td><th align="center" width="60%">8.2. Production Settings</th><td align="right" width="20%"> <a accesskey="n" href="8-3-test-baseline.md">Next</a></td></tr></table>

---

#### <a id="konfigurationseditor"></a>8.2.2. Configuration Editor

Within the editor, the settings are structured by theme as follows and compiled in individual tabs:

1. Creation interval for the production baseline (see [Figure 605, “Creation Interval”](8-2-2-configuration-editor.md#figure.produktiv.baseline.konfig.editor1 "Figure 605. Creation Interval"))
2. Specifications for the automatic creation of the production baseline descriptions (see [Figure 606, “Specifications for Automatic Creation”](8-2-2-configuration-editor.md#figure.produktiv.baseline.konfig.editor2 "Figure 606. Specifications for Automatic Creation"))

<a id="figure.produktiv.baseline.konfig.editor1"></a>

![Image: creation interval](images/produktiv_baseline_konfig1.png)

**Figure 605. Creation Interval**

<a id="figure.produktiv.baseline.konfig.editor2"></a>

![Image: specifications for automatic creation](images/produktiv_baseline_konfig2.png)

**Figure 606. Specifications for Automatic Creation**

The location administrator enters the times or conditions for the regular preparation in the configuration dialog in the **Creation** tab and is separated for the incremental and full baselines.

For incremental production baselines, the location administrator can set a period in days for how often an incremental production baseline is automatically created and a specific time for the creation.

Three alternatives are defined for full production baselines:

- Period in days with a time specification
- Recurring date each month with a time specification
- Subject to the size of an incremental installation package that is due:

  - if one incremental package would exceed nn% of the full version size
  - if all incremental packages since the last full version would exceed nn% of the full version size.

The location administrator enters the specifications for the automatically created names for full or incremental production baselines, the market name and any comments in the **Full or Incremental** tab in the configuration dialog. Furthermore, an exclusion list must be selected.

The **market name** field is an optional field, which the location administrator can use to integrate a market name into the rebuild, in order to communicate it to the GFF user in advance. The market name may only consist of the following characters.

- Digits 0-9
- Hyphen "-"
- Underscore "\_"
- Period "."
- Letters A-Z or a-z
- Space " "

The location administrator must specify a TFD brand baseline. The version of the TFD baseline to be used for the creation of the production baseline is selected from the available data of TFD baselines on the replacement drive for the applicable brand. The list of available TFD baselines for the brand is provided in the selection field in the display, so that you can select the TFD baseline to be used for the creation of the production baseline. The last selected TFD baseline for this market is loaded in the selection field by default.

The exclusion list is selected through a file selection dialog. The file path of the selected file is displayed in the dialogs for configuration and for the creation of production baselines and can only be filled out with the file selection dialog. The display is empty at first. The file selection dialog is preallocated with the folder path from which you selected the last exclusion list. The selected file is checked against a schema after closing the file selection dialog. If errors in the schema are detected, then the following message is displayed: "The selected file is not a valid exclusion list. Please select a valid exclusion list." The detailed list of schema errors is transferred to the engine.log.

The list for "unauthorized DTC memory entries" is selected through a file selection dialog. The file selection dialog is preallocated with the folder path, from which you selected the last list. The selected file is checked against a schema after closing the file selection dialog. If errors in the schema are detected, then the following message is displayed: "The selected file is not a valid list for 'unauthorized DTC memory entries'. The schema validation has failed when verifying the X field. Please select a valid list for 'unauthorized DTC memory entries'." The detailed list of schema errors is transferred to the engine.log. If the list is valid, then the current version of the list will be displayed after loading. If you do not want to use the list, you are able to import an empty list (only structure without content). When deploying, the file is stored on the replacement drive in a sub-folder related to the order in the baseline folder, for example "..\BRAND-V\1.0.0\DTC\_Exclusion\20160316\_163726\DtcExclusion.xml".

The list for "evaluation factors for verification calculation" is selected through a file selection dialog. The file selection dialog is preallocated with the folder path, from which you selected the last list. The selected file is checked against a schema after closing the file selection dialog. If errors in the schema are detected, then the following message is displayed: "The selected file is not a valid list for 'evaluation factors for verification calculation'. The schema validation has failed when verifying the X field. Please select a valid list for 'evaluation factors for verification calculation'." The detailed list of schema errors is transferred to the engine.log. If you do not want to use the list, you are able to import an empty list (only structure without content). When deploying, the file is stored on the replacement drive in a sub-folder related to the order in the baseline folder, for example "..\BRAND-V\1.0.0\DTC\_Factors\20160316\_163726\DtcFactors.xml".

The fields for the version of the baseline to be created and service references are filled in by the system and cannot be edited. In these fields, the respective version of the service references or XML reference tables currently available in the system are displayed.

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="8-2-1-brand-navigator.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="8-2-production-settings.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="8-3-test-baseline.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">8.2.1. Brand Navigator </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 8.3. Test Baseline</td></tr></table>
