[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md) > [7.1. Editorial Object General Information](7-1-editorial-object-general-information.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.1.3. Editorial Object Status</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-1-2-revising-an-editorial-object.md">Prev</a> </td><th align="center" width="60%">7.1. Editorial Object General Information</th><td align="right" width="20%"> <a accesskey="n" href="7-1-4-selecting-editorial-objects.md">Next</a></td></tr></table>

---

#### <a id="redaktion.status"></a>7.1.3. Editorial Object Status

##### <a id="redaktion.status.in_bearbeitung"></a>7.1.3.1. "In Processing" Status

Every version of an editorial object goes through various statuses<a id="d4e5905"></a>up to release. Some of these statuses will always be undergone, others only on a case-by-case basis. The first status of a new version is **in processing**. This is the status for every new object created for the first time, and for all objects that are revised in a new version after the release. The following requirements are necessary to acquire this status:

- The editorial object must always be able to be revised in ODIS Creator. This applies to all editorial objects from the control module tree and DTC memory, except objects for vehicle projects.
- You must set an order context<a id="d4e5914"></a>. No object can be newly created, edited or deleted in ODIS Creator without an order.
- The object must be directly or indirectly assigned to the brand, that is edited at your editing location or no brand is assigned at all (for example, with the supply of created function tests and supplemental documents, that has still not been used).
- A working version may not already exist that is edited by another team.
- Based on your role, you must have the right to edit the editorial object. For example, it can be that the equipment network objects can only be viewed, but cannot be edited.

If you have taken an object into processing, then it is assigned to the order step that you have selected as an order context. In this condition, you must fill out only the minimum required attributes, so that the editorial object can be identified in ODIS Creator. You can initiate the consistency check at any time in this status,<a id="d4e5924"></a>in order to see if the editorial object already fulfills the minimum requirements for completion. This check will run in the background. You do not have to wait on it. In the **in processing** status, the editorial object can only be viewed and changed for you and your team members. All other teams cannot view or change the object until it is released. Until then, you will continue to see the previously released version as long as you have not recreated the object. If this is the case, the members of other teams will not see the object at all.

##### <a id="redaktion.status.fertiggemeldet"></a>7.1.3.2. "Confirmed Completed" Status

To bring the editorial object into the **confirmed completed** status,<a id="d4e5931"></a>it must be consistent. All minimum entries must exist and the object must fulfill the necessary requirements for its uniqueness. You have two options for the status transfer:

- In the editor in a navigator, select one or more editorial objects in the "in processing" status. Then carry out the command **Complete** or **Edit >> Complete** in the context menu.

  <a id="figure.redaktion.kontextmenu"></a>

  ![Image: context menu editing](images/RedaktionKontextmenu.png)

  **Figure 175. Context Menu Editing**
- In the order management, select one or more editorial objects in the "in processing" in an order step from the list. Then carry out the command **Complete** or **Edit >> Complete** in the context menu.

  <a id="figure.auftragsverwaltung.kontextmenu"></a>

  ![Image: context menu editing](images/AuftragsschrittKontextmenu.png)

  **Figure 176. Order Management Context Menu**

##### <a id="redaktion.status.in_pruefung"></a>7.1.3.3. “In Testing” Status

The status of function code objects that contain Java box action elements changes automatically to the “In testing” status if the “Confirmed completed” status is reached when there is at least one untested Java box. See [Section 5.8.3, “Status Model”](5-8-3-status-model.md "5.8.3. Status Model").

##### <a id="redaktion.status.in_fertigmeldung"></a>7.1.3.4. "Being Completed" Status

The object status changes to **Being completed** and the consistency changes to **In testing**. You can see this information if you click on the object and view the properties at the bottom left. The completion may take several minutes, however it will run in the background. You do not have to wait on it. Press the **Update** command if you would like to see if there are results. You can also complete more than one editorial object at once. To do this, mark all desired objects by clicking on them while pressing the **CTRL** button and then select the command **Complete**. If the consistency check fails, then the editorial object will be set back to the **in processing** status and the consistency will be displayed **with an error**. You can obtain details from the test log, which you can access by opening the editorial object and double click on the **PTC** type log.

<a id="figure.redaktion.ptc"></a>

![Image: PTC test log](images/RedaktionPTC.png)

**Figure 177. PTC Test Log**

If completion was successful, then the editorial object will receive the **Confirmed completed** status. It can now be viewed by all other teams and can be reused or used as a copy template. The object can however be further edited by your team. If you edit it again now, ODIS Creator automatically increases the third position by one so that changes can also be made apparent to other teams. Include the version comment if this is the case. If you are finished with the revision, you must complete the object again and it must pass the consistency checks again.

##### <a id="redaktion.status.risikofreigegeben"></a>7.1.3.5. "Risk Released" Status

You can risk release objects reported as completed. To do this, switch to the order management, select the order step for which you have edited the objects and perform the [risk release](6-2-5-releasing-editorial-objects.md "6.2.5. Releasing Editorial Objects")<a id="d4e5988"></a>. Objects that are not yet confirmed completed can be first approved and then risk released using the **Complete and risk release** function.

Risk-released objects are exported with the next [provision](8-odis-creator-preparation-process.md "8. ODIS Creator Preparation Process") for the processing system, if they were edited in an adhoc order step<a id="d4e5993"></a>. The provision may be delayed for scheduled order steps until the initial deployment deadline<a id="d4e5996"></a>has been reached.

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-1-2-revising-an-editorial-object.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="7-1-editorial-object-general-information.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="7-1-4-selecting-editorial-objects.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">7.1.2. Revising an Editorial Object </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 7.1.4. Selecting Editorial Objects</td></tr></table>
