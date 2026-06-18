[ODIS Creator Help](odis-creator-help.md) > [6. ODIS Creator Order Management Process](6-odis-creator-order-management-process.md) > [6.4. Translation](6-4-translation.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">6.4.7. Translation Packages</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="6-4-6-translation-jobs.md">Prev</a> </td><th align="center" width="60%">6.4. Translation</th><td align="right" width="20%"> <a accesskey="n" href="6-4-8-monitoring-translations.md">Next</a></td></tr></table>

---

#### <a id="uebersetzungspakete"></a>6.4.7. Translation Packages

Translation requirements are included in translation packages through an automatic or manual package assembly. The included editorial objects are given in the translation with that (outside of ODIS Creator).

A translation package (see [Figure 161, “Translation Packages View”](6-4-7-translation-packages.md#figure.auftragsverwaltung.uebersetzung.paketeansicht "Figure 161. Translation Packages View")) includes information about the target and source language, editorial object location, the scheduled deadline, the package creator, information about the Trados matches, as well as the version, status, type, brand name, initial deployment date and the author of the objects in the package.

Every package is named according to the following schema: <Brand\_Location code\_Source language\_Target language\_Date\_Order number>, whereby the order number is a 9-digit number with the prefix "OC".

Translation packages always have one of the following statuses:

- ![](images/translation_package.png) **Exported:** the package was exported from ODIS Creator.
- ![](images/translation_package.png) **Exported (package name in orange):** the package is a complaint package (see [Section 6.4.10, “Translation Disputes”](6-4-10-translation-disputes.md "6.4.10. Translation Disputes")), which has been created by ODIS Creator.
- ![](images/problem_error.png) **Error:** the package could not be imported into GoCAT/DELS. The translation coordinator or the team of translation coordinators receives a notification for the translation package that an error occurred when importing into GoCAT/DELS.
- ![](images/translation_package_rejected.png) **Rejected:** the package was rejected by GoCAT/DELS. The translation coordinator or the team of translation coordinators receives a notification for the translation package with the rejection comments from GoCAT/DELS. The package can be exported again or reset by the translation coordinator.
- ![](images/translation_package_imported_gocat.png) **In translation:** the package was imported successfully into GoCAT/DELS and is now in translation.
- ![](images/translation_package_imported.png) **Imported:** the package could be imported into ODIS Creator successfully after translation.
- ![](images/translation_package_reseted.png) **Reset:** the package has been manually reset by the translation coordinator.

This status and the time stamp for the status change are displayed in the properties window (see [Figure 161, “Translation Packages View”](6-4-7-translation-packages.md#figure.auftragsverwaltung.uebersetzung.paketeansicht "Figure 161. Translation Packages View")).

<a id="figure.auftragsverwaltung.uebersetzung.paketeansicht"></a>

![Image: translation packages view](images/Uebersetzungspaket_ansicht.jpg)

**Figure 161. Translation Packages View**

The status is retrieved by GOCAT every 60 minutes. The maximum wait time between the export from ODIS Creator and the import into GOCAT can be set by the translation coordinator for each location in the translation parameters editor (see [Section 6.4.1, “Define Translation Parameters”](6-4-1-define-translation-parameters.md "6.4.1. Define Translation Parameters")).

If you are assigned to a team with the roll "read-only author" or "author", then you can double click on an editorial object to switch to the corresponding content in the editing view. Analogous to the already existing link functions in other modules, the usage location dialog is also displayed to the user here if the destination of the link cannot be clearly determined (for example, due to reusage).

##### <a id="uebersetzungspakete.paketbildung"></a>6.4.7.1. Package Image

The automatic packaging of requirements is principally handled in two disjunctive quantities

- Quantity 1: requirements that have a target date between the current date "today" (inclusive) and the date "today - translation period" (inclusive)
- Quantity 2: requirements that have a target data before the date "today - translation period" or in the future (after "today") as well as requirements from AdHoc orders

Different parameters apply for both these quantities during the package setup. The requirements for quantity 1 should always be prioritized.

Quantity 1 requirements are always completely exported. It may also be that packages are created, which are not filled up to the set threshold.

Quantity 2 requirements are only transferred to packages if the set threshold “Amount (editorial text)” or “Amount (editorial content)” is reached. The packages are always filled with the set quantity (text or content) for this. Any additional requirements will remain until they either fall in quantity 1 or they create additional packages through quantity 2.

For both quantities, the parameters are likewise considered as the top threshold per package, therefore more packages are created when necessary if the threshold is exceeded for an object type.

The maximum number of objects of any type that can be contained in each package is specified by the “Amount (editorial text)” parameter. For object contents, the maximum amount of content is specified by the parameter “Amount (editorial content)”; the type of object is not relevant. It is important that a function code or a supplemental document is exported together (text and content) into a package, as long as both are being sent for translation.

For example, a package of the maximum size may contain the following objects if the values “Amount (editorial text)” = 500 and “Amount (editorial content)” = 500 are:

- 500 objects from the equipment network (editorial text)
- 500 objects from the knowledge base (editorial text)
- 500 objects from the function library (editorial text)
- 500 objects from the supplementary documents (editorial text)
- 500 content files from the function code, supplementary documents, and measured value table types (editorial content)

500 function codes including a content file should be included. Supplemental documents with content are no longer exported in the same package.

[Table 35, “Package Creation Example”](6-4-7-translation-packages.md#table.auftragsverwaltung.uebersetzung.paketbildung "Table 35. Package Creation Example") shows an example with more than one package for quantity 2. If the requirements were in quantity 1, the remaining requirements would be exported in another package. The parameters have the following values “Amount (editorial text)” = 50 and “Amount (editorial content)” = 60.

In [Table 35, “Package Creation Example”](6-4-7-translation-packages.md#table.auftragsverwaltung.uebersetzung.paketbildung "Table 35. Package Creation Example"), the code OBE stands for the texts from objects, such as the system name of a diagnostic object, and the code TBI stands for the texts from content files, such as the textual content of a supplemental document. The codes ASN, WBS, FKC, ZDK and MWT stand for various objects, therefore ASN stands for equipment network objects, WSB for knowledge base objects, FKC for function codes, ZDK for supplemental documents and MWT for measured values table.

<a id="table.auftragsverwaltung.uebersetzung.paketbildung"></a>

<table border="1" summary="Package Creation Example"><colgroup><col align="left"/><col align="center"/><col align="center"/><col align="center"/><col align="center"/><col align="center"/><col align="center"/></colgroup><thead><tr><th align="left">Object type</th><th align="center">Requirements</th><th align="center" colspan="2">Paket1</th><th align="center" colspan="2">Paket2</th><th align="center">Remaining requirements</th></tr><tr><th align="left"> </th><th align="center">Amount of objects</th><th align="center">Objects</th><th align="center">File</th><th align="center">Objects</th><th align="center">File</th><th align="center">Amount of objects</th></tr></thead><tbody valign="top"><tr><td align="left" valign="top">ASN OBE</td><td align="center" valign="top">70</td><td align="center" valign="top">50</td><td align="center" valign="top">1</td><td align="center" valign="top">0</td><td align="center" valign="top">0</td><td align="center" valign="top">20</td></tr><tr><td align="left" valign="top">WBS OBE</td><td align="center" valign="top">130</td><td align="center" valign="top">50</td><td align="center" valign="top">1</td><td align="center" valign="top">50</td><td align="center" valign="top">1</td><td align="center" valign="top">30</td></tr><tr><td align="left" valign="top">FKC OBE</td><td align="center" valign="top">20</td><td align="center" valign="top">0</td><td align="center" valign="top">0</td><td align="center" valign="top">0</td><td align="center" valign="top">0</td><td align="center" valign="top">20</td></tr><tr><td align="left" valign="top">ZDK OBE</td><td align="center" valign="top">80</td><td align="center" valign="top">50</td><td align="center" valign="top">1</td><td align="center" valign="top">0</td><td align="center" valign="top">0</td><td align="center" valign="top">30</td></tr><tr><td align="left" valign="top"> </td><td class="auto-generated"> </td><td class="auto-generated"> </td><td class="auto-generated"> </td><td class="auto-generated"> </td><td class="auto-generated"> </td><td class="auto-generated"> </td></tr><tr><td align="left" valign="top">ZDK TBI</td><td align="center" valign="top">30</td><td align="center" valign="top">30</td><td align="center" valign="top">30</td><td align="center" valign="top">0</td><td align="center" valign="top">0</td><td align="center" valign="top">0</td></tr><tr><td align="left" valign="top">FKC TBI</td><td align="center" valign="top">70</td><td align="center" valign="top">30</td><td align="center" valign="top">30</td><td align="center" valign="top">40</td><td align="center" valign="top">40</td><td align="center" valign="top">0</td></tr><tr><td align="left" valign="top">MWT TBI</td><td align="center" valign="top">50</td><td align="center" valign="top">0</td><td align="center" valign="top">0</td><td align="center" valign="top">20</td><td align="center" valign="top">20</td><td align="center" valign="top">30</td></tr></tbody></table>

**Table 35. Package Creation Example**

The target date for a translation package is calculated as follows when packages are created automatically: packages with quantity 1 requirements always contain the earliest introduction date of all included requirements (in this package). The deadline for the generated packages are thus in the range between "today" and the date "today + translation period". The set translation period is deliberately shorter for packages from quantity 1 requirements. For packages for quantity 2 requirements, the deadline is always set to "today + translation period" depending on which deadlines the included requirements have.

##### <a id="zieltermin.uebersetzungspaket"></a>6.4.7.2. Changing the Translation Package Deadline

You can select any amount of translation packages in the translation management navigation tree. When selecting, it does not matter if the selected translation packages have the same or different source-target language combination. The selection of translation packages from different locations is also possible. After confirming the (context) menu item **Adjust deadline**, a dialog is presented to you, where you can specify the present date or a date in the future (see [Figure 162, “Adjusting the Translation Package Deadline”](6-4-7-translation-packages.md#figure.auftragsverwaltung.uebersetzung.pakete "Figure 162. Adjusting the Translation Package Deadline")). This dialog gives you the option to completely cancel the action or proceed with it.

<a id="figure.auftragsverwaltung.uebersetzung.pakete"></a>

![Image: adjusting the translation package deadline](images/Uebersetzungspaket.JPG)

**Figure 162. Adjusting the Translation Package Deadline**

If the action is carried out, then the selected date (see [Figure 163, “Adjusting the Translation Package Deadline”](6-4-7-translation-packages.md#figure.auftragsverwaltung.uebersetzung.pakete.termin "Figure 163. Adjusting the Translation Package Deadline")) for all previously selected translation packages is applied as the new deadline date. During this, the value is only adjusted in the database, so that you can see it in the ODIS Creator interface. An adjustment to the already exported files does not occur. After the action has been successfully performed, the navigation tree in translation management is updated.

<a id="figure.auftragsverwaltung.uebersetzung.pakete.termin"></a>

![Image: adjusting the translation package deadline](images/Uebersetzungspaket_termin.jpg)

**Figure 163. Adjusting the Translation Package Deadline**

##### <a id="uebersetzung.pakete.zuruecksetzen"></a>6.4.7.3. Resetting Translation Packages

The function to reset translation packages allows you to remove translation packages, that have not been imported yet, from the entire translation process. The reset packages will correspondingly be seen with the status **reset**, and the objects contained in the package are reset to the initial status of the translation process. If the reset translation package contains administrative objects (for example, default texts), translation requirements are then created for all required target languages as a result of the reset process.

<a id="figure.auftragsverwaltung.uebersetzung.pakete.zurueck"></a>

![Image: resetting translation packages](images/Uebersetzungspaket_zuruecksetzen.jpg)

**Figure 164. Resetting Translation Packages**

To reset translation packages, select the desired packages and then select the "Reset package" entry in the context menu (see [Figure 164, “Resetting Translation Packages”](6-4-7-translation-packages.md#figure.auftragsverwaltung.uebersetzung.pakete.zurueck "Figure 164. Resetting Translation Packages") with the icon) ![](images/Uebersetzung_zuruecksetzen.png). This function can also be accessed through the global menu and the button. After the menu item has been activated, a message dialog will appear (see [Figure 165, “Confirmation Dialog Before Resetting Translation Packages”](6-4-7-translation-packages.md#figure.auftragsverwaltung.uebersetzung.pakete.zurueck.dialog "Figure 165. Confirmation Dialog Before Resetting Translation Packages")), in which you must confirm the resetting of the selected translation packages.

<a id="figure.auftragsverwaltung.uebersetzung.pakete.zurueck.dialog"></a>

![Image: confirmation dialog before resetting translation packages](images/Uebersetzungspaket_zuruecksetzen_dialog.jpg)

**Figure 165. Confirmation Dialog Before Resetting Translation Packages**

Translation packages with the **reset** status are not visible at first in the navigation tree. However, these can be made visible through a corresponding filter setting (see [Figure 166, “Filter Dialog for Translation Packages”](6-4-7-translation-packages.md#figure.auftragsverwaltung.uebersetzung.filtern "Figure 166. Filter Dialog for Translation Packages")).

Reset translation packages can be displayed using the filter setting **Reset = Yes** in the navigation tree.

<a id="figure.auftragsverwaltung.uebersetzung.filtern"></a>

![Image: filter dialog for translation packages](images/Ubersetzungspaket_filterdialog.jpg)

**Figure 166. Filter Dialog for Translation Packages**

There are some restrictions when handling these reset packages, that are listed in the following:

- If translation packages are imported, that are internally labeled with the "reset" status, the import of texts from the packages is rejected. The packages are moved to the designated "Error" folder and a corresponding message is stored in the log file. The message says that the translation package could not be imported due to the package status.
- The import of translation packages with the "reset" status is still possible in expert mode.
- Reset translation packages are initially not displayed in the navigation tree. To display translation packages with this status, a respective filter must be set.
- Translation packages with the "reset" status are "grayed out" in the display, thus the name is not black but rather given in gray font.
- Translation packages with the "reset" status are displayed with the icon ![](images/uebersetzungsstatus_zurueckgesetzt.png) .
- Reset translation packages are permanently deleted from the system by an automatic job after a set retention period. The setting is identical to the retention period of imported translation packages and is set for each location within the translation parameters.

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="6-4-6-translation-jobs.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="6-4-translation.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="6-4-8-monitoring-translations.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">6.4.6. Translation Jobs </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 6.4.8. Monitoring Translations</td></tr></table>
