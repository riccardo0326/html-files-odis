[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md) > [7.20. Export and Import](7-20-export-and-import.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.20.1. Export function</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-20-export-and-import.md">Prev</a> </td><th align="center" width="60%">7.20. Export and Import</th><td align="right" width="20%"> <a accesskey="n" href="7-20-2-import-function.md">Next</a></td></tr></table>

---

#### <a id="export.only"></a>7.20.1. Export function

The "Export" menu item ![](images/export2.png) is visible or active depending on the current focus and the selection in the ODIS Creator application. Generally, an export is only possible with one type. This means that the menu action is only active, if all of the objects in the set of currently selected function code objects are of the same type (for example, general test).

The function code export is not possible if the function code is not released, or it is linked to a measured value table or a preset measurement.

The export can be started from the knowledge base or function library views. If one or more function tests, general tests or test procedures are marked, then the export can be started. The user selects a target folder, in which the file and an export log are then stored.

A checksum is calculated for each exported object file and written into the index-xml file, which is located near the other export files. The checksum is used to check the integrity of the object files.

This log contains a list of the exported functions codes and any errors that occurred.

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-20-export-and-import.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="7-20-export-and-import.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="7-20-2-import-function.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">7.20. Export and Import </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 7.20.2. Import Function</td></tr></table>
