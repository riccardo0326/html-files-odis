[ODIS Creator Help](odis-creator-help.md) > [5. ODIS Creator Administration Process](5-odis-creator-administration-process.md) > [5.4. Importing Control Module Descriptions](5-4-importing-control-module-descriptions.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">5.4.5. Checking the Input Baseline for the Control Module Import</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="5-4-4-analyzing-the-import-of-control-module-descriptions.md">Prev</a> </td><th align="center" width="60%">5.4. Importing Control Module Descriptions</th><td align="right" width="20%"> <a accesskey="n" href="5-4-6-display-oc-input-baseline.md">Next</a></td></tr></table>

---

#### <a id="sgbimport.inputbaseline"></a>5.4.5. Checking the Input Baseline for the Control Module Import

If the control module import has ended, you can display the input baseline for this control module import in addition to the log. It will then open in a separate editor (see [Figure 67, “Input baseline editor”](5-4-5-checking-the-input-baseline-for-the-control-module-import.md#figure.sgbimport.inputbaseline.editor "Figure 67. Input baseline editor")).

<a id="figure.sgbimport.inputbaseline.editor"></a>

![Input baseline editor](images/inputbaselineeditor.png)

**Figure 67. Input baseline editor**

You can view the following input baseline properties in the input baseline editor.

- Name of the control module import
- TFD baseline version
- TFD baseline creation date
- OC input baseline creation date
- Use case
- Brand
- List of vehicle projects

The list of vehicle projects has a color identifier relating to its status in the input baseline.

- **Missing projects:** all vehicle projects that should be a component of the OC input baseline but that are missing in the OC input baseline. This are displayed in red.
- **Extra projects:** all vehicle projects that should not be a component of the OC input baseline but that are contained in the OC input baseline. This are displayed in blue.
- **Baseline vehicle projects:** all vehicle projects that should be a component of the OC input baseline and that actually are contained in the OC input baseline. This are displayed in green.
- **Vehicle projects without changes:** all vehicle projects that should not be contained in the OC input baseline and that are not contained in the OC input baseline. This are displayed in gray.

The default sorting in the editor is first according to the list type and then alphanumerically. By clicking on the table header, you can sort the entire list alphanumerically in ascending or descending order without considering the list type.

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="5-4-4-analyzing-the-import-of-control-module-descriptions.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="5-4-importing-control-module-descriptions.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="5-4-6-display-oc-input-baseline.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">5.4.4. Analyzing the Import of Control Module Descriptions </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 5.4.6. Display OC input baseline</td></tr></table>
