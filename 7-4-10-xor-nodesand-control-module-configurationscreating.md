[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md) > [7.4. Equipment Network](7-4-equipment-network.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.4.10. XOR Nodesand Control Module ConfigurationsCreating</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-4-9-assigning-knowledge-base-and-diagnostic-objects.md">Prev</a> </td><th align="center" width="60%">7.4. Equipment Network</th><td align="right" width="20%"> <a accesskey="n" href="7-4-11-create-traversal-test.md">Next</a></td></tr></table>

---

#### <a id="xorknoten.steuergeraeteausstattungen.anlegen"></a>7.4.10. XOR Nodes<a id="d4e11771"></a>and Control Module Configurations<a id="d4e11774"></a>Creating

In contrast to the basic features, XOR notes and control module configurations are reusable with and without a diagnostic interface. You can recreate and copy them like basic features, but can also reuse them.

The system name for a control module configuration can be freely assigned or to the right of that, a control module can be selected from the control module tree in the interface. So that ODIS Service can interact with this object, it is however necessary that while rebuilding the baseline,<a id="d4e11779"></a>the specified system name can be dispersed to an actual control module.

<a id="figure.redaktion.stgausstattung.stg.auswahl"></a>

![Image: selecting a control module at a control module configuration](images/stgausstattung_stg_zuweisen.png)

**Figure 247. Selecting a Control Module at a Control Module Configuration**

Control module configurations have additional attributes. **Installation ensured**<a id="d4e11790"></a>indicates that a control module must be installed, therefore that this control module object must be found. Through **OBDII**<a id="d4e11794"></a>the DTC memory is only then deleted at the end of the diagnostic session, because of the readiness code, if previous errors were set. **Delete/Read-wait time**<a id="d4e11798"></a>will delete the DTC memory in the control module at the end of GFF and will be read out again after the configured wait time. **Always read DTC memory**<a id="d4e11802"></a>indicates that the DTC memory is always read for this control module, even if no DTC memory is in the warranty installation list. In the **diagnostic address** attribute,<a id="d4e11806"></a>this is given as a 4-digit hexadecimal number.

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-4-9-assigning-knowledge-base-and-diagnostic-objects.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="7-4-equipment-network.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="7-4-11-create-traversal-test.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">7.4.9. Assigning Knowledge Base and Diagnostic Objects </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 7.4.11. Create Traversal Test</td></tr></table>
