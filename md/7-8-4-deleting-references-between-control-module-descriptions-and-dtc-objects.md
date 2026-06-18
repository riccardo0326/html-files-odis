[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md) > [7.8. DTC Memory Tree](7-8-dtc-memory-tree.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.8.4. Deleting References Between Control Module Descriptions and DTC Objects</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-8-3-allocating-dtc-objects-to-control-module-descriptions.md">Prev</a> </td><th align="center" width="60%">7.8. DTC Memory Tree</th><td align="right" width="20%"> <a accesskey="n" href="7-8-5-using-dtc-objects.md">Next</a></td></tr></table>

---

#### <a id="fehlerspeicherbaum.sgbloeschen"></a>7.8.4. Deleting References Between Control Module Descriptions and DTC Objects

For **UDS control module descriptions**, the link to DTC objects are only deleted by the control module import. When deleting a control module-DTC link via the control module import, all the diagnostic and function code objects are checked if there is still at least one relationship here of a DTC to another control module description with the same name. If this is not the case, then the team responsible for the current version of this diagnostic and function code object is notified about this and an entry is also created in the consistency check log.

The deletion is done by the author for **KWP control module descriptions**. A reference deletion is only possible, if the consistency of the usage locations is also ensured after the deletion. This means there must be at least one other control module description with the same name, which is still assigned to the DTC memory. If the DTC memory has no other references to KWP control module descriptions, then the reference removal is canceled with an error message.

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-8-3-allocating-dtc-objects-to-control-module-descriptions.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="7-8-dtc-memory-tree.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="7-8-5-using-dtc-objects.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">7.8.3. Allocating DTC Objects to Control Module Descriptions </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 7.8.5. Using DTC Objects</td></tr></table>
