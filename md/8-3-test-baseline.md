[ODIS Creator Help](odis-creator-help.md) > [8. ODIS Creator Preparation Process](8-odis-creator-preparation-process.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">8.3. Test Baseline</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="8-2-2-configuration-editor.md">Prev</a> </td><th align="center" width="60%">8. ODIS Creator Preparation Process</th><td align="right" width="20%"> <a accesskey="n" href="8-3-1-test-baseline-browser.md">Next</a></td></tr></table>

---

### <a id="baselines.test"></a>8.3. Test Baseline

In contrast to the production baselines, test baselines do not just include editorial objects released at a specific time, but rather the most recent version of all editorial objects for a brand regardless of their current status. The full test baselines always contain the newest version of all editorial objects for a brand.

For test baselines, the target folder for the result is always specified in the applicable [test baseline settings](8-4-2-configuration-editor.md "8.4.2. Configuration Editor"). In contrast to production baselines, for which zip archives are stored with the prepared object descriptions and contents, a [DIDB](11-appendix.md#didb "DIDB") test as well as the required zip archive with object contents are stored for test baselines in the defined target folder. The defined target folder applies as the basis for this. To structure the filing, corresponding sub-folders are created when necessary.

In contrast to production baselines, test baselines are always exported in the source languages of the respective objects only. Because there are multiple editorial languages in ODIS Creator, the source language content is exported in the "OD-OD" fallback language. This fallback language includes all ODIS Creator editorial languages under a unique ISO code. This grouping permits unified access to the source language content in the processing system regardless of which editorial language the respective object was created with. This handling also affects hotfixes that were created from text baselines. There the texts for the objects are likewise only exported in the "OD-OD" language.

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="8-2-2-configuration-editor.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="8-odis-creator-preparation-process.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="8-3-1-test-baseline-browser.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">8.2.2. Configuration Editor </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 8.3.1. Test Baseline Browser</td></tr></table>
