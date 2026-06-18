[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.8. DTC Memory Tree</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-7-10-error-types.md">Prev</a> </td><th align="center" width="60%">7. ODIS Creator Editing Process</th><td align="right" width="20%"> <a accesskey="n" href="7-8-1-creating-a-fault-location.md">Next</a></td></tr></table>

---

### <a id="fehlerspeicherbaum"></a>7.8. DTC Memory Tree

The **DTC memory tree** contains all available DTC memory entries in the group as **DTC objects**. The DTC objects in the DTC memory tree are sorted under the P/U/B/C structure nodes and the VAG, Crafter, and Cyclone nodes. Fault location objects that cannot be allocated in the corresponding subfolders in the “Cyclone” structure nodes according to the P/U/B/C codes will be assigned to the separate “PUBC” collective folder in the “Cyclone” structure nodes. All DTC entries from the group data import and the ODX export will be listed. DTC memory can also be manually created. This is to be able to define DTC memory codes first, that are not yet available from the import data. If these are imported later, then the import data has priority and overwrites the manually created attributes.

<a id="figure.fehlerspeicherbaum"></a>

![Image: DTC memory tree](images/fehlerspeicherbaum.png)

**Figure 290. DTC Memory Tree**

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-7-10-error-types.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="7-odis-creator-editing-process.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="7-8-1-creating-a-fault-location.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">7.7.10. Error Types </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 7.8.1. Creating a Fault Location</td></tr></table>
