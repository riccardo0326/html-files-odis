[ODIS Creator Help](odis-creator-help.md) > [6. ODIS Creator Order Management Process](6-odis-creator-order-management-process.md) > [6.4. Translation](6-4-translation.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">6.4.4. Translation Requirements</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="6-4-3-sorting-translations.md">Prev</a> </td><th align="center" width="60%">6.4. Translation</th><td align="right" width="20%"> <a accesskey="n" href="6-4-5-commissioning-translations-manually.md">Next</a></td></tr></table>

---

#### <a id="uebersetzungsbedarfe"></a>6.4.4. Translation Requirements

All released (or confirmed completed, if this is set for the brand) editorial objects and administrative objects, that still do not have a translation for the current version, are initially checked for requirements and can then be automatically or manually sent to translation.

A translation requirement folder (see [Figure 153, “Translation Requirements”](6-4-4-translation-requirements.md#figure.auftragsverwaltung.uebersetzung.bedarfsansicht "Figure 153. Translation Requirements")) contains information about location and target language for the editorial objects, as well as version, status, type, source language, translation status, market name, initial deployment date and author of the objects in the requirement folder.

If you are assigned to a team with the roll "read-only author" or "author", then you can double click on an editorial object to switch to the corresponding content in the editing view. Analogous to the already existing link functions in other modules, the usage location dialog is also displayed to the user here if the destination of the link cannot be clearly determined (for example, due to reusage).

<a id="figure.auftragsverwaltung.uebersetzung.bedarfsansicht"></a>

![Image: translation requirements](images/uebBedarfe.jpg)

**Figure 153. Translation Requirements**

##### <a id="zieltermin.uebersetzungsbedarfe"></a>6.4.4.1. Changing the Deadline of Translation Requirements

If translation requirements for editorial objects in this order context are already completed in the system, then the initial deployment date of the order can no longer be changed. The reason is that the order header is locked from revision when it is in this status.

If this is the case, a drag and drop mechanism is implemented between the display of translation requirements and the navigation tree in the translation management. Translation coordinators can use this drag and drop mechanism to influence the last possible export data of translation requirements, therefore move the translation requirements from one date to another date or into the requirements folder without a date (undefined). It is also possible to move translation requirements from the requirement folder without a date (undefined) into a requirements folder with a date. (see [Figure 154, “Drag and Drop of Translation Requirements”](6-4-4-translation-requirements.md#figure.auftragsverwaltung.uebersetzung.bedarfe "Figure 154. Drag and Drop of Translation Requirements"))

<a id="figure.auftragsverwaltung.uebersetzung.bedarfe"></a>

![Image: drag and drop of translation requirements](images/zieltermin_uebBedarfe.jpg)

**Figure 154. Drag and Drop of Translation Requirements**

There are some restrictions that are listed in the following:

- The drag and drop mechanism only goes over the existing date node in the tree. This means that only the date node specified there (same location and same source/target language combination) can also be used as new dates. It is especially not possible to drag objects to a date, that were deleted from the tree view, because translation requirements are no longer included from previous drag and drop actions. In this way, removed date nodes are then permanently lost as drop targets. For this reason, an info dialog is displayed to the user if a drag and drop action would delete a requirement folder. This dialog gives the user the option to perform or cancel their action.
- It is not checked while using the drag and drop mechanism, if the translations of objects for the scheduled market introduction date are made available through the adjustment. The translation coordinator is responsible for the technical correctness of the adjustment. The translation coordinator is particularly responsible for maintaining the scheduled deadlines or to communicate any movement of translations that occurred.

##### <a id="uebersetzungsbedarfe.zuruecksetzen"></a>6.4.4.2. Resetting Translation Requirements

All existing translation requirements can be deleted for one or more objects. The action can no longer be performed in the object is already in translation for one or more target languages. Objects that are affected by this function are reset back to the initial status of the translation process. The function can only be performed for translation requirements for editorial objects.

<a id="figure.auftragsverwaltung.uebersetzung.bedarfe.zurueck"></a>

![Image: resetting translation requirements](images/Uebersetzungsbedarf_zuruecksetzen.jpg)

**Figure 155. Resetting Translation Requirements**

Resetting translation requirements to administrative objects (such as default texts) is not possible, because there is no defined previous status here as opposed to translation requirements for editorial objects. Translation requirements for administrative objects are always created directly for all group languages.

To reset translation requirements, select the desired editorial objects in a requirement package and then select the entry in the context menu "Reset requirements" with the icon ![](images/Uebersetzung_zuruecksetzen.png). This function can also be accessed through the global menu and the toolbar.

When the action is performed, all required translations for all objects will be reset, except for required translations that are already in translation. After the action is successfully performed, the ODIS Creator interface is automatically updated.

##### <a id="uebersetzungsbedarfe.berechnen"></a>6.4.4.3. Determining Translation Requirements

Decisive for the respective deadline of translation requirements is the order context of the object to be translated. This means that if an object to be translated is linked to a scheduled order, then the deadline for the translation requirements is based on the set initial deployment date. This applies regardless of which location is ultimately assigned to the translation requirement.

Translation requirements, also when reusing objects, are always generated only for the target languages, that are necessary due to the links to the basic features and for which the respective editorial object does not have a corresponding translation yet. When reusing editorial objects, for which the user's editing language is still missing, new translation requirements are created for the authoring location. For all other target languages, translation requirements are generated for the user's location.

It is technically possible, that a user can reuse an unknown brand object, that is not yet in the user's editing language. The creator location of the respective editorial object being reused always assumes the costs incurred for the translation from the source language of the object to the editing language of the locations reusing it.

###### <a id="d4e4903"></a>6.4.4.3.1. Deadline Calculation for Translation Requirements

The initial deployment deadline of the order header is used as the basis for calculating the deadline for translation requirements, if the editorial object to be translated is created in the context of a scheduled order. For this, the requirement deadlines are determined based on the respective translation period, so that the translations scheduled for the initial deployment deadline are returned.

If bridge languages are necessary in the translation process, then the deadline for the bridge languages must be set correspondingly, so that there is still enough time after that to translate the subsequent target languages. This regulation applies within the respective location. For the authoring location of an editorial object, the ODIS Creator system makes sure that the deadline for translation requirements correlates to the initial deployment date.

When reusing editorial objects across multiple locations, it cannot be ensured that the additional target languages of the location reusing it are available in time for the initial deployment deadline. An integration of set bridge languages across locations is not possible when calculating the deadline. Other deadlines may be necessary for the reused objects through the integration , as for the other objects of the creation location.

###### <a id="d4e4908"></a>6.4.4.3.2. Reusing without Creator Usage

It may happen that an editorial object was set up and released by the brand that created it, however has not been used again. The option for a user from another brand to (re)use this object is then technically possible. If the calculation logic for translation requirements is carried out without the initial brand usage, then the other brand location will assume all translation costs incurred.

If the object is then used later by the actual creator brand, then this brand must still assume the additional translation costs for the target languages still missing. If a revision relevant to translation occurs later, then the creator brand is again considered as the leading brand.

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="6-4-3-sorting-translations.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="6-4-translation.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="6-4-5-commissioning-translations-manually.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">6.4.3. Sorting Translations </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 6.4.5. Commissioning Translations Manually</td></tr></table>
