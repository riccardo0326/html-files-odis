[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md) > [7.1. Editorial Object General Information](7-1-editorial-object-general-information.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.1.19. Additional Functions</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-1-18-templates.md">Prev</a> </td><th align="center" width="60%">7.1. Editorial Object General Information</th><td align="right" width="20%"> <a accesskey="n" href="7-2-recently-used-objects.md">Next</a></td></tr></table>

---

#### <a id="redaktion.weitere.funktionen"></a>7.1.19. Additional Functions

##### <a id="redaktion.weitere.funktion.inkonsistent.kompile.funktionstest"></a>7.1.19.1. Inconsistent Recompiled Function Tests

In the editing view, the function **Inconsistent recompiled function tests** is in the **File** menu. This allows recompiled function tests that were not able to be brought to a consistent status to be displayed, corresponding to the function described under [Section 5.2.10.1, “Recompiling all Function Tests”](5-2-10-additional-functions.md#administration.weitere.funktionen.neukompilieren "5.2.10.1. Recompiling all Function Tests"). The function tests are shown in a non-modal dialog, and you have the option to continue using the corresponding objects manually in the function library. Jumping to the object from the dialog is not provided here.

##### <a id="redaktion.weitere.funktion.systemtexte.importieren"></a>7.1.19.2. Import System Texts

In the editing view, the function **Import texts** is in the **File** menu. To select this menu item, you require to have both roles of author and location administrator (see [Section 3.3, “Roles and Teams”](3-3-roles-and-teams.md "3.3. Roles and Teams")). With this function, the system texts are imported into the ODIS Creator.

If you have selected the menu item, a dialog will open in which you can select and import the XML file with the system texts.

The system texts are divided into three categories:

- **General system texts** include standardized texts (such as "U/R/D-measuring cable (+) to"), which can be updated and added to by the import. For example, these are used in the function editor (see [Section 7.14, “Function Test Editor”](7-14-function-test-editor.md "7.14. Function Test Editor")).
- **Vehicle status texts** include texts for the vehicle status, which can be selected in the function test editor among other things, for example in the vehicle condition action element (see [Section 7.14, “Function Test Editor”](7-14-function-test-editor.md "7.14. Function Test Editor")).
- **Document categories** includes the document categories of supplemental documents (see [Section 7.10, “Supplemental documents”](7-10-supplemental-documents.md "7.10. Supplemental documents")), or the document type that can be selected for external references, for example in suspicious rules.

By selecting the XML file, the texts will then be imported to one of these three categories.

##### <a id="redaktion.weitere.funktion.invalid.efa.code"></a>7.1.19.3. Invalid EFA Codings

In the editing view, the function **Editorial objects with invalid EFA codings** is in the **File** menu. After the selection is made, a modal dialog opens displaying all editorial objects that have an invalid EFA coding through a previous import of EFA elements. An editorial object can be selected in the dialog. This will then be selected in the respective navigator via the **Open** button, and is opened in read mode in the associated editor.

##### <a id="redaktion.weitere.funktion.gueltigkeit"></a>7.1.19.4. Validity

In the used editorial object table, the status is displayed in the validity column for the reference to a control module description (see [Figure 216, “Used Table with Validity Statuses”](7-1-19-additional-functions.md#figure.redaktion.weitere.funktion.gueltigkeit "Figure 216. Used Table with Validity Statuses")). This information can be found in the following editorial objects:

- Control Module Configuration
- Diagnostic Object
- Measured Values Table
- Function test
- General test
- Test Procedure
- Traversal test

<a id="figure.redaktion.weitere.funktion.gueltigkeit"></a>

![Image: used table with validity statuses](images/sgb-gueltigkeit.png)

**Figure 216. Used Table with Validity Statuses**

The validity can assume the following statuses here:

- **Current** - For all currently valid control module descriptions.
- **From the last baseline** - For all control module descriptions from the last deployment.
- **Invalid** - For all control module descriptions that are no longer valid.

##### <a id="redaktion.weitere.funktion.verlinkung"></a>7.1.19.5. Cross-Brand Link

To set the object range for a brand deployment, it must be determined which objects are assigned to the brand. Due to performance reasons, this brand assignment is computed ahead of time in a brand relation.

The brand assignment occurs transitively through all use relationships based on the brand nodes in the equipment network. It is distinguished for the use relationships if they are relevant for the calculations of the brand assignment and the market allocation or not. The use relationships are grouped in a hierarchy for this. See

<a id="figure.redaktion.weitere.funktion.hierarchie"></a>

![Image: hierarchy of use relationships](images/hierarchie_verlinkung.png)

**Figure 217. Hierarchy of Use Relationships**

The editorial objects are grouped in the areas visible in [Figure 217, “Hierarchy of Use Relationships”](7-1-19-additional-functions.md#figure.redaktion.weitere.funktion.hierarchie "Figure 217. Hierarchy of Use Relationships"). Only the use relationships that point „from top to bottom and from left to right“ may be included for the brand inheritance. Relationships within the areas are always considered. This means that the use relationships marked in blue in [Figure 217, “Hierarchy of Use Relationships”](7-1-19-additional-functions.md#figure.redaktion.weitere.funktion.hierarchie "Figure 217. Hierarchy of Use Relationships") are included and the use relationships marked in red are not relevant for the brand evaluation.

Determining the required languages in the translation process applies analogously:

- The market allocation is carried out at the basic features in the equipment network.
- The inheritance of the market allocation is done the same as the inheritance of the brand allocation. This means that the use relationships marked in blue in [Figure 217, “Hierarchy of Use Relationships”](7-1-19-additional-functions.md#figure.redaktion.weitere.funktion.hierarchie "Figure 217. Hierarchy of Use Relationships") are included and the use relationships marked in red are not relevant for the market allocation inheritance.
- By calculating the inherited markets, the required target languages are then determined as a union of all languages assigned to these markets.

The following image shows a table, which contains the complete overview of everything for the computation of relevant use relationships for the brand and market allocations:

<a id="figure.redaktion.weitere.funktion.verwendung"></a>

![Image: overview of the use relationships for the computation of brand and market allocation](images/markenuebergreifende_verlinkung_verwendungsbeziehungen.png)

**Figure 218. Overview of the Use Relationships for the Computation of Brand and Market Allocation**

The [Figure 218, “Overview of the Use Relationships for the Computation of Brand and Market Allocation”](7-1-19-additional-functions.md#figure.redaktion.weitere.funktion.verwendung "Figure 218. Overview of the Use Relationships for the Computation of Brand and Market Allocation") shows between which types of editorial objects use relationships are allowed. For this, the table is limited to the types and editorial objects relevant for the deployment and translation. The types of parent objects are listed in the left column. The types of child objects are listed in the other columns. All combinations that are able to have a use relationship between them, are marked with 'yes'. The label 'Mig only' indicates use relationships that are only allowed within the context of migration to transfer the old data from DES. The red fields mark the use relationships that are not relevant for the brand and market allocation. An additional special case creates the green marked use locations between knowledge bases and vehicle models, since the inheritance of the brand and market relationship runs in the opposite direction of the use relationship from the child object (vehicle model) to the parent object (knowledge base).

##### <a id="redaktion.weitere.funktion.exportfunktion.equipmentexclusions"></a>7.1.19.6. Create EquipmentExclusions

In the editing view, the function **Create EquipmentExclusions** is in the **File** menu. To be able to select this menu item, you need the site administrator role (see [Section 3.3, “Roles and Teams”](3-3-roles-and-teams.md "3.3. Roles and Teams")). This function is used to export the EquipmentExclusions from ODIS Creator.

After you select the menu item, a dialog window opens in which the brands for which the EquipmentExclusions will be exported can be selected.

If you have selected one or more brands, the “OK” button becomes active. Confirming with the “OK” button exports the EquipmentExclusions to an xml file. If multiple brands are selected, a file is created for each brand. The storage location and the file name are configured in the administration.

<a id="figure.redaktion.weitere.funktion.exportfunktion.equipmentexclusions"></a>

![Figure: Creating EquipmentExclusions](http://127.0.0.1:55991/help/topic/MasterData_Client_Control/html/images/equ_excl.png)

**Figure 219. Creating EquipmentExclusions**

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-1-18-templates.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="7-1-editorial-object-general-information.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="7-2-recently-used-objects.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">7.1.18. Templates </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 7.2. Recently used objects</td></tr></table>
