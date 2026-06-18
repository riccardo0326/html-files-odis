[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md) > [7.4. Equipment Network](7-4-equipment-network.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.4.9. Assigning Knowledge Base and Diagnostic Objects</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-4-8-determining-the-engine-code-from-the-engine-control-module.md">Prev</a> </td><th align="center" width="60%">7.4. Equipment Network</th><td align="right" width="20%"> <a accesskey="n" href="7-4-10-xor-nodesand-control-module-configurationscreating.md">Next</a></td></tr></table>

---

#### <a id="wissensbasis.diagnoseobjekt.zuordnen"></a>7.4.9. Assigning Knowledge Base and Diagnostic Objects

To prepare for this action, open the knowledge base view in addition to the equipment network view.<a id="d4e11718"></a>. Click on the records tab in the knowledge base navigator and pull it next to the equipment network navigator so that you can see both navigators next to each other, or select **Insert > Reference > Knowledge base**

Every knowledge base<a id="d4e11723"></a>must be assigned to exactly one vehicle model<a id="d4e11726"></a>. To do this, click on the desired vehicle model in the equipment network navigator, hold the mouse button down and then pull the vehicle model to the knowledge base. The mouse cursor shows you incorrect positions by a circle with a line through it and the correct position with a link arrow. Release the mouse button, if the link arrow displays on the desired knowledge base. ODIS Creator creates a reference from the knowledge base to the vehicle model. Through this action, the knowledge base receives their brand allocation and all diagnostic objects contained in it. If you have assigned the incorrect vehicle model or the incorrect knowledge base, select **Delete reference**. This allows you to only delete the reference between the vehicle model and the knowledge base, however not the objects themselves.

<a id="figure.redaktion.ausstattungsnetz.wissensbasis.zuordnen"></a>

![Image: allocation of a vehicle model to a knowledge base](images/zuordnung_asn_wbs.png)

**Figure 243. Allocating a Vehicle Model to a Knowledge Base**

Each engine of the vehicle model that you have just assigned a knowledge base can also reference a diagnostic object directly from this knowledge base. To do this, click on the respective diagnostic object in the knowledge base navigator, hold the mouse button down and then pull the diagnostic object to the corresponding engine. The mouse cursor signals the correct position again here as well. This reference is then exported to the deployment, and you will receive a message (see [Figure 244, “Message When a Communication Malfunction Generates”](7-4-9-assigning-knowledge-base-and-diagnostic-objects.md#figure.redaktion.ausstattungsnetz.meldung1 "Figure 244. Message When a Communication Malfunction Generates")).

<a id="figure.redaktion.ausstattungsnetz.meldung1"></a>

![Image: message when a communication malfunction generates](images/kommunikationsstoerung.png)

**Figure 244. Message When a Communication Malfunction Generates**

There is also the option to link an engine to a diagnostic object. This reference is for determining the volume of translation for the diagnostic object and its primary and secondary objects. This referencing is not deployed.

If you have the author role, you can categorize one or more engine objects under a diagnostic object. On the other hand, you can also assign an engine object to multiple diagnostic objects. It is ensured that only engine objects can be referenced under the diagnostic objects, if the corresponding vehicle model is likewise assigned to the corresponding knowledge base. The allocation of engine objects can occur on any level of the knowledge base. The system checks if an engine object was already linked in the path above or under the diagnostic object. If an engine object was already assigned, then the error message appears in [Figure 245, “Message When Link to an Engine is Reused”](7-4-9-assigning-knowledge-base-and-diagnostic-objects.md#figure.redaktion.ausstattungsnetz.meldung2 "Figure 245. Message When Link to an Engine is Reused") and the action is canceled.

<a id="figure.redaktion.ausstattungsnetz.meldung2"></a>

![Image: message when link to an engine is reused](images/doppelterMotor.png)

**Figure 245. Message When Link to an Engine is Reused**

When a diagnostic object is reused, it also checks whether the reuse would cause an engine object to be used on different levels. If this is the case, then an error message would be displayed (see [Figure 246, “Message when Reusing Diagnostic Objects”](7-4-9-assigning-knowledge-base-and-diagnostic-objects.md#figure.redaktion.ausstattungsnetz.meldung3 "Figure 246. Message when Reusing Diagnostic Objects")).

<a id="figure.redaktion.ausstattungsnetz.meldung3"></a>

![Image: message when reusing diagnostic objects](images/wiederholterMotor.png)

**Figure 246. Message when Reusing Diagnostic Objects**

It may be that a diagnostic object in an engine object is in the "used" and in the "used by" table. Therefore the diagnostic object in the "used" table of the engine object is used in the deployment for a communication malfunction. The diagnostic object in the "used by" table of the engine object is for determining the volume of translation. The same also applies to the display of engine objects in both diagnostic object tables.

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-4-8-determining-the-engine-code-from-the-engine-control-module.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="7-4-equipment-network.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="7-4-10-xor-nodesand-control-module-configurationscreating.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">7.4.8. Determining the Engine Code from the Engine Control Module </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 7.4.10. XOR Nodesand Control Module ConfigurationsCreating</td></tr></table>
