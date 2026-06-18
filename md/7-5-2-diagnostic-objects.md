[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md) > [7.5. Knowledge base](7-5-knowledge-base.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.5.2. Diagnostic objects</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-5-1-knowledge-base-root-node.md">Zurück</a> </td><th align="center" width="60%">7.5. Knowledge base</th><td align="right" width="20%"> <a accesskey="n" href="7-5-3-specify-the-used-relationship.md">Weiter</a></td></tr></table>

---

#### <a id="diagnoseobjekt"></a>7.5.2. Diagnostic objects<a id="d4e11865"></a>

Diagnostic objects create the diagnostic object tree within a knowledge base. They control with this the diagnostic process in use. The validity of a diagnostic object in actual usage is expressed through variant rules. Diagnostic objects contain allocations to function tests (see [Section 7.6, “Function Library”](7-6-function-library.md "7.6. Function Library")) and documentation references (see [Section 7.10, “Supplemental documents”](7-10-supplemental-documents.md "7.10. Supplemental documents")), that can likewise be qualified through variant rules. A suspicion rule can be assigned to a diagnostic object.

A diagnostic object is always assigned to exactly one knowledge base, which can however be used at various locations in the diagnostic object tree within a knowledge base (see [Section 7.1.8, “Copy Editorial Objects”](7-1-8-copy-editorial-objects.md "7.1.8. Copy Editorial Objects")). However, no recursive reuse is possible. If you try to reuse a diagnostic object "DGO A" in the diagnostic object structure under "DGO A", then a message will appear and reuse is blocked.

##### <a id="diagnoseobjekt.anlegen"></a>7.5.2.1. Create New Diagnostic Object<a id="d4e11874"></a>

You can create a new diagnostic object by selecting an already existing diagnostic object and then clicking on the menu item **New parallel node > Diagnostic object** in the context menu or click on **Parallel node > Diagnostic object** in the Insert selection menu.

A new diagnostic object can also be created directly under an already existing knowledge base root node. After the knowledge base root node is selected, the menu item **Subnode > Diagnostic object** must be selected in the context menu or in the selection menu.

##### <a id="diagnoseobjekt.attribute"></a>7.5.2.2. Diagnostic Object Attributes<a id="d4e11884"></a>

<a id="figure.redaktion.diagnoseobjekt.attribute"></a>

![Image: diagnostic object attributes](images/dgo_attribute.png)

**Abbildung 249. Diagnostic Object Attributes**

**Migration protection:**

This attribute is explained in [Section 7.1.1, “Creating a New Editorial Object”](7-1-1-creating-a-new-editorial-object.md "7.1.1. Creating a New Editorial Object").

**Transfer of external links:**

The document references to diagnostic objects can be inherited (see 'document inheritance' field), when creating a new associated diagnostic object ('used' relationship).

**Internal:**

This attribute is explained in [Abschnitt 7.5.1.2, „Knowledge Base Root Node Attributes“](7-5-1-knowledge-base-root-node.md#wissensbasis.attribute "7.5.1.2. Knowledge Base Root Node Attributes").

**P-differ:**

This attribute is explained in [Abschnitt 7.5.1.2, „Knowledge Base Root Node Attributes“](7-5-1-knowledge-base-root-node.md#wissensbasis.attribute "7.5.1.2. Knowledge Base Root Node Attributes").

**Guided Function:**

The diagnostic object and the referenced test programs can be selected in ODIS Service through the Guided Functions in the network diagram (this attribute is inheritable).

**General function:**

The diagnostic object and the referenced test programs can be selected in ODIS Service through the "General function" tab.

**Order:**

This flag indicates that the order of the diagnostic objects in GFF in ODIS Service is relevant.

##### <a id="diagnoseobjekt.variantenregel"></a>7.5.2.3. Creating a Variant Rule in a Diagnostic Object<a id="d4e11921"></a><a id="d4e11924"></a>

Variant rules in a diagnostic object will restrict its validity. Here any number of variant expressions can be combined in a rule using Boolean algebra. The variant rule is edited directly in the diagnostic object editor.

To create a variant rule, the table editor must be activated using the ![](images/plus.png)- symbol. If there is a previous selection of an existing variant rule, the new variant rule will be added under the selected variant rule. When selecting one or more variant rules in an associated block, they can be sorted or moved up or down using the ![](<images/Pfeil hoch.png>) ![](<images/Pfeil runter.png>)symbols. The link between strings of the expression is done with logical operators (AND, OR, NOT, ...) and parentheses. The selection of the type (basic features, control module equipment, query, VIN, control module-dependent versions, importer, and dealer) (see [Abbildung 250, „Type Selection“](7-5-2-diagnostic-objects.md#figure.redaktion.wissensbasis.variantenregel "Abbildung 250. Type Selection")) and the value (in [Abbildung 251, „Value Selection“](7-5-2-diagnostic-objects.md#figure.redaktion.wissensbasis.variantenregel.auswahlobjekt "Abbildung 251. Value Selection") from editorial objects equipment network) complete the variant expression. The value selection can be achieved here through the dialog displayed in the [Abbildung 251, „Value Selection“](7-5-2-diagnostic-objects.md#figure.redaktion.wissensbasis.variantenregel.auswahlobjekt "Abbildung 251. Value Selection") or by typing the desired system name directly in the table cell (with auto completion). For **Questions**, the default text selection dialog will open [Figure 342, “Default Texts”](7-14-3-use-cases.md#figure.Funktionstesteditor.Allgemeine_Funktionalitaet.Standardtexte "Figure 342. Default Texts").

The term ‘control module-dependent version’ includes the following types: hardware version, hardware part number, software part number, software version, ODX file version and IdentMaster data. The value for these control module-dependent variants can be selected using the dialog shown in [Abbildung 252, „Value Selection Using IdentMaster Data as an Example“](7-5-2-diagnostic-objects.md#figure.redaktion.wissensbasis.variantenregel.sgabhaengigeauswahl "Abbildung 252. Value Selection Using IdentMaster Data as an Example"). The importer and dealer values are free text fields. The ODX file identifier variant rule can be configured both as free text and as a dialog selection and must not contain the EV main version. This EV main version is automatically removed when selected via the selection dialog.

With the ![](images/minus.png)- symbol, a string of the variant expression can be removed again.

<a id="figure.redaktion.wissensbasis.variantenregel"></a>

![Image: type selection](images/variantenregel.png)

**Abbildung 250. Type Selection**

  

<a id="figure.redaktion.wissensbasis.variantenregel.auswahlobjekt"></a>

![Image: value selection at equipment network example](images/variantenregel_auswahlobjekt.png)

**Abbildung 251. Value Selection**

##### <a id="diagnoseobjekt.variantenregel.sgabhaengigeauswahl"></a>7.5.2.4. Control Module-Dependent Variants Selection Dialog

The following illustration [Abbildung 252, „Value Selection Using IdentMaster Data as an Example“](7-5-2-diagnostic-objects.md#figure.redaktion.wissensbasis.variantenregel.sgabhaengigeauswahl "Abbildung 252. Value Selection Using IdentMaster Data as an Example") shows the dialog for selecting the value for the types of control module-dependent variants.

<a id="figure.redaktion.wissensbasis.variantenregel.sgabhaengigeauswahl"></a>

![Image: value selection using IdentMaster data as an example](images/variantenregel_sgabhaengig_auswahlobjekt.png)

**Abbildung 252. Value Selection Using IdentMaster Data as an Example**

- Control module

  Defines the short name of the control module group for which the identification value is to be checked. Input is mandatory and content is entered using the “editorial objects selection dialog” [Abbildung 253, „Editorial objects selection dialog“](7-5-2-diagnostic-objects.md#figure.diagnoseobjekt.variantenregel.sgabhaengigeauswahl.ecushortname "Abbildung 253. Editorial objects selection dialog").
- Ident Key (RDID/long name)

  Content is entered as free text. Input is mandatory and is only shown for the “IdentMaster data” type. An RDID or long name is expected as the value.
- IdentMaster

  Defines the value that the control module must return in order to fulfill the variant rule. Input is mandatory and is entered for the “ODX file identifier” type using the “editorial objects selection dialog”, in which only control module variants may be selected. Input for other types is free text. The name of the field is dynamic and the name updates depending on the type that is selected.

The parameters set in the selection dialog will be displayed in the “Value” column as follows: **Control Module;Ident Key;IdentMaster**. Value selection using IdentMaster data as an example.

<a id="figure.diagnoseobjekt.variantenregel.sgabhaengigeauswahl.ecushortname"></a>

![Image: editorial object selection dialog](images/variantenregel_sgabhaengig_ecushortname.png)

**Abbildung 253. Editorial objects selection dialog**

##### <a id="diagnoseobjekt.verdachtsregel"></a>7.5.2.5. Creating a Suspicion Rule in a Diagnostic Object<a id="d4e11997"></a><a id="d4e12000"></a>

There are various options to create a suspicion rule. On one hand, a new rule can be created through the ![](images/plus.png)- symbol. On the other hand, a DTC memory object from the control module tree can be dragged to the suspicion rule list via drag and drop, in order to create a suspicion rule with a string, that the dragged DTC memory object ([DTC](11-appendix.md#dtc "DTC")) contains. Error locations from various reference tables can be included in the suspicion rule list. If multiple DTCs are dragged per drag and drop, then a separate suspicion rule is created for each object.

The list of suspicion rules for a diagnostic object can also be sorted manually and persistently if necessary. By selecting a suspicion rule, it can be sorted or moved up and down with the ![](<images/Pfeil hoch.png>) ![](<images/Pfeil runter.png>)symbols. After saving and opening again, the order that was previously set using the arrow keys will be visible again.

<a id="figure.redaktion.wissensbasis.verdachtsregel"></a>

![Image: new suspicion rule](images/verdachtsregel.png)

**Abbildung 254. New Suspicion Rule**

Double-clicking on a suspicion rule in the suspicion rule list table opens an auxiliary editor in a new tab (parallel to the editor that is currently open) (see [Abbildung 255, „Edit Suspicion Rule“](7-5-2-diagnostic-objects.md#figure.redaktion.wissensbasis.verdachtsregel.bearbeiten "Abbildung 255. Edit Suspicion Rule")) for editing the suspicion rule. No other suspicion rules can be edited as long as the auxiliary editor is open. The supplemental editor allows the name, the importance as well as the individual suspicion expressions (lines) to be edited. Suspicion rules allow all symptom types (DTC, EFA code, TSB) to be used in a rule. Here any amount of suspicion expressions can be combined in a rule using Boolean algebra. Using the ![](images/plus.png)- symbol, additional suspicion expression strings can be added. With the ![](images/Minus01.png)- symbol, a suspicion rule string can be removed. To add the values of symptom types to a suspicion expression, there are specialized input options. To input an EFA code, the EFA code assist (see [Section 7.17, “Standard Fault Description Language (EFA)”](7-17-standard-fault-description-language-efa.md "7.17. Standard Fault Description Language (EFA)")) is used; DTCs can be entered through an editorial object selection dialog or (see [Abbildung 256, „Enter DTC for Suspicion Expression“](7-5-2-diagnostic-objects.md#figure.redaktion.wissensbasis.verdachtsregel.bearbeiten.dnd "Abbildung 256. Enter DTC for Suspicion Expression")) from the control module tree using drag and drop, and TSBs are entered directly into the table cell. Depending on the error code, you can also give the fault type 1 and fault type 2 here.

Just like the ability to sort the suspicion rules in the list, which was described above, it is also possible to sort the individual lines within a suspicion rule. Selecting a line of the suspicion rule means this can be sorted or moved up and down with the ![](<images/Pfeil hoch.png>) ![](<images/Pfeil runter.png>)symbols.

<a id="table.hinweis.verdachtsregel"></a>

<table border="1" summary="Note on sorting suspicion rule lines"><colgroup><col align="center"/><col align="left"/></colgroup><tbody valign="top"><tr><td align="center" valign="top"><span class="inlinemediaobject"><img alt="Note symbol" src="images/info.png"/></span></td><td align="left" valign="top"><span class="bold"><strong>Note:</strong></span> When moving, the lines including all values (Boolean operator, parentheses, etc.) are moved. When this happens, the previously-defined Boolean logic may not longer be technically correct. The author is then responsible here for ensuring that the suspicion rule logic is correctly defined in the technical sense. No technical support is provided here for the Boolean algebra and for the parentheses.</td></tr></tbody></table>

**Tabelle 56. Note on sorting suspicion rule lines**

By clicking the button in the lower section of the supplemental editor, the edited suspicion rule is either applied (**Apply**) or discarded (**Cancel**).

<a id="figure.redaktion.wissensbasis.verdachtsregel.bearbeiten"></a>

![Image: editing a suspicion rule](images/verdachtsregel_subeditor.png)

**Abbildung 255. Edit Suspicion Rule**

<a id="figure.redaktion.wissensbasis.verdachtsregel.bearbeiten.dnd"></a>

![Image: entering DTC for suspicion expression](images/verdachtsregel_subeditor_dnd.png)

**Abbildung 256. Enter DTC for Suspicion Expression**

If a suspicion rule was edited and applied, then the author can also see its content in the object editor. This function is also available, if you have not opened the diagnostic object for editing. Here, the respective rule must be selected in the suspicion rule list and its content is automatically displayed in the **suspicion rule** table.

<a id="figure.redaktion.wissensbasis.verdachtsregel.ansehen"></a>

![Image: viewing a suspicion rule](images/verdachtsregel_anzeige.png)

**Abbildung 257. Viewing a Suspicion Rule**

The control module relationship to the DTC can now be understood and checked in a suspicion rule for every DTC object in the **suspicion rule** table; use the context menu function **Display path** to do this. The dialog window will open from [Abbildung 258, „Display DTC Control Modules Context“](7-5-2-diagnostic-objects.md#figure.redaktion.wissensbasis.verdachtsregel.pfadanzeige "Abbildung 258. Display DTC Control Modules Context"), in which the DTC path from the suspicion rule is displayed. This function is also available if you have not opened the diagnostic object for editing.

The results can be limited to the individual brand using the checkbox **only particular brand** in the usage location dialog. If you set knowledge base as the filter, you can also limit the display to a concrete knowledge base. You can also have invalid control modules displayed by marking the control field **All ECU Usage Locations**. These will be displayed in gray text.

<a id="figure.redaktion.wissensbasis.verdachtsregel.pfadanzeige"></a>

![Image: display DTC control modules context](images/verdachtsregel_pfadanzeige.png)

**Abbildung 258. Display DTC Control Modules Context**

##### <a id="diagnoseobjekt.regelkopieren"></a>7.5.2.6. Copy of Variant/Suspicion Rules Between Diagnostic Objects<a id="d4e12099"></a><a id="d4e12102"></a>

To facilitate the authors, defined rules can be copied from a diagnostic object to another diagnostic object. It is possible to copy either suspicion or variant rules or both rules together. To get the source object on the clipboard, the existing copy function (menu, toolbar, context menu) is used. Rules can only be copied from exactly one diagnostic object, however they can be added to multiple diagnostic objects at the same time. The target objects must be in the "in processing" status, however they do not need to be checked out by the author. To add source object rules from the clipboard to diagnostic objects, the target objects must be selected in the navigation tree and then the desired menu item from [Abbildung 259, „Menu to Copy Variant/Suspicion Rules“](7-5-2-diagnostic-objects.md#figure.redaktion.diagnoseobjekt.regelkopieren "Abbildung 259. Menu to Copy Variant/Suspicion Rules") must be performed. The menu items can be reached through the context menu and also through the main menu **Insert >> Insert only ...**

<a id="figure.redaktion.diagnoseobjekt.regelkopieren"></a>

![Image: menu to copy variant/suspicion rules](images/regelkopieren_menue.png)

**Abbildung 259. Menu to Copy Variant/Suspicion Rules**

Possible restrictions on the copying and insertion operations for rules are:

- The source objects has no variant rule.
- The source objects has no suspicion rule.
- The source object only has one of the two rules, but both should be inserted.
- A referenced object from a rule to be inserted is not visible to you in the Creator.

If one of the restrictions mentioned above occurs, then the entire item is canceled and none of the target objects are changed.

- One or more of the target objects are not in the **in processing** status.
- One or more of the target objects are locked by another user (checked out).
- One or more of the target objects already have variant/suspicion rules - an overwrite of rules is not wanted.

This applies to the three items given above: you are informed of any existing restrictions with a dialog after the insert operation. The editing of other target objects remains unaffected.

##### <a id="diagnoseobjekt.werkzeuge"></a>7.5.2.7. Using a Tool in a Diagnostic Object

In the "Used tools" table, tools can be assigned to the diagnostic object. Using the ![](images/plus.png) and ![](images/Minus01.png) icons, lines can be added or removed.

<a id="figure.redaktion.diagnoseobjekt.werkzeug"></a>

![Image: Used tools](images/werkzeugliste_verwendung.png)

**Abbildung 260. Used Tools Table**

  

In the **tool number/name** column, the plain text of the selected text ID is displayed. The display is in the data language that is currently set. In editing mode, the display is in the editing language. If no translation in this language is available for the text ID, the text is displayed in German (de-DE).

Only available for selection are the text IDs of categories, for which the "Used tools" usage location is selected. The selection is done with the dialog "text library selection", the same as for questions in variant rules.

If for the selected TextID there is an automatically created entry in the categories **023 - Tool (code in front)** or **024 - Tool (code behind)** during the tool list import, the image number created during the import is displayed in the image number column. The image number column cannot be edited.

In the logical link column, the used tools are linked to each other through the logical operators **AND** and **OR**. The logical expressions can be grouped using parentheses in the columns **"("** and **")"**.

###### <a id="diagnoseobjekt.werkzeug.vererbung"></a>7.5.2.7.1. Inheriting Tools

With the "Inherit tools" function, it is possible to copy the allocation of the used tools for a selected diagnostic object automatically to all of the subordinate diagnostic objects. This function can be accessed in the context menu ([Abbildung 261, „Inherit Tools Context Menu“](7-5-2-diagnostic-objects.md#figure.redaktion.diagnoseobjekt.werkzeug.vererbung "Abbildung 261. Inherit Tools Context Menu")) and in the "Edit" menu.

<a id="figure.redaktion.diagnoseobjekt.werkzeug.vererbung"></a>

![Image: Inherit tools context menu](images/werkzeugliste_vererbung.png)

**Abbildung 261. Inherit Tools Context Menu**

  

Because the allocation of the used tools can only be changed for the diagnostic objects in processing, all subordinate diagnostic objects must be set to the **in processing** status. For released diagnostic objects, a new working version is generated for this in the current order context. If this is not possible, because, for example, a different team already created a working version or because a diagnostic object is checked out for editing by another used, a message (see [Abbildung 262, „Error Message During Inheritance“](7-5-2-diagnostic-objects.md#figure.redaktion.diagnoseobjekt.werkzeug.vererbung_meldung "Abbildung 262. Error Message During Inheritance")) is given and skips copying for this diagnostic object and all subordinate objects.

<a id="figure.redaktion.diagnoseobjekt.werkzeug.vererbung_meldung"></a>

![Image: error message during inheritance](images/werkzeugliste_vererbung_meldung.png)

**Abbildung 262. Error Message During Inheritance**

  

If a subordinate diagnostic object already has an allocation of used tools, this is added. All assigned tools from the inherited diagnostic object that are not included in the allocation of the subordinate diagnostic object, are added. They will be added at the end of the table without a logical link.

If inheritance could not be performed for at least one subordinate diagnostic object, a notification will be created for the current user who had accessed the Inherit tools function after processing is complete. This notification references a log file where all diagnostic objects for which inheritance could not be performed are listed with all the detected conflicts when inheritance is performed. The user is alerted about the notification with a brief message.

##### <a id="drag.allgemein"></a>7.5.2.8. Drag and Drop for Suspicion Rules

###### <a id="drag.navigationsbaum"></a>7.5.2.8.1. Drop in Navigation Tree

With this implementation, it is possible for you to drag multiple selected DTC memory entries per drag and drop to a diagnostic object in the knowledge base navigation tree. If the diagnostic object was already checked out, the drop behaves the same as that described in [Abschnitt 7.5.2.8.2, „Drop in the Object Editor“](7-5-2-diagnostic-objects.md#drag.objekteditor "7.5.2.8.2. Drop in the Object Editor") when dropping into an object editor. The details can be seen there. If the object is still not checked out by you, then an automatic checkout will be initiated. If the checkout does not work for some reason, then a corresponding error message is displayed (the same occurs after double clicking in the navigation tree) and the entire drag and drop is canceled. A selection dialog is presented after a checkout is successful, as described in [Abschnitt 7.5.2.8.3, „Selection Dialog for One or More Rules“](7-5-2-diagnostic-objects.md#drag.auswahldialog "7.5.2.8.3. Selection Dialog for One or More Rules"), if more than one DTC memory entry is in the amount of dragged objects. If you pressed the „Cancel“ button in the selection dialog, the entire drag and drop action is canceled. Otherwise the selected process is performed and the diagnostic object is automatically checked in. If you only selected a DTC memory entry, a suspicion rule is created with this DTC memory entry. After checking in successfully, the changed and persisting diagnostic object is presented in a read-only object editor. This procedure is performed as an operation on a navigation tree and contains a save action (check in). The object editor displayed at the end is read-only. For these reasons, a drag and drop action cannot be undone by entering 'CTRL Z'.

###### <a id="drag.objekteditor"></a>7.5.2.8.2. Drop in the Object Editor

You have the option to use drag and drop to create suspicion rules in the suspicion rule list table of the diagnostic object editor. To do this, the diagnostic object must be checked out, because all read-only object editors are automatically closed when the drag process starts. It is possible to drag multiple DTC memory entries to the object editor at the same time. If this process is selected, then the selection dialog described in [Abschnitt 7.5.2.8.3, „Selection Dialog for One or More Rules“](7-5-2-diagnostic-objects.md#drag.auswahldialog "7.5.2.8.3. Selection Dialog for One or More Rules") appears after dropping the DTC memory entries in the object editor. Depending on the selection, the corresponding selected procedure is then initiated or the entire action is canceled. The most important difference to the process from [Abschnitt 7.5.2.8.1, „Drop in Navigation Tree“](7-5-2-diagnostic-objects.md#drag.navigationsbaum "7.5.2.8.1. Drop in Navigation Tree") is that the change to the diagnostic object is not saved here. You must save the object editor and the added suspicion rule(s) in a separate step.

###### <a id="drag.auswahldialog"></a>7.5.2.8.3. Selection Dialog for One or More Rules

The dialog asks if you would like to create only one suspicion rule with all DTC memory objects as „value/fault location“ or multiple suspicion rules each with a DTC memory object as „value/fault location“. You also still have the option to cancel the entire action with the „Cancel“ button in the dialog. This selection dialog appears for both drop operations of DTC memory entries to diagnostic objects described in [Abschnitt 7.5.2.8.1, „Drop in Navigation Tree“](7-5-2-diagnostic-objects.md#drag.navigationsbaum "7.5.2.8.1. Drop in Navigation Tree") and [Abschnitt 7.5.2.8.2, „Drop in the Object Editor“](7-5-2-diagnostic-objects.md#drag.objekteditor "7.5.2.8.2. Drop in the Object Editor"), if more than one DTC memory entry is contained in the object volume of the drop operation.

If you select the „one rule“ button in the selection dialog, then all DTC memory entries from the volume of objects in the drop operation are combined in one suspicion rule. The following conditions apply to this:

- The name of the new suspicion rule is automatically created and always reads as new suspicion rule x, (x is the amount of currently existing suspicion rules +1). An analysis of names of suspicion rules already existing is not performed here. If suspicion rules previously created through the drag and drop method are not renamed, then suspicion rules with the same name may result under certain circumstances (for example, suspicion rules were deleted again in the meantime). It is therefore recommended to change the name of the suspicion rule after it is created automatically.
- The quantifier of the suspicion rule is set to the „medium“ value and can be changed later.
- The strings within the suspicion rule (one line per DTC memory entry) are linked with „OR“.
- If the diagnostic object already contains a suspicion rule, then the newly created suspicion rule is attached to the lower end of the suspicion rule list for the diagnostic object.

###### <a id="drag.verdachtsregeleditor"></a>7.5.2.8.4. Drop in the Suspicion Rule Editor

The drop from DTC memory entries into the suspicion rule editor is permitted in the entire suspicion rule table. Two cases are differentiated for this, which are described in further detail in this section. If a drop occurs somewhere in the suspicion rule table, where there is **NO** row, for example, under the last row or on the header row in the table, then new suspicion rule rows are automatically created. One line is created per DTC memory entry. Every newly created row has the „fault location“ entry in the „type“ column, the respective DTC memory entry in the „value/fault location“ column and „n/a“ in the „fault location type 2“ column. The new rows are always inserted under the rows that already exist. The new rows are all linked to each other with „OR“. „OR“ also connects the already existing rows.

The other case is dropping into the existing content in the suspicion rule table. This will replace the existing content with the new content at this location.

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-5-1-knowledge-base-root-node.md">Zurück</a> </td><td align="center" width="20%"><a accesskey="u" href="7-5-knowledge-base.md">Nach oben</a></td><td align="right" width="40%"> <a accesskey="n" href="7-5-3-specify-the-used-relationship.md">Weiter</a></td></tr><tr><td align="left" valign="top" width="40%">7.5.1. Knowledge Base Root Node </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Zum Anfang</a></td><td align="right" valign="top" width="40%"> 7.5.3. Specify the "Used" Relationship</td></tr></table>
