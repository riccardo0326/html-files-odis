[ODIS Creator Help](odis-creator-help.md) > [6. ODIS Creator Order Management Process](6-odis-creator-order-management-process.md) > [6.2. Orders](6-2-orders.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">6.2.7. Monitoring the Translation Status from the Order Step</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="6-2-6-switching-the-context-for-editorial-objects.md">Prev</a> </td><th align="center" width="60%">6.2. Orders</th><td align="right" width="20%"> <a accesskey="n" href="6-2-8-determining-the-market-supply.md">Next</a></td></tr></table>

---

#### <a id="auftrag.uebersetzung.ueberwachen"></a>6.2.7. Monitoring the Translation Status from the Order Step

Depending on what is set for your market, the order step can give the author or editorial coordinator the option to track the status of the translation after an editorial object is completed or released. There is a "translation" column in the editorial objects table for this, as seen in [Figure 128, “Translation Management in Order Step”](6-2-7-monitoring-the-translation-status-from-the-order-step.md#figure.auftragsschritt.uebersetzungssteuerung.ohne.detail "Figure 128. Translation Management in Order Step"). The column is not filled out before the editorial object is completed or released. This column may contain the following values after the completion or release:

- **Ready for translation** - This means that there are translation requirements for at least one language, however no translation packages or translations exist yet.
- **In translation** - This means that there is no translation yet for at least one language.
- **Complete** - This means that there is one translation for every language.
- **Not analyzed** - This means that the analysis of translation requirements has not been performed yet for this editorial object.
- **Source language only** - This means that translation requirements could still potentially be generated for this editorial object. This status may occur, if for example, no market link exists yet.

<a id="figure.auftragsschritt.uebersetzungssteuerung.ohne.detail"></a>

![Image: translation management in order step](images/Auftragsschritt_Uebersetzungssteuerung_ohne_Detail.png)

**Figure 128. Translation Management in Order Step**

To enable an overview of the editorial objects table, select the "In translation" filter button to see the editorial objects - as in [Figure 129, “Filter for Translation Management in Order Step”](6-2-7-monitoring-the-translation-status-from-the-order-step.md#figure.auftragsschritt.uebersetzungssteuerung.mit.filter "Figure 129. Filter for Translation Management in Order Step") - in which the table is reduced to those which currently have the translation status.

<a id="figure.auftragsschritt.uebersetzungssteuerung.mit.filter"></a>

![Image: filter for translation management in order step](images/Auftragsschritt_Uebersetzungssteuerung_mit_Filter.png)

**Figure 129. Filter for Translation Management in Order Step**

Using the "Show translation details" button ([Figure 128, “Translation Management in Order Step”](6-2-7-monitoring-the-translation-status-from-the-order-step.md#figure.auftragsschritt.uebersetzungssteuerung.ohne.detail "Figure 128. Translation Management in Order Step")) within the order step, it is possible to receive more information about the translation for an editorial object found in the corresponding table. The information for translation is displayed separately according to the individual languages in the table [Figure 130, “Detailed Information for Translation in the Order Step”](6-2-7-monitoring-the-translation-status-from-the-order-step.md#figure.auftragsschritt.uebersetzungssteuerung.mit.detail "Figure 130. Detailed Information for Translation in the Order Step"). The current translation status for every language can be seen here. If you are assigned to a team with the "translation coordinator" role, then you can double click to switch from the entry in the table to this line in the corresponding content in the translation view. (see [Figure 147, “Translation Overview”](6-4-translation.md#figure.auftragsverwaltung.uebersetzung "Figure 147. Translation Overview"))

<a id="figure.auftragsschritt.uebersetzungssteuerung.mit.detail"></a>

![Image: detailed information for translation in the order step](images/Auftragsschritt_Uebersetzungssteuerung_mit_Detail.png)

**Figure 130. Detailed Information for Translation in the Order Step**

By pressing the button "Hide translation details", the original display will be restored [Figure 128, “Translation Management in Order Step”](6-2-7-monitoring-the-translation-status-from-the-order-step.md#figure.auftragsschritt.uebersetzungssteuerung.ohne.detail "Figure 128. Translation Management in Order Step").

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="6-2-6-switching-the-context-for-editorial-objects.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="6-2-orders.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="6-2-8-determining-the-market-supply.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">6.2.6. Switching the Context for Editorial Objects </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 6.2.8. Determining the Market Supply</td></tr></table>
