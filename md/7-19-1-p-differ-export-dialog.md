[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md) > [7.19. Manual P-Differ Export](7-19-manual-p-differ-export.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.19.1. P-Differ Export Dialog</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-19-manual-p-differ-export.md">Prev</a> </td><th align="center" width="60%">7.19. Manual P-Differ Export</th><td align="right" width="20%"> <a accesskey="n" href="7-19-2-selection-of-knowledge-base-objects.md">Next</a></td></tr></table>

---

#### <a id="manueller.export"></a>7.19.1. P-Differ Export Dialog

For authors that also have the editing coordinator role, the menu item **P-Diff direct export** is offered in the editing view under the file menu. A dialog ([Figure 595, “Manual P-Differ Export”](7-19-1-p-differ-export-dialog.md#figure.pdifferdialog "Figure 595. Manual P-Differ Export")) will open with this menu item to create a P-Differ export job, that is performed one time. Like the administrator, you can select the location from a list and an object status amount that should be used for the export.

The decision of which function test version is considered for the P-differ export occurs based on the selected object status during the P-differ export configuration. The newest version of the function test will be included, that is located in one of the selected object statuses. If none of the versions is located in any of the selected object statuses, then the entire function test is not included.

After confirming the dialog with OK, a corresponding export job is created that is then processed subsequently by the server.

<a id="figure.pdifferdialog"></a>

![Image: manual P-differ export](images/pdifferdialog.png)

**Figure 595. Manual P-Differ Export**

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-19-manual-p-differ-export.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="7-19-manual-p-differ-export.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="7-19-2-selection-of-knowledge-base-objects.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">7.19. Manual P-Differ Export </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 7.19.2. Selection of Knowledge Base Objects</td></tr></table>
