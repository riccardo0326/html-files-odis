[ODIS Creator Help](odis-creator-help.md) > [6. ODIS Creator Order Management Process](6-odis-creator-order-management-process.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">6.4. Translation</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="6-3-3-text-request-status.md">Prev</a> </td><th align="center" width="60%">6. ODIS Creator Order Management Process</th><td align="right" width="20%"> <a accesskey="n" href="6-4-1-define-translation-parameters.md">Next</a></td></tr></table>

---

### <a id="auftragsverwaltung.uebersetzung"></a>6.4. Translation

In translation management through ODIS Creator, brand and language-specific translations can be commissioned to a translation portal outside of ODIS Creator. A translation order can be created automatically by ODIS Creator or manually by a translation coordinator.

A translation is necessary, if an editorial object is released and newer texts or text files are kept the same as their previous version, if new target markets with additional languages are set or if a new language is added to a target market.

The allocation of an editorial object in the equipment network determines which target languages are relevant for it. A knowledge base contains its target languages from the linked vehicle model. A diagnostic object and all linked primary and secondary objects receive the target languages as follows:

- If an engine is not given as a child object of the diagnostic object to be considered, then the calculation of target languages is done through the vehicle model of the knowledge base.
- If there are one or more engine nodes as child nodes, the union of the languages of the engine object is considered for the calculation of the target languages of the diagnostic object.

As a general rule, a translation is performed for each released version of an editorial object. For specific brands, the translation process may already be performed for objects in the “Confirmed completed” status. This brand-specific modification does not change the actual course of the translation process. Excluded from this in both cases are versions in which the translation-relevant contents were not changed.

- Translation packages are automatically created based on a specific retention time or when exceeding a certain volume.
- Translation coordinators can also manually order translation packages in order to make translations available quickly in a market.

<a id="figure.auftragsverwaltung.uebersetzung"></a>

![Image: translation overview](images/AuftragsverwaltungUebersetzung.png)

**Figure 147. Translation Overview**

<a id="table.hinweis.uebersetzung"></a>

<table border="1" summary="Note for Translation"><colgroup><col align="center"/><col align="left"/></colgroup><tbody valign="top"><tr><td align="center" valign="top"><span class="inlinemediaobject"><img alt="Note symbol" src="images/info.png"/></span></td><td align="left" valign="top"><span class="bold"><strong>Note:</strong></span> Adding new dependencies (for example, through new markets) to editing locations other than the original authoring location may result in a new translation requirement for a document that has already existed for a long time. This will then be added to the involved editing location and also specified there in the navigator.</td></tr></tbody></table>

**Table 33. Note for Translation**

For the clone language to be taken into consideration, it must be selected for the location in the Administration area under “Master data -> Location data -> Clone languages”. After that, manual packages that include the clone languages can be compiled.

<a id="figure.auftragsverwaltung.uebersetzung.clone.admin"></a>

![Image: clone language translation note](images/clonesprache_konfiguration.png)

**Figure 148. Clone Language Translation Note**

If the target language is set as a cloned language in the clone language settings for the affected location, the translation status of the associated clone language will be adopted.

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="6-3-3-text-request-status.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="6-odis-creator-order-management-process.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="6-4-1-define-translation-parameters.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">6.3.3. Text request status </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 6.4.1. Define Translation Parameters</td></tr></table>
