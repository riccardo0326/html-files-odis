[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md) > [7.7. Control Module Tree](7-7-control-module-tree.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.7.10. Error Types</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-7-9-control-module-version-groups.md">Prev</a> </td><th align="center" width="60%">7.7. Control Module Tree</th><td align="right" width="20%"> <a accesskey="n" href="7-8-dtc-memory-tree.md">Next</a></td></tr></table>

---

#### <a id="sgbaum.Fehlerarten"></a>7.7.10. Error Types

It is possible to check fault location suspicions in relation to the fault type 1 and 2 for KWP or UDS control module descriptions.

##### <a id="sgbaum.Fehlerarten.Objekteditor"></a>7.7.10.1. Display in Object Editor

In addition to the respective suspicion rules of diagnostic objects and function codes, the suspicion of fault locations in a table can be checked.

For fault locations from UDS control module groups, no fault type 1 can be selected when linking (for example, suspicion rule in a diagnostic object); therefore, no value will be displayed for fault type 1 in the table. For KWP control module groups, fault type 1 and fault type 2 can be selected for a fault location and are also displayed respectively.

<a id="figure.redaktion.redaktioneditor"></a>

![Image: "suspected fault locations" - Table in editor](images/verdaechtige_Fehlerorte.png)

**Figure 287. "Suspected Fault Locations" - Table In Editor**

By double clicking on the fault location in the "suspected fault locations" table, you are taken to the fault location in the control module tree navigator, while a usage location dialog appears beforehand where you can select the respective path.

##### <a id="sgbaum.Fehlerarten.sgbaum"></a>7.7.10.2. Display from the Control Module Tree

It is also possible, for a concrete fault location to display all function codes and diagnostic objects (see [Figure 289, “Usage Locations of Fault Locations in the Function Library”](7-7-10-error-types.md#figure.redaktion.fktdgo "Figure 289. Usage Locations of Fault Locations in the Function Library")), that suspect these fault locations. This amount of concrete fault locations can also be limited.

<a id="figure.redaktion.menue_verdaechtigung"></a>

![Image: context menu at a fault location](images/Verdaechtigung_anzeigen_menu.png)

**Figure 288. Context Menu at a Fault Location**

To do this, select a fault location or a fault type 1/2 in the control module tree and select **Display suspicions** (see [Figure 288, “Context Menu at a Fault Location”](7-7-10-error-types.md#figure.redaktion.menue_verdaechtigung "Figure 288. Context Menu at a Fault Location")) in the menu. It opens a dialog, which displays all function codes or diagnostic objects that suspect the corresponding fault location in the name context of the higher-level control module group. Depending on the selected fault type node, the amount of results is still filtered down to the respective fault type 1 or to the combination of fault type 1 and 2.

The display of diagnostic objects or function codes is only possible at the used locations. For example, a diagnostic object under a fault location is only then displayed if this link has no fault type 1 or 2.

<a id="figure.redaktion.fktdgo"></a>

![Image: usage locations of fault locations in the function library](images/verwendungsstellen_auf_fehlerorte.png)

**Figure 289. Usage Locations of Fault Locations in the Function Library**

When there is a fault location suspicion, it is always selected in the context of a control module group (BV). In the function test editor, "fault location" is at an IF command (see [Section 7.14.13.1, “Action Element - IF Command”](7-14-13-category-process.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Ablauf.IF-Anweisung "7.14.13.1. Action Element - IF Command"))<Name of BV> -> <Name of fault location> [-> <Fault type 1>] [-> <Fault type 2>] and the base version context for the respective fault location is in the action element editor (see [Figure 418, “IF Command with Symptoms Action Element”](7-14-13-category-process.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Ablauf.IF-Symptome "Figure 418. IF Command with Symptoms Action Element")). The BV context for the fault location in the suspicion rule is displayed in the diagnostic objects.

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-7-9-control-module-version-groups.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="7-7-control-module-tree.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="7-8-dtc-memory-tree.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">7.7.9. Control Module Version Groups </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 7.8. DTC Memory Tree</td></tr></table>
