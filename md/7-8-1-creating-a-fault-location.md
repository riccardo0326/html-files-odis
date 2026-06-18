[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md) > [7.8. DTC Memory Tree](7-8-dtc-memory-tree.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.8.1. Creating a Fault Location</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-8-dtc-memory-tree.md">Prev</a> </td><th align="center" width="60%">7.8. DTC Memory Tree</th><td align="right" width="20%"> <a accesskey="n" href="7-8-2-importing-dtc-objects.md">Next</a></td></tr></table>

---

#### <a id="fehlerspeicherbaum.anlegen"></a>7.8.1. Creating a Fault Location

You can create a new fault location by selecting an already existing fault location and then clicking on the menu item Parallel node > Fault location in the context menu or click on Parallel node > Fault location in the Insert selection menu. Alternatively, a new fault location can also be created by selecting a higher-level node, such as "C0". For this, the menu item Subnode > Fault location must be selected in the context menu or in the selection menu.

The required fields of a fault location are the VAG code or the P/U/B/C code. Both fields are displayed as a required field, however it will suffice if you fill in one of the two fields. Based on the specified code, the newly created fault location will be organized under the structure node.

The release of a fault location occurs only through an import of reference tables, VWG reference tables, LT3 text tables, or Cyclone text tables and VFA reference tables (see [Section 5.2.5, “Import”](5-2-5-import.md "5.2.5. Import")). The use of fault locations not yet released will prevent the release of referenced editorial objects.

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-8-dtc-memory-tree.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="7-8-dtc-memory-tree.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="7-8-2-importing-dtc-objects.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">7.8. DTC Memory Tree </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 7.8.2. Importing DTC Objects</td></tr></table>
