[ODIS Creator Help](odis-creator-help.md) > [3. ODIS Creator Basic Information](3-odis-creator-basic-information.md) > [3.2. Program Structure](3-2-program-structure.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">3.2.7. Preconfiguration Selection Dialogs</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="3-2-6-tables-and-lists.md">Prev</a> </td><th align="center" width="60%">3.2. Program Structure</th><td align="right" width="20%"> <a accesskey="n" href="3-2-8-separating-views.md">Next</a></td></tr></table>

---

#### <a id="auswahldialog.vorbelegung.arten"></a>3.2.7. Preconfiguration Selection Dialogs

The following cases are distinguished:

- Opening of selection dialog for revision
- Opening of selection dialog for new entries

##### <a id="auswahldialog.vorbelegung.%C3%BCberarbeitung"></a>3.2.7.1. Selection Dialog for Revision

If you open the selection dialog in the context of an existing entry, then the corresponding editorial or data object will be displayed and selected. For example, if a [**DTC**](11-appendix.md#dtc "DTC") is set as a symptom in an IF command in a function test, then the object tree will be opened and the [**DTC**](11-appendix.md#dtc "DTC") preselected when revising the symptom in the respective selection dialog.

The memory status of the source object is irrelevant for the system behavior. If you open a function test for editing and there is an IF command with a [**DTC**](11-appendix.md#dtc "DTC") revise 'XYZ' in it, then the tree structure is opened in the respective dialog and the [**DTC**](11-appendix.md#dtc "DTC") 'XYZ' is selected. Then change the selection to the [**DTC**](11-appendix.md#dtc "DTC") 'ABC' and close the dialog with OK. If you open the dialog again now, then the [**DTC**](11-appendix.md#dtc "DTC") 'ABC' is selected this time and does not depend on if you have persisted the [**DTC**](11-appendix.md#dtc "DTC") change previously or not.

If the path to an object is not unique, then the path that is found first by the system will open. Then, for example, a linked diagnostic object can be used at multiples places in a knowledge base. The selection dialog for fault locations offers two options for the path display (navigation and log). To abstract from the multiplicity of control module instances through the various vehicle projects, the preselection for fault locations is always displayed in the log view.

##### <a id="auswahldialog.vorbelegung.neu"></a>3.2.7.2. Selection Dialog for New Entries

If you open a selection dialog for a new entry, then the object that was selected when you last confirmed the dialog with OK, is preselected. For this the system memorizes the entire object path so that the same context can be restored again. However, this information is only saved for the duration of a session and does not carry over to other sessions. The preconfigurations are discarded as soon as you log out of the system.

###### <a id="auswahldialog.vorbelegung.neu.redaktionsobjekt"></a>3.2.7.2.1. Editorial Object Selection Dialog

This selection dialog is used for all editorial object types. If the simple rule would be applied that the last object is always reselected, then it would not cover enough area, because, for example, if this dialog was used last time to search an equipment network for a variant rule, however now a diagnostic object is being searched for. Because of this, this dialog is preconfigured based on the editorial object type. The data to preconfigure this dialog for equipment network, function library, knowledge base, DTC memory, control module description and supplemental document objects is considered and saved separately. In addition to this, it will differentiate when selecting control module description objects if your selection was made through the navigation ([Figure 39, “Selection Dialog for Editorial Objects in the form of Control Module Description Objects by means of Object Structure”](3-2-7-preconfiguration-selection-dialogs.md#auswahldialog.vorbelegung.auswahl.sgb.objekt "Figure 39. Selection Dialog for Editorial Objects in the form of Control Module Description Objects by means of Object Structure")) or through the vehicle projects ([Figure 40, “Selection Dialog for Editorial Objects in the form of Control Module Description Objects by means of Vehicle Projects”](3-2-7-preconfiguration-selection-dialogs.md#auswahldialog.vorbelegung.auswahl.sgb.fahrzeug "Figure 40. Selection Dialog for Editorial Objects in the form of Control Module Description Objects by means of Vehicle Projects")).

<a id="auswahldialog.vorbelegung.auswahl.sgb.objekt"></a>

![Image: selection dialog for editorial objects in the form of control module description objects by means of object structure](images/Steuergeraetebeschreibungsobjekte_mittels_Objektstruktur.png)

**Figure 39. Selection Dialog for Editorial Objects in the form of Control Module Description Objects by means of Object Structure**

<a id="auswahldialog.vorbelegung.auswahl.sgb.fahrzeug"></a>

![Image: selection dialog for editorial objects in the form of control module description objects by means of vehicle projects](images/Steuergeraetebeschreibungsobjekte_mittels_Fahrzeugprojekten.png)

**Figure 40. Selection Dialog for Editorial Objects in the form of Control Module Description Objects by means of Vehicle Projects**

###### <a id="auswahldialog.vorbelegung.neu.diagnose"></a>3.2.7.2.2. Diagnostic Service Selection Dialog

The dialog to select an operation or a service can be opened from the (ASAM) Ecukom dialog of the function test editor. If an operation or a service is already displayed in (ASAM) Ecukom, then the respective entry will be selected in the selection field ([Figure 41, “Operations/Services Selection Dialog”](3-2-7-preconfiguration-selection-dialogs.md#auswahldialog.vorbelegung.auswahl.sgb.dienste "Figure 41. Operations/Services Selection Dialog")).

<a id="auswahldialog.vorbelegung.auswahl.sgb.dienste"></a>

![Image: operations/services selection dialog](images/Auswahldialog_fuer_Operationen_Dienste.png)

**Figure 41. Operations/Services Selection Dialog**

###### <a id="auswahldialog.vorbelegung.neu.parameter"></a>3.2.7.2.3. Parameter Selection Dialog

Likewise, the dialog to select a parameter can be accessed from the (ASAM) Ecukom dialog of the function test editor. If this dialog is called up in the context of an existing entry in a table, then the parameter path displayed there is automatically selected after opening the dialog ([Figure 42, “Parameter Selection Dialog”](3-2-7-preconfiguration-selection-dialogs.md#auswahldialog.vorbelegung.auswahl.parameter "Figure 42. Parameter Selection Dialog")).

<a id="auswahldialog.vorbelegung.auswahl.parameter"></a>

![Image: parameter selection dialog](images/Auswahldialog_fuer_Parameter.png)

**Figure 42. Parameter Selection Dialog**

###### <a id="auswahldialog.vorbelegung.neu.eintrag"></a>3.2.7.2.4. Entry Selection Dialog

The dialog to select a parameter can be accessed from the (ASAM) Ecukom dialog parameter table. If this dialog is called up in the context of an existing table entry, then the ID displayed there is preselected together with the corresponding RDID in the dialog selection field ([Figure 43, “Entry Selection Dialog”](3-2-7-preconfiguration-selection-dialogs.md#auswahldialog.vorbelegung.auswahl.eintrag "Figure 43. Entry Selection Dialog")).

<a id="auswahldialog.vorbelegung.auswahl.eintrag"></a>

![Image: entry selection dialog](images/Auswahldialog_Eintrag.png)

**Figure 43. Entry Selection Dialog**

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="3-2-6-tables-and-lists.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="3-2-program-structure.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="3-2-8-separating-views.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">3.2.6. Tables and Lists </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 3.2.8. Separating Views</td></tr></table>
